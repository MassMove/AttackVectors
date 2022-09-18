using Microsoft.VisualBasic.FileIO;
using System;
using System.IO;
using System.Net;

namespace FacebookUrlExtractor
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("This is our world now");

            // iterate through the domains in sites.csv
            using (TextFieldParser parser = new TextFieldParser("../../../../../sites.csv"))
            {
                parser.TextFieldType = FieldType.Delimited;
                parser.SetDelimiters(",");
                parser.ReadFields(); // skip header

                String header = "awsOrigin,domain,state,lat,lng,locationVerified,httpResponseCode,contentLength,facebookUrl,siteName,twitterUsername,itunesAppStoreUrl,twitterAccountCreatedAt,twitterUserId,twitterFollowers,twitterFollowing,twitterTweets,siteOperator,twitterSuspended";
                String lines = header;
                while (!parser.EndOfData)
                {
                    string[] fields = parser.ReadFields();

                    // extract a line from sites.csv
                    String awsOrigin = fields[0];
                    String domain = fields[1];
                    String state = fields[2];
                    String lat = fields[3];
                    String lng = fields[4];
                    String locationVerified = fields[5];
                    String httpResponseCode = fields[6];
                    String contentLength = fields[7];
                    String facebookUrl = fields[8];
                    String siteName = fields[9];
                    String twitterUsername = fields[10];
                    String itunesAppStoreUrl = fields[11];
                    String twitterAccountCreatedAt = fields[12];
                    String twitterUserId = fields[13];
                    String twitterFollowers = fields[14];
                    String twitterFollowing = fields[15];
                    String twitterTweets = fields[16];
                    String siteOperator = fields[17];
                    String twitterSuspended = fields[18];

                    // get the facebook URL
                    if (facebookUrl == "")
                    {
                        try
                        {
                            HttpWebRequest request = (HttpWebRequest)WebRequest.Create("https://" + domain);
                            request.Method = "GET";

                            //Fake firefox-like header. Valid HTTP request headers, particularly the user-agent are used to determine if
                            //web request are valid. We can emulate different browsers using different headersl
                            request.Headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36";

                            using (var response = request.GetResponse())
                            using (var stream = response.GetResponseStream())
                            using (var reader = new StreamReader(stream))
                            {
                                String domainSource = reader.ReadToEnd();

                                int facebookUrlStart = domainSource.IndexOf("href=\"https://www.facebook.com/");
                                if (facebookUrlStart > 0)
                                {
                                    facebookUrlStart += "href=\"".Length;
                                    int facebookUrlEnd = domainSource.IndexOf("\"", facebookUrlStart);
                                    facebookUrl = domainSource.Substring(facebookUrlStart, facebookUrlEnd - facebookUrlStart);

                                    Console.WriteLine(domain + ": " + facebookUrl);
                                    File.AppendAllText("facebookUrls.txt", domain + ": " + facebookUrl + "\r\n");
                                } 
                                else
                                {
                                    Console.Write(".");
                                }
                            }
                        }
                        catch (Exception ex)
                        {
                        }
                    }

                    // write a new line for the updated sites.csv
                    String line = awsOrigin + ",";
                    line += domain + ",";
                    line += state + ",";
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
                    line += twitterTweets + ",";
                    line += siteOperator + ",";
                    line += twitterSuspended;

                    lines += "\r\n" + line;
                }
                File.WriteAllText("../../../../../sites.csv", lines);
            }
        }
    }
}

