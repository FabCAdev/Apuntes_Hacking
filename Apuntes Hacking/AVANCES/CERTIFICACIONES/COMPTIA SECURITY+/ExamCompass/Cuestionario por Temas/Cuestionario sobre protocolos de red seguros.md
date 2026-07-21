---
tags:
  - "formato/apunte"
  - "hacking/fundamental"
  - "examen/test-especifico"
  - "gestion/estado/progreso"
---
Este apunte contiene la primera sección del análisis detallado de los cuestionarios temáticos de ExamCompass sobre protocolos seguros de red (HTTPS, SFTP, SSH, SMTPS, SRTP) para la certificación CompTIA Security+ (SY0-701), alineado con mis respuestas y las oficiales del simulador.

---

## Pregunta 1: Seguridad en la Navegación Web (HTTPS)

### English Version
Which of the protocols listed below is used to enable secure web browsing?
- [ ] L2TP
- [x] **HTTPS**
- [ ] SSH
- [ ] IPsec

### Versión en Español
¿Cuál de los protocolos que se enumeran a continuación se utiliza para permitir la navegación web segura?
- [ ] L2TP
- [x] **HTTPS**
- [ ] SSH
- [ ] IPsec

### 1. Explicación General
Cuando un usuario visita un sitio web e ingresa información confidencial (como credenciales de acceso o datos bancarios), es crítico blindar el canal de comunicación contra interceptaciones (*sniffing*) y alteraciones de datos. HTTPS cumple este propósito integrando mecanismos criptográficos directamente sobre el protocolo de transferencia hipertexto tradicional.

### 2. ¿Por qué es la correcta y no el resto?
- **HTTPS** (Hypertext Transfer Protocol Secure) combina la lógica de aplicación de HTTP con las capacidades de cifrado de **TLS (Transport Layer Security)**, garantizando confidencialidad, integridad y autenticación del servidor web mediante certificados digitales.
- **L2TP:** Protocolo de tunelización para redes privadas virtuales (VPN) que, por sí solo, carece de funciones de cifrado nativas.
- **SSH:** Diseñado para la administración remota y control de consolas de comandos de servidores, no para la entrega o renderizado de páginas web.
- **IPsec:** Trabaja en la capa de red (Capa 3 del modelo OSI) para proteger todo el tráfico IP; es demasiado general y no está especializado en la navegación web del usuario final.

### 3. Clave para el Examen SY0-701
CompTIA asocia de forma directa la navegación web segura con **HTTPS**. Debo memorizar obligatoriamente su puerto de control estándar por defecto: **TCP 443**.

---

## Pregunta 2: Transferencia Segura de Archivos (SFTP vs. FTPS)

### English Version
Which of the following protocols allow(s) for secure file transfer? (Select all that apply)
- [x] **FTPS**
- [ ] TFTP
- [ ] FTP
- [x] **SFTP**

### Versión en Español
¿Cuáles de los siguientes protocolos permiten la transferencia segura de archivos? (Seleccione todas las opciones que correspondan)
- [x] **FTPS**
- [ ] TFTP
- [ ] FTP
- [x] **SFTP**

### 1. Explicación General
Los protocolos heredados de transferencia de archivos carecen de protección perimetral, lo que expone los datos confidenciales y las claves de acceso a ataques de intercepción en tránsito. Los protocolos modernos subsanan esto inyectando capas criptográficas robustas.

### 2. ¿Por qué es la correcta y no el resto?
- **FTPS** (FTP Secure) añade seguridad al protocolo FTP clásico montándolo sobre un túnel TLS/SSL para proteger los comandos y los datos.
- **SFTP** (SSH File Transfer Protocol) es un protocolo completamente rediseñado que corre de manera nativa sobre un canal seguro **SSH**, cifrando la sesión desde el inicio.
- **FTP** y **TFTP:** Transmiten la información y las credenciales en texto plano. TFTP (Trivial FTP) es aún más peligroso debido a que no implementa ningún control de autenticación de usuarios.

### 3. Clave para el Examen SY0-701
Aunque ambos cumplen la misma función operativa (transferir archivos con seguridad), a nivel arquitectónico **FTPS y SFTP son tecnologías completamente distintas**. Nunca debo tratarlos como sinónimos en las preguntas de opción múltiple.

---

## Pregunta 3: Diferencias Técnicas entre FTPS y SFTP

### English Version
FTPS is an extension to the SSH protocol and runs by default on TCP port 22.
- [ ] True
- [x] **False**

### Versión en Español
FTPS es una extensión del protocolo SSH y se ejecuta de forma predeterminada en el puerto TCP 22.
- [ ] Verdadero
- [x] **Falso**

### 1. Explicación General
Uno de los distractores favoritos en el examen Security+ es mezclar las bases tecnológicas de los protocolos seguros de transferencia de archivos para confundir al estudiante con la nomenclatura.

