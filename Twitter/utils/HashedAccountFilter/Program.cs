using Microsoft.VisualBasic.FileIO;
using System;
using System.IO;

namespace HashedAccountFilter
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("This is our world now\r\n");

            // iterate through the domains in sites.csv
            var fileInfo = new FileInfo("../../../../../datasets/People’s Republic of China/Changyu Culture/hashed_2021_12_CNCC_0621_CNCC_0621_users.csv");
            using (var parser = new TextFieldParser(fileInfo.FullName))
            {
                parser.TextFieldType = FieldType.Delimited;
                parser.SetDelimiters(",");
                parser.ReadFields(); // skip header

                var header = "userid,userDisplayName,userScreenName,userReportedLocation,userProfileDescription,userProfileUrl,followerCount,followingCount,accountCreationDate,accountLanguage";
                var lines = header;
                while (!parser.EndOfData)
                {
                    string[] fields = parser.ReadFields();

                    // extract a line from sites.csv
                    var userid = fields[0];
                    var userDisplayName = fields[1];
                    var userScreenName = fields[2];
                    var userReportedLocation = fields[3];
                    var userProfileDescription = fields[4];
                    var userProfileUrl = fields[5];
                    var followerCount = fields[6];
                    var followingCount = fields[7];
                    var accountCreationDate = fields[8];
                    var accountLanguage = fields[9];

                    if (!userid.EndsWith("=")) {
                        var line = $"{userid}," +
                            $"{userDisplayName}," +
                        $"{userScreenName}," +
                        $"{userReportedLocation}," +
                        $"{userProfileDescription}," +
                        $"{userProfileUrl}," +
                        $"{followerCount}," +
                        $"{followingCount}," +
                        $"{accountCreationDate}," +
                        $"{accountLanguage}";
                        lines += "\r\n" + line;

                        Console.WriteLine($"{userScreenName}: {followerCount}, {followingCount}");
                    }
                }
                File.WriteAllText(fileInfo.FullName.Replace("hashed_", ""), lines);
            }
        }
    }
}
