from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
import numpy as np
from PIL import Image
from deepface import DeepFace
import io


class TinderPerson:
    def __init__(self, driver: uc.Chrome):
        self.driver = driver
        self.name = self.get_name()
        self.age = self.get_age()
        self.race = self.get_race(1)

    def get_name(self) -> str:
        class_name: str = format_class_name('Typs(display-1-strong) Fxs(1) Fxw(w) Pend(8px) M(0) D(i)', 'h1')
        name: str = self.driver.find_element(By.CSS_SELECTOR, class_name).text
        return name

    def get_age(self) -> str:
        age = self.driver.find_element(By.CSS_SELECTOR, format_class_name('Whs(nw) Typs(display-2-strong)',
                                                                          'span')).text
        return age

    def get_race(self, i: int) -> str:
        img = self.driver.find_element(By.CSS_SELECTOR, format_class_name('profileCard__slider__img Z(-1)', 'div'))
        img_content = img.screenshot_as_png
        img = Image.open(io.BytesIO(img_content))
        img_rgb = img.convert('RGB')
        img_array = np.array(img_rgb)
        obj = DeepFace.analyze(img_array, actions=['race'], detector_backend='opencv', enforce_detection=False)
        race = obj[0]['dominant_race']
        return race


def format_class_name(class_name: str, element: str) -> str:
    formatted_class_name = class_name.replace('(', '\\(').replace(')', '\\)').replace(' ', '.')
    formatted_class_name = f'{element}.{formatted_class_name}'
    return formatted_class_name
