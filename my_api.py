from flask import Flask, request
from flask import jsonify
import json
import markdown.extensions.fenced_code
import tools.getdata as get
import tools.postdata as pos

app = Flask(__name__)


@app.route('/')
def index():
    readme_file = open('README.md', 'r')
    md_template = markdown.markdown(
        readme_file.read(), extensions = ['fenced_code']
    )
    return md_template

@app.route('/posts/<ticker>')
def ticker_posts(ticker):
    ticker_posts = get.ticker_posts(ticker)
    return jsonify(ticker_posts)

@app.route('/top/')
def count_ticker():
    count = get.top_posts()
    return jsonify(count)

@app.route('/sentiment_over/<number>/')
def title_sentiment_over(number):
    t_sent = get.title_sentiment_over(number)
    return jsonify(t_sent)

@app.route('/sentiment_less/<number>/')
def title_sentiment_less(number):
    l_sent = get.title_sentiment_less(number)
    return jsonify(l_sent)

@app.route('/newposts/', methods = ['POST'])
def newposts():
    created = request.args.get("created"), 
    id = request.args.get('id'), 
    token_title = request.args.get("token_title"), 
    upvotes = request.args.get("upvotes"), 
    num_comments = request.args.get("num_comments"), 
    token_comment = request.args.get("token_comment"), 
    tickers = request.args.get("tickers"), 
    datetime = request.args.get("datetime"), 
    title_sentiment = request.args.get("title_sentiment"), 
    topcomment_sentiment = request.args.get("topcomment_sentiment")
    pos.newposts(created, id, token_title, upvotes, num_comments, token_comment, tickers, datetime, title_sentiment, topcomment_sentiment)
    return "You have entered the information"



app.run("0.0.0.0", 5000, debug=True)


