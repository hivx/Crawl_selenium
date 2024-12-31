import time
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Cấu hình Chrome WebDriver
options = ChromeOptions()
options.add_argument("--start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])

driver = webdriver.Chrome(options=options)

# URL của trang web
url = "https://diachidohanoi.vr360.com.vn/"

try:
    # Mở trang web
    driver.get(url)

    # Mở file để ghi dữ liệu
    with open("vr360/vr.txt", "w", encoding="utf-8") as file:
        try:
            # Chờ iframe xuất hiện và chuyển đổi ngữ cảnh sang iframe
            iframe = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "iframe[src*='globe/index.php']"))
            )
            driver.switch_to.frame(iframe)
            
            #Cho the body xuat hien
            body_element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.TAG_NAME, 'body'))
            )
            
            # Find elements with the class 'vt-card'
            cards = body_element.find_elements(By.CLASS_NAME, 'vt-card')

            # Iterate through the elements and print their attributes
            for card in cards:
                #Find data_panorama
                data_panorama = card.get_attribute('data-panorama')
                
                print(data_panorama)
                
                # file.write("'"+ data_panorama + "', ")
                file.write(data_panorama + "\n")
                
            # Chuyển đổi ngữ cảnh trở lại trang chính
            driver.switch_to.default_content()

        except Exception as e:
            print(f"Lỗi: {e}")
finally:
    time.sleep(1000)
    # Đóng trình duyệt
    driver.quit()
    