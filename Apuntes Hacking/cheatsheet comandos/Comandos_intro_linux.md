## Comandos básicos de Linux (1-2)

|Comando|Descripción|
|---|---|
|`whoamI`|Nombre de la cuenta|
|`id`|Saber a que grupos pertenezco|
|`sudo`|Sudo se refiere a realizar una accion de administrador o del root|
|`sudo su`|Cambiarse a root|
|`exit`|Exit se refiere de salirse de algo o salirse de la terminal|
|`exit` (despues de poner sudo su)|Sales de la sesion de root|
|`sudo whoami`|Nombre de la cuenta del root|
|`sudo id`|Saber a que grupos pertenece root|
|`cat [dirreccion]`|imprimir todo el contenido de un archivo/carpeta a la terminal|
|`cat [/etc/group]`|Imprime todo el contenido de ese archivo/carpeta|
|`less [dirreccion]`|Imprime el contenido de un archivo/carpeta, solamente lo que quepa en la ventana de la terminal, permitiendo navegar por diferentes secciones|
|`less [/etc/group]`|Imprime el contenido de ese archivo/carpeta, dividiendolo en secciones|
|`which [comando]`|Muestra el alias donde se ubica la ruta para activar el comando|
|`which [cat]`|Muestra el alias de la ruta de ese comando|
|`/usr/bin/whoami`|El comando "extendido o completo" de whoami, dirigiendose a la ruta|
|`echo [palabra o directorio]`|Se imprime la palabra que quieras mencionar en la terminal, o la dirrecion de un archivo o carpeta|
|`echo [hola]`|Imprime la palabra "hola" en el terminal|
|`echo [$PATH]`|Imprime la dirrección de la carpeta/archivo PATH|
|`[comando 1] \| [comando 2]`|Se pueden ejecutar 2 comandos, separando con \|, en donde el segundo comando dependa del primero|
|`cat [dirreccion] \| grep [operador]`|Primero ejecuta el comando cat y despues el comando grep, este sirve para añadir filtros a la lista de items del archivo|
|`cat /etc/group \| grep "floppy"`|Registra todo el contenido de la carpeta group, y despues añade filtro de floppy para que solo imprima los resultados con esa palabra|
|`cat /etc/group \| grep "floppy" -n`|Lo mismo que lo anterior pero se añade -n, para mostrar en que linea se encuentra ese registro-item|
|`command -v [comando]`|Sustituto de which, se usa especialmente a la hora de pentesting|
|`commando -v [whoami]`|Lo mismo que which|

## Comandos básicos de Linux (2-2)

|Comando|Descripción|
|---|---|
|`pwd`|Muestra la ubicación donde estas ubicado actualmente|
|`ls`|En la ubicación deonde estas actualmente, se muestran las subcarpetas y archivos|
|`ls -l`|Mismo que lo anterior, pero organizandolo en tabla con columnas acerca de ultima fecha de modificacion, permisos, peso, entre otros|
|`tree [direccion]`|Mismo que ls pero te muestra un arbol|
|`cd [dirrección]`|Cambias de dirreccion para modificarlo|
|`cd Descargas`|Cambias a la dirreccion de descargas para modificarlo|
|`cd ..`|Los 2 puntos .. indica irte para atras|
|`bash`|Para comandos, otra terminal dentro de la terminal|
|`mktemp -d`|Crea una carpeta temporal|

Referencias:

- https://www.bonaval.com/kb/cheats-chuletas/comandos-basicos-linux
- https://www.fing.edu.uy/inco/cursos/sistoper/recursosLaboratorio/tutorial0.pdf

## Control del flujo stderr-stdout, operadores y procesos en segundo plano

