using Microsoft.VisualBasic.FileIO;
using System;
using System.IO;
using System.Net;

namespace HttpResponseMonitor
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("This is our world now");

            // ignore invalid certs so we can capture 404s
            ServicePointManager.ServerCertificateValidationCallback += (sender, cert, chain, sslPolicyErrors) => true;

            // copy lat and lng from sites-geocoded.csv to sites.csv
            using (TextFieldParser parser = new TextFieldParser("../../../../../sites-http-response-code.csv"))
            {
                parser.TextFieldType = FieldType.Delimited;
                parser.SetDelimiters(",");
                parser.ReadFields(); // skip header

                String header = "awsOrigin,domain,lat,lng,locationVerified,httpResponseCode,contentLength,facebookUrl,siteName,twitterUsername,itunesAppStoreUrl,twitterAccountCreatedAt,twitterUserId,twitterFollowers,twitterFollowing,twitterTweets";
                String lines = header;
                while (!parser.EndOfData)
                {
                    string[] fields = parser.ReadFields();

                    // extract a line from sites.csv
                    String awsOrigin = fields[0];
                    String domain = fields[1];
                    String lat = fields[2];
                    String lng = fields[3];
                    String locationVerified = fields[4];
                    String httpResponseCode = fields[5];
                    String contentLength = fields[6];
                    String facebookUrl = fields[7];
                    String siteName = fields[8];
                    String twitterUsername = fields[9];
                    String itunesAppStoreUrl = fields[10];
                    String twitterAccountCreatedAt = fields[11];
                    String twitterUserId = "";
                    String twitterFollowers = "";
                    String twitterFollowing = "";
                    String twitterTweets = "";

                    try
                    {
                        twitterUserId = fields[12];
                        twitterFollowers = fields[13];
                        twitterFollowing = fields[14];
                        twitterTweets = fields[15];
                    }
                    catch (Exception ex)
                    {
                        String x = ex.Message;
                    }

                    // get the http response code
                    try
                    {
                        HttpWebRequest request = (HttpWebRequest)WebRequest.Create("https://" + domain);
                        request.Method = "GET";
                        using (var response = request.GetResponse())
                        using (var stream = response.GetResponseStream())
                        using (var reader = new StreamReader(stream))
                        {
                            HttpStatusCode statusCode = ((HttpWebResponse)response).StatusCode;
                            httpResponseCode = ((int)statusCode).ToString();
                            contentLength = response.ContentLength.ToString();
                        }
                    }
                    catch (WebException we)
                    {
                        if (we.Response != null)
                        {
                            HttpStatusCode statusCode = ((HttpWebResponse)we.Response).StatusCode;
                            httpResponseCode = ((int)statusCode).ToString();
                            contentLength = we.Response.ContentLength.ToString();
                        }
                    }
                    catch (Exception ex)
                    { 
                    }

                    // write a new line for the updated sites.csv
                    String line = awsOrigin + ",";
                    line += domain + ",";
                    line += lat + ",";
                    line += lng + ",";
                    line += locationVerified + ",";
                    line += httpResponseCode + ",";
                    line += contentLength + ",";
                    line += facebookUrl + ",";
                    line += siteName + ",";
                    line += twitterUsername + ",";
                    line += itunesAppStoreUrl + ",";
                    line += twitterAccountCreatedAt + ",";
                    line += twitterUserId + ",";
                    line += twitterFollowers + ",";
                    line += twitterFollowing + ",";
                    line += twitterTweets;

                    lines += "\r\n" + line;

                    Console.WriteLine(domain + ": " + httpResponseCode + ", " + contentLength);
                }
                File.WriteAllText("../../../../../sites2.csv", lines);
            }
        }
    }
}
