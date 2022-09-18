using Microsoft.VisualBasic.FileIO;
using System;
using System.IO;
using System.Net;
using System.Threading;

namespace HttpResponseMonitor
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("This is our world now");
            int threads = 0;

            String readMe = "# Reddit Post Monitor\r\n\r\n";

            readMe += "Last run: " + DateTime.UtcNow.ToString("yyyy-MM-dd hh:mm UTC") + "\r\n\r\n";

            // iterate through the domains in sites.csv
            using (TextFieldParser parser = new TextFieldParser("../../../../../sites.csv"))
            {
                parser.TextFieldType = FieldType.Delimited;
                parser.SetDelimiters(",");
                parser.ReadFields(); // skip header

                while (!parser.EndOfData)
                {
                    string domain = parser.ReadFields()[1];

                    threads++;
                    new Thread((ThreadStart)(() =>
                    {
                        try
                        {
                            HttpWebRequest httpWebRequest = (HttpWebRequest)WebRequest.Create("https://www.reddit.com/domain/" + domain);
                            httpWebRequest.Method = "GET";
                            httpWebRequest.Headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36";
                            using (WebResponse response = httpWebRequest.GetResponse())
                            {
                                using (Stream responseStream = response.GetResponseStream())
                                {
                                    using (StreamReader streamReader = new StreamReader(responseStream))
                                    {
                                        string domainHtml = streamReader.ReadToEnd();
                                        string domainUrl = "- [" + domain + "](" + "https://www.reddit.com/domain/" + domain + ")";
                                        if (domainHtml.IndexOf("hour ago") > 0)
                                        {
                                            readMe += domainUrl + ": an hour ago!" + "\r\n";
                                            Console.WriteLine("\r\n" + domain + ": an hour ago!");
                                        }
                                        else if (domainHtml.IndexOf("hours ago") > 0)
                                        {
                                            string hours = getTimeframe(domainHtml, "hours ago");
                                            readMe += domainUrl + ": " + hours + " hours ago!" + "\r\n";
                                            Console.WriteLine("\r\n" + domain + ": " + hours + " hours ago!");
                                        }
                                        else if (domainHtml.IndexOf("day ago") > 0)
                                        {
                                            readMe += domainUrl + ": a day ago!" + "\r\n";
                                            Console.WriteLine("\r\n" + domain + ": a day ago!");
                                        }
                                        else if (domainHtml.IndexOf("days ago") > 0)
                                        {
                                            string days = getTimeframe(domainHtml, "days ago");
                                            readMe += domainUrl + ": " + days + " days ago" + "\r\n";
                                            Console.WriteLine("\r\n" + domain + ": " + days + " days ago");
                                        }
                                        else
                                            Console.Write(".");
                                    }
                                }
                            }
                        }
                        catch (Exception ex)
                        {
                            Console.Write("\r\n" + domain + ": " + ex.Message);
                        }
                        --threads;
                    })).Start();
                    Thread.Sleep(10);
                }
            }

            while (threads > 0)
            {
                Thread.Sleep(512);
            }

            File.WriteAllText(@"..\..\..\README.md", readMe);
        }

        static string getTimeframe(string searchString, string endText)
        {
            int end = searchString.IndexOf(endText);
            int start = searchString.IndexOf(">", end - endText.Length - 3) + 1;
            return searchString.Substring(start, end - start - 1);
        }
    }
}

