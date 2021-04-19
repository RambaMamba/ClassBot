from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import schedule
from datetime import datetime
from datetime import timedelta
from tkinter import *
from functools import partial
import threading

class InfoSave():

      def __init__(self, p_gotinfo):
            self.gotinfo = p_gotinfo

      def getInfo(self):
          return self.gotinfo

      def updateInfo(self, info):
          self.gotinfo = info

      def printSelf(self):
          print(self.gotinfo)
          return self.gotinfo 
          
def turnOffMicCam(driver):
    time.sleep(2)
    driver.find_element_by_xpath(
        '//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div[1]/div/div/div').click()
    driver.implicitly_wait(3000)
  
    time.sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div[2]/div/div').click()
    driver.implicitly_wait(3000)
    return driver
  
  
def joinNow(driver):
    time.sleep(5)
    driver.implicitly_wait(2000)
    driver.find_element_by_css_selector(
        'div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt').click()
    return driver

def login(email, psw):

  opt=Options()
  opt.add_argument("start-maximized")
  opt.add_argument("--disable-extensions")
  opt.add_argument('--ignore-ssl-errors=yes')
  opt.add_argument('--ignore-certificate-errors')

  opt.add_experimental_option("prefs", { \
  "profile.default_content_setting_values.media_stream_mic": 1,
  "profile.default_content_setting_values.media_stream_camera": 1,
  "profile.default_content_setting_values.geolocation": 1,
  "profile.default_content_setting_values.notifications": 1
  })

  driver=webdriver.Chrome(chrome_options=opt, executable_path = "C:\\Users\\Shrey Birmiwal\\Downloads\\chromedriver_win32\\chromedriver.exe")
  driver.get('https://accounts.google.com/ServiceLogin/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin')

  username=driver.find_element_by_id('identifierId')
  username.click()

  username.send_keys(email)

  next=driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]')
  next.click()
  time.sleep(2)
  password=driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
  password.click()
  password.send_keys(psw)


  next=driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]')
  next.click()
  return driver

def period1(saved):
  info = saved.printSelf()
  driver = login(info[0], info[1])

  if(info[10] == "2"):
    info[11] = info[11] - timedelta(days=1)
    info[10] = "1"
   
  now = datetime.now()
  daysFromType = now - info[11]
  number_of_days = daysFromType.days
  driver.get("https://meet.google.com/")
  but = driver.find_element_by_class_name("glue-caption")
  but.send_keys(info[6])

  driver.find_element_by_class_name("glue-button    glue-button glue-button--low-emphasis join-button").click()

  driver.implicitly_wait(10)
  if(number_of_days % 2 == 0):
    driver.get(info[2])
  else:
    driver.get(info[6])
  driver.implicitly_wait(10)
  driver = turnOffMicCam(driver)


  driver = joinNow(driver)
  GotInfo = [mail, password, p1, p2, p3, p4, p5, p6, p7, p8, dayType, DayOfStart]


def period2(saved):
  info = saved.printSelf()
  driver = login(info[0], info[1])

  if(info[10] == "2"):
    info[11] = info[11] - timedelta(days=1)
    info[10] = "1"
   
  now = datetime.now()
  daysFromType = now - info[11]
  number_of_days = daysFromType.days

  if(number_of_days % 2 == 0):
    driver.get(info[3])
  else:
    driver.get(info[7])

  driver.implicitly_wait(10)
  driver = turnOffMicCam(driver)
  driver = joinNow(driver)

def period3(saved):
  info = saved.printSelf()
  driver = login(info[0], info[1])

  if(info[10] == "2"):
    info[11] = info[11] - timedelta(days=1)
    info[10] = "1"
   
  now = datetime.now()
  daysFromType = now - info[11]
  number_of_days = daysFromType.days

  if(number_of_days % 2 == 0):
    driver.get(info[4])
  else:
    driver.get(info[8])

  driver.implicitly_wait(10)
  driver = turnOffMicCam(driver)
  driver = joinNow(driver)

def period4(saved):
  info = saved.printSelf()
  driver = login(info[0], info[1])

  if(info[10] == "2"):
    info[11] = info[11] - timedelta(days=1)
    info[10] = "1"
   
  now = datetime.now()
  daysFromType = now - info[11]
  number_of_days = daysFromType.days

  if(number_of_days % 2 == 0):
    driver.get(info[5])
  else:
    driver.get(info[9])

  driver.implicitly_wait(10)
  driver = turnOffMicCam(driver)
  driver = joinNow(driver)



def submitClick(info):
  #print("Sub,it")
  mail = info[0].get()
  password = info[1].get()
  p1 = info[2].get()
  p2 = info[3].get()
  p3 = info[4].get()
  p4 = info[5].get()
  p5 = info[6].get()
  p6 = info[7].get()
  p7 = info[8].get()
  p8 = info[9].get()
  dayType = info[10].get()
  DayOfStart = datetime.now()
  saved = info[11]
  
  GotInfo = [mail, password, p1, p2, p3, p4, p5, p6, p7, p8, dayType, DayOfStart]
  saved.updateInfo(GotInfo)
  #saved.printSelf()
 
def setupUI(saved):
  root = Tk()
  email = Entry(root, width = 50)
  email.pack()
  email.insert(0, "Replace with email")
  password = Entry(root, width = 50)
  password.pack()
  password.insert(0, "Replace with password")
  period1 = Entry(root, width = 50)
  period1.pack()
  period1.insert(0, "Replace with period one code")
  
  period2 = Entry(root, width = 50)
  period2.pack()
  period2.insert(0, "Replace with period two code")
  
  period3 = Entry(root, width = 50)
  period3.pack()
  period3.insert(0, "Replace with period three code")
  
  period4 = Entry(root, width = 50)
  period4.pack()
  period4.insert(0, "Replace with period four code")
  
  period5 = Entry(root, width = 50)
  period5.pack()
  period5.insert(0, "Replace with period five code")

  period6 = Entry(root, width = 50)
  period6.pack()
  period6.insert(0, "Replace with period six code")
  
  period7 = Entry(root, width = 50)
  period7.pack()
  period7.insert(0, "Replace with period seven code")

  period8 = Entry(root, width = 50)
  period8.pack()
  period8.insert(0, "Replace with period eight code")


  dayType = Entry(root, width = 50)
  dayType.pack()
  dayType.insert(0, "Type 1 if it is A day. Type 2 if it B day today")

  keepOn = Label(root, text="KEEP PROGRAM ON")
  keepOn.pack()

  info = [email, password, period1, period2, period3, period4, period5, period6, period7, period8, dayType, saved]
  Submit = Button(root, text='Submit', command= lambda: submitClick(info))
  Submit.pack()

  return root

def threadedLOOP():
    while True:
        schedule.run_pending()
        time.sleep(1)

def main():
  sb = []
  saved = InfoSave(sb)
  root = setupUI(saved)

  th = threading.Thread(target=threadedLOOP)
  th.start()

  schedule.every().day.at("08:38").do(period1, saved)
  schedule.every().day.at("09:50").do(period2, saved)
  schedule.every().day.at("12:35").do(period3, saved)
  schedule.every().day.at("02:05").do(period4, saved)
  root.mainloop()

  th.join()
  

if __name__ == '__main__':
    main()


