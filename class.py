import time
from links import *
from info import *
from join import *
from datetime import datetime

from datetime import date
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.options import Options
name = ('ur name lol')


def joinenglish():
    driver.get(english)
    time.sleep ( 5 )
    driver.find_element_by_xpath ('//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div/div' ).click()
    time.sleep ( 1 )
    driver.find_element_by_xpath ('//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div/div/div' ).click()
    time.sleep ( 2 )
    driver.find_element_by_xpath ('//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]' ).click()
    print ( 'English class has been joined successfully' )
    time.sleep(6)
    driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[6]/div[3]/div/div[2]/div[3]/span/span/div/div/span').click()
    time.sleep ( 2 )
    driver.find_element_by_xpath ('//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[3]/div[1]/div[1]/div[2]/textarea' ).send_keys ( name )
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[3]/div[2]').click()

def joinmath():
    driver.get(math)
    time.sleep ( 8 )
    driver.find_element_by_xpath ('//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div/div' ).click ()
    time.sleep ( 1 )
    driver.find_element_by_xpath ('//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div/div/div' ).click ()
    time.sleep ( 2 )
    driver.find_element_by_xpath ('//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]' ).click ()
    print ( 'Maths class has been joined successfully' )
    time.sleep ( 6 )
    driver.find_element_by_xpath ('//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[6]/div[3]/div/div[2]/div[3]/span/span/div/div/span' ).click ()
    time.sleep ( 2 )
    driver.find_element_by_xpath ('//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[3]/div[1]/div[1]/div[2]/textarea' ).send_keys(name)
    time.sleep ( 3 )
    driver.find_element_by_xpath ( '//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[3]/div[2]' ).click ()

def joinhistory():
    driver.get(history)
    time.sleep ( 8 )
    driver.find_element_by_xpath ('//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div/div' ).click ()
    time.sleep ( 1 )
    driver.find_element_by_xpath ('//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div/div/div' ).click ()
    time.sleep ( 2 )
    driver.find_element_by_xpath ('//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]' ).click()
    print ( 'History/Civics class has been joined successfully' )
    time.sleep ( 6 )
    driver.find_element_by_xpath ( '//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[6]/div[3]/div/div[2]/div[3]/span/span/div/div/span' ).click ()
    time.sleep ( 2 )
    driver.find_element_by_xpath ('//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[3]/div[1]/div[1]/div[2]/textarea' ).send_keys (name )
    time.sleep ( 3 )
    driver.find_element_by_xpath ('//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[3]/div[2]' ).click ()

def joinphy():
    driver.get(physics)
    time.sleep(8)
    driver.find_element_by_xpath ('//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div/div' ).click ()
    time.sleep ( 1 )
    driver.find_element_by_xpath ('//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div/div/div' ).click ()
    time.sleep ( 2 )
    driver.find_element_by_xpath ('//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]' ).click ()
    print ( 'Physics class has been joined successfully' )
    time.sleep ( 6 )
    driver.find_element_by_xpath ('//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[6]/div[3]/div/div[2]/div[3]/span/span/div/div/span' ).click ()
    time.sleep ( 2 )
    driver.find_element_by_xpath ('//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[3]/div[1]/div[1]/div[2]/textarea' ).send_keys ( name )
    time.sleep ( 3 )
    driver.find_element_by_xpath ('//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[3]/div[2]' ).click ()

def joinmal():
    driver.get(malayalam)
    time.sleep ( 8 )
    driver.find_element_by_xpath ( '//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div/div' ).click ()
    time.sleep ( 1 )
    driver.find_element_by_xpath ('//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div/div/div' ).click ()
    time.sleep ( 2 )
    driver.find_element_by_xpath ('//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]' ).click ()
    print ( 'Malayalam class has been joined successfully' )
    time.sleep ( 6 )
    driver.find_element_by_xpath ( '//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[6]/div[3]/div/div[2]/div[3]/span/span/div/div/span' ).click ()
    time.sleep ( 2 )
    driver.find_element_by_xpath ('//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[3]/div[1]/div[1]/div[2]/textarea' ).send_keys (name )
    time.sleep ( 3 )
    driver.find_element_by_xpath ('//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[3]/div[2]').click ()

