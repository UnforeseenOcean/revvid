import os
import sys
import time
import json

import praw

from core.screenshots import fetch_screenshots
from core.audio import generate_audio
from core.video import composite_video


if "dump" not in os.listdir():
    os.mkdir("dump")

reddit = praw.Reddit(
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    user_agent="Reddit Video Bot",
)

if len(sys.argv) > 1:
    submission = praw.models.Submission(reddit, id=sys.argv[1])
    print("Fetching screenshots from:", submission.title)
else:
    sub = reddit.subreddit("askreddit")
    hot = list(sub.hot(limit=10))

    print("Hot posts for today: \n")

    for i, s in enumerate(hot):
        print(f"[{i}]: {s.title}")

    index = int(input("\nSelect one: "))
    submission = hot[index]

if __name__ == "__main__":
    comment_text = fetch_screenshots(submission, night_mode=True, limit=3)
    title_text = 'r slash ask reddit... ' + submission.title # lol
    generate_audio(title_text, comment_text, end='Thanks for watching, make sure to like and subscribe since I am not a bot lol, you are.')
    composite_video()
    print("Done.")
