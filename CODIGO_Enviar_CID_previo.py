# -*- coding: utf-8 -*-
"""
Enviar codigos CID a todos los alumnos de la lista

Autor: Alejandro E. Martinez Castro amcastro@ugr.es
       Departamento de Mecánica de Estructuras e Ingeniería Hidráulica. 
       Universidad de Granada
Fecha: 27-julio-2017


Licencia Creative Commons Reconocimiento-NoComercial 4.0 Internacional.


"""

#==============================================================================
# Código para enviar a cada estudiante su CID. (Código de IDentificación)
# Dentro del sistema de exámenes semiautomático, este código es el primero a usar
# Permite depurar la lista de estudiantes. 
#
# Reglas aconsejables: 
# 1) Este fichero debe correr dentro de un directorio que contenga un fichero csv
#    en formato UTF-8 (para no tener problemas de acentos, o eñes). 
# 2) Asignar código CID fácil de recordar para el estudiante. En mi experiencia: 
#    -> Usar el propio DNI de 8 dígitos. Si algún estudiante tiene 7 dígitos, 
#       completar con un 9 por "delante". No con un "0", pues da problemas a veces en AMC. 
# 3) Si es estudiante con NIE, eliminar los caracteres previos que no sean números, 
#    y reemplazarlos con uno o varios 9. 
#
# El fichero .csv (Ejemplo en este caso, lista_de_alumnos.csv), debe contener
# una estructura similar al siguiente ejemplo. 
# 
# id,surname, name,email
# 12345678, MARTÍNEZ CASTRO, ALEJANDRO, amcastro@ugr.es
# 87654321, ESTUDIANTE SIGUIENTE, NOMBRE, amcastro@ugr.es
#
# Posibles problemas: 
# -> Plantear únicamente direcciones DENTRO de la propia universidad. No incluir emails de Google, 
#    pues muchos de ellos tienen bloqueada la posibilidad de que un gestor automático envíe los emails. 
#    Yo utilizo correo institucional, estrictamente. 
# -> Problemas con caracteres. Utilizar codificación UTF-8 estrictamente. 



# Funcionamiento. Buscar la palabra "EDITAR" para ver qué lineas deben editarse estrictamente para cada profesor 

#==============================================================================
# Mensajes en html y texto plano a mostrar
#==============================================================================

def mensaje_html(apellidos,nombre,codigoID): 

# EDITAR. Escribir el mensaje en código html
    mensaje = """<p><span style="font-size: small;">Estimado alumno/a de An&aacute;lisis de Estructuras (GIC):</span></p>
    <p><span style="font-size: small;">Le escribo este mensaje para enviarle i<strong>nformaci&oacute;n muy importante para el examen del 13 de septiembre. :</strong><br /></span></p>
    <p><span style="font-size: small;"><strong>Imprima este mensaje y tr&aacute;igalo impreso el d&iacute;a del examen. </strong></span></p>
    <p><span style="font-size: small;"><br /></span></p>
    <p><span style="font-size: small;">Durante el ejercicio se le pedir&aacute; codificar un c&oacute;digo, que coincide en general con su DNI (8 d&iacute;gitos, sin la letra)<br /></span></p>
    <p><span style="font-size: small;">En caso de no tener DNI, se le ha asignado un c&oacute;digo de 8 d&iacute;gitos. </span></p>
    <ul>
    <li><span style="font-size: small;">APELLIDOS: """ + apellidos.strip() + """ </span></li>
    </ul>
    <ul>
    <li><span style="font-size: small;">NOMBRE: """ + nombre.strip() + """</span></li>
    </ul>
    <ul>
    <li><span style="font-size: small;">C&Oacute;DIGO:""" + codigoID.strip() + """</span></li>
    </ul>
    <p><span style="font-size: small;">Verifique que sus apellidos y nombre son correctos.&nbsp;</span></p>
    <p><span style="font-size: small;">En caso de que observe alguna anomal&iacute;a, contacte conmigo por email a la mayor brevedad.&nbsp;</span></p>
    <p><span style="font-size: small;">Gracias, </span></p>
    <p>&nbsp;</p>
    <p><span style="font-size: small;">Alejandro E. Mart&iacute;nez Castro</span></p>
    <div id="_rc_sig">&nbsp;</div> """
