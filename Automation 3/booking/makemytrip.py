from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time


class MakeMyTrip(webdriver.Chrome):

    def __init__(self):
        options = Options()
        options.add_argument('--ignore-certificate-errors')
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        # time.sleep(10)
        self.driver.implicitly_wait(30)

    def land_page(self):
        self.driver.get('https://www.makemytrip.com/')
        time.sleep(5)

    def close_popup(self):
        closebtn = self.driver.find_element(By.CSS_SELECTOR, 'div[class="makeFlex hrtlCenter"]')
        closebtn.click()
        time.sleep(5)

    def search_from_city(self, city='Bangalore'):
        searchcity = self.driver.find_element(By.CLASS_NAME, 'searchCity')
        searchcity.click()
        time.sleep(5)

        from_city = self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="From"]')
        from_city.send_keys(city)
        time.sleep(5)

        select_city = self.driver.find_element(By.ID, 'react-autowhatever-1-section-0-item-0')
        select_city.click()
        time.sleep(5)

    def search_to_city(self, city='Kolkata'):
        searchcity = self.driver.find_element(By.CLASS_NAME, 'searchToCity')
        searchcity.click()
        time.sleep(5)

        to_city = self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="To"]')
        to_city.send_keys(city)
        time.sleep(5)

        select_city = self.driver.find_element(By.ID, 'react-autowhatever-1-section-0-item-0')
        select_city.click()
        time.sleep(5)

    def departure_date(self, date=''):
        select_date = self.driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Sat May 27 2023"]')
        select_date.click()
        time.sleep(5)

    def travellers(self, tcount=1, ccount=0, icount=0, tclass=0):
        
        select_travellers = self.driver.find_element(By.CLASS_NAME, 'flightTravllers')
        select_travellers.click()
        time.sleep(5)

        if tcount > 1:
            traveller_count = self.driver.find_element(By.CSS_SELECTOR, f'li[data-cy="adults-{str(tcount)}"]')
            traveller_count.click()
            time.sleep(5)
        
        if ccount > 0:
            child_count = self.driver.find_element(By.CSS_SELECTOR, f'li[data-cy="children-{ccount}"]')
            child_count.click()
            time.sleep(5)
        
        if icount > 0:
            infant_count = self.driver.find_element(By.CSS_SELECTOR, f'li[data-cy="infants-{icount}"]')
            infant_count.click()
            time.sleep(5)

        if tclass > 0:
            traveller_class = self.driver.find_element(By.CSS_SELECTOR, f'li[data-cy="travelClass-{tclass}"]')
            traveller_class.click()
            time.sleep(5)
        
        apply = self.driver.find_element(By.CSS_SELECTOR, 'button[data-cy="travellerApplyBtn"]')
        apply.click()
        time.sleep(5)

    def submit_btn(self):
        submitbtn = self.driver.find_element(By.CSS_SELECTOR, 'p[data-cy="submit"]')
        submitbtn.click()
        time.sleep(5)

    def press_okay_btn(self):
        okaybtn = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/div/div/div[3]/button')
        okaybtn.click()
        time.sleep(5)

    def filter_minimum(self):
        slider = self.driver.find_element(By.CLASS_NAME, 'rangeslider__handle')
        
        move = ActionChains(self.driver)
        move.click_and_hold(slider).move_by_offset(-300,0).release().perform()
        time.sleep(10)