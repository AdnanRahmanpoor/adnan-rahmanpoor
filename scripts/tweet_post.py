import tweepy
import os
import glob
import re

last_tweeted_file = 'last_tweeted.txt'


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
    print(f"Slug from generate slug func: {slug}")
    return slug

def get_all_posts():
    """Retrieve all posts and their titles, URLs, and slugs."""
    post_files = glob.glob("src/content/post/*.md")
    posts = []

    for post_file in post_files:    
        with open(post_file, 'r') as f:
            post_title = None
            for line in f:
                # Find the title line in the markdown file
                if line.startswith('title:'):
                    post_title = line.replace('title:', '').strip()
                    # Create slug from post title
                    post_slug = generate_slug(post_title)
                    post_url = f'https://adnanrp.pages.dev/{post_slug}'
                    posts.append((post_title, post_url, post_slug))
                    print(f"Posts: {posts}")
                    break  # Exit the loop after finding the title

    return posts

def get_tweeted_slugs():
    """Read slugs of the previously tweeted posts from the file."""
    if os.path.exists(last_tweeted_file):
        with open(last_tweeted_file, 'r') as f:
            print(f)
            return set(f.read().splitlines())  # Return a set of slugs for quick lookup
    return set()

def append_new_tweeted_slugs(new_slugs):
    """Write the slugs of all tweeted posts to the file."""
    with open(last_tweeted_file, 'a') as f:
        for slug in new_slugs:
            f.write(f'{slug}\n')
            print(f"Tweeted slugs: {f}")


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


# Get all posts
posts = get_all_posts()

# Get slugs of previously tweeted posts
tweeted_slugs = get_tweeted_slugs()

# Set to store newly tweeted slugs
new_tweeted_slugs = set()

# Iterate through posts and tweet any new ones
for post_title, post_url, post_slug in posts:
    if post_slug not in tweeted_slugs:
        # New post detected, tweet it
        tweet_new_post(post_title, post_url)
        new_tweeted_slugs.add(post_slug)

# Append the slugs file with newly tweeted slugs
if new_tweeted_slugs:
    append_new_tweeted_slugs(new_tweeted_slugs)
