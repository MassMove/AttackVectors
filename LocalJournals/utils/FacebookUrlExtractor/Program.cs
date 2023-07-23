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

                String header = "awsOrigin,domain,state,lat,lng,locationVerified,httpResponseCode,contentLength,facebookUrl,siteName,twitterUsername,itunesAppStoreUrl,twitterAccountCreatedAt,twitterUserId,twitterFollowers,twitterFollowing,twitterTweets,siteOperator,twitterSuspended,facebookFollowers,facebookLikes";
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
                    String facebookFollowers = fields[19];
                    String facebookLikes = fields[20];

                    // get the facebook URL
                    try
                    {
                        Console.Write(domain + ": ");

                        var domainSource = getWebResponse("https://" + domain);

                        int facebookUrlStart = domainSource.IndexOf("href=\"https://www.facebook.com/");
                        if (facebookUrlStart > 0)
                        {
                            facebookUrlStart += "href=\"".Length;
                            int facebookUrlEnd = domainSource.IndexOf("\"", facebookUrlStart);
                            facebookUrl = domainSource.Substring(facebookUrlStart, facebookUrlEnd - facebookUrlStart);
                        }

                        Console.Write(facebookUrl);
                        if (facebookUrl != "") { 
                            var facebookSource = getWebResponse(facebookUrl);

                            var textTag = "text\":";

                            var followersTag = " followers\"}";
                            int facebookFollowersStart = facebookSource.IndexOf(followersTag);
                            facebookFollowersStart = facebookSource.IndexOf(textTag, facebookFollowersStart - followersTag.Length - textTag.Length) + textTag.Length + 1;
                            if (facebookFollowersStart > 0) { 
                                int facebookFollowersEnd = facebookSource.IndexOf(" ", facebookFollowersStart - 2);
                                facebookFollowers = facebookSource.Substring(facebookFollowersStart, facebookFollowersEnd - facebookFollowersStart);
                            }

                            var likesTag = " likes\"}";
                            int facebookLikesStart = facebookSource.IndexOf(likesTag);
                            facebookLikesStart = facebookSource.IndexOf(textTag, facebookLikesStart - likesTag.Length - textTag.Length) + textTag.Length + 1;
                            if (facebookLikesStart > 0)
                            {
                                int facebookLikesEnd = facebookSource.IndexOf(" ", facebookLikesStart - 2);
                                facebookLikes = facebookSource.Substring(facebookLikesStart, facebookLikesEnd - facebookLikesStart);
                            }

                            Console.Write(" - " + facebookFollowers + ", " + facebookLikes);
                        }
                    }
                    catch (Exception ex)
                    {
                        Console.Write(ex.Message);
                    }
                    Console.WriteLine("");

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
                    line += twitterSuspended + ",";
                    line += facebookFollowers + ",";
                    line += facebookLikes;

                    lines += "\r\n" + line;
                }
                File.WriteAllText("../../../../../sites.csv", lines);
            }
        }

        static string getWebResponse(string url)
        {
            HttpWebRequest request = (HttpWebRequest)WebRequest.Create(url);
            request.Headers.Add("user-agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36");

            request.Headers.Add("accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9");
            request.Headers.Add("accept-language", "en-US,en;q=0.9");
            request.Headers.Add("upgrade-insecure-requests", "1");
            request.Headers.Add("sec-fetch-user", "?1");
            request.Headers.Add("sec-fetch-site", "none");
            request.Headers.Add("sec-fetch-mode", "navigate");
            request.Headers.Add("sec-fetch-dest", "document");
            request.Headers.Add("sec-ch-ua-platform", "\"Windows\"");
            request.Headers.Add("sec-ch-ua-mobile", "?0");
            request.Headers.Add("sec-ch-ua", "\"Google Chrome\";v=\"105\", \"Not)A; Brand\";v=\"8\", \"Chromium\";v=\"105\"");

            using (HttpWebResponse response = (HttpWebResponse)request.GetResponse())
            {
                using (var reader = new StreamReader(response.GetResponseStream()))
                {
                    return reader.ReadToEnd();
                }
            }
        }
    }
}

