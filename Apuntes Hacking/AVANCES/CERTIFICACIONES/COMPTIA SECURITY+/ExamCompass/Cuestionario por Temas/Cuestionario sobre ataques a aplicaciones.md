---
tags:
  - "formato/apunte"
  - "vulnerabilidades/web"
  - "examen/test-especifico"
  - "gestion/estado/terminado"
---
Este apunte contiene el análisis detallado del quinto bloque del cuestionario temático sobre vulnerabilidades de aplicaciones, inyecciones y seguridad web de la plataforma ExamCompass para la certificación CompTIA Security+ (SY0-701), alineado con las respuestas oficiales del simulador.

---

## Pregunta 1: Mecánica de Explotación de XSS (Cross-Site Scripting)

### English Version
What type of action allows an attacker to exploit the XSS (Cross-Site Scripting) vulnerability?
* [✅] **Code injection**
* [ ] Privilege escalation
* [ ] Session hijacking *(Your answer)*
* [ ] Packet sniffing

### Versión en Español
¿Qué tipo de acción permite a un atacante explotar la vulnerabilidad XSS?
* [✅] **Inyección de código (Code injection)**
* [ ] Escalada de privilegios (Privilege escalation)
* [ ] Secuestro de sesión (Session hijacking) *(Tu respuesta)*
* [ ] Interceptación de paquetes (Packet sniffing)

### 1. Explicación General
El Cross-Site Scripting (XSS) ocurre cuando una aplicación web toma datos de entrada del usuario que no han sido saneados y los incluye de vuelta en una página web dinámica sin validarlos. El atacante aprovecha esto para meter código (generalmente JavaScript) que se ejecutará en el navegador del usuario que visite esa página.

### 2. ¿Por qué falló tu respuesta?
Tu respuesta es el **efecto o consecuencia**, no la acción que explota la vulnerabilidad. Un atacante utiliza XSS para inyectar código malicioso y, gracias a esa ejecución, puede robar las cookies del usuario para lograr un secuestro de sesión (*Session hijacking*). Sin embargo, la acción técnica que realiza para explotar la vulnerabilidad XSS en primer lugar es la **Inyección de código**.

### 3. Clave para el Examen SY0-701
Recuerda siempre esta distinción: XSS es, por definición, un ataque de **inyección de código del lado del cliente** (*Client-side code injection*). Su objetivo final suele ser el secuestro de sesiones o el robo de tokens, pero el vector de ataque técnico inicial siempre es la inyección.

---

## Pregunta 2: Inyección LDAP y Gestión de Recursos de Red

### English Version
Which of the following exploits targets a protocol used for managing and accessing networked resources?
* [ ] CSRF/XSRF attack
* [ ] XML injection attack
* [✅] **LDAP injection attack**
* [ ] SQL injection attack

### Versión en Español
¿Cuál de los siguientes ataques se dirige a un protocolo utilizado para gestionar y acceder a recursos de red?
* [ ] Ataque CSRF/XSRF
* [ ] Ataque de inyección XML
* [✅] **Ataque de inyección LDAP (LDAP injection attack)**
* [ ] Ataque de inyección SQL

### 1. Explicación General
LDAP (*Lightweight Directory Access Protocol*) es el protocolo de red estándar que se utiliza para buscar e interactuar con servicios de directorio (como Microsoft Active Directory). Las empresas lo usan para gestionar usuarios, permisos, computadoras y otros recursos de la red corporativa.

### 2. ¿Por qué es la correcta y no el resto?
El enunciado especifica que el objetivo es un protocolo para "gestionar y acceder a recursos de red". Una inyección LDAP manipula las consultas enviadas al directorio para saltarse la autenticación o extraer información confidencial de los usuarios de la red. SQL ataca bases de datos relacionales, XML manipula archivos de estructuración de datos, y CSRF manipula peticiones web del cliente.

### 3. Clave para el Examen SY0-701
En cuanto veas en el examen palabras como "servicios de directorio", "recursos de red compartidos", "Active Directory" o "organigrama de usuarios", asócialo inmediatamente con **LDAP**.

---

## Pregunta 3: Inyección XML y Transporte de Datos

