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

Añadidos de Rafael Gallego: 
envioMSG.py -> Fichero avanzado de envío de exámenes. 
             EnviarMSG -h

usage: EnvioMSG.py [-h] [-v] [-d [DIRPDF]] [-p PATRON] [-a ASUNTO] [-e EXAMEN]
                   [--asignatura ASIGNATURA] [--acuse] [--emailrte EMAILRTE]
                   [--remitente REMITENTE] [--servidor SERVIDOR]
                   fichCSV fichMSG

positional arguments:
  fichCSV          Fichero CSV con datos estudiantes: CID, apellidos, nombre, email
  fichMSG         Fichero con el mensaje a enviar. Puede personalizarse el texto en cada mensaje con las variables:                             %(EXAMEN), %(ASIGNATURA), %(REMITENTE), %(APELLIDOS), %(NOMBRE),
                        %(CID). (Insensible a mayúsc./minúsc.)

optional arguments:
  -h, --help        show this help message and exit
  -v, --verbose  Incrementa el número de mensajes de seguimiento de la ejecución
  -d [DIRPDF], --dirpdf [DIRPDF]
                        Directorio donde se encuentran los ficheros a adjuntar a los estudiantes (examenes, ejercicios, etc).                         Si no se da esta opción, simplemente se envía el mensaje sin adjuntos
  -p PATRON, --patron PATRON
                        Patrón con el nombre de los ficheros PDF a buscar.
                        Por omisión: 'APELLIDOS NOMBRE'. Pueden usarse
                        también 'CID' y 'EMAIL'. (Insensible a mayúsc./minúsc.)
  -a ASUNTO, --asunto ASUNTO
                        Asunto para el correo electrónico enviado (por omisión: 'Correo del profesor Rafael Gallego')
  -e EXAMEN, --examen EXAMEN
                        Nombre del examen sobre el que se envía información
  --asignatura ASIGNATURA
                        Asignatura sobre la que se envía información
  --acuse          Para recibir acuse de recibo de los mensajes enviados (por omisión, no se recibe)
  --emailrte EMAILRTE   Correo electrónico del remitente (por omisión: 'gallego@ugr.es')
  --remitente REMITENTE
                        Nombre del remitente (por omisión: 'Rafael Gallego')
  --servidor SERVIDOR   Servidor para envío correos (por omisión: 'smtp.ugr.es:587')

------------------------------------------

Para que lo use cualquiera basta llamarlo con el 'remitente' y 'emailrte' correspondientes (o mejor, cambiar estas dos variables en las líneas 29 y 30 del script).

Los ficheros PDF que se envían pueden tener el nombre de la forma 'APELLIDO NOMBRE' (por omisión), como tu haces, o el 'CID' como lo hacía yo, o cualquier PATRON basado en estos valores (p.e 'APELLIDO_NOMBRE', o 'APELLIDO-(CID)', o lo que sea)
