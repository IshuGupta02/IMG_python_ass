import mysql.connector
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import email_pass
from selenium.webdriver.common.by import By
import time
import json


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=email_pass.mysql,
    database="python_assignment",
    auth_plugin="mysql_native_password"
)

class Person:
    def __init__(self, name, city="Roorkee", work=None):
        self.name=name
        self.city=city
        if work is not None:
            self.work=work

    def show(self):
        print('My name is {} and my current city is {}'.format(self.name, self.city))

    def upload(self, username):
        mycursor = mydb.cursor()

        mycursor.execute("UPDATE user SET name=%s,work=%s,city=%s WHERE username=%s", (str(self.name), json.dumps(self.work), str(self.city), username))

        mydb.commit()
        return "uploaded"
       

def check(myresult):
    for x in myresult:
        if(x[1] is not None):
            if(x[2] is not None):
                if(x[3] is not None):
                    return Person(name=x[1], city= x[2], work=json.loads(x[3]))
                else:
                    return Person(name=x[1], city= x[2])
            else:
                if(x[3] is not None):
                    return Person(name=x[1], work=json.loads(x[3]))
                else:
                    return Person(name=x[1])

        else:
            return None

def validate(func):
    def inner(username):
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM user where username=\'"+username+"\'")

        myresult = mycursor.fetchall()
        found=False
        for x in myresult:
            found=True

        if(found==False):
            raise ValueError('username is not valid!')
        else:
            previous= check(myresult)
            if(previous is not None):
                previous.show()
            else:
                func(username)

        return "Task completed!"

    return inner


@validate
def scrap(username):

    URL= "https://m.facebook.com/"+username+"/about"
    r = requests.get(URL)
    
    soup = BeautifulSoup(r.content, 'html5lib') 

    work= find_work(username, soup)
    name= find_name(username, soup)
    city=find_city(username, soup)
    find_fav(username)

    person= Person(name, city, work)

    person.show()

    person.upload(username)
      

def find_work(username, soup):

    for link in soup.find_all('div'):
        if link.string=="कार्य":
            break
    link=link.parent.parent.parent.parent.parent.parent.contents[1]
    work=[]
    for div in link.children:
        work.append(div.contents[0].contents[1].contents[0].contents[0].contents[0].string)
    return work


def find_name(username, soup):
   
    div= soup.find('h3')
    name= div.string

    return name


def find_city(username, soup):

    for link in soup.find_all('div'):
        if link.string=="वर्तमान शहर":
            break

    city=link.parent.parent.contents[1].contents[0].contents[0].string
    return city

def find_fav(username):

    driver = webdriver.Chrome() 
    driver.maximize_window()
    time.sleep(2)

    driver.get("https://m.facebook.com/"+username+"/about")
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="mobile_login_bar"]/div[2]/a[2]').click()

    email = driver.find_element_by_id("m_login_email")
    passwd = driver.find_element_by_id("m_login_password")

    email.send_keys(email_pass.user_name)
    passwd.send_keys(email_pass.password)

    passwd.send_keys(Keys.RETURN)
    time.sleep(5)


    driver.find_element(By.XPATH, '//*[@id="checkpointSubmitButton-actual-button"]').click()

    time.sleep(2)

    radioBtn1= driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/form/div/article/section/div/fieldset/label[1]/div/div[2]/div')
    radioBtn1.click()

    time.sleep(1)

    driver.find_element(By.XPATH, '//*[@id="checkpointSubmitButton-actual-button"]').click()

    time.sleep(5)

    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/form/div/article/section/div/div[2]/div/div[1]/div[2]/fieldset/label[25]/div/div[1]').click()

    time.sleep(1)

    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/form/div/article/section/div/div[2]/div/div[2]/div[2]/fieldset/label[11]/div/div[1]').click()

    time.sleep(1)

    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/form/div/article/section/div/div[2]/div/div[3]/div[2]/fieldset/label[7]/div/div[1]').click()

    time.sleep(3)

    driver.find_element(By.XPATH, '//*[@id="checkpointSubmitButton-actual-button"]').click()

    time.sleep(3)

    driver.find_element(By.XPATH, '//*[@id="checkpointSubmitButton-actual-button"]').click()

    time.sleep(3)

    SCROLL_PAUSE_TIME = 2

# Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    time.sleep(2)

    driver.find_element(By.XPATH, "//div[contains(text(),'Likes')]/../../div[3]/a").click()

    time.sleep(3)

    driver.find_element(By.XPATH, '//*[@id="timelineBody"]/div/div/div/div[1]/div/header/div/div[3]/a').click()

    time.sleep(3)


    fav =[]

    for span in driver.find_elements(By.XPATH, '/html/body/div[1]/div[1]/div[4]/div/div/div/div/div/div/div/div/div[1]/div[*]/div/span'):
        fav.append(span.text)

    for span in driver.find_elements(By.XPATH, '/html/body/div[1]/div[1]/div[4]/div/div/div/div/div/div/div/div/div[2]/div[*]/div/span'):
        fav.append(span.text)

    print("here's the list of my favourites: ")
    print(fav)
    print()

    driver.quit()


# usname="anshul.d.sharma.7"
# scrap(usname)