|Comando|Descripción|
|---|---|
|`[comando 1]; [comando 2]; [comando 3]; ...`|Puedes ejecutar 2 comandos o mas en vez de hacerlo por separado, donde cuando termine el primer comando inicie el siguiente y sucecivamente, a diferencia de "\|", el segundo comando depende del primero para ejecutarse|
|`whoami; ls;`|Ejecuta primero whoami, una vez acabe ejecuta ls;|
|`[comando 1] && [comando 2] && [comando 3] ...`|A diferencia de los ";", los && ejecuta el siguiente comando solamente si el comando actual devuelve un valor|
|`whoami && ls`|Ejecuta primero whoami, y como regresara un valor (nombre del usuario), se ejecutara ls|
|`whoam && ls`|como no existe el colamdno "whoam", siempre dara error y por ende no ejecutara el siguiente comando que es ls|
|`echo $?`|$? es un valor booleano donde el resultado es 0/1, lo que hace es verificar si el comando(s) anterior(es) han funcionado correctamente y no fallaron, siendo 1 o mayor positivo (si hubo error), o 0 negativo (no hubo error)|
|`[comando 1] \| [comando 2] \| [comando3]...`|Ejecuta el primer comando, en caso de que sea exitoso no ejecuta el segundo ni los demas, si el primer comando falla ejecuta el segundo, si falla el tercero y asi sucecivamente|
|`whoam \| ls`|Como el primer comando fallara, ejecuta el segundo|
|`whoami \| ls`|Ejecuta el primer comando, sera exitoso y no ejecutara el segundo|
|`[comando1 (mal escrito)] 2>[direccion]`|El comando mal escrito deberia salir un mensaje de error, pero lo que estamos haciendo es que este se diriga hacia una direccion en particular para ejecutar otro comando, anunciandose con el canal 2 para errores|
|`whoam 2>/dev/null`|como whoam no existe deberia salir error y mensaje del canal 2, pero lo envia al comando de la direccion /dev/null, que lo que hace es no mostrar ningun mensaje de error|
|`whoami 2>/dev/null`|whoami esta correcto, y por ende no ocurrira ningun mensaje de error o evento similar|
|`cat /etc/host > /dev/null 2>&1`|Este caso similar tiene 2>&1, lo que hace es apuntar el canal 2 de errores al mismo donde esta apuntando canal 1, haciendo que la ejecucion de error sea lo mismo que exito|
|`cat /etc/host &>/dev/null`|lo mismo que lo anterior, &> sirve para capturar ambos canales al mismo tiempo, tanto si esta corrercto como incorrecto|
|`wireshark &> /dev/null`|wireshack es un programa, el punto es que con /dev/null hacemos que no deje ningun mensaje en la consola|
|`wireshark &> /dev/null &`|Caso anterior, pero añadiendo & mostrara el ID del proceso del programa ejecutandose|
|`wireshark &> /dev/null & disown`|Caso anterior, pero añadiendo disown, como es un subproceso ejecutandose de la terminal, el programa se deberia cerrar cuando te salgas de la terminal (exit), pero como tienes disown, son procesos a parter y si sales de la terminal no afectara el programa|
|`top` / `htop`|Mostrar los procesos en tiempo real (consumo de CPU/RAM)|
|`ps aux \| grep [nombre]`|Buscar el ID de un proceso (PID) especifico para poder interactuar con el|
|`kill -9 [PID]`|Forzar cierre de un proceso de forma inmediata|

Referencia:

- https://hack4u.io/wp-content/uploads/2022/05/bash-redirections-cheat-sheet.pdf

## Descriptores de archivos

|Comando|Descripción|
|---|---|
|`exec [numero]<> [nombre del archivo]`|Crea un archivo, con <> para indicar al terminal que es para la creacion|
|`exec 3<> file`|Crea un archivo de tipo file, con el numero 3 de tuberia ya que es personalizable para uso de variables, pues 1 es para éxito y 2 para error|
|`file [nombre del archivo]`|Analiza el archivo diciendote que tipo es y cuando tamañoo tiene el archivo|
|`file file`|Analiza el archivo file|
|`[comando] >&[numero]`|Ejecuta el comando y luego envia la informacion al archivo guardado en el canal 3|
|`whoami >&3`|Ejecuta whoami y luego lo envia al canal 3, si hay un archivo guardado en ese canal se guardara en ese archivo, como ya habiamos hecho exec 3<> file antes, se guardara la informacion en el archivo file|
|`exec [numero]>&-`|Desvincula o cierra el canal a elegir (descriptor)|
|`exec 3>&-`|Desvincula o cierra el canal 3 (descriptor)|
|`exec [numero 2]>&[numero 1]`|La informaciondescriptor del numero 1 se hace una copia al al siguiente descriptor a elegir|
|`exec 4>&3`|El descriptor 3 se copia al 4|
|`exec [numero 2]>&[numero 1]-`|Caso anterior pero tambien cierra el descritor emisor|
|`exec 6>&5-`|El descriptor 5 se copia al 6 y se cierra el 5|

Referencia:

- https://hack4u.io/wp-content/uploads/2022/05/bash-redirections-cheat-sheet.pdf

## Lectura e interpretación de permisos

|Comando|Descripción|
|---|---|
|`touch [nombre del archivo].[extension]`|Crea un archivo|
|`touch file.txt`|Crea el archivo file.txt|
|`echo [mensaje] > [archivo]`|Guarda texto en un archivo, pero si vuelves a usar el comando con el mismo archivo, se reemplazara con la infromacion antigua ya que es lo que indica >, si lo que se quiere es hacer un append, se debe usar »|
|`echo "Hola probando" > file.txt`|Guarda el texto en el archivo|
|`echo [mensaje] » [archivo]`|Al poner doble > ya se estaria realizando un append, añadir informacion en vez de sobreescribir|
|`echo adios » file.txt`|Añade adios al archivo en vez de sobreescribir y quitar "Hola probando"|
|`rm [archivo]`|Elemina un archivo|
|`rm file.txt`|Elemina el archivo file.txt|
|`rm -r *`|Elemina todos los archivos y/o direcctorios|
|`nano [archivo]`|Te metes adentro del archivo para editarlo, en caso de que no exista el archivo lo crea|
|`nano file.txt`|Modificas el archivo file.txt, en caso de que ese archivo no exista, se crea|
|`vi [archivo]`|Tambien editas un archivo, pero usando el programa/plugin vin|
|`mkdir [nombre]`|Crea un directorio|
|`mkdir prueba`|Crea el directorio prueba|

Referencias:

- https://blog.desdelinux.net/permisos-y-derechos-en-linux/?msclkid=22f8cb88ba8111ecb5d8a3db91f066ab
- https://www.softzone.es/programas/linux/permisos-archivos-directorios-linux/

