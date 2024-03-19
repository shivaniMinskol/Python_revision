from selenium import webdriver
import pytest
@pytest.fixture(params=["chrome","firefox"],scope="class")


def init_browser(request):
    if request.param == "chrome":
        driver=webdriver.Chrome()
        driver.get('https://www.google.com')
    elif request.param=="firefox":
        driver= webdriver.Firefox()
        driver.get("https://www.google.com")
    else:
        print("incorrect driver")
    request.cls.driver = driver

    yield driver
    driver.quit()

@pytest.mark.usefixtures("init_browser")
class arrangment:
    pass
class assertion(arrangment):
    def test_title(self):
        assert self.driver.title == "Google"
        print("test case pass")

