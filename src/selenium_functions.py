import os
import random
import sys
import time
import undetected_chromedriver as uc
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
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
    for _ in range(random.randint(1, 4)):
        sleep = random.uniform(1, 2)
        time.sleep(sleep)

        # mouse_hover = driver.find_element(By.XPATH, '//div[@class="Expand D(f) Pos(r) tappable-view '
        #                                             'Animdur($xfast) Animtf(eio) Wc($transform) Cur(p)"]')
        # action = ActionChains(driver)
        # action.move_to_element(mouse_hover).perform()
        #
        # try:
        #     next_button = driver.find_element(By.XPATH,
        #                                       '//*[local-name()="svg"][@class="Pos(a) Pe(n) Z(1) T(50%) End(0) Mx(10px)'
        #                                       'D(n)--s C($c-ds-foreground-button-primary) Op(0) tappable-view:h_Op(1) '
        #                                       'Trsdu($fast) Rotate(180deg)"]')
        #     action.move_to_element(next_button).click().perform()
        # except:
        #     pass

        ActionChains(driver).send_keys(Keys.SPACE).perform()


def like(driver: uc.Chrome, amount: int, ratio: int, races: list, names: list, bio_keywords: list,
         interests: list) -> None:
    for i in range(amount):
        sleep = random.uniform(1, 5)
        time.sleep(sleep)

        try:
            if len(driver.find_elements(By.XPATH, '//div[@class="W(100%) Px(20px) Pb(16px) Typs(display-2-strong) Ta('
                                                  'start)"]')) > 0:
                print('End of likes')
                break
        except:
            pass

        try:
            if len(driver.find_elements(By.XPATH, '//*[@id="c-1941919723"]/main/div/div[1]/div/div[2]/div/div[1]')) > 0:
                print('Matched')
                driver.get('https://tinder.com/app/recs')
        except:
            pass

        # # info button
        # wait = WebDriverWait(driver, 10)
        # list_length = 2
        # wait.until(lambda driver: len(driver.find_elements(By.CSS_SELECTOR, 'button.P\\(0\\).Trsdu\\(\\$normal\\)')
        #                               ) >= list_length)
        # driver.find_elements(By.CSS_SELECTOR, 'button.P\\(0\\).Trsdu\\(\\$normal\\)')[1].click()
        ActionChains(driver).send_keys(Keys.ARROW_UP).perform()

        person = TinderPerson(driver)

        dislike = handle_filters(driver, person, races, names, bio_keywords, interests)

        wait = WebDriverWait(driver, 10)
        list_length = 3
        wait.until(lambda driver: len(
            driver.find_elements(By.CSS_SELECTOR,
                                 'button.button.Lts\\(\\$ls-s\\).Z\\(0\\).CenterAlign.Mx\\(a\\).Cur\\(p\\).Tt\\(u\\)')
        ) >= list_length)
        # interaction_buttons = driver.find_elements(By.CSS_SELECTOR, 'button.button.Lts\\(\\$ls-s\\).Z\\('
        #                                                             ' 0\\).CenterAlign.Mx\\(a\\).Cur\\(p\\).Tt\\(u\\)')

        if random.random() * 100 < ratio and not dislike:
            click_next_photo(driver)
            # interaction_buttons[2].click()
            ActionChains(driver).send_keys(Keys.ARROW_RIGHT).perform()

        else:
            # interaction_buttons[0].click()
            ActionChains(driver).send_keys(Keys.ARROW_LEFT).perform()


def deny_notifications(driver: uc.Chrome) -> None:
    try:
        driver.find_elements(By.CLASS_NAME, 'c9iqosj oxn9zzn')[1].click()
    except:
        pass


def handle_filters(driver: uc, person: TinderPerson, races: list, names: list, bio_keywords: list,
                   interests: list) -> bool:
    dislike: bool = False

    if person.race not in races:
        dislike = True

    if names:
        if person.name not in names:
            dislike = True

    if bio_keywords:
        for keyword in bio_keywords:
            if keyword not in person.bio:
                dislike = True

    if interests:
        for interest in interests:
            if interest not in person.interests:
                dislike = True

    return dislike
