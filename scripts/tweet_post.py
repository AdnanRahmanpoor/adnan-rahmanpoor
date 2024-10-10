import tweepy
import os
import glob
import re

last_tweeted_file = 'last_tweeted.txt'

# setting api to 2.0
api = tweepy.Client(
    os.getenv('bearer_token'),
    os.getenv('consumer_key'),
    os.getenv('consumer_secret'),
    os.getenv('access_token'),
    os.getenv('token_secret')
    )

def generate_slug(title):
    """
    Generate slug similar to AstroJS:
    - Converts to lowercase
    - Replaces spaces with hyphens
    - Removes special characters except hyphens
    - Condenses multiple hyphens into one
    """
    slug = title.lower()
    slug = slug.replace(' ', '-')
    slug = re.sub(r'[^a-z0-9-]', '', slug)
    slug = re.sub(r'-+', '-', slug)

    return slug

def get_latest_post():
    # Get the latest post based on creation time
    post_files = glob.glob("src/content/post/*.md")
    latest_post = max(post_files, key=os.path.getctime)

    post_title = None
    post_url = None
    post_slug = None

    with open(latest_post, 'r') as f:
        for line in f:
            # Find the first line starting with '#' (post title)
            if line.startswith('title:'):
                post_title = line.replace('title:', '').strip()
                # Create slug from post title
                post_slug = generate_slug(post_title)
                post_url = f'https://adnanrp.pages.dev/{post_slug}'
                break  # Exit the loop after finding the title

    # Ensure post_title and post_url are initialized properly
    if post_title and post_url and post_slug:
        return post_title, post_url, post_slug
    else:
        return None, None, None

def get_last_tweeted():
    """Read slug of the last tweeted post from the file"""

    if os.path.exists(last_tweeted_file):
        with open(last_tweeted_file, 'r') as f:
            return f.read().strip()
    return None

def set_last_tweeted(post_slug):
    """Write the slug of the last tweeted post to the file"""
    with open(last_tweeted_file, 'w') as f:
        f.write(post_slug)


# Post tweet
def tweet_new_post(post_title, post_url):
    if post_title and post_url:
        tweet = f"New Post: {post_title} - Read more at {post_url}"
        try:
            api.create_tweet(text=tweet)
            print(f'Tweeted: {tweet}')
        except Exception as e:
            print(f'Failed to tweet: {e}')
    else:
        print("No post found to tweet.")

# Get the latest post title and URL
post_title, post_url, post_slug = get_latest_post()
last_tweeted = get_last_tweeted()

if post_slug and post_slug != last_tweeted:
    tweet_new_post(post_title, post_url)
    set_last_tweeted(post_slug)
else:
    print("No new post to tweet.")

