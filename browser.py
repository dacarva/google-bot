from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Initiate browser
browser = webdriver.Chrome(ChromeDriverManager().install())

# Open website
while True:
    browser.get('https://google.com')

    # Fill search field
    to_search = 'TRU'

    # Find input
    the_input = browser.find_element_by_name('q')
    the_input.send_keys(to_search)
    the_input.submit()
    sleep(5)

    element = browser.find_element_by_partial_link_text('trugroup')
    element.click()
    print('Element', element)
    sleep(10)
