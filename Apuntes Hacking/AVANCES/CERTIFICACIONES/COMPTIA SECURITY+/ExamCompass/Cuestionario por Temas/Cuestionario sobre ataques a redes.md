---
tags:
  - "formato/apunte"
  - "hacking/fundamental"
  - "examen/test-especifico"
  - "gestion/estado/terminado"
---
Este apunte contiene el análisis detallado del cuarto bloque del cuestionario temático sobre comunicaciones, protocolos y ataques de red de la plataforma ExamCompass para la certificación CompTIA Security+ (SY0-701), alineado con las respuestas oficiales del simulador.

---

## Pregunta 1: Arquitectura de Ataques DDoS y Botnets

### English Version
Unlike simple DoS attacks, which are typically launched from a single system, a DDoS attack uses multiple compromised computer systems to target its victim. The intermediate systems serving as the attack platform (often referred to as zombies, and collectively as a botnet) are the secondary victims of the DDoS attack.
* [✅] **True**
* [ ] False

### Versión en Español
A diferencia de los ataques DoS simples, que generalmente se realizan desde un solo sistema, un ataque DDoS utiliza múltiples sistemas informáticos comprometidos para atacar a su objetivo. Los sistemas intermedios que sirven de plataforma para el ataque (a menudo denominados zombis y, en conjunto, botnet) son las víctimas secundarias del ataque DDoS.
* [✅] **Verdadero**
* [ ] Falso

### 1. Explicación General
Los ataques de Denegación de Servicio Distribuido (DDoS) aprovechan la fuerza numérica. El atacante principal no interactúa directamente con la víctima; en su lugar, toma el control de miles de dispositivos vulnerables en internet (los "zombis") mediante malware, conformando una red de bots (botnet) para que lancen el tráfico simultáneamente bajo sus órdenes.

### 2. ¿Por qué es la correcta y no el resto?
Es **Verdadero** porque los dueños de los dispositivos de la botnet no son conscientes de que sus sistemas están siendo explotados para atacar a un tercero, convirtiéndolos formalmente en víctimas secundarias de la intrusión.

### 3. Clave para el Examen SY0-701
En Security+, una red de sistemas bajo el control de un servidor de Comando y Control (C2) se define como una Botnet, y cada nodo infectado de forma individual se denomina Zombie o Bot.

---

## Pregunta 2: Mecánica de los Ataques DDoS Amplificados

### English Version
A type of DDoS attack where an attacker exploits vulnerabilities in certain services or protocols to generate responses much larger than the original request is called:
* [✅] **Amplified DDoS attack**
* [ ] Volumetric DDoS attack
* [ ] Reflected DDoS attack
* [ ] Application DDoS attack

### Versión en Español
Un tipo de ataque DDoS en el que un atacante explota vulnerabilidades en ciertos servicios o protocolos para generar respuestas mucho mayores que la solicitud original se denomina:
* [✅] **Ataque DDoS amplificado (Amplified DDoS attack)**
* [ ] Ataque DDoS volumétrico (Volumetric DDoS attack)
* [ ] Ataque DDoS reflejado (Reflected DDoS attack)
* [ ] Ataque DDoS a la aplicación (Application DDoS attack)

### 1. Explicación General
La amplificación es un factor multiplicador. El atacante envía una solicitud pequeña a un servicio abierto (como NTP, Memcached o DNS) y este responde con un volumen de datos masivo. Si el atacante falsifica la IP de origen, el flujo gigante de datos golpea a la víctima.

### 2. ¿Por qué es la correcta y no el resto?
**Ataque DDoS amplificado** es la respuesta correcta porque el enunciado se centra explícitamente en el desequilibrio de tamaño entre la solicitud y la respuesta ("respuestas mucho mayores"). *Reflejado* describe el acto de rebotar el tráfico en un tercero, pero no necesariamente implica que la respuesta sea de mayor tamaño (aunque suelen combinarse). *Volumétrico* es una categoría general de saturación de ancho de banda. *A la aplicación* se enfoca en agotar recursos de servidores web (capa 7 del modelo OSI).