## Asignacion de permisos [1-2]

|Comando|Descripción|
|---|---|
|`chmod [u/g/o]+[r/w/x] [archivo]`|Modifica Permisos añadiendolos ya sea al User (Usuario), Group (Grupto) u Other (Otro) acerca de poder Read (Leer), Write (Escribir) o eXecute (Ejecutar) a un archivo o directorio|
|`chmod o+w prueba`|Añade el permiso de escribir a otros en el directorio de prueba|
|`chmod [u/g/o]-[r/w/x] [archivo]`|Lo mismo pero ahora quita permisos (esta el – en vez de +)|
|`chmod o-w prueba`|Quita el permiso de escribir a otros en el directorio de prueba|
|`chgrp [grupo] [archivo/directorio]`|Cambia de grupo o usuario para un archivo o directorio|
|`chgrp fabca06 prueba`|Cambia de grupo para el directorio de prueba|
|`chmod u-x,g-rx,o+w,o-x prueba`|Puedes modificar varios permisos en un mismo archivo tanto usuario, grupos y otros|

## Asignacion de permisos [2-2]

|Comando|Descripción|
|---|---|
|`useradd [usuario] -s [ruta] -d [ruta]`|Crea un usuario nuevo, con las especificaciones del shell a usar y el directorio donde estara ubicado|
|`useradd pepe -s /bin/bash -d /home/pepe`|Crea el usuario pepe con su propio sheel y ubicación a usar|
|`chown [usuario] [usuario]`|Dar propietario de la cuenta, especificando a que usuario se quiere dar propietario y para quien|
|`chown pepe pepe`|Dar propietario de la cuenta de pepe al usuario pepe|
|`sudo chown pepito:pepito pepito`|Dar propietario de todo|
|`groupadd [nombre]`|Añade un nuevo grupo|
|`groupadd Alumnos`|Añade un grupo nuevo llamado Alumnos|
|`usermod -a -G [grupo] [usuario]`|Añade un grupo a un usuario|
|`usermod -a -G Alumnos pepe`|Modifica los grupos del usuario pepe para añadir el grupo Alumnos|
|`sudo userdel [usuario]`|Elemina a un usuario|
|`sudo userdel -r [usuario]`|Elemina a un usuario y todos sus datos|
|`grep [usuario] /etc/passwd`|Verifica si un usuario existe o no|

Referencias:

- https://computernewage.com/2016/05/22/gestionar-usuarios-y-permisos-en-linux/
- https://www.ionos.es/digitalguide/servidores/know-how/asignacion-de-permisos-de-acceso-con-chmod/

## Notacion octal de permisos

|Comando|Descripción|
|---|---|
|`chmod 755 testing`|Otra forma de dar permisos, pues el primer digito corresconde al binario de user, el segundo a grupos y tercero otros|

|Dígito|Significado|
|---|---|
|0|no hay persmisos de nada|
|1|solo ejecutar|
|2|solo escribir|
|3|escribir y ejecutar|
|4|solo leer|
|5|leer y ejecutar|
|6|escribir y ejecutar|
|7|los 3 permisos, osea todo|

Referencia:

- https://blog.alcancelibre.org/staticpages/index.php/permisos-sistema-de-archivos

## Permisos especiales – Sticky Bit

|Comando|Descripción|
|---|---|
|`chmod +t pruebaspepito/`|Aplica Sticky Bit, donde los usuarios no puedan hacer cambios a los archivos dentro del directorio si no son los propietarios de los archivos, incluyendo si los propios archivos tengan permisos de escritura|

Referencia:

- https://www.fpgenred.es/GNU-Linux/el_bit_sticky.html

## Control de atributos de ficheros en Linux – Chattr y Lsattr

|Comando|Descripción|
|---|---|
|`cp [archivo/directorio] [nombre del archivo]`|Crea una copia de un archivo y lo introduce en el archivo que indiques, en caso de no existir se crea el archivo dentro de la misma ruta de la terminal|
|`lsattr [archivo]`|Permite listar los atributos asignados a los ficheros de un sistema de ficheros|
|`lsattr prueba`|Verifica los atributos asignados al archivo pruebas|
|`chattr +i -V [archivo]`|Permite modificar dichos atributos de los ficheros, +i es de inmutable (no se puede eleminar), mientras -V indica que sea descriptivo la informacion que nos da|
|`chattr +i -V prueba`|Le añade la inmutabilidad al archivo prueba|

Igualmente existen varios atributos no solo la "i" de inmutable:

|Atributo|Significado|
|---|---|
|A|para deshabilitar la modificacion de la fecha de acceso al fichero|
|c|para comprimir automaticamente el fichero en el disco|
|i|para bloquear la modificacion o borrado de un archivo (inmutable)|
|u|para permitir la recuperacion de archivo aunque sea eliminado|
|s|para escrifir de forma asincrona a discos cambios en los ficharos|
|e|para al eliminar un archivo, sobreescribir con 0 todos sus bloques|

Referencia:

- https://programmerclick.com/article/5604675172/

## Permisos especiales – SUID y SGID

