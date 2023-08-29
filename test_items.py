#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_basket(browser):
    browser.get(link)
    time.sleep(30)
    buttons = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert len(buttons) > 0, 'button not found'

