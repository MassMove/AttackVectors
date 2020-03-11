import csv


"""
Open <path> as sites.csv file. 
URL = row[1]
return: row[1] = {'status': '', 'quant': '', 'pixel': '', 'ganal': ''} 
"""
def open_sites_csv(path):
    sites_info = dict() 
    with open(path) as csvfile:
        #skip the header
        next(csvfile)
        csvreader = csv.reader(csvfile, dialect='excel')
        for row in csvreader:
            info = {'status': '', 'quant': '', 'pixel': '', 'ganal': ''} 
            sites_info[row[1]] = info
    return sites_info


"""
Outputs <sites_info> to CSV file <outfile>
row: site, status, ganal, pixel, quant
"""
def output_sites_information(sites_info, outfile):
    with open(outfile, 'w', newline='') as csvfile:
        output = csv.writer(csvfile, dialect='excel')
        output.writerow(['site', 'status-code', 'google-analytics', 'fb-pixel', 'quantserve'])
        for key in sites_info:
            output.writerow([key, sites_info[key]['status'], 
                                  sites_info[key]['ganal'], 
                                  sites_info[key]['pixel'], 
                                  sites_info[key]['quant']])

"""
Open <path> as sites-information.csv file. 
URL = row[1]
return: row[1] = {'status': '***', 'quant': '****', 'pixel': '****', 'ganal': '****'} 
"""
def open_sites_information(path):
    sites_info = dict() 
    with open(path) as csvfile:
        #skip the header line in the file before reading in rows.
        next(csvfile)
        csvreader = csv.reader(csvfile, dialect='excel')
        for row in csvreader:
            info = {'status': [1], 'quant': row[4], 'pixel': row[3], 'ganal': row[2]} 
            sites_info[row[0]] = info
    return sites_info


"""
Open publicWWW outputfile <outfile>:
output csv format: site, linked linked linked
                   site2, site2_linked site2_linked site2_linked
"""
def output_publicwww(sites_linked, outfile):
    with open(outfile, 'w', newline='') as csvfile:
        output = csv.writer(csvfile, dialect='excel')
        output.writerow(["site", "links"])
        for key in sites_linked:
            output.writerow([key, " ".join(sites_linked[key])])
    return


"""
Read output of output_lynx_map and parse
return: site => link link link
"""
def open_lynx_map(path):
    link_map = dict()
    with open(path, 'r') as csvfile:
        #skip the 'domain' header
        next(csvfile)
        csvreader = csv.reader(csvfile, dialect='excel')
        for row in csvreader:
            site = row[0]
            links = row[1].split(' ')
            link_map[site] = links
    return link_map


"""
Output lynx site->links map to csv file.
output: row: site, link link link
        row: site2, link link link
"""
def output_lynx_map(path, site_map):
    with open(path, 'w', newline='\n') as csvfile:
        output = csv.writer(csvfile, dialect='excel')
        output.writerow(["site", "links"])
        for site in site_map:
            output.writerow([site, " ".join(site_map[site])])
