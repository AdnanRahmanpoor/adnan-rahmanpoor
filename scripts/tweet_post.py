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

def get_all_posts():
    # Get the latest post based on creation time
    post_files = glob.glob("src/content/post/*.md")
    posts = []

    for post_file in post_files:    
        with open(post_file, 'r') as f:
            post_title = None
            for line in f:
                # Find the first line starting with '#' (post title)
                if line.startswith('title:'):
                    post_title = line.replace('title:', '').strip()
                    # Create slug from post title
                    post_slug = generate_slug(post_title)
                    post_url = f'https://adnanrp.pages.dev/{post_slug}'
                    break  # Exit the loop after finding the title

    return posts

def get_tweeted_slugs():
    """Read slug of the last tweeted post from the file"""

    if os.path.exists(last_tweeted_file):
        with open(last_tweeted_file, 'r') as f:
            return set(f.read().splitlines())
    return set()

def set_last_tweeted(post_slug):
    """Write the slug of the last tweeted post to the file"""
    with open(last_tweeted_file, 'w') as f:
        f.write('\n'.join(post_slug))


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


posts = get_all_posts()
tweeted_slugs = get_tweeted_slugs()
new_tweeted_slugs = set()

for post_title, post_url, post_slug in posts:
    if post_slug not in tweeted_slugs:
        tweet_new_post(post_title, post_url)
        new_tweeted_slugs.add(post_slug)

tweeted_slugs.update(new_tweeted_slugs)
set_last_tweeted(tweeted_slugs)
