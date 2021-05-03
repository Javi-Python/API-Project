import os
import dotenv
import praw
import pandas as pd



def from_reddit(subreddit, limit):
    client_id = os.getenv('client_id')
    secret = os.getenv('secret')
    user = os.getenv('user')
    dotenv.load_dotenv()
    reddit = praw.Reddit(client_id=client_id, client_secret= secret, user_agent= user)
    hot_posts = reddit.subreddit(f'{subreddit}').top('month', limit=limit)
    df = pd.DataFrame(columns = ['created', 'id', 'title', 'upvotes', 'num_comments', 'comment_body'])
    lista = []
    for post in hot_posts:
        lista.append({ 'created': post.created_utc, 'id': post.id, 'title': post.title, 'upvotes': post.score, 'num_comments': post.num_comments,
                    'comment_body': [comment.body for comment in post.comments if (hasattr(comment, "body") and comment.distinguished==None)][0]})
    return lista