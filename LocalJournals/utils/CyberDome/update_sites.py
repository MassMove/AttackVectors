#!/usr/bin/python3
#Creates sites.txt list from sites.csv, which can be grabbed with a command like "curl https://raw.githubusercontent.com/MassMove/AttackVectors/master/LocalJournals/sites.csv -o sites.csv"
import csv
import praw
import logging
import sys
import hashlib
from pathlib import Path


def write_wiki(subreddit, page, new_data, reddit):
    wiki_page = reddit.subreddit(subreddit).wiki[page]
    try:
        wiki_page.edit(new_data)
        logging.info("Updated wiki page")
    except Exception as e:
        logging.error("There was a problem writing to wiki page: " + str(e))


bot = 'cyber_dome_bot'
reddit = praw.Reddit(bot)
testing = True
home = str(Path.home())
if (testing):
    home = str(Path.home())+'/bots/cyber_dome'

#print logging output to file
logging.basicConfig(level=logging.INFO,
                    filename=home+'/data/update_sites.log',
                    format='%(asctime)s - %(levelname)s - %(message)s')
#print logging output to console
root = logging.getLogger()
root.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
root.addHandler(handler)

BLOCK_SIZE = 65536
file_hash = hashlib.sha256()
domain_list = []

with open(home+"/data/sites.csv", 'rb') as f:
    fb = f.read(BLOCK_SIZE)
    while len(fb) > 0:
        file_hash.update(fb)
        fb = f.read(BLOCK_SIZE)
        new_hash = file_hash.hexdigest()
    with open(home + "/data/sites.hash", "r+") as h:
        old_hash = h.read()
        if (str(old_hash) == str(new_hash)):
            logging.info('No update needed')
            sys.exit()
        else:
            logging.info(f'Updating hash to {new_hash}')
            h.seek(0)
            h.write(new_hash)
            h.truncate()

with open(home+"/data/sites.csv") as csvfile:
    filereader = csv.DictReader(csvfile)
    for row in filereader:
        domain_list.append(row['domain'])
    if (len(domain_list) < 1000):
        logging.error('CSV File too short.  Exiting')
        sys.exit()

automod_code = 'Example Cyber Dome automod code is listed below.  You can of course tweak it however you like\n\n    ' \
               'type: any\n    url+body(includes): '+str(domain_list)+'\n    action: spam\n    action_reason: "Fake ' \
               'Local Journal Domain: {{match}}"\n    modmail_subject: "Fake Local Journal Domain ' \
               'Detected"\n    modmail: "A fake local news site was detected.  Please investigate and ' \
               'notify /r/cyber_dome if appropriate"\n    ---\n\nThis code is automatically generated and updated ' \
               'based on the master list [here](https://github.com/MassMove/AttackVectors/blob/master/LocalJournals/sites.csv)'

logging.info(automod_code)

write_wiki('cyber_dome', 'sites_automod', automod_code, reddit)

with open(home+"/data/sites.txt", "w") as o:
    for domain in domain_list:
        o.write(domain + "\n")
