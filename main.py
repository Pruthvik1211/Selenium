from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.binary_location = "C:/Web_Driver_Test/chrome-win64/chrome.exe"  # Replace with the actual path

# Initialize the Chrome WebDriver without specifying the executable_path
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.google.com")
print(driver.page_source)

driver.quit()
