from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def test_table_search_demo():
    # Specify the path to ChromeDriver using Service
    service = Service("C:\\Users\\Rajesh\\Downloads\\Compressed\\chromedriver_win32\\chromedriver.exe")
    
    # Initialize the WebDriver with the Service object
    driver = webdriver.Chrome(service=service)
    
    try:
        # Navigate to the Selenium Playground Table Search Demo
        driver.get("https://www.seleniumeasy.com/test/table-search-filter-demo.html")

        # Locate the search box and input "New York"
        search_box = driver.find_element(By.ID, "task-table-filter")
        search_box.send_keys("New York")
        
        # Validate that the search results show 5 entries
        rows = driver.find_elements(By.XPATH, "//table[@id='task-table']/tbody/tr")
        visible_rows = [row for row in rows if row.is_displayed()]
        
        assert len(visible_rows) == 5, f"Expected 5 visible rows, but found {len(visible_rows)}"
    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    pytest.main()
