from pprint import pprint
import pandas as pd
import nltk
import praw
import seaborn as sns
from matplotlib import pyplot as plt

nltk.download('vader_lexicon')

user_agent = "ConfusedScraper 0.1 by /u/CobaltDoofus"
reddit = praw.Reddit(
    client_id="q-47jXqN4JQs6XBMWyzsWw",
    client_secret="-U6J92hdsT8vTD2L9kMGWLqiN46AJg",
    user_agent=user_agent
)

headlines = set()
for submission in reddit.subreddit('CryptoCurrency').hot(limit=None):
    headlines.add(submission.title)
print(len(headlines))

df = pd.DataFrame(headlines)

df.to_csv('redditHeadlines.csv',header=False,encoding='utf-8', index=False)


from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA

sia = SIA()
results=[]

for line in headlines:
    pol_score = sia.polarity_scores(line)
    pol_score['headline'] = line
    results.append(pol_score)

pprint(results[:3],width=100)

df = pd.DataFrame.from_records(results)

df['label'] = 0
df.loc[df['compound'] > 0.2,'label'] = 1
df.loc[df['compound'] < -0.2,'label'] = -1

df.head()

df.to_csv('redditHeadlinesWLabels.csv',header=False,encoding='utf-8', index=False)

fix,ax = plt.subplots(figsize=(8,8))
counts = df.label.value_counts(normalize=True)*100

sns.barplot(x=counts.index,y=counts,ax=ax)

ax.set_xlabel(['Negative','Neutral','Positive'])
ax.set_ylabel("Percentage")

plt.show()
