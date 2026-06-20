# Direcciones IP

Etiquetas: #hacking/teoria/redes #hacking/teoria/tcp-ip #hacking/teoria/modelo-osi #hacking/teoria/subnetting #hacking/auditoria/seguridad-informatica #hacking/herramientas/burpsuite #hacking/tecnica/payloads

Las direcciones IP son identificadores numéricos únicos que se utilizan para identificar dispositivos en una red, como ordenadores, routers, servidores y otros dispositivos conectados a Internet.

Existen dos versiones de direcciones IP: IPv4 e IPv6. La versión IPv4 utiliza un formato de dirección de 32 bits y se utiliza actualmente en la mayoría de las redes. La versión IPv6 utiliza un formato de dirección de 128 bits y se está implementando gradualmente en todo el mundo para hacer frente a la escasez de direcciones IPv4.

Las direcciones IPv4 se representan como cuatro números separados por puntos, como 192.168.0.1, mientras que las direcciones IPv6 se representan en notación hexadecimal y se separan por dos puntos, como 2001:0db8:85a3:0000:0000:8a2e:0370:7334.


## Direcciones MAC (OUI y NIC)

La dirección MAC es un número hexadecimal de 12 dígitos (número binario de 6 bytes), que está representado principalmente por notación hexadecimal de dos puntos.

Los primeros 6 dígitos (digamos 00:40:96) del MAC Address identifican al fabricante, llamado OUI (Identificador Único Organizacional). El Comité de la Autoridad de Registro de IEEE asigna estos prefijos MAC a sus proveedores registrados.

Los seis dígitos más a la derecha representan el controlador de interfaz de red, que es asignado por el fabricante.

Es decir, los primeros 3 bytes (24 bits) representan el fabricante de la tarjeta, y los últimos 3 bytes (24 bits) identifican la tarjeta particular de ese fabricante. Cada grupo de 3 bytes se puede representar con 6 dígitos hexadecimales, formando un número hexadecimal de 12 dígitos que representa la MAC completa.

Para una búsqueda de fabricante utilizando direcciones MAC, se requieren al menos los primeros 3 bytes (6 caracteres) de la dirección MAC. Una de las herramientas que vemos en esta clase para lograr dicho fin es 'macchanger', una herramienta de GNU/Linux para la visualización y manipulación de direcciones MAC.


## Protocolos comunes (UDP, TCP) y el famoso Three-Way Handshake

Los protocolos TCP (Transmission Control Protocol) y UDP (User Datagram Protocol) son dos de los protocolos de red más comunes utilizados en la transferencia de datos a través de redes de ordenadores.

El protocolo TCP, es un protocolo orientado a la conexión que proporciona una entrega de datos confiable, mientras que el protocolo UDP, es un protocolo no orientado a conexión el cual no garantiza la entrega de datos.

Una parte crucial del protocolo TCP es el Three-Way Handshake, un procedimiento utilizado para establecer una conexión entre dos dispositivos. Este procedimiento consta de tres pasos: SYN, SYN-ACK y ACK, en los que se sincronizan los números de secuencia y de reconocimiento de los paquetes entre los dispositivos. El Three-Way Handshake es fundamental para establecer una conexión confiable y segura a través de TCP.

Puertos TCP comunes:

21: FTP (File Transfer Protocol) - permite la transferencia de archivos entre sistemas.

22: SSH (Secure Shell) - un protocolo de red seguro que permite a los usuarios conectarse y administrar sistemas de forma remota.

23: Telnet - un protocolo utilizado para la conexión remota a dispositivos de red.

80: HTTP (Hypertext Transfer Protocol) - el protocolo que se utiliza para la transferencia de datos en la World Wide Web.

443: HTTPS (Hypertext Transfer Protocol Secure) - la versión segura de HTTP, que utiliza encriptación SSL/TLS para proteger las comunicaciones web.

Puertos UDP comunes:

53: DNS (Domain Name System) - un sistema que traduce nombres de dominio en direcciones IP.

67/68: DHCP (Dynamic Host Configuration Protocol) - un protocolo utilizado para asignar direcciones IP y otros parámetros de configuración a los dispositivos en una red.

69: TFTP (Trivial File Transfer Protocol) - un protocolo simple utilizado para transferir archivos entre dispositivos en una red.

123: NTP (Network Time Protocol) - un protocolo utilizado para sincronizar los relojes de los dispositivos en una red.

