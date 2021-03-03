from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
import os
import datetime
import time
import pyautogui


opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("--disable-extensions")
# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1,
    "profile.default_content_setting_values.notifications": 1
  })

wait=15
chrome_options = Options()
chrome_options.add_argument("--use-fake-ui-for-media-stream")



"""check version of cromeme   
check for camer and mic
odfnAEUDFIBD IQediqwehj DEBWEHBFUIWBVFRV SW BFSW"""

class webex:
    def __init__(self, starttime, endtime,day,nameofuser,email,link):
        self.starttime=starttime
        self.endtime=endtime
        self.email=email
        self.link=link

        self.day=day
        self.nameofuser=nameofuser
        self.driver= webdriver.Chrome(options=chrome_options, executable_path="chromedriver.exe")

    def main1(self):


        self.driver.get(self.link)

        time.sleep(5)
        pyautogui.press("enter")
        #WebDriverWait(self.driver, 10).until(EC.frame_to_be_available_and_switch_to_it("wbx-extension-iframe-43c85c0d-d633-af5e-c056-32dc7efc570b"))

        jointhro=self.driver.find_element_by_xpath("""/html/body/div/div[3]/div/div[1]/div/div[2]/div[1]/div[2]/div[2]/div[3]/a""")
        jointhro.click()

        #self.driver.switch_to.default_content()
        #.switch_to.frame(driver.find_element_by_id("pbui_iframe"))
        WebDriverWait(self.driver, 10).until(EC.frame_to_be_available_and_switch_to_it("pbui_iframe"))


        name = WebDriverWait(self.driver, wait).until(EC.presence_of_element_located((By.XPATH, '''//*[@id="meetingSimpleContainer"]/div[2]/div[2]/input''')))
        name.send_keys(self.nameofuser)

        email=WebDriverWait(self.driver, wait).until(EC.presence_of_element_located((By.XPATH, '''//*[@id="meetingSimpleContainer"]/div[2]/div[3]/input''')))
        email.send_keys(self.email)

        nextbuttoon=WebDriverWait(self.driver, wait).until(EC.presence_of_element_located((By.XPATH, '''//*[@id="guest_next-btn"]''')))

        nextbuttoon.click()
        #switch back

        self.driver.switch_to.default_content()
        #meeting screen
        WebDriverWait(self.driver, 20).until(EC.frame_to_be_available_and_switch_to_it("pbui_iframe"))

        joinbuttoon=WebDriverWait(self.driver, wait).until(EC.presence_of_element_located((By.XPATH, '''//*[@id="interstitial_join_btn"]''')))
        joinbuttoon.click()



    def checktime(self):
        ongoing = True
        print(self.day)
        while ongoing:
            if datetime.datetime.now().strftime("%A") == self.day:
                timerightnow = datetime.datetime.now().strftime("%H:%M:%S")
                if int(timerightnow[0:2]) > int(self.starttime[0:2]):
                    self.driver.close()
                    break
                if  datetime.datetime.now().strftime("%A") == self.day and timerightnow[0:2] == self.starttime[0:2] and int(
                        timerightnow[3:5]) == int(self.starttime[3:5]) + 2:


                    # open
                    self.main1()


                    while ongoing:

                        print(timerightnow[3:5])
                        print(self.endtime[3:5])
                        timerightnow = datetime.datetime.now().strftime("%H:%M:%S")
                        if int(timerightnow[3:5]) == int(self.endtime[3:5]):
                            print("Closing the link: ", self.link)
                            self.driver.close()
                            ongoing = False
                            break
            else:
                self.driver.close()
                print("Closing the link: ",self.link)
                ongoing=False
                break

    def run(self):
        self.checktime()


#webex("10:45:00","20:56:00",datetime.datetime.now().strftime("%A"),"MADHAV","ce20b0662@gmail.com",'https://iitmadras.webex.com/webappng/sites/iitmadras/meeting/download/0f7b16d2c0504088a4aa6c6581a04050?siteurl=iitmadras&MTID=mbe1c15997de318db8308feeb79c94efb').run()