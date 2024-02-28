import tkinter
from selenium_functions import *


def main(amount: int = 100, ratio: int = 85, first_login: bool = False,
         races: list = ['indian', 'asian', 'latino hispanic', 'black', 'middle eastern', 'white'],
         headless: bool = False, names: list = []) -> None:
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

    like(driver, amount, ratio, races, names)

    driver.quit()


if __name__ == '__main__':
    main()
