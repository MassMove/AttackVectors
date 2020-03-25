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

            // iterate through the domains in sites.csv
            using (TextFieldParser parser = new TextFieldParser("../../../../../sites.csv"))
            {
                parser.TextFieldType = FieldType.Delimited;
                parser.SetDelimiters(",");
                parser.ReadFields(); // skip header

                String header = "awsOrigin,domain,lat,lng,locationVerified,httpResponseCode,contentLength,facebookUrl,siteName,twitterUsername,itunesAppStoreUrl,twitterAccountCreatedAt,twitterUserId,twitterFollowers,twitterFollowing,twitterTweets,siteOperator";
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
                    String siteOperator = "";

                    try
                    {
                        twitterUserId = fields[12];
                        twitterFollowers = fields[13];
                        twitterFollowing = fields[14];
                        twitterTweets = fields[15];
                        siteOperator = fields[16];
                    }
                    catch (Exception ex)
                    {
                    }

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
                }
                File.WriteAllText("../../../../../sites.csv", lines);
            }
        }
    }
}

