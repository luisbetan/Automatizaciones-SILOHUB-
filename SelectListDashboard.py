from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException


def verify_text_and_click(driver, xpath1, xpath2, xpath3, xpath4, xpath5):
    try:
        element_list = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, xpath1))
        )
        element_list.click()

        # Verifica si el número está presente en el elemento
        status = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, xpath2))
        ).text
        if status == "Pendiente":
            # Si el número está presente, realiza la acción necesaria
            # Por ejemplo, hacer clic en otro elemento
            otro_elemento2 = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, xpath3))
            )
            otro_elemento2.click()
            print(f"El status {status} está presente.")

            otro_elemento3 = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, xpath4))
            )
            otro_elemento3.click()
        else:
            otro_elemento4 = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, xpath5))
            )
            otro_elemento4.click()
            print(f"El status Pendiente no está presente.")

    except TimeoutException:
        print("Se ha agotado el tiempo de espera al buscar el elemento.")
    except NoSuchElementException:
        print("No se ha encontrado el elemento en la página.")