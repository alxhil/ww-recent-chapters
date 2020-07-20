from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import difflib
import sys

# Constants #

PATH = r"C:\Users\alxhi\Documents\Code\Python\chromedriver.exe"
FILENAME = "recentchapters.txt"
print("[STARTING]")



# webpage binds diver to a chrome webdriver and loads URL for given website #
# PATH : path/to/webdriver                                                  #
# time.sleep(3) to account for any connection delay                         #

def refresh_webpage():
    driver.get("https://wuxiaworld.com")
    time.sleep(10)

def send_to_file(str, filename):
    with open(filename, 'w') as f:
            sys.stdout = f
            print(str)
            sys.stdout = original_stdout

def read_from_file(filename):
    with open(filename, 'r') as f:
        read = f.read()
        return read

def compare_newest(str, str2):
    print(next(difflib.ndiff(str,str2)))
    return next(difflib.ndiff(str, str2))




file_string = ""
driver = webdriver.Chrome(PATH)
refresh_webpage()

while(True):
    for i in range(1,20):
        recentchapter = driver.find_element_by_xpath(f"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[6]/div[2]/table[1]/tbody[1]/tr[{i}]")
        file_string += recentchapter.text+"\n"
    if(compare_newest(file_string, read_from_file(FILENAME) == '+')):
        send_to_file(file_string,FILENAME)
    else:
        refresh_webpage()