|Comando|Descripción|
|---|---|
|`python3`|Ejecuta python|
|`python3 --version`|Verifica que version de python estas usuando|
|`which [programa/script] \| xargs [comando]`|El xargs actua como un puente, pues toma el output del comando anterior y lo convierte en argumento para el siguiente|
|`which python3 \| xargs ls -l`|Verifica la ubicación de python primero, para despues usarlo de argumento para ls|
|`chmod [notacion permisos] [archivo]`|Activa el bit SGID (Set Group ID)|
|`chmod 2755 prueba`|(ejemplo del comando anterior)|
|`chmod [notacion permisos] [archivo]`|Activa el bit SUID (Set User ID)|
|`chmod 4755 prueba`|(ejemplo del comando anterior)|

Referencias:

- https://deephacking.tech/permisos-sgid-suid-y-sticky-bit-linux/
- https://www.ochobitshacenunbyte.com/2019/06/17/permisos-especiales-en-linux-sticky-bit-suid-y-sgid/
- https://www.ibiblio.org/pub/linux/docs/LuCaS/Manuales-LuCAS/SEGUNIX/unixsec-2.1-html/node56.html

## Privilegios especiales – Capabilities

|Comando|Descripción|
|---|---|
|`getcap -r / 2>/dev/null`|Consigue ver las capacidades de todos los archivos, las capacidades vendrian siendo permisos de root pero dividido en partes, sin necesidad de otorgar todas las clases de permisos de root, y que estos los pueden ejecutar los programas|
|`setcap [capacidad] [ruta]`|Asigna capacidades especificando que atributos del root se puede aplicar al programa|
|`setcap cap_setuid+ep /usr/bin/python3`|Asigna capacidad de setuid para manipular la propia ID del usuario, se añade los atributos e (Effective) para activarse cuando se ejecuta el programa (Python) y p de dar permiso al programa de usar la capacidad|

Referencia:

- http://www.etl.it.uc3m.es/Linux_Capabilities

## Sistema de estructura de directorios

_Nota: Esta tabla es informativa, acerca del funcionamiento de cada uno de los directorios raiz, por lo tanto no es papeleta de comando_

|Directorio|Descripción|
|---|---|
|`bin`|Se almacenan los binarios ejecutables para usuario|
|`sbin`|Se almacenan los binarios ejecutables para root y/o el sistema|
|`boot`|Se almacenan los ejecutables necesarios para arrancar el sistema, incluido el kernel|
|`dev`|Se almacenan todos los dispositivos|
|`etc`|Se almacenan los archivos ficheros de configuracion, especialmente los externos|
|`home`|Se almacenan los usuarios y sus directorios, asi como archivos temporales para los usuarios|
|`lib`|Se almacenan las bibliotecas necesarias para ejecutar los binarios|
|`lib64`|Se almacenan las bibliotecas necesarias para ejecutar los binarios en 64 bits|
|`media`|Se almacenan los dispositivos extraibles (USB, SD, LECTORES CD, ETC.)|
|`opt`|Se almacenan programas externos|
|`proc`|Se almacenan los procesos que estan actualmente ejecutandose|
|`root`|Se almacena el usuario root y directorios, es ajeno a home|
|`srv`|Se almacenan servidores|
|`sys`|Se almacena la kernel|
|`tmp`|Se almacenan archivos temporales|
|`usr`|Se almacenan archivos solo lectura del usuario, asi como software instalado por paquetes|
|`var`|Se almacenan archivos con informacion del sistema|

## Uso de bashrc y zshrc

|Comando|Descripción|
|---|---|
|`ls -a`|El parametro -a indica ver todos los archivos, estos incluyen los archivos ocultos|
|`hostname -I`|Ver las IP|
|`ifconfig`|Ver todas las redes y sus IP|
|`[comando] -I \| awk '{print $[numero]}'`|Al añadir awk vendria siendo un filtro del registro de informacion, seleccionando el ID que quieres que se musetre|
|`hostname -I \| awk '{print $1}'`|Imprime la primer IP de todas las Ips mostradas|
|`echo "Tu IP privada es: $(hostname -I \| awk '{print $1}')"`|Puedes hacer un echo para imprimir solo la primera IP con el comando anterior|
|`source [directorio/archivo]`|Recarga un archivo o directorio especifico|
|`source ~/.zshrc`|Recarga el directorio zshrc|

Referencias:

- https://www.compuhoy.com/que-es-bashrc-en-linux/
- https://respontodo.com/que-es-zsh-y-por-que-deberia-usarlo-en-lugar-de-bash/

## Actualizacion y Upgradeo del sistema

|Comando|Descripción|
|---|---|
|`apt update`|Descarga las actualizaciones|
|`apt update list --upgradable`|Ve toda la lista a actualizar|
|`apt search [modulo]`|Busca un modulo en especifico|

## Busquedas a nivel sistema

