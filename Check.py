import json


tweets1 = []
with open('Telehealth/tweets1.json', encoding='utf-8') as f:
        tweets1 = json.load(f)
good = 0
for tweet in tweets1:
    text = tweet['text']
    tweet_id = tweet['id']
    if 'extended_tweet' in tweet:
        text = tweet['extended_tweet']['full_text']
    if 'retweeted_status' in tweet:
        if 'extended_tweet' in tweet['retweeted_status']:
            text = tweet['retweeted_status']['extended_tweet']['full_text']
        tweet_id = tweet['retweeted_status']['id']
    text = text.lower()
    if tweet_id == 1257731821170819075 or tweet_id == 1258065155021090817 or tweet_id == 1258094532471767040 or tweet_id == 1258402496478920704 or tweet_id == 1258502123345645571 or tweet_id == 1258834354622599169 or tweet_id == 1259202848165892102 or (('telehealth' in text or 'telepractice' in text) and ('slp' in text or 'slpeeps' in text or 'speechtherapy' in text or 'speech therapy' in text)):
        good += 1
    else:
        print('https://twitter.com/user/status/%s' % tweet_id)
print('%s / %s' % (good, len(tweets1)))