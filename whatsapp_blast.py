import time
import pyautogui
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd 

# FICCCC APOEMOe4r4
df = pd.read_excel('data_user.xlsx')

# untuk driver Selenium
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:/Users/Fachrul Islam/AppData/Local/Google/Chrome/User Data/profile 4")
options.add_argument("profile-directory=Profile 1")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Buka WhatsApp Web
driver.get('https://web.whatsapp.com/')
# input("Scan QR code dan tekan Enter setelah login...")

# Fungsi untuk mengirim pesan
def kirim_pesan(nomor, nama, pesan):
    # Buka chat
    driver.get(f'https://web.whatsapp.com/send?phone={nomor}&text={pesan}')
    
    try:
        # search_box = WebDriverWait(driver, 20).until(
        #     EC.presence_of_element_located((By.XPATH, '//div[@data-testid="chat-list-search"]//p[@contenteditable="true"]'))
        # )
        # search_box.clear()
        # search_box.send_keys(nomor)
        # search_box.send_keys(Keys.ENTER)

        # Tunggu hingga pesan terisi di kotak chat
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="x1hx0egp x6ikm8r x1odjw0f x1k6rcq7 x6prxxf"][@data-tab="10"]'))
        )
    
        time.sleep(3)
        
        # Tekan tombol Enter untuk mengirim pesan
        message_box = driver.find_element(By.XPATH, '//div[@class="x1hx0egp x6ikm8r x1odjw0f x1k6rcq7 x6prxxf"][@data-tab="10"]')
        message_box.send_keys(pesan)
        message_box.send_keys(Keys.ENTER)

        print(f"Pesan berhasil dikirim ke {nama} ({nomor})")
        
        time.sleep(3) 
        
    except Exception as e:
        print(f"Gagal mengirim pesan ke {nama} ({nomor}): {str(e)}")

# disini fungsi loop di eksekusi
for index, row in df.head(2).iterrows():
    id_pelanggan = row['id_pelanggan']
    nama = row['nama']
    nomor_wa = row['nomor_wa']
    status = row['status']
    
    # Buat pesan
    pesan = f"HELLO!! {nama}, ini adalah pesan otomatis untuk pelanggan dengan ID: {id_pelanggan}. Status Anda saat ini adalah: {status}"
    
    try:
        kirim_pesan(nomor_wa, nama, pesan)
    except Exception as e:
        print(f"Gagal mengirim pesan ke {nama} ({nomor_wa}): {str(e)}")

# Tutup browser
driver.quit()
