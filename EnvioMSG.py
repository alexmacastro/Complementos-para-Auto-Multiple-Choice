#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

# La primera línea es para ejecutar el script sin tener que poner delante python2.7
# Para ello también hay que hacer chmod +x EnvioMSG.py, para hacer el fichero ejecutable

# Enviar mensaje con adjunto personalizado (examen, ejercicio, etc) a lista de alumnos contenida en fichero CSV
# Los ficheros adjuntos a enviar a cada alumno deben contener en su nombre el CID del alumno.

# Autor: Rafael Gallego Sevilla
#   Departamento de Mecánica de Estructuras e Ingeniería Hidráulica. 
#   Universidad de Granada
#   Fecha: diciembre 2018

# Generado a partir de los scripts creados por Alejandro E. Martinez Castro [AMC] (amcastro@ugr.es)
#   Departamento de Mecánica de Estructuras e Ingeniería Hidráulica. 
#   Universidad de Granada
#   Fecha: 29-julio-2016
# Usa el modulo ModuloEmail.py creado por AMC.

# Para ver uso y opciones ejecute
#
#   dirscript/EnvioMSG.py -h
#
# siendo 'dirscript' el directorio donde está el fichero EnvioMsg.py. Lógicamente puede ponerse 'dirscript'
# en el PATH, en cuyo caso puede eliminarse 'dirscript/' y ejecutar simplemente
#
#   EnvioMSG.py -h
#
# Sale esto:
#
#   usage: EnvioMSG.py [-h] [-v] [-d [DIRPDF]] [-p PATRON] [-a ASUNTO] [-e EXAMEN]
#                      [--asignatura ASIGNATURA] [--acuse] [--emailrte EMAILRTE]
#                      [--remitente REMITENTE] [--servidor SERVIDOR]
#                      fichCSV fichMSG
#   
#   positional arguments:
#     fichCSV               Fichero CSV con datos estudiantes: CID, apellidos, nombre, email
#     fichMSG               Fichero con el mensaje a enviar. Puede personalizarse el texto en cada 
#                           mensaje con las variables: %(EXAMEN), %(ASIGNATURA), %(REMITENTE), 
#                           %(APELLIDOS), %(NOMBRE), %(CID). (Insensible a mayúsc./minúsc.)
#   
#   optional arguments:
#     -h, --help            show this help message and exit
#     -v, --verbose         Incrementa el número de mensajes de seguimiento de la ejecución
#     -d [DIRPDF], --dirpdf [DIRPDF]
#                           Directorio donde se encuentran los ficheros a adjuntar a los estudiantes 
#                           (examenes, ejercicios, etc).Si no se da esta opción, simplemente se envía el 
#                           mensaje sin adjuntos
#     -p PATRON, --patron PATRON
#                           Patrón con el nombre de los ficheros PDF a buscar. Por omisión: 'APELLIDOS NOMBRE'.
#                           Pueden usarse también 'CID' y 'EMAIL'. (Insensible a mayúsc./minúsc.)
#     -a ASUNTO, --asunto ASUNTO
#                           Asunto para el correo electrónico enviado (por omisión: 
#                           'Correo del profesor Rafael Gallego')
#     -e EXAMEN, --examen EXAMEN
#                           Nombre del examen sobre el que se envía información
#     --asignatura ASIGNATURA
#                           Asignatura sobre la que se envía información
#     --acuse               Para recibir acuse de recibo de los mensajes enviados (por omisión, no se recibe)
#     --emailrte EMAILRTE   Correo electrónico del remitente (por omisión: 'gallego@ugr.es')
#     --remitente REMITENTE
#                           Nombre del remitente (por omisión: 'Rafael Gallego')
#     --servidor SERVIDOR   Servidor para envío correos (por omisión: 'smtp.ugr.es:587')

# El script necesita dos ficheros obligatoriamente, fichCSV y fichMSG,
#
#   fichCSV: Fichero CSV de los alumnos con los datos: CID, Apellido, Nombre, email
#            separados por comas y en ese orden. Puede tener una línea de encabezamiento.
#   fichMSG: Mensaje de TEXTO que se envía a los alumnos. Este mensaje puede personalizarse incluyendo
#            una serie de 'variables' de la forma %(VAR) que se sustituirán por su valor para cada alumno.
#            Los valores posible de VAR son:
#               EXAMEN:      Nombre del examen sobre el que se informa en el correo
#               ASIGNATURA:  Nombre de la asignatura
#               REMITENTE:   Profesor remitente
#               APELLIDOS:   Apellidos del alumno
#               NOMBRE:      Nombre del alumnos
#               CID:         CID del alumno
#
#            Pueden ponerse en minúsculas también

# Si se quieren adjuntar archivos PDF a cada mensaje, se da la opción -d (--dirpdf). Si se da esta opción
# sin ningun valor, se buscan los archivos PDF en el directorio actual ('./').
#
# A cada alumno se le envía el archivo en cuyo nombre aparezca el 'patron' de dicho alumno (ver 'patron'
# más arriba.

