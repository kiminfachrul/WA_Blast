# WhatsApp Automation Script

## Description
This script is designed to automatically send WhatsApp messages using Selenium, PyAutoGUI, and Pandas. The script reads customer data from an Excel file and sends personalized messages to each customer via WhatsApp Web. It also includes features for sending attachments (images/videos) and adding delays between messages to avoid being detected as spam by WhatsApp.

## Libraries Used
This script uses the following Python libraries:
1. **Selenium**: Used to automate the browser and access WhatsApp Web.
2. **PyAutoGUI**: Used to automate mouse clicks and keyboard inputs, particularly for handling UI elements that are difficult to access with Selenium.
3. **Pyperclip**: Used for clipboard manipulation, such as copying the file path of an image.
4. **Pandas**: Used to read and manage data from an Excel file.
5. **Webdriver Manager**: Used to automatically manage the Chrome browser driver.

## Dependency Installation
Before running the script, you need to install all required dependencies. Run the following command in your terminal or command prompt:
```sh
pip install selenium pyautogui pyperclip pandas webdriver-manager
```

## Setup and Code Customization

1. **Excel File (`data_user.xlsx`)**:
   Ensure that the Excel file named `data_user.xlsx` is in the same directory as the script. This file should have the following columns:
   - `id_pelanggan`: Customer ID.
   - `nama`: Customer name.
   - `nomor_wa`: Customer's WhatsApp number (in international format, without the + sign).
   - `status`: Customer status.
   - `teks`: Additional text to be included in the WhatsApp message.

2. **Chrome Profile Configuration**:
   To allow the script to access WhatsApp Web without requiring repeated logins, you need to set the `user_data` variable with the path to the Chrome profile that is already logged into WhatsApp Web:
   ```python
   user_data = "user-data-dir=C:\\Users\\your_username\\AppData\\Local\\Google\\Chrome\\User Data"
   ```
