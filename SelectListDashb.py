
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def seleccionar_movimiento_pendiente(driver):
    try:
        # Esperar a que la página cargue completamente
        movimientos = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grain-dashboard/app-grain-dashboard-list/app-responsive-table/div/div/table/tbody/tr[1]/td[1]")))
        movimientos.click()
        time.sleep(3)

        # Verificar el estado del movimiento
        estado_movimiento_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-intentions-detail/app-responsive-table/div/div/table/tbody/tr/td[5]/span/span/div/div[1]")))
        estado_movimiento_text = estado_movimiento_element.text

        if estado_movimiento_text == "Pendiente":
            print(f"El estado actual es : '{estado_movimiento_text}'")
            # Seleccionar la opción de aceptar en el desplegable
            desplegable = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//i[@class="bx bx-dots-horizontal-rounded ps-1"]')))
            desplegable.click()
            time.sleep(2)
            opcion_aceptar = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-intentions-detail/app-responsive-table/div/div/table/tbody/tr/td[5]/span/span/div/div[2]/div/a[1]/text()")))
            opcion_aceptar.click()

            # Hacer clic en algún botón de confirmación o continuar
            # (Esto puede variar dependiendo de la página web)
        else:
            # Volver al listado de movimientos
            go_out= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-layout/app-vertical/div/div/div/app-header-for-screen/div/div/div/a")))
            go_out.click()
    except TimeoutException:
        print("Tiempo de espera excedido. No se encontró el elemento esperado.")
        # Manejar la excepción según sea necesario