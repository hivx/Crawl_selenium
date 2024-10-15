from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Thay đổi thông tin đăng nhập của bạn ở đây
USERNAME = 'niknamenr01@gmail.com'  # Thay 'your_username' bằng tên đăng nhập Twitter của bạn
PASSWORD = 'testpython'    # Thay 'your_password' bằng mật khẩu của bạn

# Khởi tạo Chrome WebDriver
driver = webdriver.Chrome()

# Mở Twitter
driver.get("https://twitter.com/login")
#auth_token = "fe18d7f6c0c5da7a2679aca6fafd9c393e4bb3d3"

# Đợi cho đến khi các trường đăng nhập có sẵn
try:
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "text"))
    )
    username_field.send_keys(USERNAME)
    username_field.send_keys(Keys.RETURN)

    # Đợi cho đến khi trường mật khẩu có sẵn
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
    password_field.send_keys(PASSWORD)
    password_field.send_keys(Keys.RETURN)

    # Đợi cho đến khi trang chính của Twitter tải xong
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Search Twitter"]'))
    )

    # Tìm kiếm
    search_box = driver.find_element(By.XPATH, '//input[@placeholder="Search Twitter"]')
    search_box.send_keys("Blockchain")
    search_box.send_keys(Keys.RETURN)

    # Đợi kết quả tải
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//article'))
    )

    # Lấy dữ liệu từ các tweet
    tweets = driver.find_elements(By.XPATH, '//article')

    for tweet in tweets:
        try:
            content = tweet.find_element(By.XPATH, './/div[2]/div[1]').text
            print(content)
        except Exception as e:
            print("Lỗi:", e)

finally:
    # Đóng trình duyệt
    driver.quit()
