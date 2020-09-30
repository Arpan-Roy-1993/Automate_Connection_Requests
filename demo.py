import pandas as pd
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time
import sys
from webdriver_manager.chrome import ChromeDriverManager
import utils
df = pd.read_excel (r'C:\Users\arpan\Downloads\HIRING RECRUITERS DATABASE.xlsx')
df.columns=['A','B','C','D','E']

df = df[df['E'].notna()]
df=df[6:]

links=df['E']

# open browser
options = Options()
# options.add_argument('--headless')
options.add_argument('--disable-gpu')  # Last I checked this was necessary.
CHROMEDRIVER_PATH = 'C:\\Users\\arpan\\Downloads\\chromedriver.exe'
driver = webdriver.Chrome(CHROMEDRIVER_PATH, chrome_options=options)
utils.signin_to_linkedin(driver)

already_connected=open("already_connected.txt","r")


for row in df.itertuples():
    flag=0
    link=row.E
    hiring_company=row.B
    hiring_person=row.C.split(' ')[0]
    print(hiring_person,hiring_company)
    for line in already_connected:
        line=line.strip()
        # print(line)

        if link==line:
            flag=1
            break
    if flag==1:
        continue

    driver.get(link)
    time.sleep(5)
    my_message= '\n I am a Computer Science Graduate from Arizona State University and I was able to find roles at '+hiring_company+ ' (SWE) where my skill set (fluent in Python and experience with cloud platforms and machine learning) can add immediate value to your team. Please let me know if you feel the same.'

    print("Click connect button!")
    try:
        connect_button = driver.find_elements_by_xpath("/html/body/div[7]/div[3]/div/div/div/div/div[2]/main/div[1]/section/div[2]/div[1]/div[2]/div/div/span[1]/div/button")[0]
        # driver.execute_script("arguments[0].click();", connect_button)
        connect_button.click()

    except:
        # more_button = driver.find_element_by_xpath("/html/body/div[7]/div[3]/div/div/div/div/div[2]/main/div[1]/section/div[2]/div[1]/div[2]/div/div/div/div/button")
        # driver.execute_script("arguments[0].click();", more_button)
        # more_button = driver.find_elements_by_xpath("/html/body/div[7]/div[3]/div/div/div/div/div[2]/main/div[1]/section/div[2]/div[1]/div[2]/div/div/div/div/button")[0]
        # more_button.click()
        # connect_button = driver.find_elements_by_xpath("/html/body/div[7]/div[3]/div/div/div/div/div[2]/main/div[1]/section/div[2]/div[1]/div[2]/div/div/div/div/div/div/ul/li[4]/div/div/span[1]")[0]
        # connect_button.click()

        # connect_button = driver.find_element_by_xpath("/html/body/div[7]/div[3]/div/div/div/div/div[2]/main/div[1]/section/div[2]/div[1]/div[2]/div/div/div/div/button")
        # driver.execute_script("arguments[0].click();", connect_button)
        continue
    time.sleep(5)
    try:
        print("click add note")
        connect_button = driver.find_elements_by_xpath("/html/body/div[4]/div/div/div[3]/button[1]/span")[0]
        connect_button.click()
    except:
        continue

    time.sleep(5)
    print("Adding in my message")
    inputElement = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div[1]/textarea')
    # inputElement = driver.find_element_by_xpath('//*[@id="custom-message"]')

    message = "Hey " + hiring_person +","+ my_message
    inputElement.send_keys(message)
    time.sleep(10)
    done_button = driver.find_elements_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]/span")[0]
    done_button.click()
    already_connected_write=open("already_connected.txt","a")
    already_connected_write.write(link)

    time.sleep(5)




