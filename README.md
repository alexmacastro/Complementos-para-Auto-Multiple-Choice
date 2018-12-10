# Complementos-para-Auto-Multiple-Choice
Complementos para sistema de exámenes con Auto-Multiple-Choice

Ficheros para ser utilizados junto con Auto-Multiple-Choice

Código 1: Comunicar a cada estudiante su ID

Ficheros: CODIGO_Enviar_CID_previo.py + Modulo_email.py

Código 2: Modificar nombre de fichero pdf previo a ser enviado
          Para que conste la asignatura, año, tipo de prueba, etc. 
          en el propio nombre del fichero.
          
          Guardarlo en acceso directo tipo /bin
          Hacerlo ejecutable chmod +x 
          
Fichero: AMC_Cambianombres.py

Código 3: Enviar a cada estudiante su examen corregido a su email. 

Fichero: CODIGO_Enviar_Examenes_Mejorado.py + Modulo_email.py


Reto futuro: Mejorar la interface de usuario, o integrarlo en AMC. 

Añadidos de Rafael Gallego: script avanzado para enviar correos con o sin adjuntos, basados en los scripts de AMC
Ver ayuda con:
   EnvioMSG.py -h

    usage: EnvioMSG.py [-h] [-v] [-d [DIRPDF]] [-p PATRON] [-a ASUNTO] [-e EXAMEN]
                   [--asignatura ASIGNATURA] [--acuse] [--emailrte EMAILRTE]
                   [--remitente REMITENTE] [--servidor SERVIDOR]
                   [--password PASSWORD]
                   fichCSV fichMSG

          ....

Para que lo use cualquier PROFESOR basta llamarlo con el 'remitente' y 'emailrte' correspondientes (o mejor, cambiar estas dos variables en las líneas 109 y 110 del script donde se definen los valores por omisión).

Los ficheros PDF que se envían pueden tener el nombre de la forma 'APELLIDO NOMBRE' (por omisión), o el 'CID', o cualquier PATRON basado en estos valores (p.e 'APELLIDO_NOMBRE', o 'APELLIDO-(CID)', o lo que sea)
