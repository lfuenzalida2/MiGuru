from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import os

# Función que retorna un dataframe con todos los trabajos de los terminos de la página "n" de busquedas mas recientes
def page_n(driver, df):
    # Obtenemos las busquedas mas recientes
    terms = driver.find_elements(By.CLASS_NAME, "col-l-3")

    # Revisamos todoas las busquedas
    for term in terms:
        # Termino que estamos revisando actualmente
        actual_term = term.text
        term.click()
        # Ofertas de trabajo que se encuentran en el término
        titles = driver.find_elements(By.XPATH, titles_Xpath)

        # Obtenemos el titulo que tiene la oferta de trabajo
        for result in titles:
            # Guardamos el titulo y el termino en un dataframe
            df2 = pd.DataFrame([[result.text, actual_term]], columns=['title', 'term'])
            df = pd.concat([df, df2], ignore_index=True)
        
        # Volvemos a la página donde están todos los términos
        driver.back()
    
    return df


# Algunas variables que se utilizan mas adelante
pagina_principal = "https://www.opcionempleo.cl/topqueries/"
freq_searchs = "//*[@id='browse-jobs']/div/div/ul[1]"
titles_Xpath = "//*[@id='search-content']/ul[2]/li/article/header/h2/a"
next_page = "//*[@id='browse-jobs']/div/div/ul[2]/li[12]/a"

# Usado para que no se tenga que abrir google chrome cada vez que se ejecuta el programa
options = webdriver.ChromeOptions()
# options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
service = Service(os.getcwd() + "\chromedriver.exe")

# Abre el browser y vamos a la página opcionesmpleo.cl/topqueries/
driver = webdriver.Chrome(service=service, options=options)
driver.get(pagina_principal)

# Espera a que la página haya cargado para evitar errores
while True:
    try:
        # Espera a que se cargue la página
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, freq_searchs)))
        print("Ha comenzado exitosamente el programa")
        break

    except:
        print("No se pudo contectar a la página, se volvera a intentar")

# Instanciamos el dataframe que guardará toda la información extraida
df = pd.DataFrame()

# Recorremos las 10 páginas que tienen las busquedas mas recientes
actual_page = 1
while(actual_page < 10):
    df = page_n(driver, df)
    actual_page += 1
    
    # Avanzamos a la siguiente página
    next_page_jobs = driver.find_element(By.XPATH, next_page)
    next_page_jobs.click()

driver.quit()

print(df)
# Guardamos la información en un archivo .csv
df.to_csv("results.csv")

print("Ha finalizado con éxito el programa")