import sys
import argparse
import os

# Valores por omisión: aquí se DEBEN cambiar para personalizar cada profesor
# 
# También pueden cambiarse en la llamada al script (ver '--help')
emailrte  = 'gallego@ugr.es'
remitente = 'Rafael Gallego'
#
servidor  = 'smtp.ugr.es:587'

# Lectura
parser = argparse.ArgumentParser()
parser.add_argument("fichCSV", 
    help="Fichero CSV con datos estudiantes: CID, apellidos, nombre, email.")
parser.add_argument("fichMSG", 
    help="Fichero con el mensaje a enviar. Puede personalizarse el texto en cada mensaje con las variables: "+\
        "%%(EXAMEN), %%(ASIGNATURA), %%(REMITENTE), %%(APELLIDOS), %%(NOMBRE), %%(CID). "+
        "(Insensible a mayúsc./minúsc.).")
parser.add_argument("-v", "--verbose", action="store_true",
    help="Incrementa el número de mensajes de seguimiento de la ejecución.")
parser.add_argument("-d", "--dirpdf", nargs='?', const='./', required='--patron' in sys.argv or '-p' in sys.argv,
    help="Directorio donde se encuentran los ficheros a adjuntar a los estudiantes (examenes, ejercicios, etc)."+
         "Si no se da esta opción, simplemente se envía el mensaje sin adjuntos.")
parser.add_argument("-p", "--patron", default='APELLIDOS NOMBRE', 
    help="Patrón con el nombre de los ficheros PDF a buscar. Por omisión: '%(default)s'. "+\
         "Pueden usarse también 'CID' y 'EMAIL'. (Insensible a mayúsc./minúsc.).")
parser.add_argument("-a", "--asunto", default="Correo del profesor "+remitente,
    help="Asunto para el correo electrónico enviado (por omisión: '%(default)s').")
parser.add_argument("-e", "--examen", 
    help="Nombre del examen sobre el que se envía información.")
parser.add_argument("--asignatura", 
    help="Asignatura sobre la que se envía información.")
parser.add_argument("--acuse", action="store_true",
    help="Para recibir acuse de recibo de los mensajes enviados (por omisión, no se recibe).")
parser.add_argument("--emailrte", default=emailrte,
    help="Correo electrónico del remitente (por omisión: '%(default)s').")
parser.add_argument("--remitente", default=remitente,
    help="Nombre del remitente (por omisión: '%(default)s').")
parser.add_argument("--servidor", default=servidor,
    help="Servidor para envío correos (por omisión: '%(default)s').")

args = parser.parse_args()

#==============================================================================
# Miro a ver errores de entrada
#==============================================================================
if not os.path.isfile(args.fichCSV):
    print '----\nERROR: no existe el fichero de alumnos '+args.fichCSV
    sys.exit()
if not os.path.isfile(args.fichMSG):
    print '----\nERROR: no existe el fichero de mensaje '+args.fichMSG
    sys.exit()
if args.dirpdf != None and not os.path.isdir(args.dirpdf):
    print '----\nERROR: no existe el directorio de PDFs '+args.dirpdf
    sys.exit()

# Leo mensaje a enviar,para comprobar otros posibles errores
with open(args.fichMSG,'r') as f: msg = f.read()

# Compruebo si el msg tiene patrones para sustituir, y si las variables correspondientes están definidas
# Los patrones posibles son: %(examen), %(asignatura), %(remitente), %(apellidos), %(nombre), %(CID).
# El tercero está definido por omisión, y los tres últimos siempre están, porque los leerá de fichCSV, 
# por lo que solo hay que preocuparse de comprobar %(examen) y %(asignatura).
if ('%(examen)' in msg or '%(EXAMEN)' in msg) and args.examen==None:
    print "----\nERROR: ha introducido el patrón '%(EXAMEN)' en el mensaje, pero NO ha definido su valor\n----"
    sys.exit()
if ('%(asignatura)' in msg or '%(ASIGNATURA)' in msg) and args.asignatura==None:
    print "----\nERROR: ha introducido el patrón '%(ASIGNATURA)' en el mensaje, pero NO ha definido su valor\n----"
    sys.exit()

#==============================================================================
# Leo lista de ficheros PDF a enviar, si es que existe
#==============================================================================

ficheros = []
if args.dirpdf!=None:
    # Los ficheros a enviar están en el directorio args.dirpdf
    # Lista con nombre de todos los pdf, indexados. 
    # Pongo / al final del directorio, por si se ha olvidado
    if args.dirpdf.find('/',-1) + 1 < len(args.dirpdf):  args.dirpdf += '/'
    for f in os.listdir(args.dirpdf):
        if f.endswith(".pdf") or f.endswith(".PDF"):
            ficheros.append(f)

#==============================================================================
# Leo password para enviar mensajes.
#==============================================================================

from ModuloEmail import *

