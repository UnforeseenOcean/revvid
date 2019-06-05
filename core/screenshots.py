from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import json


def fetch_screenshots(submission, dump_dir="dump", night_mode=False, limit=50):
    """
    Takes screenshots of all top level comments for a given reddit post.
    Dumps them into the specified dump_dir along with the text each comment has.
    """
    _browser_profile = webdriver.FirefoxProfile()
    _browser_profile.set_preference("dom.webnotifications.enabled", False)
    driver = webdriver.Firefox(firefox_profile=_browser_profile)

    print("Loading page...")
    driver.get(submission.url)

    if submission.over_18:
        yes = driver.find_element_by_class_name("bzs6dt-10")
        yes.click()

    # Enable night mode on reddit
    if night_mode:
        print("Enabling night mode")
        dropdown = driver.find_element_by_id("USER_DROPDOWN_ID")
        dropdown.click()
        night_mode = driver.find_element_by_class_name("bMUmun")
        night_mode.click()
        dropdown.click()  # hide again

    try:
        view_entire_discussion = driver.find_element_by_class_name(
            "j9NixHqtN2j8SKHcdJ0om"
        )
        view_entire_discussion.click()
    except:
        pass

    # LOAD PAGE FULLY

    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(0.3)

        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    driver.execute_script("window.scrollTo(0, 0);")

    driver.find_element_by_class_name("Post").screenshot(f"{dump_dir}/title.png")

    comments = driver.find_elements_by_class_name("top-level")

    _id = 1

    comment_text = {}

    for comment in comments:
        try:
            text = comment.find_element_by_xpath("./div[2]/div[2]").text
            if len(text) > 1000:
                continue
            comment_text[_id] = text
            comment.screenshot(f"{dump_dir}/comment-{_id}.png")
            print("Took screenshot of comment", _id)
            if _id == limit:
                break
            _id += 1
        except NoSuchElementException:
            pass

    driver.quit()
    return comment_text
