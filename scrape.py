# main web scraping
# import selenium model 
import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time

# grab a content from a particular website/ interact with pae

def scrape_website(website):
    print("Launhing chrome browser...")
    # need to specify where our chrome driver is that allows ous to control chrome
    chrome_driver_path = "./chromedriver.exe"
    # options on how the chrome driver will operate
    options = webdriver.ChromeOptions()
    # setup actual driver
    # automate any browser we want.
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)
    
    # use the driver to get page
    try:
        driver.get(website)
        print("Page loaded...")
        html = driver.page_source
        time.sleep(10)
        return html
    finally:
        driver.quit()

# start watching from 13:03
# with amazon they will be blocking you.
# brightdata to scraping site which will technically stop us.


def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    # body tag to parse it
    body_content = soup.body()
    if body_content:
        return str(body_content)
    return ""

def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")
    # look inside our parse content whether there is any script or style and simply going to remove them
    for script_or_style in soup(["script","style"]):
        script_or_style.extract()
    # get all the text and separate it with a new line
    cleaned_content = soup.get_text(separator="\n")
    # remove any backslash character which is not necessary
    cleaned_content = "\n".join(line.strip() for line in cleaned_content.splitlines() if line.strip())
    
    return cleaned_content

# split our text into difference batches because llm has a token limit.
def split_dom_content(dom_content, max_length = 6000):
    # will take the dom content and make it into batches of 6000 characters.
    # for loop will step upto i + next 6000 characters
    return[
        dom_content[i : i + max_length] for i in range(0, len(dom_content), max_length)
    ]


