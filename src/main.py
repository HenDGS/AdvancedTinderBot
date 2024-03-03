import threading
from selenium_functions import *
from tkinter import Tk, messagebox


def main(amount: int = 100, ratio: int = 85, races: list = ['indian', 'asian', 'latino hispanic', 'black',
                                                            'middle eastern', 'white'], headless: bool = False,
         names: list = [], bio_keywords: list = [], interests: list = []) -> None:
    print('Bot started')

    driver: uc.Chrome = init_chrome(headless)

    driver.maximize_window()
    driver.get('https://tinder.com/app/recs')

    sleep = random.uniform(1, 5)
    time.sleep(sleep)

    thread = threading.Thread(target=deny_notifications, args=(driver,))
    thread.start()
    print('Started liking')
    like(driver, amount, ratio, races, names, bio_keywords, interests)

    driver.quit()
    thread.join()
    print('Bot finished')


def handle_first_login() -> None:
    root = Tk()
    root.withdraw()

    driver: uc.Chrome = init_chrome()

    driver.get('https://tinder.com/app/recs')

    try:
        login_button = driver.find_elements(By.CLASS_NAME, 'l17p5q9z')
        login_button[4].click()
    except:
        pass

    messagebox.showinfo("Tinder Bot", "Manually login and press OK to continue")
    messagebox.showinfo("Tinder Bot", "Login Saved")
    driver.quit()
    sys.exit()


def init_chrome(headless: bool = False) -> uc.Chrome:
    options = uc.ChromeOptions()
    options.add_argument('--no-first-run --no-service-autorun --password-store=basic')
    path = os.path.dirname(os.path.abspath(sys.argv[0]))
    options.add_argument(r"--user-data-dir=" + path + r"\ChromeData")

    driver = uc.Chrome(headless=headless, use_subprocess=True, options=options)

    return driver


if __name__ == '__main__':
    main()