### English Version
Which type of exploit targets web applications that generate content used to store and transport data?
* [ ] SQL injection attack
* [ ] CSRF/XSRF attack
* [✅] **XML injection attack**
* [ ] LDAP injection attack

### Versión en Español
¿Qué tipo de ataque se dirige a aplicaciones web que generan contenido utilizado para almacenar y transportar datos?
* [ ] Ataque de inyección SQL
* [ ] Ataque CSRF/XSRF
* [✅] **Ataque de inyección XML (XML injection attack)**
* [ ] Ataque de inyección LDAP

### 1. Explicación General
XML (*eXtensible Markup Language*) es un lenguaje de marcado diseñado específicamente para almacenar y transportar datos en un formato estructurado legible tanto para humanos como para máquinas.

### 2. ¿Por qué es la correcta y no el resto?
El enunciado define con precisión la función del formato XML. Si una aplicación web no filtra correctamente las entradas del usuario al construir un documento XML, un atacante puede inyectar etiquetas maliciosas. Un ejemplo crítico es el ataque XXE (*XML External Entity*), donde se inyectan entidades externas para leer archivos locales del servidor o escanear puertos internos.

### 3. Clave para el Examen SY0-701
Cuando una pregunta mencione "almacenar y transportar datos" estructurados mediante etiquetas personalizadas en la web, la respuesta correcta es **XML**.

---

## Pregunta 4: Corrupción de Memoria: Desbordamiento de Búfer

### English Version
A type of exploit that relies on overwriting contents of memory to cause unpredictable results in an application is referred to as:
* [ ] IV attack
* [ ] Privilege escalation
* [✅] **Buffer overflow**
* [ ] DLL injection

### Versión en Español
Un tipo de exploit que se basa en sobrescribir el contenido de la memoria para causar resultados impredecibles en una aplicación se conoce como:
* [ ] Ataque IV (IV attack)
* [ ] Escalada de privilegios (Privilege escalation)
* [✅] **Desbordamiento de búfer (Buffer overflow)**
* [ ] Inyección de DLL (DLL injection)

### 1. Explicación General
Un desbordamiento de búfer (*Buffer Overflow*) ocurre cuando un programa escribe más datos en un área de memoria reservada temporalmente (búfer) de los que esta puede albergar. Los datos sobrantes se desbordan y sobrescriben las direcciones de memoria adyacentes.

### 2. ¿Por qué es la correcta y no el resto?
La sobrescritura de memoria para alterar el flujo de ejecución o causar un cuelgue (*crash*) es la definición exacta de un **Buffer Overflow**. El atacante suele usar esto para inyectar un código ejecutable en la pila de memoria (*stack*) y forzar al procesador a ejecutarlo con los privilegios del programa vulnerable.

### 3. Clave para el Examen SY0-701
Para mitigar desbordamientos de búfer en el desarrollo de software, se debe usar validación estricta de límites (*boundary checking*) en los inputs y evitar funciones inseguras en lenguajes como C/C++ (por ejemplo, reemplazando `strcpy` por `strncpy`).

---

## Pregunta 5: Interceptación y Retransmisión de Datos (Replay Attack)

### English Version
A situation where an attacker intercepts and retransmits valid data exchange between an application and a server, or another application is known as:
* [ ] Sideloading
* [✅] **Replay attack**
* [ ] Phishing attack
* [ ] Race condition

### Versión en Español
Una situación en la que un atacante intercepta y retransmite un intercambio de datos válido entre una aplicación y un servidor, u otra aplicación, se conoce como:
* [ ] Sideloading
* [✅] **Ataque de repetición (Replay attack)**
* [ ] Ataque de phishing (Phishing attack)
* [ ] Condición de carrera (Race condition)

### 1. Explicación General
Retransmitir información legítima previamente capturada (sin necesidad de descifrarla ni alterarla) para engañar al receptor es la definición clásica de un Ataque de Repetición.

### 2. ¿Por qué es la correcta y no el resto?
El término clave en el enunciado es "interceptar y retransmitir". *Sideloading* es la instalación de aplicaciones de fuentes no oficiales (común en dispositivos móviles). Una *condición de carrera (Race condition)* es una falla de lógica donde dos procesos compiten por el mismo recurso y el resultado depende del orden de ejecución.

