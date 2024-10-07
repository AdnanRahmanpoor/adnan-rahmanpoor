import tweepy
import os
import glob
import re

# auth
auth = tweepy.OAuth1UserHandler(
    os.getenv('TWITTER_API_KEY'),
    os.getenv('TWITTER_API_SECRET_KEY'),
    os.getenv('TWITTER_ACCESS_TOKEN'),
    os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
)

api = tweepy.API(auth)

def get_latest_post():
    post_files = glob.glob("src/content/post/*.md")
    latest_post = max(post_files, key=os.path.getctime)

    with open(latest_post, 'r') as f:
        for line in f:
            if line.startswith('#'):
                post_title = line.strip('#').strip()
                break

                post_slug = re.sub(r'[^a-zA-Z0-9-]', post_title.lower().replace('','-'))
                post_url = f'https://adnanrp.pages.dev/{post_slug}'

            return post_title, post_url
    return None, None

# post tweet

def tweet_new_post(post_title, post_url):
    tweet = f"New Post: {post_title} - Read more at {post_url}"

    api.update_status(tweet)

post_title, post_url = get_latest_post()
tweet_new_post(post_title, post_url)