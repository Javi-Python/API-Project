# API-WSB-Project

<img width="324" alt="Screen Shot 2021-05-03 at 6 17 31 PM" src="https://user-images.githubusercontent.com/1562979/116909245-d914d080-ac3b-11eb-8dce-7e5c17c8458e.png">


This api collects information from r/wallstreetbets, a reddit subreddit deidcated to talking about stocks and finance, and allows users to search by tickers mentioned in post title, search by most mentioned tickers, by sentiment analysis over a certain amount and by sentiment analysis below a certain amount. I hope it is good way to keep up to date with what people are saying with particular stocks.

My hope is to update monthly and track progress of the discussion of different stocks.


# @ GET Endpoints:

Endpoints:

- /

returns instructions for the API.

- /posts/ticker/

With this end point we can search the list of top 1000 posts by ticker. If the ticker is present in the posts title, it will lead you to it.

- /top/

with this end point we can look at a list of the frequency in which tickers appear in posts title, its organized from most to least.

- /sentiment_over/number/

With this end point we can find posts that that have a post title sentiment score over a certain value from -1 to 1.

- /sentiment_less/number/
With this end point we can find posts that that have a post title sentiment score less than a certain value from -1 to 1.


# @ POST Endpoints:

Endpoint:

- /newposts/ <params>

enables people to post new information through the url. 

parameters: 
created, id, title, upvotes, num_comments, comment_body, tickers, datetime, title_sentiment, topcomment_sentiment