### 2. ¿Por qué es la correcta y no el resto?
El enunciado es rotundamente **Falso**. El protocolo que representa una extensión directa de SSH y opera de forma predeterminada a través del puerto **TCP 22** es **SFTP**. Por el contrario, FTPS es una extensión de FTP que se apoya en TLS/SSL y utiliza tradicionalmente los puertos **TCP 21 o 990**.

### 3. Clave para el Examen SY0-701
Establezco este mapa de puertos e infraestructura en mi memoria:
- `SFTP` ➡️ Utiliza el motor de **SSH** ➡️ Puerto **TCP 22**.
- `FTPS` ➡️ Utiliza el motor de **TLS/SSL** ➡️ Puertos **TCP 21 / 990**.

---

## Pregunta 4: Gestión Remota Segura (Reemplazo de Telnet)

### English Version
Which of the answers listed below refers to a secure replacement for Telnet?
- [ ] RSH
- [ ] IPsec
- [x] **SSH**
- [ ] RTPS

### Versión en Español
¿Cuál de las respuestas que aparecen a continuación se refiere a un reemplazo seguro para Telnet?
- [ ] RSH
- [ ] IPsec
- [x] **SSH**
- [ ] RTPS

### 1. Explicación General
Durante los inicios de la administración de redes, Telnet era el estándar para gestionar dispositivos e infraestructuras remotas mediante consolas de comandos. Sin embargo, su vulnerabilidad crítica radica en que transmite las sesiones, comandos y contraseñas de administrador en texto plano.

### 2. ¿Por qué es la correcta y no el resto?
- **SSH** (Secure Shell) se diseñó explícitamente para actuar como el sustituto directo y seguro de Telnet, proveyendo confidencialidad mediante cifrado simétrico/asimétrico, autenticación robusta por llaves criptográficas e integridad de datos.
- **RSH** (Remote Shell): Es un protocolo antiguo, obsoleto e igualmente inseguro que Telnet.
- **IPsec:** Asegura túneles de red completos pero no actúa como una herramienta de gestión de terminal remota.

### 3. Clave para el Examen SY0-701
CompTIA evalúa constantemente este caso de migración tecnológica para medir la capacidad de endurecimiento (*hardening*) de redes: **Migrar de Telnet (TCP 23 - Inseguro) hacia SSH (TCP 22 - Seguro)**.

---

## Pregunta 5: Protocolos Obsoletos de Correo (SMTPS)

### English Version
Which of the answers listed below refers to a deprecated protocol designed as a secure way to send emails from a client to a mail server and between mail servers?
- [ ] IMAPS
- [ ] SFTP
- [ ] POP3S
- [x] **SMTPS**

### Versión en Español
¿Cuál de las respuestas que aparecen a continuación se refiere a un protocolo obsoleto diseñado como una forma segura de enviar correos electrónicos desde un cliente a un servidor de correo y entre servidores de correo?
- [ ] IMAPS
- [ ] SFTP
- [ ] POP3S
- [x] **SMTPS**

### 1. Explicación General
El servicio de correo electrónico maneja distintas fases lógicas: el envío y la recepción. SMTPS representó un esfuerzo temprano para proteger la fase de transporte e intercambio de mensajes cifrando la sesión desde el inicio a nivel de transporte.

### 2. ¿Por qué es la correcta y no el resto?
- **SMTPS** (Simple Mail Transfer Protocol Secure) es la variante que encapsulaba el tráfico SMTP tradicional dentro de una sesión SSL/TLS para el **envío** seguro de correos. Actualmente se considera en desuso (*deprecated*) en favor de la implementación de **STARTTLS**, que actualiza dinámicamente conexiones claras a cifradas sobre el mismo puerto estándar.
- **IMAPS** y **POP3S:** Son protocolos orientados exclusivamente a la descarga, lectura o sincronización de correos desde el buzón del servidor hacia el cliente, no a la transmisión o envío.

### 3. Clave para el Examen SY0-701
Recordar la tríada básica del correo electrónico según su función fundamental:
- **Envío / Retransmisión:** SMTP / SMTPS.
- **Descarga local:** POP3 / POP3S.
- **Sincronización y Gestión en servidor:** IMAP / IMAPS.

---

## Pregunta 6: Recuperación Segura de Mensajes (IMAPS y POP3S)

### English Version
Which of the protocols listed below enable secure retrieval of emails from a mail server to an email client? (Select 2 answers)
- [x] **IMAPS**
- [ ] FTPS
- [ ] STARTTLS
- [ ] SMTPS
- [x] **POP3S**

### Versión en Español
¿Cuáles de los protocolos que aparecen a continuación permiten la recuperación segura de correos electrónicos desde un servidor de correo hacia un cliente de correo? (Seleccione 2 respuestas)
- [x] **IMAPS**
- [ ] FTPS
- [ ] STARTTLS
- [ ] SMTPS
- [x] **POP3S**

