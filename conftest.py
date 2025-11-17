# conftest.py
import pytest
import tempfile
import shutil
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver(request, tmp_path):

    worker_id = getattr(request.config, "workerinput", {}).get("workerid", "main")

    profile_dir = tmp_path / f"chrome-profile-{worker_id}"
    download_dir = tmp_path / f"downloads-{worker_id}"
    profile_dir.mkdir(parents=True, exist_ok=True)
    download_dir.mkdir(parents=True, exist_ok=True)

    chrome_options = Options()

    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--no-first-run")
    chrome_options.add_argument("--no-default-browser-check")
    chrome_options.add_argument("--disable-gpu")
    # chrome_options.add_argument("--headless=new")

    chrome_options.add_argument(f"--user-data-dir={str(profile_dir)}")

    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "password_manager_leak_detection": False,
        "profile.password_leak_detection_enabled": False,
        "download.default_directory": str(download_dir),
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": False,
    }
    chrome_options.add_experimental_option("prefs", prefs)

    chrome_options.add_argument("--disable-save-password-bubble")
    chrome_options.add_argument("--disable-features=PasswordLeakDetection,PasswordManagerOnboarding,AutofillServerCommunication")

    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.maximize_window()
    driver.implicitly_wait(10)

    yield driver

    try:
        driver.quit()
    except Exception:
        pass

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Run the test, then get result
    outcome = yield
    result = outcome.get_result()

    driver = item.funcargs.get('driver', None)

    if driver and result.when == "call" and result.failed:
        screenshot_name = f"{item.name}.png"

        # Create screenshots directory if not exists
        import os
        folder = "screenshots"
        if not os.path.exists(folder):
            os.makedirs(folder)

        filepath = os.path.join(folder, screenshot_name)
        driver.save_screenshot(filepath)
        print(f"\n Screenshot saved on test failure → {filepath}\n")