161: SNMP (Simple Network Management Protocol) - un protocolo utilizado para administrar y supervisar dispositivos en una red.

Cabe destacar que estos son solo algunos de los más comunes. Existen muchos más puertos los cuales operan tanto por TCP como por UDP.


## Modelo OSI

En redes de ordenadores, el modelo OSI (Open Systems Interconnection) es una estructura de siete capas que se utiliza para describir el proceso de comunicación entre dispositivos. Cada capa proporciona servicios y funciones específicas, que permiten a los dispositivos comunicarse a través de la red.

A continuación, se describen brevemente las siete capas del modelo OSI:

Capa física: Es la capa más baja del modelo OSI, que se encarga de la transmisión de datos a través del medio físico de la red, como cables de cobre o fibra óptica.

Capa de enlace de datos: Esta capa se encarga de la transferencia confiable de datos entre dispositivos en la misma red. También proporciona funciones para la detección y corrección de errores en los datos transmitidos.

Capa de red: La capa de red se ocupa del enrutamiento de paquetes de datos a través de múltiples redes. Esta capa utiliza direcciones lógicas, como direcciones IP, para identificar dispositivos y rutas de red.

Capa de transporte: La capa de transporte se encarga de la entrega confiable de datos entre dispositivos finales, proporcionando servicios como el control de flujo y la corrección de errores.

Capa de sesión: Esta capa se encarga de establecer y mantener las sesiones de comunicación entre dispositivos. También proporciona servicios de gestión de sesiones, como la autenticación y la autorización.

Capa de presentación: La capa de presentación se encarga de la representación de datos, proporcionando funciones como la codificación y decodificación de datos, la compresión y el cifrado.

Capa de aplicación: La capa de aplicación proporciona servicios para aplicaciones de usuario finales, como correo electrónico, navegadores web y transferencia de archivos.

Comprender la estructura en capas del modelo OSI es esencial para cualquier analista de seguridad, ya que permite tener una visión completa del funcionamiento de la red y de las posibles vulnerabilidades que puedan existir en cada una de las capas.

Esto nos permite identificar de manera efectiva los puntos débiles de la red y aplicar medidas de seguridad adecuadas para protegerla de posibles ataques.


## Subnetting

Subnetting es una técnica utilizada para dividir una red IP en subredes más pequeñas y manejables. Esto se logra mediante el uso de máscaras de red, que permiten definir qué bits de la dirección IP corresponden a la red y cuáles a los hosts.

Para interpretar una máscara de red, se deben identificar los bits que están en "1". Estos bits representan la porción de la dirección IP que corresponde a la red. Por ejemplo, una máscara de red de 255.255.255.0 indica que los primeros tres octetos de la dirección IP corresponden a la red, mientras que el último octeto se utiliza para identificar los hosts.

Ahora bien, cuando hablamos de CIDR (acrónimo de Classless Inter-Domain Routing), a lo que nos referimos es a un método de asignación de direcciones IP más eficiente y flexible que el uso de clases de redes IP fijas. Con CIDR, una dirección IP se representa mediante una dirección IP base y una máscara de red, que se escriben juntas separadas por una barra (/).

Por ejemplo, la dirección IP 192.168.1.1 con una máscara de red de 255.255.255.0 se escribiría como 192.168.1.1/24.

La máscara de red se representa en notación de prefijo, que indica el número de bits que están en "1" en la máscara. En este caso, la máscara de red 255.255.255.0 tiene 24 bits en "1" (los primeros tres octetos), por lo que su notación de prefijo es /24.

Para calcular la máscara de red a partir de una notación de prefijo, se deben escribir los bits "1" en los primeros bits de una dirección IP de 32 bits y los bits "0" en los bits restantes. Por ejemplo, la máscara de red /24 se calcularía como 11111111.11111111.11111111.00000000 en binario, lo que equivale a 255.255.255.0 en decimal.

En cuanto a clases de direcciones IP, existen tres tipos de máscaras de red: Clase A, Clase B y Clase C.

Las redes de clase A usan una máscara de subred predeterminada de 255.0.0.0 y tienen de 0 a 127 como su primer octeto. La dirección 10.52.36.11, por ejemplo, es una dirección de clase A. Su primer octeto es 10, que está entre 1 y 126, ambos incluidos.

Las redes de clase B usan una máscara de subred predeterminada de 255.255.0.0 y tienen de 128 a 191 como su primer octeto. La dirección 172.16.52.63, por ejemplo, es una dirección de clase B. Su primer octeto es 172, que está entre 128 y 191, ambos inclusive.