### 3. Clave para el Examen SY0-701
La clave para identificar la Amplificación en el examen es la relación de tamaño (ej. enviar una petición de 60 bytes y generar una respuesta de 3000 bytes hacia la víctima).

---

## Pregunta 3: Mecánica de los Ataques DDoS Reflejados

### English Version
What defines a reflected DDoS attack?
* [ ] Overwhelming the target with high volume of traffic to saturate its bandwidth.
* [ ] Exploiting vulnerabilities in network protocols to consume resources and disrupt services.
* [✅] **Utilizing third-party servers to bounce and amplify the attack traffic toward the target**
* [ ] Targeting vulnerabilities in applications or web servers to exhaust resources.

### Versión en Español
¿Qué define un ataque DDoS reflejado?
* [ ] Abrumar al objetivo con un alto volumen de tráfico para saturar su ancho de banda.
* [ ] Explotar vulnerabilidades en los protocolos de red para consumir recursos e interrumpir servicios.
* [✅] **Utilizar servidores de terceros para reflejar y amplificar el tráfico de ataque hacia el objetivo**
* [ ] Atacar vulnerabilidades en aplicaciones o servidores web para agotar los recursos.

### 1. Explicación General
En un ataque reflejado (Reflected), el atacante nunca envía paquetes directamente a la dirección IP de la víctima. En su lugar, envía paquetes a servidores intermedios legítimos en internet (reflectores) falsificando la IP de origen (IP spoofing) para que parezca que provienen de la víctima. Los reflectores le responden a la víctima, abrumándola.

### 2. ¿Por qué es la correcta y no el resto?
La opción que menciona **utilizar servidores de terceros para reflejar y amplificar** es la correcta porque describe el desvío indirecto del tráfico a través de intermediarios. Las otras opciones describen inundaciones volumétricas directas o ataques de agotamiento de recursos de capa de aplicación, pero no el mecanismo de rebote.

### 3. Clave para el Examen SY0-701
Para que ocurra un ataque reflejado, el protocolo utilizado debe basarse en UDP, ya que UDP no requiere un acuerdo de tres pasos (Three-way handshake) y permite falsificar la IP de origen con facilidad.

---

## Pregunta 4: Ataques de Amplificación DNS

