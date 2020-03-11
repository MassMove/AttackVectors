import logging
import sitecsv
import requests
import argparse
import subprocess
from lxml import html
from urllib.error import HTTPError


#Fake firefox-like header. Valid HTTP request headers, particularly the user-agent are used to determine if
#web request are valid. We can emulate different browsers using different headersl
HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}


"""
Check that input and output files exist.
"""
def check_arguments(sitescsv_path, logfile_path):
    return1 = test_open_file(sitescsv_path, 'r') 
    return2 = test_open_file(logfile_path, 'a')
    return return1 and return2

"""
Open a <file> with <mode> return false on error
"""
def test_open_file(path, mode):
    try:
        with open(path, 'a') as tesfile:
            logging.info('Successfully opened: ' + path)
    except:
        logging.error('Unable to file: ' + path)
        return False
    return True


"""
Get arguments from command line.
Mode = start | resume. 
mode start: --csv is input sites.csv from github.
    --log is logfile. Logs appended to this file.
    --output sites-information output file name.
mode resume: --resumefile is input sites-information that output from output_sites_information.
    --log is logfile. Logs appended to this file.
    --output sites-information output file name.
"""
def parse_arguments():
    ap = argparse.ArgumentParser()
    ap.add_argument('mode', nargs=1)
    ap.add_argument('-c', '--csv', required=False, help='Input file sites.csv\'s path.')
    ap.add_argument('-r', '--resumefile', required=False, help='Resume monitoring. Continue from state in resumefile.csv.')
    ap.add_argument('-l', '--log', required=True, help='Output site-monitor log file.')
    ap.add_argument('-o', '--output', required=True, help='Output file for selected argument.')
    ap.add_argument('-k', '--key', required=False, help='API key for selected scan.')
    ap.add_argument('-x', '--lynxmap', required=False, help='Lynx map file input.')

    args = ap.parse_args()

    mode = args.mode[0]
    if mode == 'start' and args.csv is not None and args.log is not None and args.output is not None:
        pass
    elif mode == 'resume' and args.resumefile is not None and args.log is not None and args.output is not None:
        pass
    elif mode == 'publicwww' and args.resumefile is not None and args.log is not None \
                             and args.output is not None and args.key is not None:
        pass
    elif mode == 'lynxscan' and args.output is not None and args.log is not None and args.resumefile is not None:
        pass
    elif mode == 'lynxcount' and args.output is not None and args.log is not None and args.lynxmap is not None:
        pass
    else:
        ap.error('Usage: python sitemonitor.py start -c sites.csv -l logfile.txt -o sites-information.csv')
        ap.error('       python sitemonitor.py resume -r resumefile.csv -l logfile.txt -o sites-information.csv')
        exit(-1)
    return args


"""
old_sites_info site: {status, quant, ganal, pixel} is previous run's output information.
    status, quant, ganal, pixel will be empty strings if mode == start and input is sites.csv
output_path: filename of output csv file.
    
"""
def monitor(old_sites_info, output_path):
    new_sites_info = dict()

    #for each website url in parsed site information,
    for site in old_sites_info:
        #get new site content and parse IDs into new_site_info
        new_site_info = scrape_website_for_ids(site)
        new_sites_info[site] = new_site_info

        #log each websites current information to logfile
        new_status = str(new_site_info['status'])
        new_quant = new_site_info['quant']
        new_pixel = new_site_info['pixel']
        new_ganal = new_site_info['ganal']
        logging.info(site + ', ' + new_status + ', ' + new_ganal + ', ' + new_pixel + ', ' + new_quant)

    #compare new and old site information
    change_count = {'status': 0, 'quant': 0, 'ganal': 0, 'pixel': 0}
    for site in old_sites_info:
        #old info
        old_status = old_sites_info[site]['status']
        old_quant = old_sites_info[site]['quant']
        old_pixel = old_sites_info[site]['pixel']
        old_ganal = old_sites_info[site]['ganal']

        #new info
        new_status = str(new_sites_info[site]['status'])
        new_quant = new_sites_info[site]['quant']
        new_pixel = new_sites_info[site]['pixel']
        new_ganal = new_sites_info[site]['ganal']

        if old_status != new_status:
            change_count['status'] = change_count['status'] + 1
        if old_quant != new_quant:
            change_count['quant'] = change_count['quant'] + 1
        if old_ganal != new_ganal:
            change_count['ganal'] = change_count['ganal'] + 1
        if old_pixel != new_pixel:
            change_count['pixel'] = change_count['pixel'] + 1

    logging.info(str(change_count['status']) + ' status code changes since last run.')
    logging.info(str(change_count['pixel']) + ' pixel ID changes since last run.')
    logging.info(str(change_count['quant']) + ' quantserve ID changes since last run.')
    logging.info(str(change_count['ganal']) + ' google analytics ID changes since last run.')

    #output newest information to sites-information.csv output file
    sitecsv.output_sites_information(new_sites_info, output_path)
    return 0


