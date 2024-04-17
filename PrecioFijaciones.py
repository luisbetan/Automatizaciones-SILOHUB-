
import unittest
import xmlrunner
import time
from Elements import  click_icon_delete,displace_element,find_and_click_element, find_elements,find_send_element, hop_element,search_and_displace_account, select_option_click, validate_text
from LoginSample import LoginSample
from startSession import StartSession




class precio_granos_fijaciones(unittest.TestCase):
    
    def setUp(self):
       
       
        self.start_session = StartSession()
        self.driver = self.start_session.driver
        # Inicializar la clase LoginHelper
        self.login_sample = LoginSample(self.driver)
   
   
    def test_price_fixings(self):
        # Utilizar métodos de LoginHelper para el inicio de sesión
        self.login_sample.login("admingd@silohub.ag", "G@viglio123")
        self.login_sample.select_tenant()

        select_grain = "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[2]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[3]/a/span"
        find_elements(self.driver,select_grain)
        time.sleep(2)

        select_price_grain = "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[2]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[3]/div/ul/li[3]/a"
        find_elements(self.driver,select_price_grain)
        time.sleep(2)

        # validar titulo de la pantalla
        
        title_pag_market = "/html/body/app-root/app-layout/app-vertical/div/div/div/app-header-for-screen/div/div/span"
        value_expected = "MERCADOS"
        validate_text(self.driver, title_pag_market, value_expected)

        self.driver.execute_script("window.scrollTo(0,600);")
        time.sleep(4)

        # borrar listado de disponible

        delete_price_grain = "#layout-wrapper > div > div > div > app-market-main > app-grain-price > div:nth-child(2) > app-grain-price-table:nth-child(3) > div > div > table > tbody > tr:nth-child(1) > td.pt-3.padding-last-column > svg-icon > svg"
        click_icon_delete(self.driver, delete_price_grain)
        time.sleep(2)

        
        # agrgar productos 

        available = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-market-main/app-grain-price/div[2]/app-grain-price-table[3]/div/app-grain-price-table-header/div/div[2]/app-add-and-clean/div/div[1]/app-button/button"
        find_elements(self.driver,available)

        

        switch_button = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-market-main/app-grain-price/div[2]/app-grain-price-table[3]/div/div/table/tbody/tr[1]/td[1]/app-switch/div/input"
        find_elements(self.driver,switch_button)
        time.sleep(2)

        select_option_grain = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-market-main/app-grain-price/div[2]/app-grain-price-table[3]/div/div/table/tbody/tr[1]/td[2]/app-select/select"
        option_grain = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-market-main/app-grain-price/div[2]/app-grain-price-table[3]/div/div/table/tbody/tr/td[2]/app-select/select/option[14]"
        select_option_click(self.driver, select_option_grain, option_grain )
        time.sleep(2)

        select_campaign = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-market-main/app-grain-price/div[2]/app-grain-price-table[3]/div/div/table/tbody/tr[1]/td[3]/app-select/select"
        option_campaign = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-market-main/app-grain-price/div[2]/app-grain-price-table[3]/div/div/table/tbody/tr[1]/td[3]/app-select/select/option[2]"
        select_option_click(self.driver, select_campaign, option_campaign )
        time.sleep(2)

        select_destination = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-market-main/app-grain-price/div[2]/app-grain-price-table[3]/div/div/table/tbody/tr[1]/td[4]/app-select/select"
        option_destination = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-market-main/app-grain-price/div[2]/app-grain-price-table[3]/div/div/table/tbody/tr[1]/td[4]/app-select/select/option[3]"
        select_option_click(self.driver, select_destination, option_destination )
        time.sleep(2)

        select_money = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-market-main/app-grain-price/div[2]/app-grain-price-table[3]/div/div/table/tbody/tr/td[5]/app-select/select"
        option_money = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-market-main/app-grain-price/div[2]/app-grain-price-table[3]/div/div/table/tbody/tr/td[5]/app-select/select/option[1]"
        select_option_click(self.driver, select_money, option_money )
        time.sleep(2)

        insert_price = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-market-main/app-grain-price/div[2]/app-grain-price-table[3]/div/div/table/tbody/tr[1]/td[6]/input"
        send_price = "3000"
        find_send_element(self.driver, insert_price, send_price )

       # aplicar rango de fecha 01/10/2024 al 31/10/2024
        select_date = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-market-main/app-grain-price/div[2]/app-grain-price-table[3]/div/div/table/tbody/tr[1]/td[7]/app-date-picker/div/input[2]"
        displace_element(self.driver, select_date)

        select_arrow = "/html/body/div[3]/div[1]/span[2]"
        clicks = 6
        find_and_click_element(self.driver, select_arrow, clicks)

        insert_date1 = "/html/body/div[3]/div[2]/div/div[2]/div/span[2]"
        find_elements(self.driver, insert_date1)
        time.sleep(2)

        insert_date2 = "/html/body/div[3]/div[2]/div/div[2]/div/span[32]"
        find_elements(self.driver, insert_date2)
        time.sleep(2)

        insert_amount1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-market-main/app-grain-price/div[2]/app-grain-price-table[3]/div/div/table/tbody/tr[1]/td[8]/input"
        send_amount1 = "8000"
        find_send_element(self.driver, insert_amount1, send_amount1 )



        select_idea = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-market-main/app-grain-price/div[2]/app-grain-price-table[3]/div/div/table/tbody/tr[1]/td[10]/input"
        find_elements(self.driver, select_idea)
        time.sleep(2)

        self.driver.execute_script("window.scrollTo(600,0);")
        time.sleep(2)


        select_post = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-market-main/app-grain-price/div[1]/app-grain-price-header/app-grain-price-header-release/div/div[2]/div/div[2]/app-button/button"
        find_elements(self.driver, select_post)
        time.sleep(2)

        select_accept_post = "/html/body/div[4]/div/div[6]/button[3]"
        find_elements(self.driver, select_accept_post)
        time.sleep(2)

        select_button_accept = "/html/body/div[2]/div/div[6]/button[1]"
        find_elements(self.driver, select_button_accept)
        time.sleep(2)

        select_menu = "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[2]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[2]/a/span"
        find_elements(self.driver, select_menu)
        time.sleep(2)

        select_market_home = "/html/body/app-root/app-layout/app-vertical/div/div/div/app-header-for-screen/div/div/span"
        find_elements(self.driver, select_market_home)
        time.sleep(5)

        self.driver.execute_script("window.scrollTo(0,600);")
        time.sleep(2)


        select_icon_hand ='(//*[@id="Grupo_10473"])[2]'
        find_elements(self.driver, select_icon_hand)
        time.sleep(2)

        located_element = "/html/body/ngb-modal-window/div/div/app-sales-intent-modal/div[2]/app-sales-intent-form/div/div[1]/div/div[2]/div/app-customer-searcher/ng-select/div/div/div[2]/input"
        select_input = "/html/body/ngb-modal-window/div/div/app-sales-intent-modal/div[2]/app-sales-intent-form/div/div[1]/div/div[2]/div/app-customer-searcher/ng-select/ng-dropdown-panel/div/div[2]/div[1]/span"
        account_number = "1023"
        search_and_displace_account(self.driver, account_number, select_input, located_element )
        time.sleep(2)

        select_account = "/html/body/ngb-modal-window/div/div/app-sales-intent-modal/div[2]/app-sales-intent-form/div/div[1]/div/div[2]/div/app-customer-searcher/ng-select/ng-dropdown-panel/div/div[2]/div[1]/span"
        find_elements(self.driver, select_account)
        time.sleep(2)

        select_number_contract = "/html/body/ngb-modal-window/div/div/app-sales-intent-modal/div[2]/app-sales-intent-form/div/div[2]/div/div[2]/div/app-contract-searcher/ng-select/div/div/div[2]/input"
        option_number_contract = "/html/body/ngb-modal-window/div/div/app-sales-intent-modal/div[2]/app-sales-intent-form/div/div[2]/div/div[2]/div/app-contract-searcher/ng-select/ng-dropdown-panel/div/div[2]/div[2]/span"
        select_option_click(self.driver, select_number_contract, option_number_contract )
        time.sleep(2)


        insert_amount2 = "/html/body/ngb-modal-window/div/div/app-sales-intent-modal/div[2]/app-sales-intent-form/div/div[3]/div/div[2]/div/div/input"
        send_amount = "30"
        find_send_element(self.driver, insert_amount2, send_amount )

        select_button_request = "/html/body/ngb-modal-window/div/div/app-sales-intent-modal/div[2]/app-sales-intent-form/div/div[6]/app-button[2]/button"
        find_elements(self.driver, select_button_request)
        time.sleep(2)



        


    
    
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
  test_suite = unittest.TestLoader().loadTestsFromTestCase(precio_granos_fijaciones)
  runner = xmlrunner.XMLTestRunner(output='reportGranospreciofijaciones')
  runner.run(test_suite)
