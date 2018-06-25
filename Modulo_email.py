# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 10:18:25 2016

@author: Alejandro E. Martínez Castro
         amcastro@ugr.es
"""

#----------------------
import os
import smtplib
import string
import email

from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
from email.Utils import formatdate
from email import Encoders

#_________________
def mandar_mail(
    pm_servidor_correo,
    pm_login_usuario,
    pm_login_password,
    pm_emisor_nombre,
    pm_emisor_correo,
    pm_receptor_nombre,
    pm_receptor_correo,
    pm_asunto,
    pm_archivo_texto,
    pm_archivo_html,
    pm_adjuntos = [],
    pm_acuse_recibo = False,
    pm_imagenes_embebidas = []):
    """
    Rutina para enviar correo electrónico, permitiendo enviar el
    mensaje alternativa/conjuntamente en modo texto y html, así como
    con archivos adjuntos, imágenes embebidas y pudiendo solicitar
    confirmación de lectura.
    """
    assert type(pm_adjuntos) == list
    assert type(pm_imagenes_embebidas) == list

    #Inicializamos el mensaje a enviar y vamos añadiendo partes
    msgRaiz = MIMEMultipart('related')
    msgRaiz['From'] = pm_emisor_nombre + ' <' + pm_emisor_correo +'>'
    msgRaiz['To'] = pm_receptor_correo
    msgRaiz['Subject'] = pm_asunto
    msgRaiz['Date'] = formatdate(localtime = True)
    msgRaiz.preamble = '' #De momento, no lo uso
    msgRaiz.epilogue = '' #De momento, no lo uso

    if pm_acuse_recibo:
        msgRaiz['Disposition-Notification-To'] = pm_emisor_correo

    #Se encapsulan las versiones de texto plano y html del cuerpo
    #del mensaje en una parte 'alternative' para que el cliente de
    #correo decida qué parte mostrar
    msgAlternativo = MIMEMultipart('alternative')
    msgRaiz.attach(msgAlternativo)

    #Abrimos mensaje de texto alternativo y lo añadimos
 #   fp = open(pm_archivo_texto, 'rb')
    msgTexto = MIMEText(pm_archivo_texto, 'plain')
 #   msgTexto = MIMEText(fp.read(), 'plain') 
    msgAlternativo.attach(msgTexto)
 #   fp.close() 

    #Abrimos mensaje html alternativo y lo añadimos
 #   fp = open(pm_archivo_html, 'rb')
    msgHtml = MIMEText(pm_archivo_html, 'html')
 #   msgHtml = MIMEText(fp.read(), 'html')
    msgAlternativo.attach(msgHtml)
 #   fp.close()

    #Añadimos las imágenes embebidas, si las hay
    for imagen in pm_imagenes_embebidas:
        #Cargar imagen
        archivo_imagen = open(imagen, 'rb')
        msgImage = MIMEImage(archivo_imagen.read())
        archivo_imagen.close()

        #Hemos de adjuntar la imagen en el content-id.
        #En el archivo html se debe hacer referencia al content-id
        #como fuente en el source de la imagen, por ejemplo:
        #<img src="cid:/nombre/de_la_ruta_entera/imagen.jpg">
        msgImage.add_header('Content-ID', '<' + imagen + '>')
        msgRaiz.attach(msgImage)

    #Añadimos los ficheros adjuntos a mandar , si los hay
    for file in pm_adjuntos:
        adjunto = MIMEBase('application', "octet-stream")
        adjunto.set_payload(open(file, "rb").read())
        Encoders.encode_base64(adjunto)
        adjunto.add_header('Content-Disposition', 'attachment; filename = "%s"' %  os.path.basename(file))
        msgRaiz.attach(adjunto)

    #Conectamos con el servidor de correo y mandamos el mensaje
    servidor = smtplib.SMTP(pm_servidor_correo)
    #servidor.set_debuglevel(1)
    servidor.starttls()
    servidor.ehlo()
    servidor.login(pm_login_usuario, pm_login_password)
    try:
        servidor.sendmail(pm_emisor_correo, pm_receptor_correo, msgRaiz.as_string())
        servidor.quit()
        resultado =  True
    except:
        resultado = False

    return(resultado)

