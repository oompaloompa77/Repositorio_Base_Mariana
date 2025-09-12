# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# import time

# navegador = webdriver.Chrome()
# navegador.get(" https://books.toscrape.com")

# time.sleep(14)

# livros = navegador.find_elements(By.CLASS_NAME, "product_pod")

# for livro in livros[:5]:
#     titulo = livro.find_element(By.TAG_NAME, "h3").find_element(By.TAG_NAME, "a").get_attribute("title")
#     preco = livro.find_element(By.CLASS_NAME, "price_color").text
#     print(f"Livro: {titulo} - Preço: {preco}")



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

navegador = webdriver.Chrome()
navegador.get('https://www.timeanddate.com/weather/brazil/sao-paulo')

time.sleep(14)

temperatura = navegador.find_element(By.CSS_SELECTOR, "div#qlook .h2").text
print("A temperatura atual em São Paulo é:", temperatura)