|Comando|Descripción|
|---|---|
|`find / -[filtro]`|Hace una busqueda a nivel sistema|
|`find / -name passwd 2>/dev/null`|Encuentra todos los directorios y archivos con nombre de passwd, asi como usar el 2>/dev/null para enviar a la basura los resultados de permisos denegados u otros errores|
|`find / -name passwd 2>/dev/null \| xargs ls -l`|Lo puedes combinar con xargs para hacer una indicacion por cada resultado encontrado, por ejemplo ls para ver permisos de cada directorio encontrado|
|`find / -perm 4000 2>/dev/null`|Este es otro ejemplo, pues busca todos los archivos y directorios SUID con el filtrador de perm|
|`find / -group fabca06 2>/dev/null`|Ahora con el filtro group buscas todos los directorios y archivos que estan al grupo de fabca06|
|`find / -user root 2>/dev/null`|Obviamente esta busqueda por usuario|
|`find / -group fabca06 -type d 2>/dev/null`|Agregas el modificador -type d para buscar solo directorios|
|`find / -group fabca06 -type f 2>/dev/null`|Y con F para archivos solamente|
|`find / -user root -writable 2>/dev/null`|Encontrar archivos con capacidad de escritura|
|`find / -user root -executable 2>/dev/null`|Ejecutables solamente, pero tambien cuentan directorios pues si tecnicamente se puede "atravesar" son ejecutables|
|`find / -user root -executable -type f 2>/dev/null`|Ahora si solo busca ejecutables de archivos|
|`find / -name dex\* 2>/dev/null`|Por nombre, que comienzen con "dex"|
|`find / -name dex\*.sh 2>/dev/null`|Que comienze por dex y tenga la extension .sh|
|`man find`|Abre el manual para find, con todos los atributos y atributos restantes|
|`grep -r "texto_a_buscar" /ruta`|Busca una palabra dentro de todos los archivos de una carpeta de forma recursiva|
|`locate [nombre]`|Mucho más rápido que find, aunque requiere que la base de datos esté actualizada (updatedb)|

Referencia:

- https://www.hostinger.es/tutoriales/como-usar-comando-find-locate-en-linux/

## Creacion de scripts en bash

|Comando|Descripción|
|---|---|
|`./[archivo]`|Ejecuta un archivo (mayormente scripts)|
|`./touch [archivo.sh]`|Los scripts en bash usan extension sh|

## Lectura archivos especiales y busquedas con find y cat especificos

