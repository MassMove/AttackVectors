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

            String sitesCsv = File.ReadAllText("../../../../../sites.csv").ToLower();

            String[] domainsToCheck = File.ReadAllText("../../../DomainsToCheck.txt").ToLower().Split(new[] { "\r\n" }, StringSplitOptions.None);

            foreach (String domainToCheck in domainsToCheck)
            {
                if (!sitesCsv.Contains(domainToCheck))
                {
                    File.AppendAllText("../../../DomainsToAdd.txt", domainToCheck + "\r\n");
                    Console.WriteLine("Add " + domainToCheck);
                }
            }
        }
    }
}
