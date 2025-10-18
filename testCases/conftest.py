import pytest
from selenium import webdriver

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()                   # Launch browser
    driver.maximize_window()                      # Maximize browser window
    yield driver                                  # Return driver to the test
    driver.quit()                                 # Close browser after test finishes


# --- Optional: attach screenshot on failure for pytest-html report ---
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("setup")       # ✅ Get driver from fixture, not self
        if driver:
            driver.save_screenshot("reports/failure_screenshot.png")