Las redes de clase C usan una máscara de subred predeterminada de 255.255.255.0 y tienen de 192 a 223 como su primer octeto. La dirección 192.168.123.132, por ejemplo, es una dirección de clase C. Su primer octeto es 192, que está entre 192 y 223, ambos incluidos.

Es importante tener en cuenta que, además de estos tres tipos de máscaras de red, también existen máscaras de red personalizadas que se pueden utilizar para crear subredes de diferentes tamaños dentro de una red.

Tal y como mencionamos en la descripción de la clase anterior sobre los CIDRs (Classless Inter-Domain Routing), se trata de un método de asignación de direcciones IP que permite dividir una dirección IP en una parte que identifica la red y otra parte que identifica el host. Esto se logra mediante el uso de una máscara de red, que se representa en notación CIDR como una dirección IP base seguida de un número que indica la cantidad de bits que corresponden a la red.

Con CIDR, se pueden asignar direcciones IP de forma más precisa, lo que reduce la cantidad de direcciones IP desperdiciadas y facilita la administración de la red.

El número que sigue a la dirección IP base en la notación CIDR se llama prefijo o longitud de prefijo, y representa el número de bits en la máscara de red que están en "1".

Por ejemplo, una dirección IP con un prefijo de /24 indica que los primeros 24 bits de la dirección IP corresponden a la red, mientras que los 8 bits restantes se utilizan para identificar los hosts.

Para calcular la cantidad de hosts disponibles en una red CIDR, se deben contar el número de bits "0" en la máscara de red y elevar 2 a la potencia de ese número. Esto se debe a que cada bit "0" en la máscara de red representa un bit que se puede utilizar para identificar un host.

Por ejemplo, una máscara de red de 255.255.255.0 (/24) tiene 8 bits en "0", lo que significa que hay 2^8 = 256 direcciones IP disponibles para los hosts en esa red.

A continuación, se representan algunos ejemplos prácticos de CIDR:

Una dirección IP con un prefijo de /28 (255.255.255.240) permite hasta 16 direcciones IP para los hosts (2^4), ya que los primeros 28 bits corresponden a la red.

Una dirección IP con un prefijo de /26 (255.255.255.192) permite hasta 64 direcciones IP para los hosts (2^6), ya que los primeros 26 bits corresponden a la red.

Una dirección IP con un prefijo de /22 (255.255.252.0) permite hasta 1024 direcciones IP para los hosts (2^10), ya que los primeros 22 bits corresponden a la red.


## 5.1 SUBNETING, CALCULO IP 192.168.1.0/26

Explicamos cómo calcular para la dirección IP 192.168.1.0/26, su máscara de red, el número total de hosts a repartir, el identificador de red y la dirección Broadcast.

A continuación, se detalla paso a paso cómo hemos ido calculando cada apartado:

Cálculo de la máscara de red:

La dirección IP que se nos dio es 192.168.1.0/26, lo que significa que los primeros 26 bits de la dirección IP corresponden a la red y los últimos 6 bits corresponden a los hosts.

Para calcular la máscara de red, necesitamos colocar los primeros 26 bits en 1 y los últimos 6 bits en 0. En binario, esto se ve así:

11111111.11111111.11111111.11000000

Cada octeto de la máscara de red se compone de 8 bits. El valor de cada octeto se determina convirtiendo los 8 bits a decimal. En este caso, los primeros 24 bits son todos 1s, lo que significa que el valor decimal de cada uno de estos octetos es 255. El último octeto tiene los últimos 6 bits en 0, lo que significa que su valor decimal es 192.

Por lo tanto, la máscara de red para esta dirección IP es 255.255.255.192.

Cálculo del total de hosts a repartir:

En este caso, se pueden utilizar los 6 bits que quedan disponibles para representar la parte de host. En una máscara de red de 26 bits, los 6 bits restantes representan 2^6 - 2 = 62 hosts disponibles para asignar.

El número máximo de hosts disponibles se calcula como 2^(n) - 2, donde n es la cantidad de bits utilizados para representar la parte de host en la máscara de red.

Cálculo del Network ID:

Para calcular el Network ID, lo que debemos hacer es aplicar la máscara de red a la dirección IP de la red. En este caso, la máscara de red es 255.255.255.192, lo que significa que los primeros 26 bits de la dirección IP pertenecen a la parte de red.

