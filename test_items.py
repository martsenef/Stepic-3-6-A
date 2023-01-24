from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep

# button search class
class Test_36A:
	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
	def test_add_to_cart_button_search(self, browser):
		browser.get(self.link)
		find_button = browser.find_elements(By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
		assert find_button, "!!! No 'Add to basket' buttons !!!"
		sleep(5)