def joinbio():
    driver.get(biology)
    time.sleep ( 8 )
    driver.find_element_by_xpath ('//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div/div' ).click ()
    time.sleep ( 1 )
    driver.find_element_by_xpath ('//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div/div/div' ).click ()
    time.sleep ( 2 )
    driver.find_element_by_xpath ('//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]' ).click ()
    print ( 'Biology class has been joined successfully' )
    time.sleep ( 6 )
    driver.find_element_by_xpath ('//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[6]/div[3]/div/div[2]/div[3]/span/span/div/div/span' ).click ()
    time.sleep ( 2 )
    driver.find_element_by_xpath ('//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[3]/div[1]/div[1]/div[2]/textarea' ).send_keys (name )
    time.sleep ( 3 )
    driver.find_element_by_xpath ('//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[3]/div[2]' ).click ()
    
def joinchem():
    driver.get(chem)
    time.sleep ( 8 )
    driver.find_element_by_xpath ( '//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[3]/div[2]/div/div' ).click ()
    time.sleep ( 1 )
    driver.find_element_by_xpath ( '//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div/div/div' ).click ()
    time.sleep ( 3 )
    driver.find_element_by_xpath ('//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]' ).click ()
    print ( 'Chemistry class has been joined successfully' )
    time.sleep ( 6 )
    driver.find_element_by_xpath ('//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[6]/div[3]/div/div[2]/div[3]/span/span/div/div/span' ).click ()
    time.sleep ( 2 )
    driver.find_element_by_xpath ('//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[3]/div[1]/div[1]/div[2]/textarea' ).send_keys ( name )
    time.sleep ( 3 )
    driver.find_element_by_xpath ('//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[3]/div[2]' ).click ()

def joinhindi():
    driver.get(hindi)
    time.sleep ( 8 )
    driver.find_element_by_xpath ('//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div/div' ).click ()
    time.sleep ( 1 )
    driver.find_element_by_xpath ('//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div/div/div' ).click ()
    time.sleep ( 2 )
    driver.find_element_by_xpath ( '//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]' ).click ()
    time.sleep ( 6 )
    driver.find_element_by_xpath ( '//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[6]/div[3]/div/div[2]/div[3]/span/span/div/div/span' ).click ()
    print ( 'Hindi class has been joined successfully' )
    time.sleep ( 2 )
    driver.find_element_by_xpath ('//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[3]/div[1]/div[1]/div[2]/textarea' ).send_keys (name )
    time.sleep ( 3 )
    driver.find_element_by_xpath ('//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[3]/div[2]' ).click ()
    print ( 'Hindi class has been joined successfully' )

def joinface():
    driver.get(face)
    time.sleep ( 8 )
    driver.find_element_by_xpath ('//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div/div' ).click ()
    time.sleep ( 1 )
    driver.find_element_by_xpath ('//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div/div/div' ).click ()
    time.sleep ( 2 )
    driver.find_element_by_xpath ('//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]' ).click ()
    print ( 'Facetime c has been joined successfully' )
    time.sleep ( 6 )
    driver.find_element_by_xpath ( '//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[6]/div[3]/div/div[2]/div[3]/span/span/div/div/span' ).click ()
    time.sleep ( 2 )
    driver.find_element_by_xpath ('//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[3]/div[1]/div[1]/div[2]/textarea' ).send_keys ( name )
    time.sleep ( 3 )
    driver.find_element_by_xpath ('//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[3]/div[2]' ).click ()

def joingeo():
    driver.get(geo)
    time.sleep(8)
    driver.find_element_by_xpath ('//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div/div' ).click ()
    time.sleep ( 2 )
    driver.find_element_by_xpath ('//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div/div/div' ).click ()
    time.sleep ( 2 )
    driver.find_element_by_xpath ( '//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]' ).click ()
    print ( 'Geography class has been joined successfully' )
    time.sleep ( 6 )
    driver.find_element_by_xpath ( '//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[6]/div[3]/div/div[2]/div[3]/span/span/div/div/span' ).click ()
    time.sleep ( 2 )
    driver.find_element_by_xpath ('//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[3]/div[1]/div[1]/div[2]/textarea' ).send_keys(name)
    time.sleep ( 3 )
    driver.find_element_by_xpath ('//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[3]/div[2]' ).click ()

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.media_stream_mic" : 1,
         "profile.default_content_setting_values.notifications": 2,
         "profile.default_content_setting_values.media_stream_camera": 1}

chrome_options.add_experimental_option("prefs",prefs)

path = r'C:\Users\User\Documents\chromedriver_win32 (3)\chromedriver.exe'
driver = webdriver.Chrome(path, chrome_options = chrome_options)



