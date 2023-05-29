from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import user
import time

import unittest


class SpotifyPlay(unittest.TestCase):

    def setUp(self):
    # Setting chrome driver and navigating to spotify
        self.driver = Chrome()
        self.driver.get('https://open.spotify.com')
        time.sleep(5)

    def test_play_spotify(self):
        # clicking on log in button
        login = self.driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/header/div[5]/button[2]')
        login.click()
        time.sleep(5)

        # clicking facebook button
        fbbtn = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/ul/li[2]')
        fbbtn.click()
        time.sleep(5)

        # Entering email
        emailId = self.driver.find_element(By.ID, 'email')
        emailId.send_keys(user.email)
        time.sleep(5)

        # Entering password
        password = self.driver.find_element(By.ID, 'pass')
        password.send_keys(user.password)
        time.sleep(5)

        # pressing login button
        loginBtn = self.driver.find_element(By.ID, 'loginbutton')
        loginBtn.click()
        time.sleep(10)

        # close banner
        crossBtn = self.driver.find_element(By.XPATH, '//*[@id="onetrust-close-btn-container"]/button')
        crossBtn.click()
        time.sleep(10)

        # click on search button
        searchBtn = self.driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/nav/div[1]/ul/li[2]')
        searchBtn.click()
        time.sleep(10)

        # search for a song
        search = self.driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/header/div[3]/div/div/form/input')
        search.send_keys('Bhayanak Aatma')
        time.sleep(10)

        # click on card
        card = self.driver.find_element(By.CLASS_NAME, '_gB1lxCfXeR8_Wze5Cx9')
        card.click()
        time.sleep(5)

        # click on play
        playbtn = self.driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[4]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div[3]/div[4]/div/div/div/div/div/button')
        playbtn.click()
        time.sleep(10)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()