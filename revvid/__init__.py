import os
import sys
import time
import json

import praw

from .screenshots import fetch_screenshots
from .audio import generate_audio
from .video import composite_video

import click


if "dump" not in os.listdir():
    os.mkdir("dump")

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent="Reddit Video Bot",
)


def interactive(subname):
    sub = reddit.subreddit(subname)
    hot = list(sub.hot(limit=10))
    print("Hot posts right now:\n")
    for i, s in enumerate(hot):
        print(f"[{i}]: {s.title}")
    index = int(input("\nSelect one: "))
    return hot[index]


@click.command()
@click.option("-p", "--postid", help="The post ID to generate the video from")
@click.option(
    "-s",
    "--subreddit",
    help="The subreddit to display hot posts from.",
    default="askreddit",
)
@click.option(
    "-o",
    "--out",
    help="The file path to output the video to.",
    default="video.mp4",
    type=click.Path(file_okay=True),
)
@click.option("-l", "--limit", help="The amount of comments to process.", default=10, type=int)
@click.option(
    "--night-mode",
    help="Whether or not the screenshots are in night mode",
    default=True,
    type=bool,
)
@click.option("--title", help="The text to prepend to the submission title.")
@click.option("--outro", help="The outro text to be spoken.")
@click.option(
    "--bg-music", help="Supply your own background music", type=click.Path(exists=True)
)
@click.option(
    "--transition",
    help="Supply your own tv static transition",
    type=click.Path(exists=True),
)
def main(postid, subreddit, out, limit, title, outro, bg_music, transition, night_mode):
    if not postid:
        submission = interactive(subreddit)
    else:
        submission = praw.models.Submission(reddit, id=postid)
        print("Fetching screenshots from:", submission.title)

    comment_text = fetch_screenshots(submission, night_mode=True, limit=limit)
    title_text = (title or "r slash ask reddit... ") + submission.title
    generate_audio(
        title=title_text,
        comment_text=comment_text,
        outro=outro
        or "Thanks for watching mate, make sure to smash "
        "that star button for more low quality content.",
    )
    composite_video(out, bg_music, transition)
