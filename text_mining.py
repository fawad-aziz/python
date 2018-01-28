import tweepy, codecs
from aylienapiclient import textapi
import csv, io, time
import matplotlib.pyplot as plt 
import pandas as pd
from collections import Counter

# consumer_key = 'B4iW9VALsCTp6PcpK0Gc2wcgH'
# consumer_secret = 'xwHE2lurMfBEm5SUE0UYCaR7fJVuSoGRbrIywaEgOWPF9vg9J3'
# access_token = '818087845265018881-c6dqe2pfsWsvnKQs1S9C8p8WxGSP0Sd'
# access_token_secret = 'ByaBKi9t30pz8O88RtvQIMxrtjkq00nmyWUg5J5oZuzX0'

# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)

# api = tweepy.API(auth)

# results = api.search(q="ikea", lang="en", result_type="recent", count=1000)

# file = codecs.open("tweets.txt", "w", "utf-8")
# for result in results:
#     file.write(result.text)
#     file.write("\n")
# file.close()

# client = textapi.Client("7cc9dd6d", "c853eef8aad10c1525306c40933ff092")
# sentiment = client.Sentiment({'text': 'i am feeling happy'})
# print(sentiment)

# with io.open("ikea_tweets.csv", "w", encoding="utf-8", newline='') as csvfile:
#     csv_writer = csv.writer(csvfile)
#     csv_writer.writerow(["Tweet", "Sentiment"])
#     with io.open("tweets.txt", "r", encoding="utf-8") as f:
#         for tweet in f.readlines():
#             tweet = tweet.strip()

#             if len(tweet) == 0:
#                 print("skipped")
#                 continue

#             print(tweet)

#             time.sleep(2)
#             sentiment = client.Sentiment({'text': tweet})

#             csv_writer.writerow([sentiment['text'], sentiment['polarity']])

## open up your csv file with the sentiment results
with open('ikea_tweets.csv', 'r', encoding = 'utf8') as csvfile:
	## use Pandas to read the “Sentiment” column,
    df = pd.read_csv(csvfile)
    sent = df["Sentiment"]

    ## use Counter to count how many times each sentiment appears
    ## and save each as a variable
    counter = Counter(sent)
    positive = counter['positive']
    negative = counter['negative']
    neutral = counter['neutral']

## declare the variables for the pie chart, using the Counter variables for “sizes”
labels = 'Positive', 'Negative', 'Neutral'
sizes = [positive, negative, neutral]
colors = ['green', 'red', 'grey']
yourtext = "Your Search Query from Step 2"

## use matplotlib to plot the chart
plt.pie(sizes, labels = labels, colors = colors, shadow = True, startangle = 90)
plt.title("Sentiment of 200 Tweets about "+yourtext)
plt.show()