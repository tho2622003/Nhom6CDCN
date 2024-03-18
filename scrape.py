import time
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

data = []
youtube_video_url = "https://www.youtube.com/watch?v=f_fuHRyQbOc"

option = webdriver.ChromeOptions()
option.add_argument('--headless')
option.add_argument("--mute-audio")
option.add_argument("--disable-extensions")
option.add_argument('-disable-dev-shm-usage')

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 5)
driver.set_window_size(960, 800)

time.sleep(1)
driver.get(youtube_video_url)
time.sleep(2)
pause = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'ytp-play-button')))
pause.click()
time.sleep(0.2)
pause.click()
time.sleep(4)
comment_content_css_selector = "#content-text, .style-scope ytd-comment-renderer"

for item in range(10):
    wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
time.sleep(15)

for comment_element in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, comment_content_css_selector))):
    comment_content_text = comment_element.text
    data.append(comment_content_text.split('\n'))

driver.quit()

username = []
likecount = []
commentdate=[]
commenttext=[]

flat_data = [comment for sublist in data for comment in sublist]

for item in flat_data:
    if "@" in item and len(item) < 20:
        username.append(item)
    elif len(item) < 5:
        likecount.append(item)
    elif "years ago" in item or "months ago" in item or "weeks ago" in item:
        commentdate.append(item)
    elif item == "Reply" or item == "":
        pass
    else: 
        commenttext.append(item)
        np.unique(commenttext)

print(likecount)
print(username)
print(commentdate)
print(commenttext)
print(len(username))
print(len(likecount))
print(len(commentdate))
print(len(commenttext)) 

'''pd.set_option('display.max_colwidth', None)
df = pd.DataFrame({'comment': flat_data})
df.head(50)'''