|Comando|Descripción|
|---|---|
|`cat ./[archivo]`|Otras formas de usar cat, pues hay caracteres especiales como guion "-" que se bugea ya que sirve para parametros en los comandos|
|`cat /[direccion]`|Otras formas de usar cat|
|`cat $(pwd)/[archivo]`|Otras formas de usar cat|
|`grep -r "\w" 2>dev/null \| tail -n 1`|Otras formas de encontrar el texto/registro deseado|
|`grep -r "\w" 2>dev/null \| tail -n 1 \| awk '{print $2}' FS=":"`|Otras formas de encontrar el texto/registro deseado|
|`grep -r "\w" 2>dev/null \| tail -n 1 \| cut -d ':' -f 2`|Otras formas de encontrar el texto/registro deseado|
|`grep -r "\w" 2>dev/null \| tail -n 1 \| tr ':' ' '`|Otras formas de encontrar el texto/registro deseado|
|`grep -r "\w" 2>dev/null \| tail -n 1 \| tr ':' ' ' \| awk '{print $2}`|Otras formas de encontrar el texto/registro deseado|
|`grep -r "\w" 2>dev/null \| tail -n 1 \| tr ':' ' ' \| awk 'NF{print $NF}'`|Otras formas de encontrar el texto/registro deseado|
|`cat ./-`|Abre el archivo "-" sin ser parametro|
|`cat [palabra 1]\ [palabra 2]\ [palabra3]\...`|Uso de cat para archivos donde tengan espacios, teniendo que especificar con ""|
|`cat spaces\ in\ thist\ filename\`|Abre el archivo "spaces in this filename" que contiene espacios|
|`cat s*`|Abre el archivo "spaces in this filename" que contiene espacios|
|`cat /home/bandit2/s*`|Abre el archivo "spaces in this filename" que contiene espacios|
|`cat /home/bandit2/*`|Abre el archivo "spaces in this filename" que contiene espacios|
|`cat ./--spaces\ in\ this\ filename--`|Abre el archivo "—spaces in this filename—" que contiene espacios y guiones al principio|
|`find . -type f \| grep [nombre] \| xargs file`|Hace una busqueda de los archivos que especifiques pero haciendo xargs file muestras el tipo de archivo|
|`find . -type f \| grep ./-file \| xargs file`|Muestra todos los archivos con nombre file, indicando el tipo de archivo|
|`find . -type f -readable`|Encontrar archivos humanamente leibles|
|`find . -type f ! -executable -size [Tamaño]`|Busqueda de archivo NO ejecutable, especificando su peso|
|`find . -type f ! -executable -size 1033c`|Busqueda de un archivo no ejecutable, file y que pese 1033 bytes|
|`finde -type f -size 33c -user bandit7 -group bandit6 2>dev/null`|Busqueda de un archivo con es file, con 33 bytes de peso, el usuario propietario es bandit7 y el grupo propietario bandit6, con el 2>/dev/null|
|`cat data.txt \| grep "millionth"`|Formas de encontrar el texto que va despues de la palabra "millonth", considerando que el txt sean 2 columnas y entre ellas 2 haya separacion con espacios|
|`cat data.txt \| grep "millionth" \| awk 'NF{print $NF}'`|Formas de encontrar el texto que va despues de la palabra "millonth"|
|`cat data.txt \| grep "millionth" \| awk '{print $2}'`|Formas de encontrar el texto que va despues de la palabra "millonth"|
|`cat data.txt \| cut -d ' ' -f 1`|Formas de encontrar el texto que va despues de la palabra "millonth"|
|`sort data.txt \| uniq -u`|Encontrar la unica palabra que no se repite|
|`diff [archivo 1] [archivo 2]`|Con diff encuentras cambios que se hicieron en el archivo 1 para tener lo mismo que el archivo 2|
|`diff passwords.old passwords.new`|Checa las diferencias entre estos 2 archivos|
|`sed 's/antiguo/nuevo/g' archivo`|Sustituye palabras en todo un documento sin abrirlo|
|`head -n [numero]`|Muestra las primeras líneas de un archivo (lo opuesto a tail)|
|`wc -l [archivo]`|Cuenta cuántas líneas tiene un archivo (muy útil para listas de contraseñas o diccionarios)|

Referencias:

- https://en.wikipedia.org/wiki/List_of_file_signatures
- https://www.ionos.es/digitalguide/servidores/configuracion/comando-linux-find/
- AWK Cheat Sheet: https://www.shortcutfoo.com/app/dojos/awk/cheatsheet
- AWK Cheat Sheet 2: https://bl831.als.lbl.gov/~gmeigs/scripting_help/awk_cheat_sheet.pdf
- Cheat Sheet: Cutting Text with cut: https://bencane.com/2012/10/22/cheat-sheet-cutting-text-with-cut/
- Tutorial del uso de SORT: https://www.ibidemgroup.com/edu/tutorial-sort-linux-unix/
- Tutorial del uso de UNIQ: https://victorhckinthefreeworld.com/2021/10/21/el-comando-uniq-de-gnu/
- Diferencias con diff: https://eltallerdelbit.com/comando-diff-ejemplos/

## Decodificacion de mensajes

|Comando|Descripción|
|---|---|
|`string data.txt \| grep "==="`|Agrupa todos los strings de un archivo, y los filtra por los que tienen mas de 3 iguales|
|`string data.txt \| grep "===" \| tail -n 1`|Agrupa todos los strings de un archivo, y los filtra por los que tienen mas de 3 iguales|
|`strings data.txt \| grep "===" \| tail -n 1 \| awk 'NF{print $NF}'`|Agrupa todos los strings de un archivo, y los filtra por los que tienen mas de 3 iguales|
|`echo "VGhlIHBhc3N3b3JkIGlzIGR0UjE3M2ZaS2IwUlJzREZTR3NnMlJXbnBOVmozcVJyCg==" \| base64 -d`|Desifra el mensaje encriptado en base 64|
|`cat data.txt \| tr '[G-ZA-Fg-za-f]' '[T-ZA-St-za-s]'`|Descifra el mensaje encriptado en rot13|
|`cat data \| xxd -r \| sponge data`|Con xxd convierte el archivo de bytes a hexadecimal, pero con -r es reverso encontes hexadecimal a bytes. Y con sponge es poner la infromacion en un arhcivo en especifico, en este caso a su propio archivo data|
|`ghex data`|Abre el editor hexadecimal, para editar datos binarios, para saber de binarios que representan al inicio se usa https://filesig.search.org/|
|`mv data data.gz`|Cambias de nombre al archivo añadiendole la extension .gz|

Referencia:

- Binarios search: https://filesig.search.org/

## SSH

|Comando|Descripción|
|---|---|
|`ping [atributos] [cuantos pings] [IP, pagina]`|Envia un ping para comprobar si se recibe señal|
|`ping -c 1 bandit.labs.overthewire.org`|Envia 1 ping a esa pagina|
|`ssh [user]@[IP/pagina web] -p [puerto]`|Activa el protocolo SSH para controlar una computadora de forma remota y que sea segura, usando un nombre de cuenta, mencionando la IP o pagina web y tambien especificas el puerto con -p|
|`ssh bandit0@bandit.labs.overthewire.org -p 2220`|Accedes a los laboratorios de bandit especificando tu usuario "bandit0" y conectandote con el puerto 2220|
|`sshpass -p [contraseña] ssh [usuario]@[IP/pagina web] -p [puerto]`|Para entrar poniendo la contraseña de una vez|
|`sshpass -p 'ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If' ssh bandit1@bandit.labs.overthewire.org -p 2220`|Entrar a la maquina poniendo la contraseña de una vez|
|`export TERM=xterm`|Necesario para importar configuraciones de tu terminal en la tuya como Control + l para limpieza|
|`systemctl start ssh`|Inicia el servicio ssh para que otras computadoras con la terminal puedan conectarse a la tuya|
|`systemctl status ssh`|Verifica la conecion con el ssh|
|`ssh fabca06@localhost`|Te conectas a tu propia maquina remotamente en tu maquina|
|`ssh key-gen`|Genera dos llaves para conectarse remotamente sin la necesidad de una contraseña, tanto privada como publica, este comando se uso en la carpeta /home/fabca06/pwd. La clave publica siempre tendra como extension .pub|
|`cp [archivo] authorized_keys`|Copia el archivo con la llave y ponlo en un archillo llamado authorized_keys, esto es importante ya que open-ssh busca todas las llaves autorizadas en esa carpeta|
|`cp id_ed25519.pub authorized_keys`|Ese archivo con mi llave publica se copio a authorized_keys, gracias a eso conectandome a mi propio maquina no me pidio contraseña|
|`ssh-copy-id -i id_ed25519 fabca06@localhost`|Esta es otra manera de autorizacion, especificando la maquina|
|`ssh -i id_ed25519 fabca06@localhost`|Ya conectandote remotamente sin contraseña, le pides a tu terminal que busques la llave necesario para autenticarse y se conecte por ende a la maquina|
|`systemctl stop ssh`|Recuerda cerrar el servicio ssh cuando no se use|
|`ssh -i /home/fabca06/.ssh/bandit14_key bandit14@bandit.labs.overthewire.org -p 2220`|Mismo comando, al archivo con la clave privada ubicado en bandit13 en Over the Wire se copia a tu maquina local, lo pones en un archivo adentro de .ssh y te conectas mencionando el nombre de tu archivo con la llave privada. IMPORTANTE: Todas las llaves privadas deben de disponer solo de chmod 600|
|`ssh bandit19@bandit.labs.overthewire.org -p 2220 [comando]`|Envia un comando despues de conectarse remotamente|
|`ssh bandit19@bandit.labs.overthewire.org -p 2220 bash`|Abre una bash despues de conectarte|
|`ip a`|La forma moderna y recomendada de ver tus interfaces de red e IPs (sustituto de ifconfig)|
|`curl [URL]`|Descarga o visualiza el contenido de una web desde la terminal. Muy útil para descargar scripts de explotación|
|`wget [URL]`|Similar a curl, ideal para descargar archivos directos|
|`scp [archivo] [user]@[IP]:[ruta]`|Copia archivos a través de SSH de tu máquina a una remota (o viceversa)|

## Puertos

|Comando|Descripción|
|---|---|
|`nc [ip] [puerto]`|Abres una conexión al puerto que quieras especificar|
|`nc localhost 3000`|Llama al puerto 3000 de tu maquina|
|`ss -nltp`|Mapeo de los puertos ver, para ver los servicios que estar corriento. -n No intenta resolver nombres de servicios; -l Muestra solo los que esten escuchando conexiones; -t solo conexiones TCP; -p que programa o proceso tiene abierta cada puerta|
|`lsof -i :[puerto]`|Que archivos servicios corren en el puerto especifico, los puertos propietarios de root no se muestran al menos que lo corras como root|
|`lsof -i:22`|Muestra los archivos o servicios que corren en el puerto 22|
|`ps -faux`|Muestra todos los puertos. -f los que estan escuchando; -a para todos los usuarios incluyendo root; -u da informacion detallada, como el usuario al que pertenece el proceso; -x solo procesos no vinculados a la terminal|
|`ncat --ssl [ip] [puerto]`|El nc pero con seguridad ssl, necesario en procesos de seguridad|
|`ncat --ssl 127.0.0.1 30001`|Inicia una conexión con ssl a esa ip y ese puerto|
|`nc -nlvp 4646`|Abre un puerto en tu misma maquina|

Referencia:

- Usando Netcat - Algunos comandos prácticos: https://blog.desdelinux.net/usando-netcat-algunos-comandos-practicos/

## Conexion de redes

|Comando|Descripción|
|---|---|
|`nmcli device wifi list`|Escanea las redes Wi-FI cercanas|
|`nmcli device wifi connect [nombre red] password [contraseña]`|Conectate a una red desde la terminal|
|`nmcli connection show`|Mira tus perfiles guardados|
|`nmcli connection ip [ID]`|Activa una conexión especifica|
|`nmcli connection down [ID]`|Desactiva una conexión especifica|

## Tareas Cron

Rangos válidos de cada campo:

|Minuto|Hora|Dia de mes|Mes|Dia de la semana|
|---|---|---|---|---|
|0-59|0-23|1-31|1-12|0-6|

Ejemplos:

|Minuto|Hora|Dia de mes|Mes|Dia de la semana|Comando|¿Cuando se ejecuta?|
|---|---|---|---|---|---|---|
|*|*|*|*|*|`/home/usuario/scripts/check_system.sh`|Cada minuto|
|0|*|*|*|*|`/usr/bin/python3 /home/scripts/limpiar_logs.py`|Cada hora exacto, puntual|
|0|0|*|*|*|`/usr/bin/rsync -a /var/www /respaldos/`|Cada dia comenzando (medianoche)|
|30|3|*|*|0|`/usr/sbin/service mysql restart`|Cada domingo a las 3:30am|
|*/15|*|*|*|*|`/home/scripts/monitor.sh`|Cada 15 minutos|
|0|8|*|*|1-5|`home/scripts/reporte_diario.sh`|De lunes a viernes a las 8:00am|
|0|12|25|12|*|`/home/scripts/feliz_navidad.sh`|Solo en navidad|
|0|6,18|*|*|*|`/home/scripts/sync_data.sh`|2 veces al dia, 6:00am y 6:00pm|
|`@reboot`|||||`/home/scripts/start_bot.sh`|Cuando se enciende el equipo|
|`@daily`|||||`/home/scripts/start_bot.sh`|Todos los dias|
|`@hourly`|||||`/home/scripts/start_bot.sh`|Todas las horas|

