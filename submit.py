from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import base64
from twilio.rest import Client
# from pyvirtualdisplay import Display
import sys

# display = Display(visible=0, size=(1024, 768))
# display.start()


# Twilio Config: fill these
account_sid = ''
auth_token = ''
twilio_phone_no = ''  # Phone number from twilio dashboard with area code
phone_numbers = ['']


def send_text_message_with_body(phone_nos, body):
    client = Client(account_sid, auth_token)
    print(body)
    for phone_no in phone_nos:
        message = client.messages.create(
            body=body,
            from_=twilio_phone_no,
            to=f'{phone_no}'
        )


bitsmail = ''
bitsmail_p_encode = ''

done = False

while not done:
    try:

        driver = webdriver.Firefox(executable_path='./geckodriver')

        driver.get(
            'https://lms-practice-school.bits-pilani.ac.in/login/index.php')

        driver.find_element_by_xpath(
            '/html/body/div[2]/div[2]/div/div/section/div/div[2]/div/div/div/div/div/div[2]/div[3]/div').click()

        driver.find_element_by_id('identifierId').send_keys(bitsmail)
        print("sent email")

        driver.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div').click()

        driver.implicitly_wait(20)

        time.sleep(10)
        driver.find_element_by_name('password').send_keys(
            (str(base64.b64decode(bitsmail_p_encode)))[2: -1])

        driver.find_element_by_name('password').send_keys(Keys.RETURN)

        driver.implicitly_wait(20)

        driver.find_element_by_xpath(
            '/html/body/div[3]/div[3]/div/div/section[1]/div/aside/section[1]/div/div/div[1]/div/div/div[2]/div[2]/div/a')

        driver.get(
            'https://lms-practice-school.bits-pilani.ac.in/mod/attendance/view.php?id=2145')

        driver.find_elements_by_xpath(
            "//*[contains(text(), 'Submit attendance')]")[0].click()

        driver.find_element_by_xpath('//*[@id="id_status_785"]').click()

        # driver.find_elements_by_xpath("//*[contains(text(), 'Save changes')]")[0].click()

        driver.quit()
        # display.stop()
        done = True
        # send_text_message_with_body(phone_nos = phone_numbers, body = 'Submitted attendence automatically!')
    except:
        print(sys.exc_info()[0])
        print('Error occurred, retrying in 5 minutes')
        time.sleep(300)
