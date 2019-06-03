import os

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

if submission.over18:
    yes = driver.find_element_by_class_name('bzs6dt-10')
    yes.click()

# Enable night mode on red
dropdown = driver.find_element_by_id('USER_DROPDOWN_ID')
dropdown.click()
night_mode = driver.find_element_by_class_name('bMUmun')
night_mode.click()
dropdown.click() # hide again


view_entire_discussion = driver.find_element_by_class_name('j9NixHqtN2j8SKHcdJ0om')
view_entire_discussion.click()

image = driver.find_element_by_class_name('Post').screenshot('images/post.png')

comments = driver.find_elements_by_class_name('top-level')

id = 1 

for comment in comments:
    comment.screenshot(f'images/comment-{id}.png')
    id += 1


