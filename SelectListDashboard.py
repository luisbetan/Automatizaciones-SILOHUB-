from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException


def verify_text_and_click(driver, xpath1, xpath2, xpath3, xpath4, xpath5, xpath6, xpath7, xpath8, xpath9, xpath10, xpath11):
    try:
        element_list = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, xpath1))
        )
        element_list.click()

        # Verifica si el número está presente en el elemento
        status1 = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, xpath2))
        ).text
        if status1 == "Pendiente":
            # Si el estado es "Pendiente", realiza las acciones necesarias
            otro_elemento2 = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, xpath3))
            )
            otro_elemento2.click()
            print(f"El status {status1} está presente.")

            otro_elemento3 = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, xpath4))
            )
            otro_elemento3.click()
        else:
            # Verifica si el número está presente en el elemento
            status2 = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, xpath5))
            ).text
            if status2 == "Pendiente":
                # Si el estado es "Pendiente", realiza las acciones necesarias
                otro_elemento4 = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, xpath6))
                )
                otro_elemento4.click()
                print(f"El status {status2} está presente.")

                otro_elemento5 = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, xpath7))
                )
                otro_elemento5.click()
            else:
                # Verifica si el número está presente en el elemento
                status3 = WebDriverWait(driver, 10).until(
                   EC.visibility_of_element_located((By.XPATH, xpath8))
                ).text
                if status3 == "Pendiente":
                    # Si el estado es "Pendiente", realiza las acciones necesarias
                    otro_elemento6 = WebDriverWait(driver, 10).until(
                       EC.visibility_of_element_located((By.XPATH, xpath9))
                    )
                    otro_elemento6.click()
                    print(f"El status {status3} está presente.")

                    otro_elemento7 = WebDriverWait(driver, 10).until(
                        EC.visibility_of_element_located((By.XPATH, xpath10))
                    )
                    otro_elemento7.click()
                  
                    
                else:
                    otro_elemento9 = WebDriverWait(driver, 10).until(
                        EC.visibility_of_element_located((By.XPATH, xpath11))
                    )
                    otro_elemento9.click()
                    print(f"El elemento de salida fue clicado.")

    except TimeoutException:
        print("Se ha agotado el tiempo de espera al buscar el elemento.")
    except NoSuchElementException:
        print("No se ha encontrado el elemento en la página.")