### 3. Clave para el Examen SY0-701
Los ataques de repetición de datos en la web se previenen utilizando tokens de un solo uso (*nonces*) y garantizando que todas las conexiones utilicen cifrado TLS activo de extremo a extremo.

---

## Pregunta 6: Facilitadores de la Escalada de Privilegios

### English Version
Which of the following facilitate(s) privilege escalation attacks? (Select all that apply)
* [✅] **System/application vulnerabilities**
* [ ] Password hashing
* [✅] **System/application misconfigurations**
* [ ] Network segmentation
* [✅] **Social engineering techniques**

### Versión en Español
¿Cuáles de los siguientes elementos facilitan los ataques de escalada de privilegios? (Seleccione todos los que correspondan)
* [✅] **Vulnerabilidades del sistema/aplicación (System/application vulnerabilities)**
* [ ] Hasheo de contraseñas (Password hashing)
* [✅] **Malas configuraciones del sistema/aplicación (System/application misconfigurations)**
* [ ] Segmentación de red (Network segmentation)
* [✅] **Técnicas de ingeniería social (Social engineering techniques)**

### 1. Explicación General
La escalada de privilegios consiste en que un usuario con accesos limitados (ej. un empleado estándar o un servicio web con bajos privilegios) logra elevar su nivel de permisos para convertirse en administrador, *system* o *root* de un sistema.

### 2. ¿Por qué estas opciones son las correctas?
* **Vulnerabilidades:** Explotar un fallo de desbordamiento de búfer o un kernel desactualizado permite ejecutar comandos directamente con permisos del sistema.
* **Malas configuraciones:** Archivos de configuración con permisos de escritura para todos, credenciales por defecto o servicios que se ejecutan con privilegios excesivos.
* **Ingeniería social:** Engañar a un administrador (ej. soporte de TI) para que otorgue permisos adicionales o resetee una contraseña de nivel superior.

Por qué se descartan las otras: El *hasheo* de contraseñas y la segmentación de red son controles de seguridad que dificultan y mitigan los ataques, no los facilitan.

---

## Pregunta 7: Falsificación de Peticiones en Sitios Cruzados (CSRF/XSRF)

### English Version
Which of the statements listed below apply to the CSRF/XSRF attack? (Select 3 answers)
* [✅] **Exploits the trust a website has in the user's web browser**
* [✅] **A user is tricked by an attacker into submitting unauthorized web requests**
* [✅] **Website executes attacker's requests**
* [ ] Exploits the trust a user's web browser has in a website
* [ ] A malicious script is injected into a trusted website
* [ ] User's browser executes attacker's script

### Versión en Español
¿Cuáles de las afirmaciones enumeradas a continuación se aplican al ataque CSRF/XSRF? (Seleccione 3 respuestas)
* [✅] **Explota la confianza que un sitio web tiene en el navegador web del usuario.**
* [✅] **Un atacante engaña a un usuario para que envíe solicitudes web no autorizadas.**
* [✅] **El sitio web ejecuta las solicitudes del atacante.**
* [ ] Explota la confianza que el navegador web de un usuario tiene en un sitio web.
* [ ] Se inyecta un script malicioso en un sitio web de confianza.
* [ ] El navegador del usuario ejecuta el script del atacante.

### 1. Explicación General
El *Cross-Site Request Forgery* (CSRF/XSRF) es un ataque en el cual un usuario autenticado en una web legítima (ej. su portal bancario) es engañado para hacer clic en un enlace malicioso alojado en otro sitio de internet. Ese enlace envía una petición forzada al banco (como transferir dinero). Como el navegador del usuario ya está logueado en el banco y tiene cookies activas, el banco acepta la petición como válida.

### 2. ¿Por qué estas opciones son las correctas?
* **Explota la confianza que un sitio web tiene en el navegador:** El servidor del banco confía en el navegador porque este incluye automáticamente la cookie de sesión del usuario con la petición.
* **El usuario es engañado para enviar solicitudes no autorizadas:** La víctima hace clic en un elemento web que activa la transacción sin que se dé cuenta.
* **El sitio web ejecuta las solicitudes:** El servidor procesa la transferencia pensando que el usuario legítimo la solicitó conscientemente.

