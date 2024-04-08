import datetime
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import smtplib
import xmlrunner
import unittest
from CtaContOperSecundaria import contrato_operSecundarias
from CtaCtoDtalCertificados import detalle_cto_certificados
from CtaCtoDtalEntVta import detalle_ctro_entregaVentas
from CtaCtoDtalFijaciones import detalle_ctro_fijaciones
from CtaCtoDtalLiquidaciones import detalle_cto_liquidaciones
from Cuentacontrato import contrato_tenant
from EntregasAplicadas import cta_entregasAplicadas
from EntregasPendApli import entregas_pend_Aplicadas
from GranosContratos import granos_contratos
from Home import HomeTenant
from IndicaInsumosHome import IndicaInsumosHome
from RegistroUsuario import TestRegistroUsuario 
from Entregas import cuenta_entregas
from Ventas import cuenta_ventas
from Onboarding import Onboarding_test_tenant
from ComproContratos import comprobanteContrato
from ComproCtaCte import comprobanteCtacte
from ComproEntregas import comprobanteEntregas
from ComproVentas import comprobanteVentas
from CtaCte_Aplicada import cuenta_ctacte_aplicada
from CtaCte_Histórica import cuenta_ctacte_historica
from insumos_producto import insumosProductos


def ejecutar_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestRegistroUsuario))
    test_suite.addTest(unittest.makeSuite(HomeTenant))
    test_suite.addTest(unittest.makeSuite(IndicaInsumosHome))
    test_suite.addTest(unittest.makeSuite(granos_contratos))
    test_suite.addTest(unittest.makeSuite(insumosProductos))
    test_suite.addTest(unittest.makeSuite(contrato_tenant))
    test_suite.addTest(unittest.makeSuite(detalle_ctro_entregaVentas))
    test_suite.addTest(unittest.makeSuite(detalle_ctro_fijaciones))
    test_suite.addTest(unittest.makeSuite(detalle_cto_certificados))
    test_suite.addTest(unittest.makeSuite(detalle_cto_liquidaciones))
    test_suite.addTest(unittest.makeSuite(contrato_operSecundarias))
    test_suite.addTest(unittest.makeSuite(cuenta_entregas))
    test_suite.addTest(unittest.makeSuite(cta_entregasAplicadas))
    test_suite.addTest(unittest.makeSuite(entregas_pend_Aplicadas))
    test_suite.addTest(unittest.makeSuite(cuenta_ventas))
    test_suite.addTest(unittest.makeSuite(cuenta_ctacte_aplicada))
    test_suite.addTest(unittest.makeSuite(cuenta_ctacte_historica))
    test_suite.addTest(unittest.makeSuite(comprobanteContrato))
    test_suite.addTest(unittest.makeSuite(comprobanteCtacte))
    test_suite.addTest(unittest.makeSuite(comprobanteEntregas))
    test_suite.addTest(unittest.makeSuite(comprobanteVentas))
    test_suite.addTest(unittest.makeSuite(Onboarding_test_tenant))
    
    # Configuración para generar informes XML
    output_folder = 'report_suite'  # Cambia el nombre de la carpeta según tu preferencia
    os.makedirs(output_folder, exist_ok=True)

    runner = xmlrunner.XMLTestRunner(output=output_folder)
    return runner.run(test_suite)

def obtener_archivos_mas_recientes(carpeta_prueba):
    archivos_xml = [f for f in os.listdir(carpeta_prueba) if f.startswith('TEST-') and f.endswith('.xml')]
    
    if not archivos_xml:
        raise FileNotFoundError(f"No se encontraron archivos XML en {carpeta_prueba}")

    rutas_archivos_xml = [os.path.join(carpeta_prueba, archivo) for archivo in archivos_xml]
    rutas_archivos_xml.sort(key=os.path.getmtime, reverse=True)
    print(f"Rutas de archivos XML más recientes: {rutas_archivos_xml}")
    return rutas_archivos_xml

def enviar_informe_por_correo(resultados):
    fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cuerpo_correo = f"Resultados de las pruebas ejecutadas el {fecha_hora}:\n\n{resultados}"
    
    from_email = "luis.tacourt@gmail.com"
    to_email = "luis@silohub.ag"
    subject = "Informe de Pruebas Automatizadas"

    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_user = "luis.tacourt@gmail.com"
    smtp_password = "wrimlphlmonftprz"

    mensaje = MIMEMultipart()
    mensaje.attach(MIMEText(cuerpo_correo, 'plain'))
    mensaje['From'] = from_email
    mensaje['To'] = to_email
    mensaje['Subject'] = subject

    carpeta_prueba = "report_suite"
    try:
        rutas_archivos_xml = obtener_archivos_mas_recientes(carpeta_prueba)
        
        for ruta_archivo_xml in rutas_archivos_xml:
            with open(ruta_archivo_xml, "rb") as archivo_xml:
                adjunto = MIMEApplication(archivo_xml.read(), _subtype="xml")
                adjunto.add_header("Content-Disposition", f"attachment; filename={os.path.basename(ruta_archivo_xml)}")
                mensaje.attach(adjunto)

    except FileNotFoundError as e:
        print(str(e))

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.sendmail(from_email, to_email, mensaje.as_string())

if __name__ == "__main__":
    resultados = ejecutar_suite()
    enviar_informe_por_correo(resultados)