Para calcular el Network ID, convertimos tanto la dirección IP como la máscara de red en binario y luego hacemos una operación "AND" lógica entre los dos. La operación "AND" compara los bits correspondientes en ambas direcciones y devuelve un resultado en el que todos los bits coincidentes son iguales a "1" y todos los bits no coincidentes son iguales a "0".

En este caso, la dirección IP es 192.168.1.0 en decimal y se convierte en binario como 11000000.10101000.00000001.00000000. La máscara de red es 255.255.255.192 en decimal y se convierte en binario como 11111111.11111111.11111111.11000000.

Luego, aplicamos la operación "AND" entre estos dos valores binarios bit a bit. Los bits correspondientes en ambos valores se comparan de la siguiente manera:

El resultado final es el Network ID, que es 192.168.1.0. Este es el identificador único de la subred a la que pertenecen los hosts.

Cálculo de la Broadcast Address:

La Broadcast Address es la dirección de red que se utiliza para enviar paquetes a todos los hosts de la subred. Para calcularla, necesitamos saber el Network ID y la cantidad de hosts disponibles en la subred.

En el ejemplo que estamos trabajando, ya hemos calculado el Network ID como 192.168.1.0. La cantidad de hosts disponibles se calcula como 2^(n) - 2, donde n es la cantidad de bits utilizados para representar la parte de host en la máscara de red. En este caso, n es igual a 6, ya que hay 6 bits disponibles para la parte de host.

Para calcular la Broadcast Address, debemos asignar todos los bits de la parte del host de la dirección IP a "1". En este caso, la dirección IP es 192.168.1.0 y se convierte en binario como 11000000.10101000.00000001.00000000.

Para encontrar la dirección Broadcast, llenamos con unos la parte correspondiente a los bits de host, es decir, los últimos 6 bits:

11000000.10101000.00000001.00111111 (dirección IP con bits de host asignados a "1")

Luego, convertimos este valor binario de regreso a decimal y obtenemos la dirección de Broadcast: 192.168.1.63. Esta es la dirección a la que se enviarán los paquetes para llegar a todos los hosts de la subred.


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


## Shells

Reverse Shell: Es una técnica que permite a un atacante conectarse a una máquina remota desde una máquina de su propiedad. Es decir, se establece una conexión desde la máquina comprometida hacia la máquina del atacante. Esto se logra ejecutando un programa malicioso o una instrucción específica en la máquina remota que establece la conexión de vuelta hacia la máquina del atacante, permitiéndole tomar el control de la máquina remota.

Bind Shell: Esta técnica es el opuesto de la Reverse Shell, ya que en lugar de que la máquina comprometida se conecte a la máquina del atacante, es el atacante quien se conecta a la máquina comprometida. El atacante escucha en un puerto determinado y la máquina comprometida acepta la conexión entrante en ese puerto. El atacante luego tiene acceso por consola a la máquina comprometida, lo que le permite tomar el control de la misma.

Forward Shell: Esta técnica se utiliza cuando no se pueden establecer conexiones Reverse o Bind debido a reglas de Firewall implementadas en la red. Se logra mediante el uso de mkfifo, que crea un archivo FIFO (named pipe), que se utiliza como una especie de "consola simulada" interactiva a través de la cual el atacante puede operar en la máquina remota. En lugar de establecer una conexión directa, el atacante redirige el tráfico a través del archivo FIFO, lo que permite la comunicación bidireccional con la máquina remota.


## Payloads

Payload Staged: Es un tipo de payload que se divide en dos o más etapas. La primera etapa es una pequeña parte del código que se envía al objetivo, cuyo propósito es establecer una conexión segura entre el atacante y la máquina objetivo. Una vez que se establece la conexión, el atacante envía la segunda etapa del payload, que es la carga útil real del ataque. Este enfoque permite a los atacantes sortear medidas de seguridad adicionales, ya que la carga útil real no se envía hasta que se establece una conexión segura.

Payload Non-Staged: Es un tipo de payload que se envía como una sola entidad y no se divide en múltiples etapas. La carga útil completa se envía al objetivo en un solo paquete y se ejecuta inmediatamente después de ser recibida. Este enfoque es más simple que el Payload Staged, pero también es más fácil de detectar por los sistemas de seguridad, ya que se envía todo el código malicioso de una sola vez.


## BurpSuite

