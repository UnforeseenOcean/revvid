import os
import time
import json

from selenium import webdriver
import praw



reddit = praw.Reddit(
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    user_agent="Reddit Video Bot",
)

sub = reddit.subreddit("askreddit")
hot = list(sub.hot(limit=10))

print('Hot posts for today: \n')

for i, s in enumerate(hot):
    print(f'[{i}]: {s.title}')

index = int(input('\nSelect one: '))
submission = hot[index]

# Disable notifications
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)

driver = webdriver.Chrome(options=chrome_options)
driver.get(submission.url)

if submission.over_18:
    yes = driver.find_element_by_class_name('bzs6dt-10')
    yes.click()

# Enable night mode on red
dropdown = driver.find_element_by_id('USER_DROPDOWN_ID')
dropdown.click()
night_mode = driver.find_element_by_class_name('bMUmun')
night_mode.click()
dropdown.click() # hide again

try:
    view_entire_discussion = driver.find_element_by_class_name('j9NixHqtN2j8SKHcdJ0om')
    view_entire_discussion.click()
except:
    pass

image = driver.find_element_by_class_name('Post').screenshot('img/post.png')


# LOAD PAGE FULLY

last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(0.1)

    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

comments = driver.find_elements_by_class_name('top-level')

id = 1 

comment_text = {}

for comment in comments:
    text = comment.find_element_by_class_name('_3cjCphgls6DH-irkVaA0GM').text
    img_path = f'img/comment-{id}.png'
    comment_text[img_path] = text
    comment.screenshot(img_path)
    id += 1

with open('img/comment_text.json') as f:
    json.dump(comment_text, f)



