import csv
import json

for num in range(1, 5):
    with open('Telehealth/tweets%slate.json' % num) as f:
        json_data = json.load(f)
    data = [['id', 'text', 'username', 'timestamp', 'tweet_type', 'num_retweets', 'num_likes', 'hashtags', 'mentions', 'place_name', 'long1', 'long2', 'long3', 'long4', 'lat1', 'lat2', 'lat3', 'lat4']]
    for tweet in json_data:
        tweet_id = tweet['id']
        text = tweet['text']
        username = tweet['user']['screen_name']
        timestamp = tweet['created_at']
        tweet_type = 'tweet'
        if tweet['is_quote_status']:
            tweet_type = 'quote'
        elif 'retweeted_status' in tweet:
            tweet_type = 'retweet'
        num_retweets = tweet['retweet_count']
        num_likes = tweet['favorite_count']
        place_name = 'none'
        longs = ['none', 'none', 'none', 'none']
        lats = ['none', 'none', 'none', 'none']
        if tweet['place']:
            place_name = tweet['place']['full_name']
            longs = [tweet['place']['bounding_box']['coordinates'][0][i][0] for i in range(4)]
            lats = [tweet['place']['bounding_box']['coordinates'][0][i][1] for i in range(4)]
        hashtags = ''
        mentions = ''
        if 'extended_tweet' in tweet:
            text = tweet['extended_tweet']['full_text']
            hashtags = ' '.join([tweet['extended_tweet']['entities']['hashtags'][i]['text'] for i in range(len(tweet['extended_tweet']['entities']['hashtags']))])
            mentions = ' '.join([tweet['extended_tweet']['entities']['user_mentions'][i]['screen_name'] for i in range(len(tweet['extended_tweet']['entities']['user_mentions']))])
        if 'retweeted_status' in tweet:
            if 'extended_tweet' in tweet['retweeted_status']:
                text = tweet['retweeted_status']['extended_tweet']['full_text']
                hashtags = ' '.join([tweet['retweeted_status']['extended_tweet']['entities']['hashtags'][i]['text'] for i in range(len(tweet['retweeted_status']['extended_tweet']['entities']['hashtags']))])
                mentions = ' '.join([tweet['retweeted_status']['extended_tweet']['entities']['user_mentions'][i]['screen_name'] for i in range(len(tweet['retweeted_status']['extended_tweet']['entities']['user_mentions']))])
            else:
                text = tweet['retweeted_status']['text']
                hashtags = ' '.join([tweet['retweeted_status']['entities']['hashtags'][i]['text'] for i in range(len(tweet['retweeted_status']['entities']['hashtags']))])
                mentions = ' '.join([tweet['retweeted_status']['entities']['user_mentions'][i]['screen_name'] for i in range(len(tweet['retweeted_status']['entities']['user_mentions']))])
        row = [tweet_id, text, username, timestamp, tweet_type, num_retweets, num_likes, hashtags, mentions, place_name]
        row.extend(longs)
        row.extend(lats)
        data.append(row)
    with open('Telehealth/tweets%slate.csv' % num, mode='w', encoding='utf-8') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerows(data)