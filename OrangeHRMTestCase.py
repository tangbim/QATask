from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import edge
import time

options = webdriver.EdgeOptions()
options.add_experimental_option('detach', True)

driver = webdriver.Edge(options=options)

url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

driver.get(url)
driver.maximize_window()
driver.implicitly_wait(10)

# test case berhasil login
driver.find_element(By.NAME, "username").send_keys("Admin")
time.sleep(0.1)

driver.find_element(By.NAME, "password").send_keys("admin123")
time.sleep(0.1)

driver.find_element(
    By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
time.sleep(2)
if ("Time at Work" in driver.page_source):
    print("Berhasil Login")

time.sleep(1.5)

driver.find_element(
    By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/i').click()
time.sleep(0.1)

driver.find_element(By.LINK_TEXT, "Logout").click()
print("Berhasil Logout")
time.sleep(3)

# test case login kosong
driver.find_element(
    By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()

if ("Required" in driver.page_source):
    print("Berhasil ujicoba login kosong")

# test case apabila username/password salah

driver.find_element(By.NAME, "username").send_keys("tes")
time.sleep(0.1)

driver.find_element(By.NAME, "password").send_keys("tes21")
time.sleep(0.1)


driver.find_element(
    By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
time.sleep(2)

if ("Invalid credentials" in driver.page_source):
    print("Login tidak berhasil, Berhasil ujicoba username dan password bernilai salah")

# ujicoba semua link text pada login page
driver.find_element(By.PARTIAL_LINK_TEXT, "Inc").click()
time.sleep(3)
if ("Free Demo" in driver.page_source):
    print("Berhasil membuka link text")
time.sleep(3)

# berpindah ke halaman utama
driver.switch_to.window(driver.window_handles[0])

# login again
driver.find_element(By.NAME, "username").send_keys("Admin")
time.sleep(0.1)

driver.find_element(By.NAME, "password").send_keys("admin123")
time.sleep(0.1)

driver.find_element(
    By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
time.sleep(2)
if ("Time at Work" in driver.page_source):
    print("Berhasil Login")

# change password
driver.find_element(
    By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/i').click()
time.sleep(0.1)

driver.find_element(By.LINK_TEXT, 'Change Password').click()
time.sleep(1)

driver.find_element(
    By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/input').send_keys("admin123")

driver.find_element(
    By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input').send_keys("GanTiPas123!")

driver.find_element(
    By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input').send_keys("GanTiPas123!")

driver.find_element(
    By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]').click()
time.sleep(0.2)

elem = driver.find_element(
    By.XPATH, '//*[@id="oxd-toaster_1"]/div/div[1]/div[2]/p[1]').text

# validate status peggantian password
if elem == "Success":
    print("Berhasil Mengubah password")
else:
    print("Gagal Mengubah password")

# tambah pegawai

driver.find_element(
    By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a').click()
time.sleep(1)

driver.find_element(
    By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button').click()
time.sleep(2)
driver.find_element(By.NAME, "firstName").send_keys("Dedy")
driver.find_element(By.NAME, "middleName").send_keys("Cahyadi")
driver.find_element(By.NAME, "lastName").send_keys("Ikram") #fill field

driver.find_element(
    By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]').click()
time.sleep(1.5)


elem = driver.find_element(
    By.XPATH, '//*[@id="oxd-toaster_1"]/div/div[1]/div[2]/p[1]').text

# validate status tambah user
if elem == "Success":
    print("Berhasil Menambah User")
else:
    print("Gagal Menambah User")
