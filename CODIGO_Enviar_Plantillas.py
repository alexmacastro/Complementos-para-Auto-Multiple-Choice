# -*- coding: utf-8 -*-
"""
Enviar plantillas (hojas que deben imprimir y rellenar)

Se asume que los pdf los ha generado Auto-Multiple-Choice

Cada estudiante de la lista tiene asignado un fichero. El orden de la lista define el número de fichero


Autor: Alejandro E. Martinez Castro amcastro@ugr.es
       Departamento de Mecánica de Estructuras e Ingeniería Hidráulica. 
       Universidad de Granada
Fecha: 26 de abril de 2020


"""

#==============================================================================
# Mensajes en html y texto plano a mostrar
#==============================================================================

def mensaje_html(apellidos,nombre,codigoID): 

    mensaje = """<p><span style="font-size: small;">Estimado alumno de AE1920:</span></p>
    <p><span style="font-size: small;">Le escribo este mensaje para enviarle la plantilla que debe usar para escribir en el examen. </span></p>
    <p><span style="font-size: small;">Debe IMPRIMIRLA y CONSERVARLA hasta el día del examen. Es &uacute;nica y personal para usted. </span></p>
    <p><span style="font-size: small;">Sus datos personales son los siguientes: </span></p>
    <ul>
    <li><span style="font-size: small;">APELLIDOS: """ + apellidos + """ </span></li>
    </ul>
    <ul>
    <li><span style="font-size: small;">NOMBRE: """ + nombre + """</span></li>
    </ul>
    <ul>
    <li><span style="font-size: small;">C&Oacute;DIGO:""" + codigoID + """</span></li>
    </ul>
    <p><span style="font-size: small;">Atentamente, </span></p>
    <p>&nbsp;</p>
    <p><span style="font-size: small;">Alejandro E. Mart&iacute;nez Castro</span></p>
    <div id="_rc_sig">&nbsp;</div> """

    return mensaje

def mensaje_texto(apellidos,nombre,codigoID):

    mensaje = """Estimado alumno/a de AE1920:

    Le escribo este mensaje para enviarle la plantilla que debe usar para escribir en el examen.

    Debe IMPRIMIRLA y CONSERVARLA hasta el día del examen. Es única y personal para usted.
    
    Sus datos personales son los siguientes: 

    APELLIDOS: """ + apellidos + """ 

    NOMBRE: """ + nombre + """

    CÓDIGO:""" + codigoID + """

    Verifique que el ejercicio que se le ha enviado es el suyo. 

    Revise la corrección. 

    Atentamente,


    Alejandro E. Martínez Castro"""

    return mensaje




#==============================================================================
# Paso 1:  Lista de todos los ficheros .pdf a distribuir entre alumnos
#==============================================================================

# Este script debe estar en el mismo directorio donde estén todos los pdf. En caso contrario, corregir ruta de directorio
# Los ficheros .pdf han sido generados por Auto-Multiple-Choice. Puden contener correcciones posteriores editando pdf. 



#==============================================================================
# Paso 2:  Libreria para enviar mensajes.
#==============================================================================

# Cambiar los campos necesarios. Por motivos de seguridad, el password se introduce por teclado

from Modulo_email import *

pm_servidor_correo = 'smtp.ugr.es:587'
pm_login_usuario = 'amcastro'

# Entrada de contraseña oculta-----------------

import getpass

print "Introduzca contraseña de email para usuario UGR " + pm_login_usuario 
print "Por seguridad, al teclear permanecerá oculta sin dar pistas" 
pm_login_password = getpass.getpass()
#-----------------------------------------------


pm_emisor_nombre = 'Alejandro Martinez Castro'
pm_emisor_correo = 'amcastro@ugr.es'

pm_asunto = 'PLANTILLA DE RESPUESTAS PARA EL EXAMEN'
#pm_archivo_texto = 'mensaje_texto.txt'
#pm_archivo_html = 'mensaje_texto.html'
pm_acuse_recibo = False
pm_imagenes_embebidas = []


#==============================================================================
# Lectura del fichero .csv
#==============================================================================
import csv
import os

directorio = os.getcwd()
 
reader = csv.reader(open('alumnos_ficticios2.csv', 'rb'))
for index,row in enumerate(reader):
    if index > 0:
        print 'Persona: ' + str(index)
        print '------------'
        print 'ID: ' + row[0].strip() + ', Apellidos y Nombre ' + row[1].strip() + ' ' + row[2].strip() + ', email: ' + row[3].strip() 

        
        nombre = row[1].strip() + " " +  row[2].strip() # Elimina espacios en blanco antes y despues
        print "El nombre y apellidos es", nombre  
        
        
        numfile = str(index)
        fichero = 'sheet-'+ numfile.zfill(4) + '-1A.pdf'
        ficheronuevo = nombre + ' ' + fichero
        
        try:
            os.rename(fichero,ficheronuevo)
        except:
            print "Fichero ya renombrado. Continuando"
        
        print "Fichero que se ha enviado a este alumno"
        print ficheronuevo
                
        pm_receptor_nombre = nombre
        pm_receptor_correo = row[3]
        pm_adjuntos = [ficheronuevo]
        print "Enviando email a: ", nombre
        print "Direccion email: ", row[3]
        print "Fichero: ", ficheronuevo
                
        pm_archivo_html = mensaje_html(row[1],row[2],row[0])
        pm_archivo_texto = mensaje_texto(row[1],row[2],row[0]) 
                
        mandar_mail( pm_servidor_correo, pm_login_usuario, 
                            pm_login_password,pm_emisor_nombre, 
                            pm_emisor_correo, pm_receptor_nombre,
                            pm_receptor_correo, pm_asunto, pm_archivo_texto,
                            pm_archivo_html, pm_adjuntos, pm_acuse_recibo,  
                            pm_imagenes_embebidas)
        print " "        



