using Microsoft.VisualBasic.FileIO;
using System;
using System.IO;

namespace CoordCopy
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("This is our world now");

            // copy lat and lng from sites-geocoded.csv to sites.csv
            using (TextFieldParser parser = new TextFieldParser("../../../../../sites.csv"))
            {
                parser.TextFieldType = FieldType.Delimited;
                parser.SetDelimiters(",");
                parser.ReadFields(); // skip header

                String header = "awsOrigin,domain,lat,lng,locationVerified,facebookUrl,siteName,twitterUsername,itunesAppStoreUrl,twitterAccountCreatedAt,twitterUserId,twitterFollowers,twitterFollowing,twitterTweets";
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
                    String facebookUrl = fields[5];
                    String siteName = fields[6];
                    String twitterUsername = fields[7];
                    String itunesAppStoreUrl = fields[8];
                    String twitterAccountCreatedAt = fields[9];
                    String twitterUserId = "";
                    String twitterFollowers = "";
                    String twitterFollowing = "";
                    String twitterTweets = "";

                    try
                    {
                        twitterUserId = fields[10];
                        twitterFollowers = fields[11];
                        twitterFollowing = fields[12];
                        twitterTweets = fields[13];
                    }
                    catch (Exception ex)
                    { 
                    }

                    // grab the coords from sites-geocoded.csv
                    using (TextFieldParser geocodedParser = new TextFieldParser("../../../../../sites-geocoded.csv"))
                    {
                        geocodedParser.TextFieldType = FieldType.Delimited;
                        geocodedParser.SetDelimiters(",");
                        geocodedParser.ReadFields(); // skip header

                        while (!geocodedParser.EndOfData)
                        {
                            string[] geocodedFields = geocodedParser.ReadFields();

                            if (domain == geocodedFields[0])
                            {
                                lat = geocodedFields[1];
                                lng = geocodedFields[2];
                                locationVerified = geocodedFields[3];
                                break;
                            }
                        }
                    }

                    // write a new line for the updated sites.csv
                    String line = awsOrigin + ",";
                    line += domain + ",";
                    line += lat + ",";
                    line += lng + ",";
                    line += locationVerified + ",";
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
                }
                File.WriteAllText("../../../../../sites.csv", lines);
            }
        }
    }
}