pm_login_usuario = args.emailrte.split('@')[0]

# Entrada de contraseña oculta
import getpass

print "Introduzca contraseña de email para usuario UGR: " + args.emailrte
print "Por seguridad, al teclear permanecerá oculta sin dar pistas" 
pm_login_password = getpass.getpass()

# Acuse de recibo e imágnes embebias (que no habrá)
pm_acuse_recibo  = args.acuse
pm_imagenes_embebidas = []

#==============================================================================
# Lectura del fichero .csv
# 
# Este fichero ha de tener en sus cuatro primeros campos los datos
#   CID, apellidos, nombre, email
# en este orden, separados por ','. Puede o no tener línea de cabecera
# Esto puede mejorarse leyendo la cabecera y ver si están todos los campos, y
# en que orden.
#==============================================================================
import csv
fCSV = csv.reader(open(args.fichCSV, 'rb'))

# Sustituyo patrones generales en el mensaje
for r in (("%(REMITENTE)",args.remitente),("%(remitente)",args.remitente),\
          ("%(EXAMEN)",args.examen),("%(examen)",args.examen),\
          ("%(ASIGNATURA)",args.asignatura),("%(asignatura)",args.asignatura)):
    msg = msg.replace(*r)

# Envio correo, con o sin adjuntos, según esté o no definido 'dirpdf'
nalumnos = 0 # Envíos que se intenta hacer
ncorreos = 0 # Envíos exitosos

# Mando el mensajito a cada alumno
for index,row in enumerate(fCSV):  
    # Si el campo email no esta, paso al siguiente: con esto también me salto tb el encabezado, si existe
    if row[3].find('@') < 0: continue
    nalumnos += 1
    if args.verbose: 
        print '\nAlumno:  ' + str(index) + '\n------------\nCID: ' + \
            row[0].strip() + ', Apellidos y Nombre: ' + \
            row[1].strip() + ', ' + row[2].strip() + ', email: ' + row[3].strip() 
    # Cambio patrones en el msg de este alumno
    mensaje = msg
    for r in (("%(APELLIDOS)",row[1].strip()),("%(apellidos)",row[1].strip()),\
              ("%(NOMBRE)",row[2].strip()),("%(nombre)",row[2].strip()),\
              ("%(CID)",row[0].strip()),("%(cid)",row[0].strip())):
        mensaje = mensaje.replace(*r)
    pm_archivo_texto   = mensaje
    pm_receptor_nombre = row[2].strip() + " " +  row[1].strip()
    pm_receptor_correo = row[3].strip()
    pm_archivo_html    = '<pre>'+mensaje+'</pre>'
    pm_adjuntos        = []
    # Busco fichero para adjuntar, si me han dicho que lo haga
    envia = True
    if args.dirpdf != None:
        envia = False  # Si no encuentro el fichero, no envío el mensaje
        patron = args.patron
        for r in (("APELLIDOS",row[1].strip()),("apellidos",row[1].strip()),\
                  ("NOMBRE",row[2].strip()),("nombre",row[2].strip()),\
                  ("EMAIL",row[3].strip()),("email",row[3].strip()),\
                  ("CID",row[0].strip()),("cid",row[0].strip())):
            patron = patron.replace(*r)
        # Y ahora busco el fichero cuyo nombre incluya al 'patron'
        for f in ficheros: 
            if patron in f:
                envia = True
                pm_adjuntos = [args.dirpdf + f]
                # Solo busco un fichero, si hay más, se envía el primero que encuentre
                # Si se quisieran enviar varios, habría que modificar estas líneas
                break
    if envia and \
       mandar_mail(args.servidor, pm_login_usuario, 
                  pm_login_password,args.remitente, 
                  args.emailrte, pm_receptor_nombre,
                  pm_receptor_correo, args.asunto, pm_archivo_texto,
                  pm_archivo_html, pm_adjuntos, pm_acuse_recibo,  
                  pm_imagenes_embebidas):
        # La rutina "manda_mail" da "False" si no puede enviar el email.
        # Podría hacerse que diera un mensaje más explícito, es decir, que explique
        # por qué no ha podido enviar el mensaje si falla, pero por ahora es así.
        ncorreos += 1 
        if args.verbose: print '*** ¡Correo enviado! ***'
if args.verbose: 
    print   "\n*** Número total de correos enviados  = ",ncorreos,\
            "\n*** Número total de alumnos           = ",nalumnos
if args.dirpdf != None:
    if args.verbose: 
        print "*** Número total de ficheros          = ",len(ficheros)
    if len(ficheros) != ncorreos:
            print '\n*** ATENCIÓN\n*** El número de envios, alumnos y/o ficheros difiere',\
                "\n    Puede ser porque:"\
                "\n\t 1) Algún alumno no tiene ningún fichero que coincida con el patrón"\
                "\n\t 2) Algún fichero PDF no tiene un nombre que coincida con el patrón"\
                "\n\t 3) Ambas cosas"