"""
HTTP get <url> and scrape quantserve ID, Google analytics ID, FB Pixel ID, and status code.
return: site: {status, quant, ganal, pixel}
"""
def scrape_website_for_ids(url):
    nsite = 'http://' + url
    ids = {'status': '', 'quant': '', 'ganal': '', 'pixel': ''}
    try:
        page = requests.get(nsite, headers=HEADERS)
        tree = html.fromstring(page.content)

        quant = tree.xpath("//img[contains(@src, 'pixel.quantserve')]")
        ganal = tree.xpath("//script[contains(@src, 'googletag')]")
        pixel = tree.xpath("//img[contains(@src, 'facebook.com/tr?id=')]")
        status = page.status_code

        ids['status'] = status
        if len(quant) > 0:
            for item in quant:
                attribute = item.attrib['src']
                index = attribute.index('p-')
                length = len(item.attrib['src'])
                ids['quant'] = item.attrib['src'][index:length]
        if len(ganal) > 0:
            for item in ganal:
                attribute = item.attrib['src']
                index = attribute.index('UA-')
                length = len(item.attrib['src'])
                ids['ganal'] = item.attrib['src'][index:length]
        if len(pixel) > 0:
            for item in pixel:
                attribute = item.attrib['src']
                index = attribute.index('id=')
                index2 = attribute.index('&ev=')
                ids['pixel'] = item.attrib['src'][index:index2]
    except HTTPError as e:
        logging.info('HTTPPExcept status code: ' + e.response.code)
        pass
    except:
        ids['status'] = 404
        logging.error('Unable to reach website: ' + url)
    return ids


def scan_publicwww(api_key, sites_info, outfile):
    gids = set()
    pids = set()
    qids = set()
    
    #add qids, gids, and pids to sets so only unique entries remain
    for site in sites_info:
        gid = sites_info[site]['ganal']
        if gid is not None and gid.strip() != '':
            gids.add(gid.strip())

        pid = sites_info[site]['pixel']
        if pid is not None and pid.strip() != '':
            pids.add(pid.strip())

        qid = sites_info[site]['qserve']
        if qid is not None and qid.strip() != '':
            qids.add(qid.strip())

        status = sites_info[site]['status']

    #use publicWWW's api to search for each unique ID.
    results = dict()
    for pid in pids:
        links = apis.publicwww(pid, api_key)
        results[pid] = links
    for gid in gids:
        links = apis.publicwww(gid)
        results[gid] = links
    for qid in qids:
        links = apis.publicwww(qid)
        results[qid] = links

    #create map site -> sites linked to sites via publicwww
    for key in results:
        links = results[key]

    sitecsv.output_publicwww(sites_linked, outfile)


"""
Use lynx to crawl website for links and output CSV file
row: site, link link link
row1: site2, link link link
"""
def output_site_links_map(sites_list, outfile):
    site_map = dict()
    i = 0
    for site in sites_list:
        if i == 9:
            break
        i = i + 1
        if site is None or site.strip() == '':
            continue
        site = site.strip()

        #create string for command to run: lynx -listonly -dump <site>
        command = 'lynx -listonly -dump ' + site
        #run command as subprocess  and store completion process info.
        completed = subprocess.run(command, shell=True, stdout=subprocess.PIPE, universal_newlines=True)

        #remove any duplicate links and create set() of site -> link link link datastructure
        site_links = set()
        for line in completed.stdout.split("\n"):
            if line.find("http") < 0:
                continue
            line = line.strip()
            link = line.split(" ")[1]
            site_links.add(link)

        site_map[site] = site_links

    sitecsv.output_lynx_map(outfile, site_map)
    return 


"""
Walk link map set of site -> link link link
Log sites and the count of their occurance. Only exact matches
to full URL counted as occurance. No stemming links so far.
"""
def count_links(link_map):
    site_counts = dict()
    for site in link_map:
        for link in link_map[site]:
            if link in site_counts.keys():
                count = site_counts[link]
                count = count + 1
                site_counts[link] = count
            else:
                count = 1
                site_counts[link] = count

    sorted_sites = {k: v for k, v in sorted(site_counts.items(), key=lambda item: item[1])}
    for site in sorted_sites:
        logging.info(site + ", " + "count: " + str(sorted_sites[site]))


def main():
    args = parse_arguments()
    mode = args.mode[0]

    #Try configuring logfile. Exception indicates invalid logfile, could not open.
    try:
        logging.basicConfig(filename=args.log, filemode='a', level=logging.INFO, 
                            format='%(asctime)s: %(levelname)s: %(message)s')
    except:
        print('Error configuring logfile. Exiting.')
        exit(-1)

    #depending upon the mode from parsed arguments, read in site information
    if mode == 'start':
        logging.info('Mode: start')
        if check_arguments(args.csv, args.log) == False:
            exit(-1)
        #read information from sites.csv into sites_info. sites.csv will only provide urls, no ids or status
        sites_info = sitecsv.open_sites_csv(args.csv)
        #using parsed site information, check if websites's status has updated
        #and if it's tracking IDs have changed
        monitor(sites_info, args.output)
    elif mode == 'resume':
        logging.info('Mode: resume')
        if check_arguments(args.resumefile, args.log) == False:
            exit(-1)
        #read information from sites-information.csv into sites_info. sites.csv should have all fields 
        sites_info = sitecsv.open_sites_information(args.resumefile)
        #using parsed site information, check if websites's status has updated
        #and if it's tracking IDs have changed
        monitor(sites_info, args.output)
    elif mode == 'publicwww':
        logging.info('Mode: publicWWW')
        if check_arguments(args.resumefile, args.log) == False:
            exit(-1)
        sites_info = sitecsv.open_sites_information(args.resumefile)
        scan_publicwww(args.key, sites_info, args.outfile) 
    elif mode == 'lynxscan':
        logging.info("Mode: lynxscan")
        sites_info = sitecsv.open_sites_information(args.resumefile)
        output_site_links_map(sites_info.keys(), args.output)
    elif mode == 'lynxcount':
        logging.info("Mode: lynxcount")
        link_map = sitecsv.open_lynx_map(args.lynxmap)
        count_links(link_map)
    else:
        logging.error('Error, invalid mode.')

    return 0


if __name__ == '__main__':
    main()
