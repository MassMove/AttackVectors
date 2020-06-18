#!/usr/bin/python3
# Mailbox function for the bot to check replies and DMs.  Currently only used for ping responses
import logging
import pprint
import praw
import sys
from pathlib import Path

def replyToUser(message, body):
    try:
        message.mark_read()
        message.reply(body)
        reddit_log(f'Completed reply to {message.author}: {body}, {message.body}', log_thread)
        logging.info(f'Completed reply to {message.author}')
    except Exception as e:
        print('Problem replying to the user')
        reddit_log(f'ERROR: Failed to reply to {message.author}: {body}, {message.body}', log_thread)
        logging.error(f'Failed reply to message.author')
    return

def reddit_log(log_text, thread_id):
    log_thread = reddit.submission(id=thread_id)
    print(f"log_output: {thread_id}-{log_text}")
    log_thread.reply(log_text)
    return


bot = 'cyber_dome_bot'
reddit = praw.Reddit(bot)
testing = False
home = str(Path.home())
if (testing):
    home = str(Path.home())+'/bots/cyber_dome'

pp = pprint.PrettyPrinter(indent=2)

#print logging output to file
logging.basicConfig(level=logging.INFO,
                    filename=home+'/data/mailbox.log',
                    format='%(asctime)s - %(levelname)s - %(message)s')
#print logging output to console
root = logging.getLogger()
root.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
root.addHandler(handler)

log_thread = 'gdp9bv'
inbox = []
domain_list = []


for message in reddit.inbox.unread():
  inbox.append(message)

if len(inbox) == 0:
  print('Mailbox empty, quitting...')
  sys.exit()

for message in reddit.inbox.unread():
    reddit.subreddit("crypto_dome_dev").message("FWD: ", "test message from PRAW")
    if (not message.was_comment):
        logging.debug('Got a DM')
        if (message.subject.lower() == 'ping'):
            #For checking if the bot is still running
            logging.info('Replying to ping')
            replyToUser(message, 'pong')
    else:
        logging.warning('Got a post reply but not setup to handle that yet.  '+vars(message))
