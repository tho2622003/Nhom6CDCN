import time
import pandas as pd
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--mute-audio")

with Chrome(options=chrome_options) as driver:
    wait = WebDriverWait(driver, 10)
    driver.get('https://www.youtube.com/watch?v=f_fuHRyQbOc')

    for item in range(50): 
        visible = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body")))
        visible.send_keys(Keys.END)
        time.sleep(3)

    commentdata = []

    for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#comment #content-text"))):
        commentdata.append(comment.text)        
    
    d = {'Comment':commentdata}
    pd.set_option('display.max_colwidth', 100)
    df = pd.DataFrame(data = d)
    df.to_csv('scraper.csv', encoding = 'UTF-16')