BurpSuite es una herramienta de prueba de penetración utilizada para encontrar vulnerabilidades de seguridad en aplicaciones web. Es una de las herramientas de prueba de penetración más populares y utilizadas en la industria de la seguridad informática. BurpSuite se compone de varias herramientas diferentes que se pueden utilizar juntas para identificar vulnerabilidades en una aplicación web.

Las principales herramientas que componen BurpSuite son las siguientes:

Proxy: Es la herramienta principal de BurpSuite y actúa como un intermediario entre el navegador web y el servidor web. Esto permite a los usuarios interceptar y modificar las solicitudes y respuestas HTTP y HTTPS enviadas entre el navegador y el servidor. El Proxy también es útil para la identificación de vulnerabilidades, ya que permite a los usuarios examinar el tráfico y analizar las solicitudes y respuestas.

Scanner: Es una herramienta de prueba de vulnerabilidades automatizada que se utiliza para identificar vulnerabilidades en aplicaciones web. El Scanner utiliza técnicas de exploración avanzadas para detectar vulnerabilidades en la aplicación web, como inyecciones SQL, cross-site scripting (XSS), vulnerabilidades de seguridad de la capa de aplicación (OSWAP Top 10) y más.

Repeater: Es una herramienta que permite a los usuarios reenviar y repetir solicitudes HTTP y HTTPS. Esto es útil para probar diferentes entradas y verificar la respuesta del servidor. También es útil para la identificación de vulnerabilidades, ya que permite a los usuarios probar diferentes valores y detectar respuestas inesperadas.

Intruder: Es una herramienta que se utiliza para automatizar ataques de fuerza bruta. Los usuarios pueden definir diferentes payloads para diferentes partes de la solicitud, como la URL, el cuerpo de la solicitud y las cabeceras. Posteriormente, Intruder automatiza la ejecución de las solicitudes utilizando diferentes payloads y los usuarios pueden examinar las respuestas para identificar vulnerabilidades.

Comparer: Es una herramienta que se utiliza para comparar dos solicitudes HTTP o HTTPS. Esto es útil para detectar diferencias entre las solicitudes y respuestas y analizar la seguridad de la aplicación.

Se trata de una herramienta extremadamente potente, la cual puede ser utilizada para identificar una amplia variedad de vulnerabilidades de seguridad en aplicaciones web. Al utilizar las diferentes herramientas que componen BurpSuite, los usuarios pueden identificar vulnerabilidades de forma automatizada o manual, según sus necesidades. Esto permite a los usuarios encontrar vulnerabilidades y corregirlas antes de que sean explotadas por un atacante.

En resumen, Burp Suite es una herramienta imprescindible para cualquier profesional de seguridad informática que busque asegurar la seguridad de aplicaciones web. En la siguiente sección, tendremos la oportunidad de utilizar BurpSuite en detalle y sacarle el máximo provecho a esta herramienta.


## Enlaces Webs

HackerOne (Plataforma de Bug Bounty y seguridad ofensiva donde empresas contratan a hackers éticos para encontrar vulnerabilidades).

Hunter.io (Buscador de correos electrónicos corporativos y verificación de dominios para encontrar contactos comerciales).

Intelligence X (Motor de búsqueda y archivo que permite encontrar datos filtrados en la Deep Web, brechas de seguridad y registros históricos de internet).

Phonebook.cz (Herramienta de búsqueda que extrae listados de subdominios, correos electrónicos y URLs de una base de datos masiva de dominios).

Clearbit Connect (Extensión que permite encontrar correos electrónicos directos de empleados de cualquier empresa directamente desde Gmail o el navegador).

Buscador por imagen web: https://pimeyes.com/en

DeHashed Informacion de dominios (correos, contraseñas hasheadas, dirrecciones, etc.): https://www.dehashed.com/

Whatweb (Tecnologias de pagina web) : https://github.com/urbanadventurer/WhatWeb

Wappalyzer (Tecnologias de pagina web): https://addons.mozilla.org/es/firefox/addon/wappalyzer/

Builtwith (Historial de herramientas de una pagina web): https://builtwith.com/

Pentest-tools (Google Hacking, filtradores de busqueda para busquedas de hacking especificas) https://pentest-tools.com/information-gathering/google-hacking

Exploit-DB (Base de datos de vulnerabilidades): https://www.exploit-db.com/

Lista valores por defecto del TTLhttps://subinsb.com/default-device-ttl-values/

Enciclopedia de hacking: https://hacktricks.wiki/en/index.html

GTFOBins (Lista de comandos para invocar shell o ser root) https://gtfobins.org/
