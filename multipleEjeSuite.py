import datetime
import os
import smtplib
import xmlrunner
import unittest
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from selenium import webdriver
from concurrent.futures import ThreadPoolExecutor

from ComproContratos import comprobanteContrato
from ComproCtaCte import comprobanteCtacte
from ComproEntregas import comprobanteEntregas
from ComproVentas import comprobanteVentas
from ConfISolicitudes import confi_Solicitudes
from ConfiClientes import confi_registro_cliente
from ConfiColaborador import confi_colaborador
from ConfigSucursales import config_Sucursales
from CtaContOperSecundaria import contrato_operSecundarias
from CtaCte_Aplicada import cuenta_ctacte_aplicada
from CtaCte_HistoApagar import cuenta_ctacte_histApagar
from CtaCte_HistoAvenver import cuenta_ctacte_histAvencer
from CtaCte_HistoVencido import cuenta_ctacte_histVencido
from CtaCte_Histórica import cuenta_ctacte_historica
from CtaCtoDtalCertificados import detalle_cto_certificados
from CtaCtoDtalEntVta import detalle_ctro_entregaVentas
from CtaCtoDtalFijaciones import detalle_ctro_fijaciones
from CtaCtoDtalLiquidaciones import detalle_cto_liquidaciones
from Ctacte_ApliAcobrar import cta_cte_apliAcobrar
from Ctacte_ApliApagar import cta_cte_apliApagar
from Ctacte_ApliAvencer import cta_cte_apliAvencer
from Ctacte_ApliVencido import cta_cte_apliVencido
from Ctacte_histoAcobrar import cuenta_ctacte_histAcobrar
from Cuentacontrato import contrato_tenant
from Entregas import cuenta_entregas
from EntregasAplicadas import cta_entregasAplicadas
from EntregasPendApli import entregas_pend_Aplicadas
from FijacionTdc import Fijaciones_tc
from Fijaciones import Fijaciones_precio
from FinanzasCobro import finanzas_cobro
from GranosContratos import granos_contratos
from Home import HomeTenant
from IndicaInsumosHome import IndicaInsumosHome
from Insumos_Producto import insumosProductos
from LogistMisSolitud import logistica_MisSolitudes
from LogistPrimaria import logistica_primarias
from LogistSecundarias import logistica_secundarias
from Metricas import Metricas
from Onboarding import Onboarding_test_tenant
from PrecioFijaciones import precio_granos_fijaciones
from Precio_Disponible import precio_granos_desponible
from RegistroUsuario import TestRegistroUsuario
from ReportCompPenFact import reportPendFacturar
from ReportEntreVentas import reportEntregasVentas
from ReportMerFacturada import reportMerFacturada
from ReportMerRemitida import reportMerRemitida
from ReportTenImpo import reportenImpositivas
from ReportUsuario import reportUsuarios
from Ventas import cuenta_ventas
from reportInsuRetirar import ReportinsumosPendRetirar
from suite_test_gd import obtener_archivos_mas_recientes
# Asegúrate de importar los módulos necesarios de tus pruebas

def ejecutar_pruebas(test_class):
    # Inicializa el WebDriver del navegador (aquí se utiliza Chrome, pero puedes cambiarlo según tu preferencia)
    options = webdriver.ChromeOptions()
    # Opciones adicionales del navegador, como el modo incógnito o la desactivación de las notificaciones, pueden agregarse aquí
    driver = webdriver.Chrome(options=options)
    
    # Instancia la clase de prueba y ejecuta las pruebas en el navegador
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    runner = xmlrunner.XMLTestRunner(output='report_suite')
    resultados = runner.run(suite)
    
    # Cierra el navegador después de las pruebas
    driver.quit()
    
    return resultados

def enviar_informe_por_correo(resultados):
    # Define el cuerpo del correo con la fecha y hora actuales y los resultados de las pruebas
    fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cuerpo_correo = f"Resultados de las pruebas ejecutadas el {fecha_hora}:\n\n{resultados}"

    # Configura el correo electrónico
    from_email = "luis.tacourt@gmail.com"
    to_email = "luis@silohub.ag"
    subject = "Informe de Pruebas Automatizadas"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_user = "luis.tacourt@gmail.com"
    smtp_password = "tu_contrasena"

    mensaje = MIMEMultipart()
    mensaje.attach(MIMEText(cuerpo_correo, 'plain'))
    mensaje['From'] = from_email
    mensaje['To'] = to_email
    mensaje['Subject'] = subject

    carpeta_prueba = "report_suite"
    try:
        # Adjunta los archivos XML de los informes de prueba al correo
        rutas_archivos_xml = obtener_archivos_mas_recientes(carpeta_prueba)
        
        for ruta_archivo_xml in rutas_archivos_xml:
            with open(ruta_archivo_xml, "rb") as archivo_xml:
                adjunto = MIMEApplication(archivo_xml.read(), _subtype="xml")
                adjunto.add_header("Content-Disposition", f"attachment; filename={os.path.basename(ruta_archivo_xml)}")
                mensaje.attach(adjunto)

    except FileNotFoundError as e:
        print(str(e))

    # Envía el correo electrónico
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.sendmail(from_email, to_email, mensaje.as_string())

def ejecutar_suite():
    # Define las clases de prueba que deseas ejecutar
    test_classes = [TestRegistroUsuario, HomeTenant, IndicaInsumosHome, granos_contratos, Fijaciones_precio,
                     Fijaciones_tc, precio_granos_desponible, precio_granos_fijaciones, insumosProductos, contrato_tenant, 
                     detalle_ctro_entregaVentas, detalle_ctro_fijaciones, detalle_cto_certificados, detalle_cto_liquidaciones, 
                     contrato_operSecundarias, cuenta_entregas, cta_entregasAplicadas, entregas_pend_Aplicadas, cuenta_ventas, 
                     cuenta_ctacte_aplicada, cta_cte_apliAcobrar, cta_cte_apliApagar, cta_cte_apliAvencer, cta_cte_apliVencido, 
                     cuenta_ctacte_historica, cuenta_ctacte_histAcobrar, cuenta_ctacte_histApagar, cuenta_ctacte_histAvencer, 
                     cuenta_ctacte_histVencido, comprobanteContrato, comprobanteCtacte, comprobanteEntregas, comprobanteVentas, 
                     reportUsuarios, reportPendFacturar, reportEntregasVentas, ReportinsumosPendRetirar, reportMerFacturada, 
                     reportMerRemitida, reportenImpositivas, logistica_primarias, logistica_secundarias, logistica_MisSolitudes, 
                     finanzas_cobro, Metricas, confi_registro_cliente, confi_colaborador, config_Sucursales, confi_Solicitudes, Onboarding_test_tenant]

    # Ejecuta las pruebas concurrentemente
    with ThreadPoolExecutor() as executor:
        resultados = list(executor.map(ejecutar_pruebas, test_classes))

    # Envía el informe por correo electrónico
    enviar_informe_por_correo(resultados)

if __name__ == "__main__":
    ejecutar_suite()