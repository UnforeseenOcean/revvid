import os
import sys
import time
import json

import praw
from core.aggregate import fetch_screenshots


if 'dump' not in os.listdir():
    os.mkdir('dump')

reddit = praw.Reddit(
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    user_agent="Reddit Video Bot",
)

if len(sys.argv) > 1:
    submission = praw.models.Submission(reddit, id=sys.argv[1])
    print('Fetching screenshots from:', submission.title)
else:
    sub = reddit.subreddit("askreddit")
    hot = list(sub.hot(limit=10))

    print('Hot posts for today: \n')

    for i, s in enumerate(hot):
        print(f'[{i}]: {s.title}')

    index = int(input('\nSelect one: '))
    submission = hot[index]

fetch_screenshots(submission)
print('Done.')




