from config.configuration import db, collection

def ticker_posts(ticker):
    '''
    Funcion que devuelve todos los posts que incluyen cierto ticker en el titulo.
    '''

    query = {'tickers': f"{ticker}"}
    ticker_posts = list(collection.find(query, {'_id': 0, 'Unnamed: 0' : 0}))
    return ticker_posts


def top_posts():
    '''
    Funcion que devuelve la cuenta de los top tickers mencionados en el titulo del post"
    '''
    count = collection.aggregate([
    { "$group": { "_id": "$tickers", "count": { "$sum": 1 } } }, 
    { "$project":{ "_id": 0, "name": "$_id", "count":"$count" } },
    { '$sort': { 'count': -1}}])
    return list(count)

def title_sentiment_over(number):
    """
    Devuelve los post con un title sentiment arriba de numero eligido,
    de -1 a 1.
    """
    query = {'title_sentiment' : {'$gte' : float(number)}} 
    t_sent = list(collection.find(query, {'_id':0}))
    return t_sent

def title_sentiment_less(number):
    '''
    Devuelve los post con un title sentiment por debajo de numero eligido.
    de -1 a 1.
    '''
    query = {'title_sentiment' : {'$lt' : float(number)}} 
    l_sent = list(collection.find(query, {'_id':0, 'datetime': 0, 'created': 0 }))
    return l_sent