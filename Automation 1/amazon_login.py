from selenium import webdriver
import time

try:
    driver = webdriver.Chrome()

    driver.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fgp%2Fcss%2Fhomepage.html%3Ffrom%3Dhz%26ref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")

    driver.find_element(by='xpath', value='//*[@id="ap_email"]').send_keys('your email here')

    driver.find_element(by='xpath', value='//*[@id="continue"]').click()

    driver.find_element(by='xpath', value='//*[@id="ap_password"]').send_keys('your password here')

    driver.find_element(by='xpath', value='//*[@id="signInSubmit"]').click()


    time.sleep(4)

    file = open('output.txt', 'w')
    file.write('Successfully Logged In')
    file.close()

    driver.close()

except:
    print('Error')