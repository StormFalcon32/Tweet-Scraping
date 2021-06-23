import json
import math
import time
from datetime import datetime, timedelta
from email.utils import parsedate_tz

from searchtweets import collect_results, gen_rule_payload, load_credentials


def to_datetime(datestring):
    time_tuple = parsedate_tz(datestring.strip())
    dt = datetime(*time_tuple[:6])
    return dt - timedelta(seconds=time_tuple[-1])


premium_search_args = load_credentials(r'C:\Data\Python\Twitter\twitter_keys_free.yaml',
                                       yaml_key="search_tweets_premium",
                                       env_overwrite=False)


# def scrape_tweets(keyword, low, high):
#     tweet_dict = {}
#     num = 0
#     while low < high:
#         results_per_call = 100
#         max_results = 100
#         pt_rule = keyword + ' lang:en'
#         low_string = low.strftime('%Y%m%d%H%M')
#         high_string = high.strftime('%Y%m%d%H%M')
#         rule = gen_rule_payload(pt_rule=pt_rule, from_date=low_string, to_date=high_string, results_per_call=results_per_call)
#         premium_search_args['tweetify'] = False
#         tweets = collect_results(rule, max_results=max_results, result_stream_args=premium_search_args)
#         if tweets == []:
#             break
#         end = to_datetime(tweets[len(tweets) - 1]['created_at'])
#         for tweet in tweets:
#             if tweet['lang'] != 'en':
#                 continue
#             tweet_dict[num] = tweet
#             num += 1
#         high = end - timedelta(seconds=1)
#         print(num)
#         print(high)
#         delay = max_results / results_per_call
#         time.sleep(delay)
#     with open('tweets1early.json', 'w', encoding='utf-8') as f:
#         json.dump(tweet_dict, f)


def scrape(keyword, low, high):
    tweet_dicts = []
    results_per_call = 100
    max_results = 5000
    pt_rule = keyword + ' lang:en'
    low_string = low.strftime('%Y%m%d%H%M')
    high_string = high.strftime('%Y%m%d%H%M')
    rule = gen_rule_payload(pt_rule=pt_rule, from_date=low_string, to_date=high_string, results_per_call=results_per_call)
    premium_search_args['tweetify'] = False
    tweets = collect_results(rule, max_results=max_results, result_stream_args=premium_search_args)
    for tweet in tweets:
        if tweet['lang'] != 'en':
            continue
        tweet_dicts.append(tweet)
    print('Dumping')
    with open('tweets.json', 'w', encoding='utf-8') as f:
        json.dump(tweet_dicts, f)

# update key directory in code - good
# update endpoint URL - good
# update start and end date - good
# update results per call and max results - good
# update keyword


if __name__ == '__main__':
    keyword = '''("lost my job" OR "laid me off" OR "I have been laid off" OR "I\'ve been laid off" OR "I got laid off" OR "I was laid off" OR "I am laid off" OR "Iam laid off" OR "I am being laid off" OR "I got on unemployment" OR "I am on unemployment" OR "I am going on unemployment" OR "I am getting on unemployment" OR "I went on unemployment" OR "I have been on unemployment" OR "I\'ve been on unemployment" OR "Iam on unemployment" OR "I am unemployed" OR "I have been unemployed" OR "I\'ve been unemployed" OR "Iam unemployed" OR "I got unemployed" OR "I don\'t have a job" OR "I dont have a job" OR "I do not have a job") (profile_country:US OR place_country:US)'''
    # keyword = 'telehealth (physicaltherapy OR "physical therapy")'
    # keyword = 'telehealth (athletictrainer OR "athletic trainer")'
    # keyword = 'telerehabilitation'
    low = datetime(year=2020, month=4, day=1)
    high = datetime(year=2020, month=6, day=1)
    scrape(keyword, low, high)