### 1. Explicación General
Cuando un usuario abre su cliente de correo (como Outlook o Thunderbird), la aplicación debe conectarse con el servidor para extraer y leer los mensajes pendientes de forma segura, protegiendo las credenciales de acceso del buzón de cualquier atacante local.

### 2. ¿Por qué es la correcta y no el resto?
- **IMAPS** (puerto TCP 993) y **POP3S** (puerto TCP 995) añaden una capa protectora TLS/SSL a los servicios tradicionales de **recuperación** (*retrieval*), garantizando que las contraseñas de las cuentas viajen completamente cifradas.
- **STARTTLS:** No es un protocolo de correo en sí mismo; es un comando/extensión que instruye a una conexión existente a elevar su nivel de seguridad a TLS.
- **SMTPS:** Se especializa en la entrega externa o envío de correo, no en su descarga.

### 3. Clave para el Examen SY0-701
Diferencia funcional crucial para el examen: **POP3S descarga** los correos eliminándolos o aislándolos del servidor (almacenamiento local), mientras que **IMAPS mantiene sincronizados** múltiples dispositivos simultáneamente al gestionar los estados en el servidor central.

---

## Pregunta 7: Gestión Avanzada de Buzones de Correo (IMAPS)

### English Version
Which of the following protocols enables secure access and management of emails on a mail server from an email client?
- [ ] POP3S
- [ ] SMTPS
- [x] **IMAPS**
- [ ] S/MIME

### Versión en Español
¿Cuál de los siguientes protocolos permite el acceso y la administración segura de correos electrónicos en un servidor desde un cliente de correo?
- [ ] POP3S
- [ ] SMTPS
- [x] **IMAPS**
- [ ] S/MIME

### 1. Explicación General
La necesidad moderna de consultar el correo electrónico desde múltiples dispositivos (teléfono móvil, laptop, interfaz web) exige un protocolo que no se limite a descargar archivos, sino que mantenga intacta la estructura de carpetas, etiquetas y estados directamente en el servidor centralizado.

### 2. ¿Por qué es la correcta y no el resto?
- **IMAPS** (Internet Message Access Protocol Secure) permite la **administración y sincronización en tiempo real** de los mensajes de forma remota sobre una conexión cifrada.
- **POP3S:** Aunque es seguro, carece de funciones avanzadas de gestión remota multi-dispositivo; su flujo natural es descargar el correo al almacenamiento local de un único equipo.
- **S/MIME:** No es un protocolo de transporte de red; es un estándar criptográfico que se utiliza para cifrar y firmar digitalmente el *contenido interno* (cuerpo y archivos adjuntos) de un correo de extremo a extremo (*End-to-End*).

### 3. Clave para el Examen SY0-701
Si una pregunta en el examen Security+ hace mención explícita a palabras clave como **"sincronizar múltiples dispositivos"** o **"administrar correos en el servidor"**, la respuesta correcta será invariablemente **IMAP/IMAPS**.

---

## Pregunta 8: Seguridad en Multimedia y Voz sobre IP (SRTP)

### English Version
Which of the answers listed below refers to a secure network protocol used to provide encryption, authentication, and integrity for real-time multimedia communication?
- [ ] IPsec
- [ ] SIP
- [ ] VoIP
- [x] **SRTP**

### Versión en Español
¿Cuál de las respuestas que aparecen a continuación se refiere a un protocolo de red seguro utilizado para proporcionar cifrado, autenticación e integridad para comunicaciones multimedia en tiempo real?
- [ ] IPsec
- [ ] SIP
- [ ] VoIP
- [x] **SRTP**

### 1. Explicación General
Las llamadas de Voz sobre IP (VoIP), las videoconferencias corporativas y las transmisiones de streaming transportan flujos continuos de datos sensibles en tiempo real. Si estos canales carecen de protección, un adversario en la red podría reconstruir los paquetes capturados para escuchar conversaciones de voz o espiar videos.

### 2. ¿Por qué es la correcta y no el resto?
- **SRTP** (Secure Real-time Transport Protocol) fue desarrollado específicamente para blindar transmisiones multimedia inyectando cifrado AES para confidencialidad, junto con autenticación y protección contra ataques de repetición (*replay attacks*).
- **SIP** (Session Initiation Protocol): Es un protocolo de control e infraestructura; se encarga únicamente de señalizar, iniciar, timbrar y colgar las llamadas, pero no transporta ni cifra el contenido del audio o video.
- **VoIP:** Es el término conceptual de la industria (*Voice over IP*), no un protocolo de seguridad técnico específico.

### 3. Clave para el Examen SY0-701
Esta distinción técnica ahorra valiosos puntos en el examen:
- **SIP / SIPS:** Establece, gestiona y finaliza la llamada web.
- **RTP / SRTP:** Transporta el flujo real de datos multimedia (la voz y la imagen) durante la comunicación.

---

[[ExamCompass - Cuestionarios por Temas|⬅️ Volver a Cuestionarios por Temas]]