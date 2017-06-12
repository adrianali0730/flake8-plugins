#!/usr/bin/env python

from selenium.webdriver.common.by import By

prices = {'apple': 0.40, 'banana': 0.50}
driver.find_elements(By.XPATH, '//button')
my_purchase = {
    'apple': 1,
    'banana': 6}
grocery_bill = sum(prices[fruit] * my_purchase[fruit]
                   for fruit in my_purchase)
print ('I owe the grocer $%.2f' % grocery_bill)
