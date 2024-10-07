import tweepy
import os
import glob
import re

# auth
auth = tweepy.OAuth1UserHandler(
    os.getenv('consumer_key'),
    os.getenv('consumer_secret'),
    os.getenv('access_token'),
    os.getenv('token_secret')
)

api = tweepy.API(auth)

def get_latest_post():
    # Get the latest post based on creation time
    post_files = glob.glob("src/content/post/*.md")
    latest_post = max(post_files, key=os.path.getctime)

    post_title = None
    post_url = None

    with open(latest_post, 'r') as f:
        for line in f:
            # Find the first line starting with '#' (post title)
            if line.startswith('#'):
                post_title = line.strip('#').strip()
                # Create slug from post title
                post_slug = re.sub(r'[^a-zA-Z0-9-]', '', post_title.lower().replace(' ', '-'))
                post_url = f'https://adnanrp.pages.dev/{post_slug}'
                break  # Exit the loop after finding the title

    # Ensure post_title and post_url are initialized properly
    if post_title and post_url:
        return post_title, post_url
    else:
        return None, None

# Post tweet
def tweet_new_post(post_title, post_url):
    if post_title and post_url:
        tweet = f"New Post: {post_title} - Read more at {post_url}"
        api.create_tweet(tweet)
    else:
        print("No post found to tweet.")

# Get the latest post title and URL
post_title, post_url = get_latest_post()
tweet_new_post(post_title, post_url)