# FIN EDITAR

    return mensaje

def mensaje_texto(apellidos,nombre,codigoID):

#Editar para escribir el modo texto.

    mensaje = """Estimado alumno/a de Análisis de Estructuras (GIC): 

    Le escribo este mensaje para enviarle información muy importante para el examen del 13 de septiembre. 

    Imprima  este mensaje y tráigalo impreso el día del examen.

    Durante el ejercicio se le pedirá codificar un código, que coincide en general con su DNI (8 dígitos, sin la letra)

    En caso de no tener DNI, se le ha asignado un código de 8 dígitos.

    APELLIDOS: """ + apellidos.strip() + """ 

    NOMBRE: """ + nombre.strip() + """

    CÓDIGO:""" + codigoID.strip() + """

    Verifique que sus apellidos y nombre son correctos.

    En caso de que observe alguna anomalía, contacte conmigo por email a la mayor brevedad.

    Gracias,


    Alejandro E. Martínez Castro"""

# FIN EDITAR

    return mensaje



#==============================================================================
# Paso 2:  Libreria para enviar mensajes.
#==============================================================================

# Cambiar los campos necesarios. Por motivos de seguridad, el password se introduce por teclado

from Modulo_email import *

# EDITAR: Personalizar para cada servidor de correo y usuario. 

pm_servidor_correo = 'smtp.ugr.es:587'
pm_login_usuario = 'amcastro'

# FIN EDITAR


# Entrada de contraseña oculta-----------------

import getpass
# EDITAR
print "Introduzca contraseña de email para usuario UGR " + pm_login_usuario 
print "Por seguridad, al teclear permanecerá oculta sin dar pistas" 
pm_login_password = getpass.getpass()

# FIN EDITAR 

#-----------------------------------------------

# EDITAR
pm_emisor_nombre = 'Alejandro Martinez Castro'
pm_emisor_correo = 'amcastro@ugr.es'

pm_asunto = 'NUMERO DE IDENTIFICACION ID EN EXAMEN'
#pm_archivo_texto = 'mensaje_texto.txt'
#pm_archivo_html = 'mensaje_texto.html'
pm_acuse_recibo = True
pm_imagenes_embebidas = []
# FIN EDITAR 


#==============================================================================
# Lectura del fichero .csv
#==============================================================================
import csv

#EDITAR modificar 
reader = csv.reader(open('lista_de_alumnos.csv', 'rb'))
# FIN EDITAR
for index,row in enumerate(reader):
    if index > 0:
        print 'Persona: ' + str(index)
        print '------------'
        print 'ID: ' + row[0].strip() + ', Apellidos y Nombre ' + row[1].strip() + ' ' + row[2].strip() + ', email: ' + row[3].strip() 
        
        nombre = row[1] + ' ' + row[2]
        print "El nombre y apellidos es ", nombre        
        
                
        pm_receptor_nombre = nombre
        pm_receptor_correo = row[3]
        pm_archivo_html = mensaje_html(row[1].strip(),row[2].strip(),row[0].strip())
        pm_archivo_texto = mensaje_texto(row[1].strip(),row[2].strip(),row[0].strip())
        pm_adjuntos = []
            
        print "Enviando email a: ", nombre
        print "Direccion email: ", row[3]
                
        mandar_mail( pm_servidor_correo, pm_login_usuario, 
                         pm_login_password,pm_emisor_nombre, 
                         pm_emisor_correo, pm_receptor_nombre,
                         pm_receptor_correo, pm_asunto, pm_archivo_texto,
                         pm_archivo_html, pm_adjuntos, pm_acuse_recibo,  
                         pm_imagenes_embebidas)
        print " "        