### English Version
A DNS amplification attack is a type of DDoS attack where an attacker sends a small, specially crafted DNS query containing a spoofed IP address (the victim's IP) to a compromised DNS server. Upon receiving the query, the DNS server generates a much larger response packet, which is then sent to the victim's IP address, potentially causing disruption due to excessive traffic.  
* [✅] **True**
* [ ] False

### Versión en Español
Un ataque de amplificación de DNS es un tipo de ataque DDoS en el que un atacante envía una consulta DNS pequeña y especialmente diseñada que contiene una dirección IP falsificada (la IP de la víctima) a un servidor DNS comprometido. Al recibir la consulta, el servidor DNS genera un paquete de respuesta mucho mayor, que luego se envía a la dirección IP de la víctima, lo que puede provocar interrupciones debido al tráfico excesivo.
* [✅] **Verdadero**
* [ ] Falso

### 1. Explicación General
Este es el ejemplo clásico de un ataque reflejado y amplificado. El atacante solicita registros DNS grandes (como registros tipo ANY o firmas de seguridad DNSSEC) utilizando la dirección IP de la víctima como remitente ficticio. Los servidores DNS (a menudo resolvedores abiertos públicos) envían la pesada respuesta a la víctima.

### 2. ¿Por qué es la correcta y no el resto?
Es **Verdadero** porque detalla de manera impecable el proceso técnico de suplantación de IP de origen combinado con la amplificación de las respuestas del protocolo DNS.

### 3. Clave para el Examen SY0-701
Mitigar la amplificación de DNS requiere que los administradores deshabiliten los resolvedores abiertos (open resolvers) en internet o implementen limitación de tasa de respuesta (Response Rate Limiting - RRL).

---

## Pregunta 5: Manipulación de la Resolución de Nombres (DNS Spoofing)

### English Version
Which of the answers listed below refers to a cyberattack technique that relies on providing false DNS information to a DNS resolver with the purpose of redirecting or manipulating domain name resolution to malicious IP addresses?
* [✅] **DNS spoofing**
* [ ] Credential stuffing
* [ ] URL hijacking
* [ ] Domain hijacking

### Versión en Español
¿Cuál de las respuestas que aparecen a continuación se refiere a una técnica de ciberataque que se basa en proporcionar información DNS falsa a un resolvedor DNS con el fin de redirigir o manipular la resolución de nombres de dominio a direcciones IP maliciosas?
* [✅] **Suplantación de DNS (DNS spoofing)**
* [ ] Relleno de credenciales (Credential stuffing)
* [ ] Secuestro de URL (URL hijacking)
* [ ] Secuestro de dominio (Domain hijacking)

### 1. Explicación General
La suplantación de DNS altera el mapa de carreteras de internet. Cuando el cliente pregunta por una dirección IP legítima (ej. banco.com), el atacante interviene o altera el flujo para entregar una IP maliciosa, enviando al usuario a un portal clonado para robar sus datos.

### 2. ¿Por qué es la correcta y no el resto?
**Suplantación de DNS (DNS Spoofing)** es el término general para alimentar a un cliente o resolvedor con respuestas de resolución falsas. *Relleno de credenciales* es el intento automatizado de autenticarse en cuentas usando bases de datos de contraseñas filtradas. *Secuestro de URL (o typosquatting)* explota errores de escritura del usuario al ingresar un dominio en el navegador. *Secuestro de dominio* implica robar el control de la cuenta de administración del dominio a nivel del registrador (ej. GoDaddy).

### 3. Clave para el Examen SY0-701
El mecanismo criptográfico diseñado para prevenir la suplantación de DNS garantizando la integridad de las respuestas DNS es DNSSEC.

---

## Pregunta 6: Envenenamiento de Caché DNS

### English Version
Which type of vulnerability constitutes an example of remapping a domain name to a malicious IP address?
* [ ] URL hijacking
* [✅] **DNS cache poisoning**
* [ ] Domain hijacking
* [ ] ARP poisoning

### Versión en Español
¿Qué tipo de vulnerabilidad constituye un ejemplo de reasignación de un nombre de dominio a una dirección IP maliciosa?
* [ ] Secuestro de URL (URL hijacking)
* [✅] **Envenenamiento de la caché DNS (DNS cache poisoning)**
* [ ] Secuestro de dominio (Domain hijacking)
* [ ] Envenenamiento por ARP (ARP poisoning)

### 1. Explicación General
El envenenamiento de caché DNS es una forma específica de DNS Spoofing. Consiste en introducir una entrada de resolución falsa directamente en la memoria temporal (caché) de un servidor DNS local o intermedio, provocando que todos los usuarios que consulten a ese servidor sean redirigidos al sitio malicioso de manera persistente hasta que la caché expire.

### 2. ¿Por qué es la correcta y no el resto?
**Envenenamiento de la caché DNS** es el ataque concreto que inyecta los registros modificados de manera persistente en el servidor. *Envenenamiento por ARP* asocia direcciones IP con direcciones MAC falsas a nivel de red local (capa 2), no tiene relación directa con nombres de dominio. *Secuestro de URL* y *Secuestro de dominio* no manipulan la caché de resolución del protocolo DNS.

### 3. Clave para el Examen SY0-701
Mientras que la suplantación de DNS es el concepto general de entregar datos DNS falsos, el Cache Poisoning es el ataque técnico que almacena de forma persistente esa falsificación en la memoria del servidor DNS local para afectar a múltiples usuarios a la vez.

---

## Pregunta 7: Secuestro de Nombres de Dominio (Domain Hijacking)

### English Version
When domain registrants lose control over their domain names due to unauthorized actions of third parties, they become victims of:
* [ ] Sybil attack
* [✅] **Domain hijacking**
* [ ] Typosquatting
* [ ] URL hijacking

### Versión en Español
Cuando los registrantes de dominios pierden el control sobre sus nombres de dominio debido a acciones ilícitas de terceros, se convierten en víctimas de:
* [ ] Ataque de Sybil (Sybil attack)
* [✅] **Secuestro de dominio (Domain hijacking)**
* [ ] Typosquatting
* [ ] Secuestro de URL (URL hijacking)

### 1. Explicación General
En este caso, el atacante no hackea el servidor DNS ni altera el tráfico; en su lugar, compromete la cuenta del administrador del dominio en el registrador de dominios (GoDaddy, Namecheap, etc.) mediante phishing, ingeniería social o robo de credenciales, y cambia el titular del dominio a su nombre.

### 2. ¿Por qué es la correcta y no el resto?
**Secuestro de dominio (Domain hijacking)** describe perfectamente la pérdida de propiedad administrativa del dominio. *Typosquatting* y *Secuestro de URL* se basan en registrar dominios con errores ortográficos similares a marcas conocidas para engañar a usuarios despistados. Un *Ataque de Sybil* es una amenaza contra sistemas distribuidos o redes P2P donde un solo actor crea múltiples identidades falsas para ganar influencia en la red.

### 3. Clave para el Examen SY0-701
Para mitigar el Domain Hijacking, las organizaciones deben habilitar la Autenticación de Múltiples Factores (MFA) en los portales de registro de dominios y activar la función de bloqueo de transferencia de dominios (Registrar Lock).

---

## Pregunta 8: Ataques Bluetooth: Robo de Datos (Bluesnarfing)

### English Version
The practice of gaining unauthorized access to a Bluetooth-enabled device is referred to as:
* [ ] Spoofing
* [ ] Bluejacking
* [ ] Smishing
* [✅] **Bluesnarfing**

### Versión en Español
La práctica de obtener acceso no autorizado a un dispositivo Bluetooth se conoce como:
* [ ] Suplantación de identidad (Spoofing)
* [ ] Bluejacking
* [ ] Smishing
* [✅] **Bluesnarfing**

### 1. Explicación General
El ecosistema de ataques Bluetooth tiene dos amenazas clásicas con nombres muy similares que suelen confundirse en el examen de certificación.

### 2. ¿Por qué es la correcta y no el resto?
**Bluesnarfing** es la respuesta correcta porque implica el robo de datos (contactos, mensajes de texto, fotos o correos) de forma no autorizada mediante el enlace Bluetooth. *Bluejacking* consiste únicamente en enviar mensajes no solicitados (como spam de texto o solicitudes de emparejamiento) al dispositivo de la víctima, pero sin acceder ni robar sus datos internos. *Smishing* es un ataque de phishing vía mensajes de texto (SMS).

### 3. Clave para el Examen SY0-701
Distíngalos con esta regla simple: Bluejacking = *Joking/Spam* (solo envía mensajes molestos); Bluesnarfing = *Snatching/Theft* (roba datos confidenciales del teléfono).

---

## Pregunta 9: Ataques de Disociación Inalámbrica

### English Version
A wireless disassociation attack is a type of: (Select 2 answers)
* [ ] Downgrade attack
* [✅] **Deauthentication attack**
* [ ] Brute-force attack
* [✅] **DoS attack**
* [ ] Cryptographic attack

### Versión en Español
Un ataque de disociación inalámbrica es un tipo de: (Seleccione 2 respuestas)
* [ ] Ataque de degradación (Downgrade attack)
* [✅] **Ataque de desautenticación (Deauthentication attack)**
* [ ] Ataque de fuerza bruta (Brute-force attack)
* [✅] **Ataque DoS (DoS attack)**
* [ ] Ataque criptográfico (Cryptographic attack)

### 1. Explicación General
En las redes Wi-Fi, un ataque de desasociación consiste en que un atacante transmite de forma inalámbrica tramas de desasociación o desautenticación falsificadas en formato de texto claro (aprovechando que no están cifradas en estándares antiguos), obligando al dispositivo de la víctima a desconectarse instantáneamente del Punto de Acceso (AP) legítimo.

### 2. ¿Por qué es la correcta y no el resto?
Es un **Ataque de desautenticación** porque interrumpe la sesión activa del cliente con el AP inalámbrico, y es un **Ataque DoS** porque le niega al usuario el servicio de conectividad a internet de manera continua. No es un ataque criptográfico porque no rompe algoritmos de cifrado, ni un ataque de degradación que intente forzar un cifrado más débil (como forzar el uso de WEP en lugar de WPA3).

### 3. Clave para el Examen SY0-701
Los atacantes usan ataques de Disasociación / Desautenticación para desconectar a una víctima e inmediatamente forzarla a reconectarse a un punto de acceso falso del atacante (Evil Twin) para capturar el acuerdo de enlace (Handshake). Se mitiga en redes modernas mediante Protected Management Frames (PMF / 802.11w).

---

## Pregunta 10: Ataque de Interferencia Inalámbrica (Jamming)

### English Version
A wireless jamming attack is a type of:
* [ ] Cryptographic attack
* [✅] **DoS attack**
* [ ] Brute-force attack
* [ ] Downgrade attack

### Versión en Español
Un ataque de interferencia inalámbrica es un tipo de:
* [ ] Ataque criptográfico
* [✅] **Ataque DoS**
* [ ] Ataque de fuerza bruta
* [ ] Ataque de degradación

### 1. Explicación General
La interferencia (Jamming) es un ataque a nivel físico (Capa 1 del modelo OSI) en el que un emisor de radio emite señales de ruido de alta potencia en la misma frecuencia de la red inalámbrica de la empresa (2.4 GHz o 5 GHz), imposibilitando la comunicación entre clientes y antenas.

### 2. ¿Por qué es la correcta y no el resto?
**Ataque DoS** es la correcta porque el ruido generado en el espectro electromagnético impide físicamente el intercambio de datos, denegando por completo el servicio inalámbrico. No tiene base criptográfica, lógica, ni de descifrado por fuerza bruta.

### 3. Clave para el Examen SY0-701
El Jamming es una denegación de servicio física. Si un sistema inalámbrico industrial de repente deja de comunicar y los analizadores de espectro muestran un ruido de radio inusualmente alto en los canales Wi-Fi, la red está bajo un ataque de interferencia.

---

## Pregunta 11: Debilidades Criptográficas en WEP (Ataques IV)

### English Version
Which wireless attack focuses on exploiting vulnerabilities found in WEP?
* [✅] **IV attack**
* [ ] War driving
* [ ] SSID spoofing
* [ ] Bluejacking

### Versión en Español
¿Qué ataque inalámbrico se centra en explotar las vulnerabilidades encontradas en WEP?
* [✅] **Ataque IV (IV attack)**
* [ ] Conducción de la guerra (War driving)
* [ ] Suplantación de SSID (SSID spoofing)
* [ ] Bluejacking

### 1. Explicación General
El estándar WEP (Wired Equivalent Privacy) utiliza un Vector de Inicialización (IV) de apenas 24 bits de longitud que se transmite en texto claro. Debido a este espacio de claves tan pequeño, en redes con tráfico activo los IVs se repiten rápidamente.

### 2. ¿Por qué es la correcta y no el resto?
**Ataque IV** es el método matemático y criptográfico diseñado para capturar estos vectores duplicados y descifrar la contraseña de la red Wi-Fi en cuestión de minutos. *War driving* es solo la práctica pasiva de conducir por una zona buscando redes inalámbricas abiertas. *Suplantación de SSID* y *Bluejacking* no atacan la criptografía de WEP.

### 3. Clave para el Examen SY0-701
WEP está completamente obsoleto. Si una pregunta del examen habla de la explotación matemática de un Vector de Inicialización reutilizado para extraer la clave de una red antigua, la respuesta es IV Attack.

---

## Pregunta 12: Características de un Ataque On-Path

### English Version
Which of the following statements can be used to describe the characteristics of an on-path attack? (Select all that apply)
* [✅] **An on-path attack is also known as a MITM attack**
* [✅] **Attackers place themselves in the communication path between two devices**
* [✅] **Attackers intercept or modify packets sent between two communicating devices**
* [ ] Attackers do not have access to packets exchanged during communication between two devices

### Versión en Español
¿Cuáles de las siguientes afirmaciones pueden usarse para describir las características de un ataque en ruta (On-path)? (Seleccione todas las que correspondan)
* [✅] **Un ataque en ruta también se conoce como ataque MITM (Man-in-the-Middle).**
* [✅] **Los atacantes se colocan en la ruta de comunicación entre dos dispositivos.**
* [✅] **Los atacantes interceptan o modifican los paquetes enviados entre dos dispositivos que se comunican.**
* [ ] Los atacantes no tienen acceso a los paquetes intercambiados durante la comunicación entre dos dispositivos.

### 1. Explicación General
En un ataque On-path (anteriormente conocido como Man-in-the-Middle o MITM), el adversario logra redirigir el tráfico de red de la víctima a través de su propia máquina antes de reenviarlo a la puerta de enlace predeterminada o servidor real.

### 2. ¿Por qué es la correcta y no el resto?
Las tres opciones marcadas con [✅] componen la definición integral de este ataque. El atacante intercepta, lee y tiene la capacidad técnica de modificar el tráfico sobre la marcha de manera transparente para ambas partes. Se descarta la última opción porque contradice por completo la naturaleza de la interceptación del ataque.

### 3. Clave para el Examen SY0-701
Los ataques On-path se logran frecuentemente en redes locales mediante ARP Spoofing/Poisoning. Para mitigarlos, se implementa inspección dinámica de ARP (Dynamic ARP Inspection - DAI).

---

## Pregunta 13: Ataques de Repetición (Replay Attacks)

### English Version
A network replay attack occurs when an attacker captures confidential user data and forwards it to the receiver with the intention of gaining unauthorized access or tricking the receiver into performing unauthorized operations.
* [✅] **True**
* [ ] False

### Versión en Español
Un ataque de repetición de red se produce cuando un atacante captura datos confidenciales del usuario y los reenvía al receptor con la intención de obtener acceso no autorizado o engañar al receptor para que realice operaciones no autorizadas.
* [✅] **Verdadero**
* [ ] Falso

### 1. Explicación General
En un ataque de repetición (Replay), el atacante no necesita descifrar la contraseña o el hash del usuario. Simplemente graba el tráfico de autenticación de red legítimo de la víctima y posteriormente lo transmite intacto al servidor para simular ser el usuario real y ganar acceso.

### 2. ¿Por qué es la correcta y no el resto?
Es **Verdadero** porque describe perfectamente el mecanismo de "captura y retransmisión diferida" de credenciales, hashes de autenticación o tokens sin alteración interna.

### 3. Clave para el Examen SY0-701
Los ataques de Replay se evitan implementando sellos de tiempo (Timestamps), números de secuencia de sesión únicos o desafíos aleatorios que expiran de inmediato (nonces).

---

## Pregunta 14: Estructura y Función de los IDs de Sesión

### English Version
What are the characteristics of a session ID? (Select 3 answers)
* [✅] **Normally stored on the server side**
* [✅] **A unique identifier assigned by the website to a specific user**
* [✅] **A piece of data that can be stored in a cookie or embedded as a URL parameter**
* [ ] Contains user authentication credentials, e.g. username and password.
* [ ] Normally stored on the client side (in the user's browser) instead of the server
* [ ] A unique identifier assigned to a server

### Versión en Español
¿Cuáles son las características de un ID de sesión (Session ID)? (Seleccione 3 respuestas)
* [✅] **Normalmente se almacena en el lado del servidor.**
* [✅] **Un identificador único asignado por el sitio web a un usuario específico.**
* [✅] **Un dato que se puede almacenar en una cookie o incrustar como parámetro de URL.**
* [ ] Contiene las credenciales de autenticación del usuario, por ejemplo, nombre de usuario y contraseña.
* [ ] Normalmente se almacena en el lado del cliente (en el navegador del usuario) en lugar de en el servidor.
* [ ] Un identificador único asignado a un servidor.

### 1. Explicación General
El protocolo HTTP no tiene estado (stateless). Para que un usuario no tenga que autenticarse en cada página que visita, el servidor web le asigna temporalmente un identificador único (ID de sesión) tras iniciar sesión con éxito.

### 2. ¿Por qué es la correcta y no el resto?
Un ID de sesión es un token temporal único asignado al usuario que viaja comúnmente en las cookies de HTTP o en la URL. El servidor debe mapear y guardar este ID en su propia base de datos temporal (normalmente almacenado en el lado del servidor) para validar la autenticidad del cliente. Se descartan las otras opciones porque un ID de sesión nunca debe contener las credenciales reales de texto plano del usuario. Tampoco se almacena exclusivamente en el navegador del cliente (el cliente solo conserva una copia temporal de referencia).

### 3. Clave para el Examen SY0-701
Si un atacante intercepta o roba tu Session ID, puede importarlo en su propio navegador y suplantar tu identidad activa en la aplicación sin conocer tu contraseña real. Esto se conoce como Secuestro de Sesión (Session Hijacking).

---

## Pregunta 15: Ataques de Repetición de Sesión (Session Hijacking)

### English Version
In a session replay attack, an attacker intercepts and steals a valid session ID from a user and forwards it to the server with the intention of gaining unauthorized access to the user's session or tricking the server into performing unauthorized operations on behalf of the legitimate user.
* [✅] **True**
* [ ] False

### Versión en Español
En un ataque de repetición de sesión (Session Hijacking), un atacante intercepta y roba un ID de sesión válido de un usuario y lo reenvía al servidor con la intención de obtener acceso no autorizado a la sesión del usuario o engañar al servidor para que realice operaciones no autorizadas en nombre del usuario legítimo.
* [✅] **Verdadero**
* [ ] Falso

### 1. Explicación General
Este ataque combina la técnica de interceptación y la repetición. Al adueñarse de la cookie que contiene la firma de sesión activa, el atacante sobrepasa todas las barreras de autenticación (incluido el MFA, si este ya fue completado por la víctima previamente).

### 2. ¿Por qué es la correcta y no el resto?
Es **Verdadero** porque define con rigor técnico el secuestro y posterior reutilización del ID de sesión activo del cliente frente al servidor de destino.

### 3. Clave para el Examen SY0-701
Para proteger los IDs de sesión contra la interceptación de red, es mandatorio habilitar banderas de seguridad en las cookies de sesión como *Secure* (fuerza la transmisión exclusiva a través de HTTPS) y *HttpOnly* (previene que scripts de XSS lean la cookie).

---

## Pregunta 16: Autenticación por Movimiento Lateral (Pass the Hash)

### English Version
A technique that allows an attacker to authenticate to a remote server without extracting the plaintext password from a digest is called:
* [✅] **Pass the hash**
* [ ] Replay attack
* [ ] Brute-force attack
* [ ] Spraying attack

### Versión en Español
Una técnica que permite a un atacante autenticarse en un servidor remoto sin extraer la contraseña en texto plano de un resumen (hash) se denomina:
* [✅] **Pasa el hash (Pass the hash - PtH)**
* [ ] Ataque de repetición (Replay attack)
* [ ] Ataque de fuerza bruta (Brute-force attack)
* [ ] Ataque de rociado (Spraying attack)

### 1. Explicación General
En entornos corporativos de Windows (Active Directory con protocolos como NTLM), el sistema no almacena contraseñas en texto claro, sino sus representaciones criptográficas (hashes). El ataque Pass-the-Hash ocurre cuando un atacante roba el valor del hash directamente de la memoria del sistema operativo local (por ejemplo, mediante LSASS) y lo presenta directamente al servicio de autenticación de red remota para iniciar sesión.

### 2. ¿Por qué es la correcta y no el resto?
**Pass the hash** es el término de ataque de identidad específico para iniciar sesión utilizando directamente el hash de la contraseña robado, saltándose la necesidad de descifrarlo por fuerza bruta para obtener la palabra clave real. Un ataque de repetición genérico de red reenvía paquetes idénticos capturados, pero PtH utiliza herramientas como Mimikatz para inyectar el valor del hash de manera nativa en las APIs de autenticación de Windows.

### 3. Clave para el Examen SY0-701
El ataque Pass the Hash (PtH) se considera una de las principales técnicas de movimiento lateral dentro de redes empresariales Windows comprometidas. Se mitiga migrando el esquema de autenticación hacia protocolos modernos como Kerberos o utilizando defensas como Credential Guard.

---

[[ExamCompass - Cuestionarios por Temas|⬅️ Volver a Cuestionarios por Temas]]