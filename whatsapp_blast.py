import time
import pyautogui
import pyperclip
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd 

df = pd.read_excel('data_user.xlsx')

user_data = "user-data-dir=C:\\Users\\Fachrul Islam\\AppData\\Local\\Google\\Chrome\\User Data"
options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
})
options.add_argument(user_data)
options.add_argument("--profile-directory=Default")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Buka WhatsApp Web
driver.get('https://web.whatsapp.com/')

# Fungsi untuk mengirim pesan
def kirim_pesan(nomor_wa, nama, pesan):
    # Buka chat
    driver.get(f'https://web.whatsapp.com/send?phone={nomor_wa}&text={pesan}')
    
    try:

        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="x1hx0egp x6ikm8r x1odjw0f x1k6rcq7 x6prxxf"][@data-tab="10"]'))
        )
    
        time.sleep(2)

        # Tekan tombol Enter untuk mengirim pesan
        message_box = driver.find_element(By.XPATH, '//div[@class="x1hx0egp x6ikm8r x1odjw0f x1k6rcq7 x6prxxf"][@data-tab="10"]')
        # message_box.send_keys(pesan)

        #Klik logo attach
        x, y = pyautogui.locateCenterOnScreen("lampir.png", confidence= 0.9)
        pyautogui.moveTo(x, y, duration = 1)
        pyautogui.leftClick()
        time.sleep(1)

        #Klik tambah foto atau video
        x, y = pyautogui.locateCenterOnScreen("ft.png", confidence= 0.9)
        pyautogui.moveTo(x, y, duration = 1)
        pyautogui.leftClick()
        time.sleep(1)

        #Menyalin path lokasi gambar/iimage
        file_path = r"D:\WAB\sebaran.png" #Ubah sesuai path yang di inginkan
        pyperclip.copy(file_path)
        pyautogui.sleep(2)
        pyautogui.hotkey("ctrl", "v")
        
        pyautogui.sleep(1)
        x, y = pyautogui.locateCenterOnScreen("open.png", confidence= 0.9)
        pyautogui.moveTo(x, y, duration = 1)
        pyautogui.leftClick()
        pyautogui.sleep(1)

        x, y = pyautogui.locateCenterOnScreen("send.png", confidence= 0.9)
        pyautogui.moveTo(x, y, duration = 1)
        pyautogui.leftClick()

        print(f"Pesan berhasil dikirim ke {nama} ({nomor_wa})")
        time.sleep(6) 
        
    except Exception as e:
        print(f"Gagal mengirim pesan ke {nama} ({nomor_wa}): {str(e)}")

# disini fungsi loop di eksekusi
for index, row in df.head(10).iterrows():
    id_pelanggan = row['id_pelanggan']
    nama = row['nama']
    nomor_wa = row['nomor_wa']
    status = row['status']
    teks_pesan = row['teks']
    
    # Buat pesan
    pesan = f"HELLO PIONER!! {nama}, ini adalah pesan otomatis untuk pelanggan PLN UP3 Makassar Selatan dengan ID: {id_pelanggan}. Status Anda saat ini adalah: {status}. \n {teks_pesan}" #pemanggilan teks_pesan ini di ambil dari excel

    try:
        kirim_pesan(nomor_wa, nama, pesan)
    except Exception as e:
        print(f"Gagal mengirim pesan ke {nama} ({nomor_wa}): {str(e)}")
        
driver.quit()
