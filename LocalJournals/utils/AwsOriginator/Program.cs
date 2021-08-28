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

            // iterate through the domains sites.csv
            using (TextFieldParser parser = new TextFieldParser("../../../../../sites.csv"))
            {
                parser.TextFieldType = FieldType.Delimited;
                parser.SetDelimiters(",");
                parser.ReadFields(); // skip header

                String header = ",awsOrigin,domain,lat,lng,locationVerified,httpResponseCode,contentLength,facebookUrl,siteName,twitterUsername,itunesAppStoreUrl,twitterAccountCreatedAt,twitterUserId,twitterFollowers,twitterFollowing,twitterTweets,siteOperator";
                String lines = header;
                while (!parser.EndOfData)
                {
                    string[] fields = parser.ReadFields();

                    // extract a line from sites.csv
                    String id = fields[0];
                    String awsOrigin = fields[1];
                    String domain = fields[2];
                    String state = fields[3];
                    String lat = fields[4];
                    String lng = fields[5];
                    String locationVerified = fields[6];
                    String httpResponseCode = fields[7];
                    String contentLength = fields[8];
                    String facebookUrl = fields[9];
                    String siteName = fields[10];
                    String twitterUsername = fields[11];
                    String itunesAppStoreUrl = fields[12];
                    String twitterAccountCreatedAt = fields[13];
                    String twitterUserId = "";
                    String twitterFollowers = "";
                    String twitterFollowing = "";
                    String twitterTweets = "";
                    String siteOperator = "";

                    Console.Write(domain + ": ");

                    try
                    {
                        twitterUserId = fields[14];
                        twitterFollowers = fields[15];
                        twitterFollowing = fields[16];
                        twitterTweets = fields[17];
                        siteOperator = fields[18];
                    }
                    catch (Exception ex)
                    {
                        String x = ex.Message;
                    }

                    // get the IP
                    try
                    {
                        Uri uri = new Uri("https://" + domain);
                        IPAddress ip = Dns.GetHostAddresses(uri.Host)[0];
                        awsOrigin = ip.ToString();
                    }
                    catch (Exception ex)
                    {
                    }

                    // write a new line for the updated sites.csv
                    String line = id + ",";
                    line += awsOrigin + ",";
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
                    line += siteOperator;

                    lines += "\r\n" + line;

                    Console.WriteLine(awsOrigin);
                }
                File.WriteAllText("../../../../../sites.csv", lines);
            }
        }
    }
}
