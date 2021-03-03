
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import datetime

# create chrome instamce
opt = Options()
opt.add_argument('--disable-blink-features=AutomationControlled')
opt.add_argument('--start-maximized')
opt.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 0,
    "profile.default_content_setting_values.notifications": 1
})




class gmeet:
    def __init__(self, starttime, endtime,day,email,password,link):
        self.starttime=starttime
        self.endtime=endtime
        self.email=email
        self.password=password
        self.link=link
        self.day=day
        self.driver= webdriver.Chrome(options=opt, executable_path="chromedriver.exe")

    def Glogin(self,email, password):
        # Login Page
        self.driver.get(
            'https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com/&ec=GAZAAQ')

        # input Gmail
        self.driver.find_element_by_id("identifierId").send_keys(email)
        time.sleep(1)
        self.driver.find_element_by_id("identifierNext").click()
        time.sleep(1)
        self.driver.implicitly_wait(10)

        # input Password
        self.driver.find_element_by_xpath(
            '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("passwordNext").click()
        self.driver.implicitly_wait(10)

        # go to google home page
        self.driver.get('https://google.com/')
        self.driver.implicitly_wait(100)

    def turnOffMicCam(self):
        # turn off Microphone

        mic = self.driver.find_element_by_xpath(
            '/html/body/div[1]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[3]/div[1]/div/div/div')
        mic.click()
        with open("user_data/gmeet_mail_password.txt") as f:
            lisstofalllines=f.readlines()
            if lisstofalllines[2]=="YES":
                 camera = self.driver.find_element_by_xpath('/html/body/div[1]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[3]/div[2]/div/div')
                 camera.click()
            else:
                pass

    def joinNow(self):
        # Join meet

        time.sleep(5)
        self.driver.implicitly_wait(2000)
        self.driver.find_element_by_css_selector('div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt').click()

    def AskToJoin(self):
        # Ask to Join meet
        time.sleep(1)
        self.driver.implicitly_wait(2000)
        self.driver.find_element_by_css_selector(
            'div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt').click()
        # Ask to join and join now buttons have same xpaths

    # assign email id and password


    def checktime(self):
        ongoing = True
        while ongoing:
            if datetime.datetime.now().strftime("%A") == self.day:
                timerightnow = datetime.datetime.now().strftime("%H:%M:%S")
                if int(timerightnow[0:2]) > int(self.starttime[0:2]):
                    print("Closing the link: ", self.link)
                    self.driver.close()
                    break

                if  datetime.datetime.now().strftime("%A") == self.day and timerightnow[0:2] == self.starttime[0:2] and int(
                        timerightnow[3:5]) == int(self.starttime[3:5]) + 2:

                    # login to Google account

                    self.Glogin( self.email, self.password)

                    # go to google meet
                    self.driver.get(self.link)

                    self.turnOffMicCam()

                    self.joinNow()

                    while ongoing:
                        timerightnow = datetime.datetime.now().strftime("%H:%M:%S")
                        if int(timerightnow[3:5]) == int(self.endtime[3:5]):
                            print("Closing the link: ", self.link)
                            self.driver.close()
                            ongoing = False
                            break
            else:
                print("Closing the link: ", self.link)
                self.driver.close()
                break

    def run(self):
        self.checktime()

#gmeet("01:47:00","01:51:00",datetime.datetime.now().strftime("%A"),mail_address,password,'https://meet.google.com/mhx-mpny-fdo').run()
