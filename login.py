import time
from selenium import webdriver
from selenium.webdriver import ChromeOptions, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Cấu hình Chrome WebDriver
options = ChromeOptions()
options.add_argument("--start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])

driver = webdriver.Chrome(options=options)
url = "https://twitter.com/i/flow/login"
driver.get(url)

# Bước 1: Nhập email
email_input = WebDriverWait(driver, 60).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[autocomplete="username"]'))
)
email_input.send_keys("niknamenr01@gmail.com")  # Thay bằng email của bạn
email_input.send_keys(Keys.ENTER)

# Bước 2: Nhập nickname sau khi trang load (có thể trang yêu cầu xác minh trước nickname)
nickname_input = WebDriverWait(driver, 60).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[autocomplete="on"]'))
)
nickname_input.send_keys("hieuervxp")  # Thay bằng nickname của bạn
nickname_input.send_keys(Keys.ENTER)

# Bước 3: Nhập mật khẩu sau khi trang load
password_input = WebDriverWait(driver, 60).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="password"]'))
)
password_input.send_keys("testpython")  # Thay bằng mật khẩu của bạn
password_input.send_keys(Keys.ENTER)


# Chờ cho đến khi quá trình đăng nhập hoàn tất
WebDriverWait(driver, 60).until(EC.url_contains("/home"))

# Bước 4: Thực hiện tìm kiếm bằng cách mở URL tìm kiếm sau khi đăng nhập
search_url = "https://twitter.com/search?q=%23btc%20%23bnb&src=typed_query&f=user"
driver.get(search_url)

time.sleep(5)

# Mở file để ghi dữ liệu
with open("data/data_test.txt", "w", encoding="utf-8") as file:
    
    # Lấy chiều cao trang ban đầu
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Tìm thẻ div có thuộc tính aria-label="Timeline: Search timeline"
        try:
            timeline_div = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[aria-label="Timeline: Search timeline"]'))
            )

            # Tìm tất cả các thẻ span bên trong thẻ div timeline_div
            spans = timeline_div.find_elements(By.TAG_NAME, "span")

            for span in spans:
                # Kiểm tra xem thẻ span có nằm bên trong thẻ div[dir="auto"] hay không
                parent_divs = span.find_elements(By.XPATH, './ancestor::div[@dir="auto"]')
                
                # Debug: In ra text của span và số lượng parent div tìm thấy
                print(f"Span text: {span.text}, Parent div count: {len(parent_divs)}")
                
                # Nếu không có thẻ div[dir="auto"] làm cha, thì ghi dữ liệu
                if len(parent_divs) == 0:
                    file.write(span.text + "\n")

        except Exception as e:
            print("Lỗi khi tìm thẻ div hoặc ghi dữ liệu: ", e)
        
        # Lăn chuột xuống cuối trang để tải thêm dữ liệu
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Chờ 3 giây để trang tải thêm nội dung
        time.sleep(5)

        # Lấy chiều cao trang mới sau khi lăn chuột
        new_height = driver.execute_script("return document.body.scrollHeight")

        # Nếu chiều cao trang không đổi, nghĩa là không có dữ liệu mới, thoát khỏi vòng lặp
        if new_height == last_height:
            break

        # Cập nhật chiều cao trang mới để tiếp tục lăn
        last_height = new_height
        
# Thời gian chờ
time.sleep(1000)

# Đóng trình duyệt sau khi hoàn thành
# driver.quit()
