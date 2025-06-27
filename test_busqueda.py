from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException




import time
#driver = webdriver.Chrome()

options = Options()
options.add_argument('--headless=new')  # O '--headless' si falla
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-gpu')
options.add_argument('--remote-debugging-port=9222')
options.add_argument('--user-data-dir=/tmp/chrome-user-data')  # Evita el conflicto

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

driver.get("https://duckduckgo.com/")

# Buscar campo de texto
buscador = driver.find_element(By.NAME, "q")
buscador.send_keys("inmuebles en Bogotá")
buscador.send_keys(Keys.RETURN)

# Esperar resultados
time.sleep(2)

# Validar que exista algún resultado
#resultados = driver.find_elements(By.CSS_SELECTOR,".LnpumSThxEWMIsDdAT17")

#resultados = WebDriverWait(driver, 10).until(
#    EC.presence_of_element_located((By.CSS_SELECTOR, ".LnpumSThxEWMIsDdAT17"))
#)
#assert len(EC) > 0, "No se encontraron resultados."
#print("✅ Prueba funcional completada con éxito")

try:
    resultados = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".LnpumSThxEWMIsDdAT17"))
)
    print("Elemento encontrado:", resultados)
except TimeoutException:
    print("El elemento NO se cargó en el tiempo esperado.")


time.sleep(5)
#driver.quit()