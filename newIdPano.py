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
url = "https://diachidohanoi.vr360.com.vn/?vt143vt"

try:
    # Mở trang web
    driver.get(url)

    # Mở file để ghi dữ liệu
    with open("vr360/vr_new.txt", "w", encoding="utf-8") as file:
        try:
            # Chờ iframe đầu tiên xuất hiện và chuyển đổi ngữ cảnh sang iframe đầu tiên
            first_iframe = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "iframe[src*='globe/index.php']"))
            )
            driver.switch_to.frame(first_iframe)

            # Chờ iframe thứ hai xuất hiện trong iframe đầu tiên và chuyển đổi ngữ cảnh sang iframe thứ hai
            second_iframe = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "iframe[src*='../viewer/index.php']"))
            )
            driver.switch_to.frame(second_iframe)

            # Tìm thẻ <div> với class là "list_slider"
            list_slider_div = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='list_slider']"))
            )

            # Tìm thẻ <ul> có class là "slidee"
            ul_elements = list_slider_div.find_elements(By.TAG_NAME, "ul")

            # Duyệt qua tất cả các thẻ <li> bên trong thẻ <ul>
            for ul in ul_elements:
                li_elements = ul.find_elements(By.TAG_NAME, "li")

                for li in li_elements:
                    # Hoặc in các thuộc tính cụ thể
                    print(f"{li.get_attribute('data-panorama')}\n")
                    
                    # Hoặc in các thuộc tính cụ thể
                    file.write(f"{li.get_attribute('data-panorama')}\n")
                
            # Chuyển đổi ngữ cảnh trở lại trang chính
            driver.switch_to.default_content()

        except Exception as e:
            print(f"Lỗi: {e}")
finally:
    time.sleep(1000)
    # Đóng trình duyệt
    driver.quit()
