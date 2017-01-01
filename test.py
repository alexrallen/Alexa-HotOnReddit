
import praw
        
        
r=praw.Reddit(user_agent="RedditCrawler", client_id="AmkrdaOoDkFM4Q", client_secret="-mKg45kDIKdz0ijiV9bxdO1VmsI")

try:
	subreddit=r.subreddit("asdfansdfba")
except:
	

for submission in subreddit.hot(limit=10):
	print(submission.title)
        