Referencia:

- https://blog.desdelinux.net/cron-crontab-explicados/

## GitHub

|Comando|Descripción|
|---|---|
|`git clone [link]`|Clona un repositorio de GitHub|
|`git clone ssh://bandit27-git@bandit.labs.overthewire.org:2220/home/bandit27-git/repo;`|Clona ese repositorio|
|`git log`|Mira todos los commits del proyecto|
|`git show [id commit]`|Mira todos los cambios que se le hicieron a un commit especifico|
|`git show b0354c7be30f500854c5fc971c57e9cbe632fef6`|Mira todos los cambios hechos a ese commit|
|`git branch`|Muestra la rama actual en la que estas|
|`git branch -a`|Muestra lista detallada de las ramas de un repositorio|
|`git checkout [rama]`|Cambia de rama a la que indiques|
|`git checkout dev`|Cambiar de rama al nombre de dev|
|`git tag`|Muestra los tags del repositorio|
|`git show [tag]`|Mostrar un tag|
|`git show secret`|Mostrar el tag secret|
|`git add -f [archivo/directorio]`|Añade archivos/directorios al repositorio|
|`git add -f key.txt`|Añade el archivo key.txt al repositorio|
|`git commit -m [mensaje]`|Realiza un commit en el repositorio|
|`git commit -m "Creamos un nuevo archivo"`|Realiza un commit en el repositorio con un mensaje|

