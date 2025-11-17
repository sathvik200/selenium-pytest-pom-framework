# 🧪 Selenium Automation Framework (Python + PyTest + POM)

A complete end-to-end UI automation framework using:

- **Python**
- **Selenium WebDriver**
- **PyTest**
- **Page Object Model (POM)**
- **WebDriver Manager**
- **HTML Reporting**
- **Automatic Screenshots on Failure**

This project automates functional test scenarios on sample e-commerce applications like **SauceDemo** using clean, scalable, maintainable architecture.

---

# 🚀 **Features**

### ✔ Page Object Model (POM)
Each page is represented as a class with:
- Locators
- UI actions
- Utility methods  
Test files contain **only assertions**, not UI logic.

### ✔ Automatic Screenshots on Failure
Every failed test generates a `.png` inside `/screenshots`.

### ✔ HTML Test Reports
Generate beautiful HTML reports with:
pytest --html=reports/report.html --self-contained-html

### ✔ Clean Test Structure
Tests are grouped by feature:
- login
- products
- cart
- checkout

### ✔ Chrome Popup Handling
Includes logic to auto-dismiss Google Chrome password popups.

---

# 🛠 **Setup Instructions**

## 1️⃣ Create Virtual Environment
python -m venv .venv

Activate:

### Windows:
.venv\Scripts\activate

### macOS / Linux:
source .venv/bin/activate


---

## 2️⃣ Install Dependencies
pip install -r requirements.txt


dependencies include:
- selenium  
- pytest  
- pytest-html  
- webdriver-manager  

---

# ▶️ **Running Tests**

### Run all tests:
pytest -v

### Run single test:
pytest tests/test_login.py -v


### Run with HTML report:
pytest --html=reports/report.html --self-contained-html


---

# 🧪 **Writing Tests (Example)**

```python
def test_valid_login(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")
    assert login.is_logged_in()
