import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
	parser.addoption(
		'--browser_name',
		action='store',
		default='firefox',  # chrome
		help='Choose browser: Chrome or FireFox'),
	parser.addoption(
		"--language",
		action='store',
		default=None,
		help='Choose language: en, ru, or another.')

@pytest.fixture(scope="class")
def browser(request):
	user_language = request.config.getoption("language")
	options = Options()
	browser_name = request.config.getoption("browser_name")
	if browser_name == "chrome":
		print("\nStart browser Chrome for test..!")
		options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
		browser = webdriver.Chrome(options=options)
	elif browser_name == "firefox":
		print("\nStart browser FireFox for test..!")
		fp = webdriver.FirefoxProfile()
		fp.set_preference("intl.accept_languages", user_language)
		browser = webdriver.Firefox(firefox_profile=fp)
	else:
		raise pytest.UsageError("--browser_name should be chrome or firefox")
	browser.implicitly_wait(9)
	yield browser
	print("\nquit browser..!")
	browser.quit()