#this part signs into google
driver.maximize_window()
driver.get('https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?redirect_uri=https%3A%2F%2Fdevelopers.google.com%2Foauthplayground&prompt=consent&response_type=code&client_id=407408718192.apps.googleusercontent.com&scope=email&access_type=offline&flowName=GeneralOAuthFlow')
time.sleep(3)
driver.find_element_by_xpath('//*[@id="yDmH0d"]').click()
driver.find_element_by_xpath('//input[@type="email"]').send_keys(email)
driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
time.sleep(3)
driver.find_element_by_xpath('//input[@type="password"]').send_keys(password)
driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
time.sleep(2)


e = datetime.now()
day = e.strftime ( "%A" )
print ( day )


if day == "Monday":
    joinmath()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[9]/div[2]/div[2]/div').click()
    print('Maths class has been left successfully')
    joinphy()
    time.sleep(3)
    driver.find_element_by_xpath ( '//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[9]/div[2]/div[2]/div' ).click()
    print ( 'Physics class has been left successfully' )
    joinhistory()
    time.sleep (3)
    driver.find_element_by_xpath ( '//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[9]/div[2]/div[2]/div' ).click()
    print ( 'History class has been left successfully' )
    joinenglish()
    time.sleep ( 3 )
    driver.find_element_by_xpath ( '//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[9]/div[2]/div[2]/div' ).click ()
    print ( 'English class has been left successfully' )

elif day == "Tuesday":
    joinmath()
    time.sleep ( 3000 )
    driver.find_element_by_xpath ( '//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[9]/div[2]/div[2]/div' ).click ()
    print ( 'Maths class has been left successfully' )
    joinhistory()
    time.sleep ( 3000 )
    driver.find_element_by_xpath ( '//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[9]/div[2]/div[2]/div' ).click ()
    print ( 'Maths class has been left successfully' )
    joinmal()
    time.sleep ( 3000 )
    driver.find_element_by_xpath ( '//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[9]/div[2]/div[2]/div' ).click ()
    print ( 'Maths class has been left successfully' )
    joinbio()
    time.sleep ( 3000 )
    driver.find_element_by_xpath ( '//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[9]/div[2]/div[2]/div' ).click ()
    print ( 'Maths class has been left successfully' )

elif day == "Wednesday":
    joinchem()
    time.sleep ( 3000 )
    driver.find_element_by_xpath ( '//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[9]/div[2]/div[2]/div' ).click ()
    print ( 'Maths class has been left successfully' )
    joinmath()
    time.sleep ( 3000 )
    driver.find_element_by_xpath ( '//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[9]/div[2]/div[2]/div' ).click ()
    print ( 'Maths class has been left successfully' )
    joinenglish()
    time.sleep ( 3000 )
    driver.find_element_by_xpath ( '//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[9]/div[2]/div[2]/div' ).click ()
    print ( 'Maths class has been left successfully' )
    joinhindi()
    time.sleep ( 3000 )
    driver.find_element_by_xpath ( '//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[9]/div[2]/div[2]/div' ).click ()
    print ( 'Maths class has been left successfully' )

elif day == "Thursday":
    joinmath()
    time.sleep ( 3 )
    driver.find_element_by_xpath ( '//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[9]/div[2]/div[2]/div' ).click ()
    print ( 'Maths class has been left successfully' )
    joinface()
    time.sleep ( 3 )
    driver.find_element_by_xpath ( '//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[9]/div[2]/div[2]/div' ).click ()
    print ( 'Maths class has been left successfully' )
    joinenglish()
    time.sleep ( 3 )
    driver.find_element_by_xpath ( '//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[9]/div[2]/div[2]/div' ).click ()
    print ( 'Maths class has been left successfully' )
    joinmal()
    time.sleep ( 3 )
    driver.find_element_by_xpath ( '//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[9]/div[2]/div[2]/div' ).click ()
    print ( 'Maths class has been left successfully' )

elif day == "Friday":
    joinmath()
    time.sleep (3)
    driver.find_element_by_xpath ( '//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[9]/div[2]/div[2]/div' ).click ()
    print ( 'Maths class has been left successfully' )
    joingeo()
    time.sleep ( 3 )
    driver.find_element_by_xpath ( '//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[9]/div[2]/div[2]/div' ).click ()
    print ( 'Maths class has been left successfully' )
    joinmal()
    time.sleep ( 3 )
    driver.find_element_by_xpath ( '//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[9]/div[2]/div[2]/div' ).click ()
    print ( 'Maths class has been left successfully' )
    joinphy()
    time.sleep ( 3 )
    driver.find_element_by_xpath ( '//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[9]/div[2]/div[2]/div' ).click ()
    print ( 'Maths class has been left successfully' )

elif day == "Saturday":
    print('its saturday bro lmao ')

elif day == 'Sunday':
    print('Its sunday bro lmao')


