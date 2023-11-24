from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# Запрашиваем URL и количество просмотров
url = input("Введите URL для генерации просмотров (или оставьте пустым для выбора предустановки): ")
if not url:
    url = "https://t.me/best_places"  # Пример предустановки
try:
    count = int(input("Введите количество желаемых просмотров: "))
except ValueError:
    print("Нужно ввести число.")
    exit()

# Установка опций WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--incognito")  # Открыть окно в режиме инкогнито

# Путь к ChromeDriver (установите свой путь, если он отличается)
driver_path = 'chromedriver'  # Обычно достаточно, если chromedriver.exe в PATH

# Функция для ожидания загрузки страницы
def wait_for_page_load(driver, timeout=7):
    try:
        # Ожидание загрузки элемента body
        WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        return True
    except TimeoutException:
        print("Страница не загрузилась в течение заданного времени.")
        return False

# Создаем экземпляр WebDriver
driver = webdriver.Chrome(driver_path, options=options)

for i in range(count):
    # Открываем новую вкладку
    driver.execute_script("window.open(arguments[0]);", url)
    time.sleep(2)  # Симуляция ожидания загрузки страницы
    if wait_for_page_load(driver):
        # Если страница загрузилась, закрываем вкладку
        if len(driver.window_handles) > 1:
            driver.switch_to.window(driver.window_handles[-1])
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
    else:
        driver.quit()
        break

# Закрыть браузер после выполнения всех операций
driver.quit()