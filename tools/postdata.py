from config.configuration import db, collection

def newposts(created, id, token_title, upvotes, num_comments, token_comment, tickers, datetime, title_sentiment, topcomment_sentiment):
    dict_insert = {'created': created,
    'id': id,
    'token_title' : token_title,
    'upvotes' : upvotes,
    'num_comments' : num_comments,
    'token_comment' : token_comment,
    'tickers' : tickers,
    'datetime' : datetime,
    'title_sentiment' : title_sentiment,
    'topcomment_sentiment' : topcomment_sentiment
    }
    collection.insert_one(dict_insert)