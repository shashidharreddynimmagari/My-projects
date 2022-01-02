from textblob import TextBlob
# tweepy is a library used for accessing twitter API
import tweepy
import sys

api_key='*********************'
api_key_secret= '************************'
access_token = '***********************'
access_token_secret = '********************'

#accessing the keys and tokens
auth_handler = tweepy.OAuthHandler(consumer_key = api_key,consumer_secret=api_key_secret)
auth_handler.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth_handler)

search_term = 'cardano'
tweet_amount = 100

tweets = tweepy.Cursor(api.search, q=search_term, lang='en').items(tweet_amount)

polarity = 0

positive = 0
negative = 0
neutral = 0

for tweet in tweets:
    # print(tweet.text)
    #data cleaning(tweets starting with RT and @ are removed)
    final_text = tweet.text.replace('RT', '')
    if final_text.startswith(' @'):
        position = final_text.index(':')
        final_text = final_text[position+2:]
    if final_text.startswith('@'):
        position = final_text.index('')
        final_text = final_text[position+2:]
    #print(final_text)
    #count of positive negative and neutral tweets
    #TextBlob is used to process textual data. provide api for NLP tasks like pos tagging, sentiment analysis, noun phrase extraction etc.
    analysis = TextBlob(final_text)
    tweet_polarity = analysis.polarity
    if tweet_polarity > 0:
        positive += 1
    elif tweet_polarity < 0:
        negative += 1
    else:
        neutral += 1
    #polarity += analysis.polarity
    polarity += tweet_polarity
    print(final_text)

print(polarity)
print(f'Amount of positive tweets: {positive}')
print(f'Amount of negative tweets: {negative}')
print(f'Amount of neutral tweets: {neutral}')
