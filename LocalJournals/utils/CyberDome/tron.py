import os
import praw
import csv
from datetime import datetime, timedelta
import time

reddit = praw.Reddit(client_id='',
                     client_secret="", password='',
                     user_agent='CYBERDOME', username='Tron_I_Fight_4_Users')

response = "User..."

with open("reply.txt", "r") as f:
    response = f.read()
        
while (True):
    yesterday = datetime.utcnow() - timedelta(days=1)
    print(datetime.utcnow())
    with open("../../sites.csv") as csvfile:
        filereader = csv.DictReader(csvfile)
        for row in filereader:
            
            posts = reddit.domain(row["domain"]).new(limit=10)
            
            # Have we run this domain before? If not, create an empty list
            if not os.path.isfile("domains/" + row["domain"] + ".txt"):
                posts_replied_to = []
            # If we have run the code before, load the list of posts we have replied to
            else:
                # Read the file into a list
                with open("domains/" + row["domain"] + ".txt", "r") as f:
                    posts_replied_to = f.read()
                    posts_replied_to = posts_replied_to.split("\n")
                    posts_replied_to = list(filter(None, posts_replied_to))

            for post in posts:
                # If we haven't replied to this post before
                if post.id not in posts_replied_to:
                    post_date = datetime.fromtimestamp(post.created_utc)
                    
                    if post_date > yesterday:
                        # Reply to the post
                        print("Replying to : ", post.id, post.author, post.permalink, post_date)
                        post.reply(response)

                        # Store the current id into our list
                        posts_replied_to.append(post.id)
        
                        # Write our updated list back to the file
                        with open("domains/" + row["domain"] + ".txt", "w") as f:
                            for post_id in posts_replied_to:
                                f.write(post_id + "\n")
                                
                        # wait 10 minutes
                        time.sleep(60.0 * 10.0)