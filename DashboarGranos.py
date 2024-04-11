from telnetlib import EC
import unittest
import xmlrunner
import time
from Elements import  find_elements, ingresar_rango_fecha
from Loginhelper import LoginHelper
from startSession import StartSession




class dashboard_granos(unittest.TestCase):
    
    def setUp(self):
       
       
        self.start_session = StartSession()
        self.driver = self.start_session.driver
        # Inicializar la clase LoginHelper
        self.login_helper = LoginHelper(self.driver)
   
   
    def test_dashboard_grain(self):
        # Utilizar métodos de LoginHelper para el inicio de sesión
        self.login_helper.login("admingd@silohub.ag", "G@viglio123")
        self.login_helper.select_tenant()
        self.login_helper.search_and_select_account("1023")

        select_grain = "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[3]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[3]/a/span"
        find_elements(self.driver,select_grain)
        time.sleep(2)

        select_dashboard_grain = "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[3]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[3]/div/ul/li[4]/a"
        find_elements(self.driver,select_dashboard_grain)
        time.sleep(2)

        # aplicar el filtro solo con los productos maiz y soja 

        select_button_filter = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grain-dashboard/app-grain-dashboard-list/app-header-for-responsive-table/div/div/div[2]/div/div/app-filter-button/button/div/i"
        find_elements(self.driver,select_button_filter)
        time.sleep(2)

        select_product1 = "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-grain-container/div/app-grain-button[2]/div/img"
        find_elements(self.driver,select_product1)
        time.sleep(2)

        select_product2 = "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-grain-container/div/app-grain-button[4]/div/div"
        find_elements(self.driver,select_product2)
        time.sleep(2)

        select_data_day = "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-date-filter/div/app-date-picker/div/input[2]"  # Reemplazar con el XPath correcto
        ingresar_rango_fecha(select_data_day, self.driver)
        time.sleep(2)

        appliy_filter = "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-date-filter/div/app-date-picker/div/input[1]"
        find_elements(self.driver,appliy_filter)
        time.sleep(2)

        select_movements_list = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grain-dashboard/app-grain-dashboard-list/app-responsive-table/div/div/table/tbody/tr[1]/td[1]"
        find_elements(self.driver,select_movements_list)
        time.sleep(2)

    def tearDown(self):
           self.driver.close()


if __name__ == "__main__":
  test_suite = unittest.TestLoader().loadTestsFromTestCase(dashboard_granos)
  runner = xmlrunner.XMLTestRunner(output='reportGranosDashboardGranos')
  runner.run(test_suite)