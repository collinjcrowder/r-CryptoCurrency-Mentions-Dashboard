# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 20:10:37 2021
Computational Thinking Final Project
Collin Crowder & Olivia Hellwig
"""

import praw
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import pandas as pd


# Function to strip emojis from comment text
def remove_emojis(string):
    temp_string = ''
    for i in string:
        if (i.isalnum() == False):
            if (i.isspace() == False):
                continue
            else:
                temp_string += i
        else:
            temp_string += i
    return temp_string


# Limit 60 requests per minute on Reddit API
def getReddit():
    reddit = praw.Reddit(client_id='KpG8gVljjtnP_A', 
                         client_secret='9iPH4RUvacgWx-QaIAp1uRrILSEFRA',
                         user_agent='Academic project app')
    # Obtain top 10 post urls for comment extraction
    hot_posts = [] # list to store top weekly post urls
    subreddit = reddit.subreddit("CryptoCurrency")
    f = open("RedditComments.txt", "w+")
    try:
        for post in subreddit.top(params={'t':'week'}, limit=12):
            if "reddit.com" in str(post.url):
                hot_posts.append(post.url)
            else:
                continue
        # top 2 posts are moderator messages, skipped over for comments    
        for x in range(2,len(hot_posts)):
            submission = reddit.submission(url=hot_posts[x])
            try:
                for text in submission.comments:
                    # change comments from HTML to str format
                    comment = ' '.join(BeautifulSoup(text.body_html, 
                                        features="lxml").findAll(text=True))
                    comment_alnum = remove_emojis(comment)
                    f.write(comment_alnum)
            except AttributeError:
                continue
    except:
        print("the Reddit server or Reddit API is down, try again later")        
    f.close()


# Function to generate list of top 500 coins on CoinMarketCap plus technical data
def getCoins():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
        'start': '1',
        'limit': '500',
        'convert': 'USD'
        }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': 'a63c899a-4a26-42a5-9800-182e8cb1db6d'
        }
    session = Session()
    session.headers.update(headers)
        
    coin_data = {}
    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        for i in data['data']:
            # added extra info
            coin_data[i['symbol']] = {'Coin':i['name'],
                                      'Supply':i['circulating_supply'],
                                      'Max Supply': i['max_supply'],
                                      'Quote':i['quote']}
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
    f = open("CoinListing.txt", 'w+')
    f.write(json.dumps(coin_data))
    f.close()
   
    
# function that accepts dict of top 10 coins by mention and grabs 30-day
# historical price data for each of the coins   
def getCoinData(top_ten):
    f = open("HistoricalData.txt", 'w+')
    f.write("{")
    for coin in top_ten:
        url = 'https://rest.coinapi.io/v1/ohlcv/'+coin+'/USD/latest?period_id=1DAY&limit=30&include_empty_items=false'
        headers = {
            'Accepts': 'application/json',
            'X-CoinAPI-Key': 'F104ACDC-83A6-4AF8-999C-F72F8D8251B2'
        }
        session = Session()
        session.headers.update(headers)

        f.write('\"' + coin + '\"' + ':[')
        try:
            response = session.get(url)
            data = json.loads(response.text)
            for day in data:
                f.write('{\"DateTime\":\"'+str(day['time_period_start'])
                        +'\",\"Close Price\":\"'+str(day['price_close'])+'\"}')
                if day == data[-1]:
                    continue
                else:
                    f.write(',')                
        except (ConnectionError, Timeout, TooManyRedirects) as e:
                print(e)
        last = list(top_ten.keys())[-1]
        if coin == last:
            f.write(']}')
        else:
            f.write('],')
    f.close()   
    
    
# Function that searches comment text, checks if a word is in the coin listing
# and then counts mentions, exlcudes common non-coin phrases/words, returns
# a dict of top 10 coins with number of mentions  
def find_mentions():
    mentions = {}
    top_ten = {}
    dummy_words = ['A', 'HODL', 'DD', 'ATH', 'IT', 'LOCK', 'APR', 'GME', 'IMO',
                   'MANY', 'NOW', 'BUT', 'AND', 'ALT', 'ID', 'ETF', 'FUD', 
                   'FOMO', 'TV', 'CUZ', 'CPU', 'GPU', 'APY', 'PC', 'OK', 'IQ',
                   'ANY', 'KCS']
    d = open('CoinListing.txt')
    raw_data = d.read()
    coin_data = json.loads(raw_data)
    f = open('RedditComments.txt', 'r')
    for comment in (line.strip().split() for line in f.readlines()):
        if type(comment) == list:
            for word in comment:
                if (word in coin_data) and (word not in dummy_words):
                    if word in mentions:
                        mentions[word] += 1
                    else:
                        mentions[word] = 1
                else:
                    continue
        elif comment in coin_data:
            if comment in mentions:
                mentions[comment] += 1
            else:
                mentions[comment] = 1
        else:
            continue
    f.close()
    d.close()
    for x in range(10):    
        top_coin = max(mentions, key=mentions.get)
        top_ten[top_coin] = mentions[top_coin]
        del mentions[top_coin]    
    return top_ten


# iterates through coin's price and date data, cleans and sorts it, and runs
# the Chart() function for each coin and its data
def Plotter(): 
    f = open("HistoricalData.txt")
    raw = f.read()
    coin_data = json.loads(raw)
    top_ten = list(find_mentions().keys())
    dates = []
    prices = []
    for coin in top_ten:
        date_temp = []
        price_temp = []
        for date_list in coin_data[coin]:
            date_temp.append(date_list['DateTime'][:10])
            price_temp.append(float(date_list['Close Price']))
        date_temp.reverse()
        price_temp.reverse()
        dates.append(date_temp)
        prices.append(price_temp)
    for i in range(0,10):
        Chart(dates[i], prices[i], top_ten[i], i+1)
    f.close()
  
# Generates a single time-series price chart for each coin passed as an argument    
def Chart(dates, prices, coin, count):
    plt.rcParams.update({"lines.color": "white", "patch.edgecolor": "white",
                         "text.color": "black", "axes.facecolor": "white",
                         "axes.edgecolor": "lightgray", "axes.labelcolor": "white",
                         "xtick.color": "white", "ytick.color": "white",
                         "grid.color": "lightgray", "figure.facecolor": "black",
                         "figure.edgecolor": "black", "savefig.facecolor": "black",
                         "savefig.edgecolor": "black"})
    start_date = dates[0]
    ds = pd.date_range(start=start_date, periods=30)
    df = pd.DataFrame(data=prices, index=ds)
    chart=df.plot(kind='line', figsize=(16,8), color="#ebb734")
    plt.xlabel("Date of Closing Price")
    plt.ylabel("Value in $USD")
    plt.title(f"30-Day Closing Price of {coin}", color='white')
    chart.set_alpha(1.0)
    chart.patch.set_facecolor('black')
    if int(prices[0]) > 100:
        form = '${x:,.0f}'
        tick = mtick.StrMethodFormatter(form)
        chart.yaxis.set_major_formatter(tick) 
    elif int(prices[0]) > 1:
        form = '${x:,.2f}'
        tick = mtick.StrMethodFormatter(form)
        chart.yaxis.set_major_formatter(tick) 
    else:
        form = '${x:,.4f}'
        tick = mtick.StrMethodFormatter(form)
        chart.yaxis.set_major_formatter(tick) 
    fig = chart.get_figure()
    title = "Chart{0}.PNG".format(count)
    fig.savefig(title)
    plt.clf()
