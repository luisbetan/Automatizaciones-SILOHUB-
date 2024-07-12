import time
import unittest
from selenium.webdriver.common.by import By
import xmlrunner
from Elements import calendar_todate_retro, find_elements, validate_character_numeric_element, validate_character_numeric_element_selector, validate_strt_selector, validate_text
from loginhelper import LoginHelper
from startSession import StartSession

class reportMerFacturada(unittest.TestCase):
    def setUp(self):
        self.start_session = StartSession()
        self.driver = self.start_session.driver

        # Inicializar la clase LoginHelper
        self.login_helper = LoginHelper(self.driver)

    def test_Report_MerFacturada(self):
        # Utilizar métodos de LoginHelper para el inicio de sesión
        self.login_helper.login("admingd@silohub.ag", "G@viglio123")
        self.login_helper.select_tenant()
        self.login_helper.search_and_select_account("1023")


        # ingresar al menú de cuentas 

        select_menu_Account = "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[3]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[5]/a/span"
        find_elements(self.driver,select_menu_Account)


        # ingresar al submenú de reportes 

        select_menu_reports ="/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[3]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[5]/div/ul/li[6]/a"
        find_elements(self.driver,select_menu_reports)

        # seleccionar el filtro 

        select_filter_reports = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-reports/div/app-header-for-responsive-table/div/div/div[2]/div/div/app-filter-button/button/div/span"
        find_elements(self.driver,select_filter_reports)
        time.sleep(2)

        select_invoiced_merchandise = "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-radio-button-list/div/app-radio[4]/div/input"
        find_elements(self.driver,select_invoiced_merchandise)
        time.sleep(2)

        # aplicar rando de fecha 01/09/2021 al 30/09/2021

        # aplicar filtro de fecha actual a seis meses para atras 

        select_calendar = "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-reports-options/app-date-filter/div/app-date-picker/div/input[2]"
        popup_xpath = "//div[contains(@class, 'flatpickr-calendar')]"
        select_chevron = "//span[@class='flatpickr-prev-month']"
        popup_xpath2 = "//div[contains(@class, 'flatpickr-calendar')]"
        click_chevron = 6
        calendar_todate_retro(self.driver, select_calendar, popup_xpath, select_chevron, popup_xpath2, clicks=click_chevron)
        time.sleep(2)

        apply_button_filter = "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-filter-buttons/div/app-button[2]/button"
        find_elements(self.driver, apply_button_filter)
        time.sleep(3)

        # validar totalizadores

        total_outputs = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-remitted-merchandise/app-header-for-responsive-table/div/div/div[1]/div/div[1]/app-totalizer/div/div/div[2]/div[2]/span[1]"
        validate_character_numeric_element(self.driver,total_outputs)

        total_money = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-remitted-merchandise/app-header-for-responsive-table/div/div/div[1]/div/div[2]/app-totalizer/div/div/div[2]/div[2]/span[1]"
        validate_character_numeric_element(self.driver,total_money)


        # validar título de la pantalla 

        title_page_receipts = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-remitted-merchandise/app-responsive-table/div/div[1]/span"
        title_page_receipts_expected = "Mercadería Facturada"
        validate_text(self.driver,title_page_receipts,title_page_receipts_expected )
      
        # validar ep primer movimiento 

        first_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-remitted-merchandise/app-responsive-table/div/div[2]/table/thead/tr/th[2]"
        first_column_expected = "Fecha"
        validate_text(self.driver,first_column,first_column_expected )

        date_movements = "#layout-wrapper > div > div > div > app-remitted-merchandise > app-responsive-table > div > div.table-responsive > table > tbody > tr:nth-child(1) > td.text-nowrap.align-middle.f-size-12.fw-bold.ellipsis-cell > span > div > span"
        validate_strt_selector(self.driver, "", date_movements)
        
        second_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-remitted-merchandise/app-responsive-table/div/div[2]/table/thead/tr/th[3]"
        second_column_expected = "Comprobante"
        validate_text(self.driver,second_column,second_column_expected )

        voucher_movements = "#layout-wrapper > div > div > div > app-remitted-merchandise > app-responsive-table > div > div.table-responsive > table > tbody > tr:nth-child(1) > td:nth-child(3) > span > div > span"
        validate_strt_selector(self.driver,"",voucher_movements )
      

        third_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-remitted-merchandise/app-responsive-table/div/div[2]/table/thead/tr/th[4]"
        third_column_column_expected = "Artículo"
        validate_text(self.driver,third_column,third_column_column_expected )

        article_description2 = "#layout-wrapper > div > div > div > app-remitted-merchandise > app-responsive-table > div > div.table-responsive > table > tbody > tr:nth-child(1) > td:nth-child(4) > span > div > span"
        validate_strt_selector(self.driver,"" ,article_description2 )
      


        quarter_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-remitted-merchandise/app-responsive-table/div/div[2]/table/thead/tr/th[5]"
        quarter_column_expected = "Cantidad"
        validate_text(self.driver,quarter_column,quarter_column_expected )

        departures = "#layout-wrapper > div > div > div > app-remitted-merchandise > app-responsive-table > div > div.table-responsive > table > tbody > tr:nth-child(1) > td:nth-child(5) > span > div > span"
        validate_character_numeric_element_selector(self.driver,departures)

        fifth_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-remitted-merchandise/app-responsive-table/div/div[2]/table/thead/tr/th[6]"
        fifth_column_expected = "Moneda"
        validate_text(self.driver,fifth_column,fifth_column_expected )

        type_money = "#layout-wrapper > div > div > div > app-remitted-merchandise > app-responsive-table > div > div.table-responsive > table > tbody > tr:nth-child(1) > td:nth-child(6) > span > div > span"
        validate_strt_selector(self.driver,"",type_money )

        sixth_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-remitted-merchandise/app-responsive-table/div/div[2]/table/thead/tr/th[7]"
        sixth_column_expected = "Precio"
        validate_text(self.driver,sixth_column,sixth_column_expected )

        price = "#layout-wrapper > div > div > div > app-remitted-merchandise > app-responsive-table > div > div.table-responsive > table > tbody > tr:nth-child(1) > td:nth-child(7) > span > div > span"
        validate_character_numeric_element_selector(self.driver,price)

           
       # descargar compromabtes 

        selecct_moviments_list1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-remitted-merchandise/app-responsive-table/div/div[2]/table/tbody/tr[1]/th/input"
        find_elements(self.driver, selecct_moviments_list1)

        selecct_moviments_list2 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-remitted-merchandise/app-responsive-table/div/div[2]/table/tbody/tr[2]/th/input"
        find_elements(self.driver, selecct_moviments_list2)

        selecct_moviments_list3 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-remitted-merchandise/app-responsive-table/div/div[2]/table/tbody/tr[3]/th/input"
        find_elements(self.driver, selecct_moviments_list3)

        dowlnload_button1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-remitted-merchandise/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/button[2]"
        find_elements(self.driver, dowlnload_button1)

        selecct_option1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-remitted-merchandise/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/ul/li[1]/a"
        find_elements(self.driver, selecct_option1)
        time.sleep(2)

        dowlnload_button2 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-remitted-merchandise/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/button[2]"
        find_elements(self.driver, dowlnload_button2)

        selecct_option2 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-remitted-merchandise/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/ul/li[2]/a"
        find_elements(self.driver, selecct_option2)
        time.sleep(2)

       

        




    def tearDown(self):
        self.driver.close()





if __name__ == "__main__":
  test_suite = unittest.TestLoader().loadTestsFromTestCase(reportMerFacturada)
  runner = xmlrunner.XMLTestRunner(output='reportMerFacturada')
  runner.run(test_suite)
