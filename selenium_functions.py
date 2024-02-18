import io
import os
import random
import sys
import time
import tkinter
from tkinter import messagebox
import numpy as np
import undetected_chromedriver as uc
from PIL import Image
from deepface import DeepFace
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

try:
    os.chdir(sys._MEIPASS)
except:
    pass


def get_race(driver: uc.Chrome, i: int) -> str:
    img = driver.find_element(By.XPATH,
                              f'//*[@id="q1434999767"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div['
                              f'2]/div[1]/div[1]/span[{i}]')
    img_content = img.screenshot_as_png
    img = Image.open(io.BytesIO(img_content))
    img_rgb = img.convert('RGB')
    img_array = np.array(img_rgb)
    obj = DeepFace.analyze(img_array, actions=['race'], detector_backend='opencv', enforce_detection=False)
    race = obj[0]['dominant_race']
    return race


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


def click_next_photo(driver: uc.Chrome) -> None:
    for _ in range(random.randint(1, 3)):
        sleep = random.uniform(1, 4)
        time.sleep(sleep)

        from selenium.webdriver.common.action_chains import ActionChains

        mouse_hover = driver.find_element(By.XPATH, '//div[@class="Expand D(f) Pos(r) tappable-view Cur(p)"]')
        action = ActionChains(driver)
        action.move_to_element(mouse_hover).perform()

        next_button = driver.find_element(By.XPATH,
                                          '//*[local-name()="svg"][@class="Pos(a) Pe(n) Z(1) T(50%) End(0) Mx(10px) '
                                          'D(n)--s C($c-ds-foreground-button-primary) Op(0) tappable-view:h_Op(1) '
                                          'Trsdu($fast) Rotate(180deg)"]')
        action.move_to_element(next_button).click().perform()


def like(driver: uc.Chrome, amount: int, ratio: int, races: list) -> None:
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

        person_race = get_race(driver, 1)
        if person_race not in races:
            dislike = True

        if random.random() * 100 < ratio and not dislike:
            click_next_photo(driver)

            like_div = wait_element(driver, 'XPATH',
                                    '//div[@class="Mx(a) Fxs(0) Sq(70px) Sq(60px)--s Bd Bdrs(50%) Bdc('
                                    '$c-ds-border-gamepad-like-default)"]')
            like_button = like_div.find_element(By.TAG_NAME, 'button')
            like_button.click()

        else:
            dislike_div = wait_element(driver, 'XPATH',
                                       '//div[@class="Mx(a) Fxs(0) Sq(70px) Sq(60px)--s Bd Bdrs(50%) Bdc('
                                       '$c-ds-border-gamepad-nope-default)"]')
            dislike_button = dislike_div.find_element(By.TAG_NAME, 'button')
            dislike_button.click()


def login(driver: uc.Chrome) -> None:
    driver.get('https://tinder.com/app/recs')

    try:
        login_button = driver.find_elements(By.CLASS_NAME, 'l17p5q9z')
        login_button[4].click()
    except:
        pass

    messagebox.showinfo("Tinder Bot", "Manually login and press OK to continue")


def main(amount: int = 100, ratio: int = 85, first_login: bool = False,
         races: list = ['indian', 'asian', 'latino hispanic', 'black', 'middle eastern', 'white'],
         headless: bool = True) -> None:

    root = tkinter.Tk()
    root.iconbitmap('./tinder-128.ico')
    root.withdraw()

    options = uc.ChromeOptions()

    options.add_argument('--no-first-run --no-service-autorun --password-store=basic')
    path = os.path.dirname(sys.argv[0])
    options.add_argument(r"--user-data-dir=" + path + r"\ChromeData")

    if first_login:
        driver = uc.Chrome(headless=False, use_subprocess=True, options=options)
    else:
        driver = uc.Chrome(headless=headless, use_subprocess=True, options=options)

    driver.maximize_window()

    driver.get('https://tinder.com/app/recs')

    if first_login:
        login(driver)
        messagebox.showinfo("Tinder Bot", "Login Saved")
        driver.quit()
        sys.exit()

    driver.get('https://tinder.com/app/recs')

    sleep = random.uniform(1, 5)
    time.sleep(sleep)

    like(driver, amount, ratio, races)

    driver.quit()


if __name__ == '__main__':
    main()
