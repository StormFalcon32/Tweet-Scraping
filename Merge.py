import json


tweets = {}
for i in range(5):
    with open('tweets%s.json' % i, encoding='utf-8') as f:
        tweets.update(json.load(f))
with open('tweetsmerged.json', 'w', encoding='utf-8') as f:
    json.dump(tweets, f)