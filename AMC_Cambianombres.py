#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SCRIPT PARA CAMBIAR NOMBRES A LOS PDF GENERADOS POR AUTO-MULITPLE-CHOICE

Autor: Alejandro E. Martinez Castro amcastro@ugr.es
       Departamento de Mecánica de Estructuras e Ingeniería Hidráulica. 
       Universidad de Granada
Fecha: 3-julio-2017

Licencia de Creative Commons Reconocimiento-NoComercial 4.0 Internacional.

"""


#==============================================================================
# Cambiar nombres a pdf para tener referencia a 
# Asignatura y curso: (e.g. AE1516)
# Parte (e.g. MEF, Matricial, Inestabilidad, etc)
# Convocatoria:junio 
# 
# Este script es auto-ejecutable debido a la primera línea. 
# 
# Se puede copiar en una ruta de ejecutables, como en ~/bin
# Para esto hay que tener claro que desde .bashrc este directorio está en el PATH
# 
# Hay que Verificar que tiene permisos de ejecución. Si no, cambiarlos con 
# 
# chmod +X AMC_Cambianombres.py
# 
# 
# Autor: Alejandro E. Martinez Castro amcastro@ugr.es
#        Departamento de Mecánica de Estructuras e Ingeniería Hidráulica. 
#        Universidad de Granada
# Fecha: 3-julio-2017
# 
# Uso: Simplemente, desde el directorio donde están los .pdf generados por AMC (mejor copiarlos a otro directorio tipo pdf_email) escribir
# AMC_Cambianombres.py
# 
# Si está bien enlazado en la ruta global, pedirá introducir la clave. En la línea, escribir algo tipo: 
# 
# AE1516 Matricial Julio
# 
# El script cambiará todos los nombres de todos los pdf que aparezcan y les añadirá al final esta clave. 
# 
#==============================================================================

import os

# Se pide al usuario por pantalla que indique la clave (se pueden incluir espacios en blanco)

clave = raw_input("Introduzca código AsignaturaAño-Parte-Convocatoria: (e.g. AE1516 Matricial Julio)\n") 
#ejemplo: AE1516 Matricial julio

# Se genera una lista con los nombres de ficheros. 

ficheros = []

for file in os.listdir("./"):  # Se asume que la ruta es local
    if file.endswith(".pdf"): 
        ficheros.append(file)

numfiles = len(ficheros) # Número de ficheros de la lista. 

for file in ficheros:
       
    nuevonombre = file.replace(".pdf","-" + clave + ".pdf")
    print "Nombre inicial: ", file
    print "Nuevo nombre: ", nuevonombre
    os.rename(file,nuevonombre)
     
