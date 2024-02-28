import threading
from selenium_functions import *
from tkinter import Tk, messagebox


def main(amount: int = 100, ratio: int = 85, races: list = ['indian', 'asian', 'latino hispanic', 'black',
                                                            'middle eastern', 'white'], headless: bool = False,
         names: list = []) -> None:
    print('Bot started')

    options = uc.ChromeOptions()
    options.add_argument('--no-first-run --no-service-autorun --password-store=basic')
    path = os.path.dirname(sys.argv[0])
    options.add_argument(r"--user-data-dir=" + path + r"\ChromeData")

    driver = uc.Chrome(headless=headless, use_subprocess=True, options=options)
    driver.maximize_window()
    driver.get('https://tinder.com/app/recs')

    sleep = random.uniform(1, 5)
    time.sleep(sleep)

    thread = threading.Thread(target=deny_notifications, args=(driver,))
    thread.start()
    print('Started liking')
    like(driver, amount, ratio, races, names)

    driver.quit()
    thread.join()
    print('Bot finished')


def handle_first_login() -> None:
    root = Tk()
    root.iconbitmap('tinder-128.ico')
    root.withdraw()

    options = uc.ChromeOptions()

    options.add_argument('--no-first-run --no-service-autorun --password-store=basic')
    path = os.path.dirname(sys.argv[0])
    options.add_argument(r"--user-data-dir=" + path + r"\ChromeData")

    driver = uc.Chrome(headless=False, use_subprocess=True, options=options)

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


if __name__ == '__main__':
    main()
