# Selenium - Automatizando tarefas no navegador
from pathlib import Path
from time import sleep
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
# Chrome Options

# Caminho para a raiz do projeto
ROOT_FOLDER = Path(__file__).parent

# Caminho para a pasta onde o chromedriver está
EDGE_DRIVER_PATH = ROOT_FOLDER / 'drivers' / 'msedgedriver.exe'

def make_edge_browser(*options: str) -> webdriver.Edge:
    edge_options = webdriver.EdgeOptions()

    # edge_options.add_argument('--headless')
    if options is not None:
        for option in options:
            edge_options.add_argument(option)  
    edge_service = Service(
        executable_path=str(EDGE_DRIVER_PATH)
    )
    
    browser = webdriver.Edge(
        service=edge_service,
        options=edge_options
    )
    return browser
if __name__ == '__main__':
    TIME_TO_WAIT = 10
    
    options = ()
    browser = make_edge_browser(*options)

    # mandando navegador abrir
    browser.get('https://www.google.com/')

    
    try:
        search_input = WebDriverWait(browser, TIME_TO_WAIT).until(
            EC.presence_of_element_located(
                (By.NAME, 'q')
            )
        )
        search_input.send_keys('Hello World!')
        search_input.send_keys(Keys.ENTER)
    except:
        print('ERRO INESPERADO.')
    
    # Dorme por 10 segundos
    sleep(TIME_TO_WAIT)