### 3. ¿Por qué falló tu respuesta?
Elegiste *"El navegador del usuario ejecuta el script del atacante"*. **¡Cuidado! Eso describe a XSS (Cross-Site Scripting)**, no a CSRF. En CSRF no hay inyección ni ejecución de scripts maliciosos dentro de la aplicación objetivo; simplemente se aprovecha el estado activo de la sesión del navegador para enviar una petición HTTP estándar.

### 4. Clave para el Examen SY0-701
Grábate esta regla de oro:
* **XSS:** Explota la confianza que el **usuario** tiene en un sitio web (inyecta scripts en la página en la que confías).
* **CSRF:** Explota la confianza que el **sitio web** tiene en el navegador del usuario (el sitio confía en tu cookie de sesión activa). Se previene usando tokens anti-CSRF únicos por cada petición.

---

## Pregunta 8: Salto de Directorio (Directory Traversal)

### English Version
A dot-dot-slash attack is also referred to as:
* [ ] Disassociation attack
* [ ] On-path attack
* [✅] **Directory traversal attack**
* [ ] Downgrade attack

### Versión en Español
Un ataque de punto-punto-barra (dot-dot-slash) también se conoce como:
* [ ] Ataque de disociación (Disassociation attack)
* [ ] Ataque en ruta (On-path attack)
* [✅] **Ataque de salto de directorio (Directory traversal attack)**
* [ ] Ataque de degradación (Downgrade attack)

### 1. Explicación General
El ataque consiste en aprovechar una mala validación de entradas en las variables que manejan rutas de archivos en un servidor para inyectar caracteres de retroceso (los famosos `../` o `..\` en Windows).

### 2. ¿Por qué es la correcta y no el resto?
El uso de `../` sirve para retroceder niveles en el árbol de directorios del servidor web con el objetivo de salir de la carpeta pública (`/var/www/`) y acceder a archivos sensibles del sistema operativo. Por esta razón, el ataque se conoce técnicamente como **Directory Traversal** (Salto o Travesía de Directorio).

### 3. Clave para el Examen SY0-701
Este ataque busca acceder a recursos del sistema de archivos a los que los usuarios comunes del servidor web no deberían tener acceso de lectura. Se mitiga mediante saneamiento estricto de rutas e implementando el principio de privilegios mínimos en el usuario que ejecuta el proceso web (ej. `www-data`).

---

## Pregunta 9: Indicadores de Directory Traversal en Logs

### English Version
Which of the following URLs is a potential indicator of a directory traversal attack?
* [ ] `http://example.com/show.asp?view=../show.asp`
* [ ] `http://example.com/show.asp?view=../../show.asp`
* [ ] `http://example.com/show.asp?view=../../../show.asp`
* [ ] `http://example.com/show.asp?view=../../../../etc/passwd`
* [✅] **Any of the above**

### Versión en Español
¿Cuál de las siguientes URLs es un indicador potencial de un ataque de salto de directorio (Directory traversal)?
* [ ] `http://example.com/show.asp?view=../show.asp`
* [ ] `http://example.com/show.asp?view=../../show.asp`
* [ ] `http://example.com/show.asp?view=../../../show.asp`
* [ ] `http://example.com/show.asp?view=../../../../etc/passwd`
* [✅] **Cualquiera de las anteriores (Any of the above)**

### 1. Explicación General
Todas las URLs de ejemplo muestran intentos estructurados de usar secuencias `../` consecutivas para escapar de los subdirectorios públicos configurados y alcanzar archivos del sistema.

### 2. ¿Por qué es la correcta y no el resto?
La opción **"Cualquiera de las anteriores"** es la correcta porque, independientemente del nivel de profundidad o del archivo objetivo, todas las direcciones buscan explotar el mismo principio de manipulación de rutas. El último ejemplo muestra un intento clásico en Linux para obtener el archivo `/etc/passwd`.

### 3. Clave para el Examen SY0-701
En las preguntas de análisis de logs en el examen de certificación, si ves secuencias de caracteres como `..%2f` o `..%5c` (que son las codificaciones URL de `/` y `\`), estás viendo un ataque de Directory Traversal codificado para evadir filtros de seguridad básicos (*WAF evasion*).

---

[[ExamCompass - Cuestionarios por Temas|⬅️ Volver a Cuestionarios por Temas]]