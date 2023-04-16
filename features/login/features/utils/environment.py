from behave import *
import allure
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
chromedriver="chromedriver"

def selenium_driver():
    context.driver = webdriver.Chrome(chromedriver)