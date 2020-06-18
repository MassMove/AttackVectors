#!/usr/bin/python3
import logging
import pprint
import sys
import datetime
import praw
from pathlib import Path


def reddit_log(log_text, thread_id):
    log_thread = reddit.submission(id=thread_id)
    logging.info(f"log_output: {log_text}")
    log_thread.reply(log_text)
    return

version = '1.1'
testing = False
bot = 'cyber_dome_bot'
reddit = praw.Reddit(bot)
reddit.validate_on_submit = True
log_thread = 'gdp9bv'
log_sub = reddit.subreddit('cyber_dome')
local_news_flair = 'fcab8c62-9bb8-11ea-8402-0ecb7761c447'
home = str(Path.home())
if (testing):
    home = str(Path.home())+'/bots/cyber_dome'
    log_sub = reddit.subreddit('cyber_dome_dev')
    local_news_flair = '2ec84894-9bb3-11ea-81c1-0e9af13a2ba1'

non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd) #For handling unicode characters
pp = pprint.PrettyPrinter(indent=2)

#print logging output to file
logging.basicConfig(level=logging.INFO,
                    filename=home+'/data/submissions.log',
                    format='%(asctime)s - %(levelname)s - %(message)s')
#print logging output to console
root = logging.getLogger()
root.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
root.addHandler(handler)

domain_set = set()
response = "User..."
post_count = 0
subreddit = reddit.subreddit('all')

logging.info(f'Starting submissions.py v{version}')

with open(home+"/data/reply.txt", "r") as f:
    response = f.read()

with open(home+"/data/sites.txt") as f:
    domain_set = f.readlines()
domain_set = [x.strip() for x in domain_set]
logging.debug(domain_set)

#Watch the submission stream for all of reddit
for submission in subreddit.stream.submissions():
    post_count = post_count+1
    #print(post_count)
    if (post_count % 10000 == 0):
        logging.info(f'Heartbeat {post_count}')
    # Check for exact match on domain and account for subdomains
    if (submission.domain.lower() in domain_set) or (submission.domain.lower().split('.', 1)[1] in domain_set):
    #TODO Fix search in self text
    #(any(substring in submission.selftext.lower() for substring in domain_set)):
        logging.debug(submission.domain)
        logging.info(f"Replying to : {submission.id}, {submission.domain}, {submission.author}, {submission.permalink}")
        try:
            # Reply to the post and report it
            custom_response = 'Hello /u/'+str(submission.author)+',\n\n'+response
            logging.info(f'Replying to: {submission.permalink}')
            submission.reply(custom_response)
            reddit_log(f'Completed reply to {submission.author}: {submission.permalink}', log_thread)
            submission.report("cyber_dome_bot: This website is a fake local journal.  See comment for details")
            logging.info(f'Completed report')
        except Exception as e:
            logging.error(f"Failed to reply to: {submission.permalink} due to error {e}")
            reddit_log(f'ERROR: Failed to reply to {submission.author}: {submission.permalink} /u/CryptoMaximalist {e}', log_thread)
        try:
            # Log the post to r/cyber_dome
            title_limit = (300-(6+len(str(submission.author))+len(str(submission.subreddit))))
            truncated_title = submission.title.translate(non_bmp_map)[:title_limit]
            post_title = str(submission.author)+' in '+str(submission.subreddit)+': '+truncated_title
            post_url = 'https://np.reddit.com'+submission.permalink
            logging.info(f'Logging to post: {submission.permalink}-{post_title}')
            log_sub.submit(post_title, url=post_url, flair_id=local_news_flair)
            reddit_log(f'Completed post for {submission.permalink}-{post_title}', log_thread)
            logging.info(f'Completed post')
        except Exception as e:
            logging.error(f"Failed to log: {submission.permalink} due to error {e}")
            reddit_log(f'ERROR: Failed to log to r/cyber_dome: {submission.author}: {submission.permalink} /u/CryptoMaximalist {e}', log_thread)
