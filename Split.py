import json

with open('tweets.json', encoding='utf-8') as f:
    data = json.load(f)

print(len(data))
datalist = [{}, {}, {}, {}, {}]
num_dict = 0
num_tweets = 0
for num in range(0, len(data)):
    datalist[num_dict][num] = data[str(num)]
    if num_tweets == 29344:
        num_dict += 1
        num_tweets = 0
    else:
        num_tweets += 1
ind = 0
for i in datalist:
    with open('tweets%s.json' % ind, 'w', encoding='utf-8') as f:
        json.dump(i, f)
    ind += 1