Cómo poner una carpeta en especifico de un repositorio:

```
# 1. Limpia el origen que quedó mal configurado
git remote remove origin
# 2. Vincula la URL del repositorio raíz (Esta es la correcta para Git)
git remote add -f origin https://github.com/vulhub/vulhub.git
# 3. Activa la función de descarga parcial (si no lo habías hecho)
git config core.sparseCheckout true
# 4. Aquí es donde SÍ va la ruta de la subcarpeta que quieres
echo "samba/CVE-2017-7494" >> .git/info/sparse-checkout
# 5. Descarga finalmente tu laboratorio
git pull origin master
```

## Compresión y Descompresión

|Comando|Descripción|
|---|---|
|`tar -cvf archivo.tar [carpeta]`|Crea un archivo empaquetado (c = create)|
|`tar -xvf archivo.tar`|Extrae un archivo tar (x = extract)|
|`unzip archivo.zip`|Descomprime archivos .zip|
|`gzip -d archivo.gz`|Descomprime archivos .gz|
|`sudo mount -t cifs //127.0.0.1/myshare /mnt/datos_USB/montaje_labs`|Monta una carpeta compartida en tu equipo de un contenedor o USB, con -t señalado el tipo de sistema de archivos, y ya despues se pone la ruta|
|`unmount /mnt/datos_USB/montaje_labs`|Desmonta la carpeta compartida|
|`sudo mount -t cifs //127.0.0.1/myshare /mnt/datos_USB/montaje_labs -o username=null,password=null,domain=,rw`|Monta una carpeta compartida especificando usuario, contraseña, dominio y permisos de lectura/escritura|

## Control de energia y Sesion

|Comando|Descripción|
|---|---|
|`poweroff`|Apaga el sistema|
|`reboot`|Reinicia el sistema|
|`shutdown -h +30`|Programa el apagado en 30 minutos|
|`shutdown -c`|Cancela un apagado programado|
|`systemctl suspend`|Suspende el equipo|
|`loginctl terminate-user $USER`|Forma de hacer logout en sistemas modernos|

## Bluetoothctl

|Comando|Descripción|
|---|---|
|`bluetoothctl`|Entra al programa|
|`bluetoothctl power on`|Enciende el adaptador|
|`bluetoothctl power off`|Apaga el adaptador|
|`bluetoothctl scan on`|Empieza a buscar dispositivos|
|`bluetoothctl scan off`|Deja de buscar dispositivos|
|`bluetoothctl pair [MAC]`|Vincula un dispositivo|
|`bluetoothctl remove [MAC]`|Desvincula un dispositivo|
|`bluetoothctl connect [MAC]`|Conecta un dispositivo|
|`bluetoothctl disconnect [MAC]`|Desconecta un dispositivo|
|`bluetoothctl trust [MAC]`|Confia en un dispositivo|

## Informacion del sistema

|Comando|Descripción|
|---|---|
|`neofetch`/`fastfetch`|El clásico comando para ver el logo de tu distro y specs del PC (muy usado en r/unixporn)|
|`df -h`|Muestra cuánto espacio libre queda en tus discos en formato "humano" (GB, MB)|
|`free -h`|Muestra cuánta memoria RAM estás usando realmente|
|`lsblk`|Muestra tus particiones y discos duros como un "árbol"|
|`alias [nombre]='[comando]'`|Crea tus propios comandos cortos|
|`history`|Muestra todos los comandos que has escrito antes (por si olvidaste uno muy largo)|

## Gestion de historial

|Comando|Descripción|
|---|---|
|`!!`|Repite el ultimo comando|
|`!n`|Repite el comando numero n del historial|
|`fc`|Abre el ultimo|
|`history -c`|Limpia el historial de la sesión actual (por si escribiste una contraseña por error)|
|`history -w`|Fuerza el guardado de los comandos actuales al archivo de historial|