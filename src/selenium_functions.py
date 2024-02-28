import os
import random
import sys
import time
from tkinter import messagebox
import undetected_chromedriver as uc
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from person import TinderPerson

try:
    os.chdir(sys._MEIPASS)
except:
    pass


def wait_element(driver: uc.Chrome, tag: str, search: str) -> WebElement:
    wait = WebDriverWait(driver, 30)

    if tag == 'XPATH':
        wait.until(ec.element_to_be_clickable((By.XPATH, f"{search}")))
        element = driver.find_element(By.XPATH, f"{search}")
        return element

    elif tag == 'ID':
        wait.until(ec.element_to_be_clickable((By.ID, f"{search}")))
        element = driver.find_element(By.ID, f"{search}")
        return element

    elif tag == 'CLASS_NAME':
        wait.until(ec.element_to_be_clickable((By.CLASS_NAME, f"{search}")))
        element = driver.find_element(By.CLASS_NAME, f"{search}")
        return element

    elif tag == 'CSS_SELECTOR':
        wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, f"{search}")))
        element = driver.find_element(By.CSS_SELECTOR, f"{search}")
        return element


def click_next_photo(driver: uc.Chrome) -> None:
    for _ in range(random.randint(1, 3)):
        sleep = random.uniform(1, 4)
        time.sleep(sleep)

        mouse_hover = driver.find_element(By.XPATH, '//div[@class="Expand D(f) Pos(r) tappable-view '
                                                    'Animdur($xfast) Animtf(eio) Wc($transform) Cur(p)"]')
        action = ActionChains(driver)
        action.move_to_element(mouse_hover).perform()

        next_button = driver.find_element(By.XPATH,
                                          '//*[local-name()="svg"][@class="Pos(a) Pe(n) Z(1) T(50%) End(0) Mx(10px) '
                                          'D(n)--s C($c-ds-foreground-button-primary) Op(0) tappable-view:h_Op(1) '
                                          'Trsdu($fast) Rotate(180deg)"]')
        action.move_to_element(next_button).click().perform()


def like(driver: uc.Chrome, amount: int, ratio: int, races: list, names: list) -> None:
    dislike = False

    for i in range(amount):
        sleep = random.uniform(1, 5)
        time.sleep(sleep)

        try:
            if len(driver.find_elements(By.XPATH, '//div[@class="W(100%) Px(20px) Pb(16px) Typs(display-2-strong) Ta('
                                                  'start)"]')) > 0:
                print('Curtidas Limitadas')
                break
        except:
            pass

        try:
            if len(driver.find_elements(By.XPATH, '//*[@id="c-1941919723"]/main/div/div[1]/div/div[2]/div/div[1]')) > 0:
                print('Deu Match')
                driver.get('https://tinder.com/app/recs')
        except:
            pass

        wait_element(driver, 'XPATH', '//*[@id="c-1398387530"]/div/div[1]/div/main/div[1]/div/div/div[1]/div['
                                      '1]/div/div[2]/div[3]/button').click()

        person = TinderPerson(driver)

        if person.race not in races:
            dislike = True

        if names:
            if person.name not in names:
                dislike = True

        if random.random() * 100 < ratio and not dislike:
            click_next_photo(driver)
            wait_element(driver, 'XPATH', '//*[@id="c-1398387530"]/div/div[1]/div/main/div[1]/div/div/div[1]/div['
                                          '2]/div/div/div[4]/button').click()

        else:
            wait_element(driver, 'XPATH', '//*[@id="c-1398387530"]/div/div[1]/div/main/div[1]/div/div/div[1]/div['
                                          '2]/div/div/div[2]/button').click()


def login(driver: uc.Chrome) -> None:
    driver.get('https://tinder.com/app/recs')

    try:
        login_button = driver.find_elements(By.CLASS_NAME, 'l17p5q9z')
        login_button[4].click()
    except:
        pass

    messagebox.showinfo("Tinder Bot", "Manually login and press OK to continue")
