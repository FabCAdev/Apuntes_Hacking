---
tags:
  - "formato/apunte"
  - "hacking/fundamental"
  - "examen/test-especifico"
  - "gestion/estado/terminado"
---
Este apunte contiene el análisis detallado del cuestionario temático sobre controles de seguridad de la plataforma ExamCompass para la certificación CompTIA Security+ (SY0-701), alineado con las respuestas oficiales del simulador.

---

## Pregunta 1: Cifrado a nivel de hardware / Hardware-level encryption

### English Version
Which of the following answers refers to a data storage device equipped with hardware-level encryption functionality?
* [ ] HSM (Hardware Security Module)
* [ ] TPM (Trusted Platform Module)
* [✅] **SED (Self-Encrypting Drive)**
* [ ] EFS (Encrypting File System)

### Versión en Español
¿Cuál de las siguientes respuestas se refiere a un dispositivo de almacenamiento de datos equipado con funcionalidad de cifrado a nivel de hardware?
* [ ] HSM (Módulo de Seguridad de Hardware)
* [ ] TPM (Módulo de Plataforma de Confianza)
* [✅] **SED (Unidad con Cifrado Automático)**
* [ ] EFS (Sistema de Archivos Cifrados)

### 1. Explicación General
El cifrado de datos en reposo puede realizarse mediante software o directamente integrado en el silicio del hardware. Cuando el propio dispositivo de almacenamiento físico procesa criptográficamente los datos sin depender del sistema operativo ni de recursos de la CPU principal, el rendimiento es óptimo y el aislamiento de seguridad es máximo frente a manipulaciones lógicas.

### 2. ¿Por qué es la correcta y no el resto?
* **Opción Correcta:** `[SED (Self-Encrypting Drive)]` es un disco duro (HDD) o unidad de estado sólido (SSD) que contiene un chip criptográfico especializado en su propia placa controladora. Cifra automáticamente cada bit al escribirse y lo descifra al leerse, de manera completamente invisible y transparente para el usuario y el sistema operativo.
* **Análisis de los distractores:**
    * *HSM:* Un Módulo de Seguridad de Hardware es un dispositivo de red externo o tarjeta PCIe dedicada a generar y administrar claves criptográficas corporativas, no es un disco de almacenamiento para archivos.
    * *TPM:* El Módulo de Plataforma de Confianza es un microchip soldado a la placa madre que almacena llaves y asiste en el arranque seguro, pero no es un medio de almacenamiento masivo.
    * *EFS:* Es un componente de software integrado exclusivamente en el sistema de archivos NTFS de Windows, por lo que no es un dispositivo físico de hardware.

### 3. Clave para el Examen SY0-701
Recordar la relación conceptual directa: "Data storage device" + "hardware-level encryption" = `SED`.

---

## Pregunta 2: Confidencialidad para todo el dispositivo / Full device confidentiality

### English Version
Which of the answers listed below refers to a software technology designed to provide confidentiality for an entire data storage device?
* [ ] TPM (Trusted Platform Module)
* [ ] HSM (Hardware Security Module)
* [ ] EFS (Encrypting File System)
* [✅] **FDE (Full Disk Encryption)**

### Versión en Español
¿Cuál de las respuestas listadas abajo se refiere a una tecnología de software diseñada para proporcionar confidencialidad a todo un dispositivo de almacenamiento de datos?
* [ ] TPM (Módulo de Plataforma de Confianza)
* [ ] HSM (Módulo de Seguridad de Hardware)
* [ ] EFS (Sistema de Archivos Cifrados)
* [✅] **FDE (Cifrado de Disco Completo)**

### 1. Explicación General
Para mitigar el impacto del robo físico de computadoras portátiles o discos duros, es necesario un sistema que selle el volumen de almacenamiento completo de extremo a extremo. Esto vuelve ilegible el sistema operativo, los archivos temporales de paginación y todos los datos de usuario si no se introduce la clave de pre-arranque correcta.

### 2. ¿Por qué es la correcta y no el resto?
* **Opción Correcta:** `[FDE (Full Disk Encryption)]` es la categoría tecnológica basada en software (como BitLocker en Windows o FileVault en macOS) que cifra cada sector de la unidad de almacenamiento ("entire data storage device"), impidiendo que un atacante extraiga el disco e intente leer los datos montándolo en otra máquina.
* **Análisis de los distractores:**
    * *TPM:* Es un chip físico de hardware en la tarjeta madre, no una tecnología o solución basada en software para el cifrado de sectores.
    * *HSM:* Es un hardware empresarial para la gestión centralizada de llaves y firmas de servidores, no una solución de software para discos locales.
    * *EFS:* Aunque es software de Windows, trabaja de forma granular únicamente a nivel de archivos y carpetas individuales, dejando el resto del disco desprotegido.

### 3. Clave para el Examen SY0-701
Asociación rápida para el examen: "Software technology" + "entire data storage device" = `FDE`.

---

## Pregunta 3: Cifrado granular en Windows / Granular Windows file encryption

### English Version
A component of MS Windows that allows encryption of individual files is called:
* [ ] BitLocker
* [✅] **EFS (Encrypting File System)**
* [ ] TPM (Trusted Platform Module)
* [ ] HSM (Hardware Security Module)

### Versión en Español
Un componente de MS Windows que permite el cifrado de archivos individuales se llama:
* [ ] BitLocker
* [✅] **EFS (Sistema de Archivos Cifrados)**
* [ ] TPM (Módulo de Plataforma de Confianza)
* [ ] HSM (Módulo de Seguridad de Hardware)

### 1. Explicación General
Windows ofrece dos esquemas criptográficos nativos complementarios: uno protege el volumen completo contra intrusos físicos mediante FDE y el otro opera de forma interna y lógica, aislando archivos específicos para que otros usuarios locales con acceso a la misma máquina encendida no puedan husmear en información confidencial ajena.

### 2. ¿Por qué es la correcta y no el resto?
* **Opción Correcta:** `[EFS (Encrypting File System)]` permite a los usuarios de Windows cifrar directorios o archivos individuales (*individual files*) directamente sobre particiones NTFS, ligando el acceso al certificado y credenciales del usuario que lo activó.
* **Análisis de los distractores:**
    * *BitLocker:* Es la solución para FDE. BitLocker desbloquea el disco completo en el arranque; una vez que el sistema operativo inicia, no restringe el acceso a archivos individuales entre diferentes usuarios locales.
    * *TPM:* Es el chip de la tarjeta madre que asiste a BitLocker guardando sus claves de volcado, no una herramienta de software para archivos individuales.
    * *HSM:* Es un dispositivo de hardware corporativo que no tiene relación directa con las funciones del explorador de archivos de Windows.

### 3. Clave para el Examen SY0-701
Diferenciación crucial en Windows: "Individual files" = `EFS`. "Entire volume/drive" = **BitLocker**.

---

## Pregunta 4: Cifrado híbrido multiuso / Multi-purpose hybrid encryption

### English Version
Which of the following software tools are specifically designed to implement encryption algorithms that protect data communication and storage? (Select 2 answers)
* [ ] IPsec
* [✅] **PGP (Pretty Good Privacy)**
* [ ] SSH
* [✅] **GPG (GNU Privacy Guard)**
* [ ] VPN

### Versión en Español
¿Cuáles de las siguientes herramientas de software están diseñadas específicamente para implementar algoritmos de cifrado que protegen la comunicación y el almacenamiento de datos? (Seleccione 2 respuestas)
* [ ] IPsec
* [✅] **PGP (Pretty Good Privacy)**
* [ ] SSH
* [✅] **GPG (GNU Privacy Guard)**
* [ ] VPN

### 1. Explicación General
La mayoría de los protocolos criptográficos protegen datos exclusivamente mientras viajan por la red (en tránsito). Sin embargo, existen herramientas de software basadas en criptografía híbrida que permiten firmar y cifrar tanto un archivo estático en un disco duro (**almacenamiento / storage**) como empaquetar de forma segura un correo electrónico antes de enviarlo (**comunicación / communication**).

### 2. ¿Por qué es la correcta y no el resto?
* **Opciones Correctas:** `[PGP y GPG]` debido a que *Pretty Good Privacy* y su contraparte de código abierto *GNU Privacy Guard* (estándar OpenPGP) permiten cifrar archivos locales o discos virtuales (storage) y, a su vez, correos electrónicos completos de extremo a extremo antes de transmitirse (communication).
* **Análisis de los distractores:**
    * *IPsec:* Suite de protocolos de red para asegurar tráfico IP a nivel de capa de red. No puede usarse para guardar un archivo cifrado estático.
    * *SSH:* Protocolo de acceso remoto interactivo. Asegura el canal de comunicación en tránsito, pero no cifra archivos en almacenamiento local.
    * *VPN:* Concepto de túnel de red para conectar infraestructuras sobre internet; no cifra datos en reposo (storage).

### 3. Clave para el Examen SY0-701
Herramientas de software con doble propósito para "communication AND storage" = `PGP` y `GPG`.

---

## Pregunta 5: Seguridad en Tráfico Web / Web Traffic Security

### English Version
What is the name of the network protocol that secures web traffic using SSL/TLS encryption?
* [ ] SFTP
* [✅] **HTTPS**
* [ ] FTPS
* [ ] SHTTP

### Versión en Español
¿Cuál es el nombre del protocolo de red que asegura el tráfico web utilizando cifrado SSL/TLS?
* [ ] SFTP
* [✅] **HTTPS**
* [ ] FTPS
* [ ] SHTTP

### 1. Explicación General
El protocolo web tradicional (HTTP) envía las páginas web, contraseñas y datos de formularios en texto plano por el puerto 80. Para evitar ataques de espionaje, se envuelve este tráfico dentro de un canal cifrado por un protocolo de capa de transporte seguro, validando también la identidad del servidor remoto.

### 2. ¿Por qué es la correcta y no el resto?
* **Opción Correcta:** `[HTTPS (Hypertext Transfer Protocol Secure)]` es la implementación de HTTP sobre un túnel seguro `[[TLS]]` (o históricamente SSL) utilizando por defecto el puerto 443, asegurando confidencialidad, integridad y autenticación.
* **Análisis de los distractores:**
    * *SFTP:* Protocolo de transferencia de archivos que corre montado sobre SSH (puerto 22), no se usa para cargar páginas web en navegadores.
    * *FTPS:* Protocolo de transferencia de archivos FTP tradicional parchado con capas SSL/TLS (puertos 989/990), ajeno al tráfico web.
    * *SHTTP:* *Secure HTTP* es un protocolo obsoleto que cifraba los mensajes web de forma individual en lugar de crear un túnel completo. Nunca prosperó frente a HTTPS.

### 3. Clave para el Examen SY0-701
Asociación directa e inmediata: "Secures web traffic" + "SSL/TLS" = `HTTPS`.

---

## Pregunta 6: Transferencia de archivos sobre SSH / File transfer over SSH

### English Version
Which of the network protocols listed below allows for secure file transfer over an SSH connection?
* [ ] TFTP
* [✅] **SFTP**
* [ ] FTP
* [ ] FTPS

### Versión en Español
¿Cuál de los protocolos de red enumerados a continuación permite la transferencia segura de archivos a través de una conexión SSH?
* [ ] TFTP
* [✅] **SFTP**
* [ ] FTP
* [ ] FTPS

### 1. Explicación General
Cuando un administrador necesita transferir scripts, parches o archivos de configuración a un servidor remoto de manera segura, busca reutilizar la misma infraestructura criptográfica que ya usa para las sesiones de comandos remotos, consolidando puertos abiertos en el firewall y credenciales.

### 2. ¿Por qué es la correcta y no el resto?
* **Opción Correcta:** `[SFTP (SSH File Transfer Protocol)]` es un protocolo diseñado desde cero que ejecuta todas sus operaciones de movimiento de archivos encapsuladas de forma nativa dentro de una sesión criptográfica `[[SSH]]` segura a través del puerto 22.
* **Análisis de los distractores:**
    * *TFTP:* *Trivial FTP* es un protocolo ultra simple que no ofrece ningún tipo de cifrado ni autenticación; envía todo en texto plano sobre UDP.
    * *FTP:* Es el protocolo clásico de transferencia de archivos que transmite contraseñas y datos expuestos en texto plano, altamente vulnerable.
    * *FTPS:* Es FTP respaldado con SSL/TLS. Aunque es seguro, no tiene ninguna relación operativa con SSH; usa puertos diferentes (989/990).

### 3. Clave para el Examen SY0-701
Conector conceptual: "File transfer" + "over SSH" = `SFTP`.

---

## Pregunta 7: Mitos y realidades de los protocolos de archivos / File protocol myths and realities

### English Version
SFTP is an extension to the FTP protocol that adds Support for Transport Layer Security (TLS) and Secure Sockets Layer (SSL). True or False?
* [ ] True
* [✅] **False**

### Versión en Español
SFTP es una extensión del protocolo FTP que añade soporte para Transport Layer Security (TLS) y Secure Sockets Layer (SSL). ¿Verdadero o Falso?
* [ ] True
* [✅] **False**

### 1. Explicación General
Existe una confusión muy común debido a la similitud de los acrónimos en los protocolos de transferencia de archivos seguros. Sin embargo, los mecanismos subyacentes de seguridad y las arquitecturas de red que utilizan son completamente diferentes e incompatibles entre sí.

### 2. ¿Por qué es la correcta y no el resto?
* **Opción Correcta:** `[False]` porque el enunciado describe con total precisión técnica a **FTPS** (FTP Secure), el cual es la extensión directa del FTP clásico sobre capas SSL/TLS. **SFTP** no es una extensión de FTP; es un protocolo completamente independiente derivado y encapsulado dentro de SSH.
* **Análisis de los distractores:**
    * *True:* Es incorrecto porque aceptar el enunciado implicaría confundir SFTP (basado en SSH) con FTPS (basado en SSL/TLS).

### 3. Clave para el Examen SY0-701
Si el texto dice "FTP extension + SSL/TLS" se refiere a **FTPS**. Si dice "SSH connection" se refiere a `SFTP`. Por tanto, cruzar los conceptos siempre dará como resultado `False`.

---

## Pregunta 8: Acceso remoto a terminal / Remote terminal access

### English Version
A type of cryptographic network protocol for secure data communication, remote command-line login, remote command execution, and other secure network services is known as:
* [ ] Telnet
* [ ] RDP
* [✅] **SSH**
* [ ] SCP

### Versión en Español
Un tipo de protocolo de red criptográfico para la comunicación segura de datos, inicio de sesión remoto por línea de comandos, ejecución remota de comandos y otros servicios de red seguros se conoce como:
* [ ] Telnet
* [ ] RDP
* [✅] **SSH**
* [ ] SCP

### 1. Explicación General
La administración diaria de servidores y dispositivos de red requiere que los ingenieros ejecuten comandos directamente en los sistemas remotos. Para evitar que actores maliciosos intercepten las contraseñas administrativas, se necesita un canal cifrado que reemplace a las terminales clásicas de texto plano.

### 2. ¿Por qué es la correcta y no el resto?
* **Opción Correcta:** `[SSH (Secure Shell)]` proporciona una consola de comandos remota segura en el puerto 22, empleando criptografía asimétrica para autenticar el host y criptografía simétrica para proteger los comandos e información introducida.
* **Análisis de los distractores:**
    * *Telnet:* Era el antiguo estándar de inicio de sesión remoto, pero carece de criptografía y transmite las credenciales en texto plano a través del puerto 23.
    * *RDP:* *Remote Desktop Protocol* se usa para la administración remota a través de una interfaz gráfica de usuario completa (GUI), no de línea de comandos pura.
    * *SCP:* *Secure Copy* usa SSH por detrás, pero sirve únicamente para transferir un archivo de un punto a otro de forma directa, no permite abrir una sesión interactiva de comandos (*remote login*).

### 3. Clave para el Examen SY0-701
Mapeo rápido: "Remote command-line login" + "Secure network services" = `SSH`.

---

## Pregunta 9: Confidencialidad en la Capa de Red / Network Layer Confidentiality

### English Version
Which part of IPsec provides authentication, integrity, and confidentiality?
* [ ] AH (Authentication Header)
* [✅] **ESP (Encapsulating Security Payload)**
* [ ] SPD (Security Policy Database)
* [ ] PFS (Perfect Forward Secrecy)

### Versión en Español
¿Qué parte de IPsec proporciona autenticación, integridad y confidencialidad?
* [ ] AH (Encabezado de Autenticación)
* [✅] **ESP (Carga Útil de Seguridad Encapsulada)**
* [ ] SPD (Base de Datos de Políticas de Seguridad)
* [ ] D) PFS (Secreto Perfecto hacia Adelante)

### 1. Explicación General
La suite `[[IPsec]]` asegura el tráfico IP dividiendo el trabajo entre sus componentes: uno se encarga puramente de verificar quién envía el paquete y que nadie lo altere, mientras que otro se encarga específicamente de ocultar el contenido de los datos empaquetándolos bajo algoritmos de cifrado simétrico.

### 2. ¿Por qué es la correcta y no el resto?
* **Opción Correcta:** `[ESP]` cifra la carga útil (los datos) del paquete IP, cumpliendo con la **confidencialidad**. Adicionalmente, incluye mecanismos para autenticar el origen y validar que el contenido no fue manipulado en tránsito (integridad).
* **Análisis de los distractores:**
    * *AH:* El Encabezado de Autenticación ofrece integridad y autenticación de todo el paquete, pero **no cifra nada**. Por ende, carece por completo de confidencialidad.
    * *SPD:* Es una tabla lógica de políticas dentro del dispositivo de red que decide si un paquete debe pasar por el túnel IPsec o no; no es un protocolo operativo.
    * *PFS:* Es una propiedad o cualidad de los sistemas de intercambio de claves, no un componente estructural de empaquetado de datos.

### 3. Clave para el Examen SY0-701
Ecuación criptográfica en IPsec: IPsec + "confidentiality" (o encryption) = `ESP`. IPsec + "NO confidentiality" = **AH**.

---

## Pregunta 10: Extensión Segura de Redes / Secure Network Extension

### English Version
A system that uses a public network (such as the Internet) as a means to create encrypted private connections between remote locations is called:
* [ ] VLAN
* [ ] PAN
* [✅] **VPN**
* [ ] WWAN

### Versión en Español
Un sistema que utiliza una red pública (como Internet) como medio para crear conexiones privadas cifradas entre ubicaciones remotas se llama:
* [ ] VLAN
* [ ] PAN
* [✅] **VPN**
* [ ] WWAN

### 1. Explicación General
En lugar de rentar costosas líneas físicas dedicadas para interconectar oficinas geográficamente dispersas, las organizaciones modernas montan canales lógicos hiperseguros y fuertemente cifrados aprovechando la infraestructura pública existente de internet.

### 2. ¿Por qué es la correcta y no el resto?
* **Opción Correcta:** `[VPN (Virtual Private Network)]` encapsula y cifra el tráfico de datos simulando un enlace directo y privado (*encrypted private connections*) a través de un medio inseguro como el internet global (*public network*).
* **Análisis de los distractores:**
    * *VLAN:* Una Red de Área Local Virtual segmenta el tráfico de manera lógica dentro de un Switch local (Capa 2), pero no cifra datos ni opera a través de internet de forma nativa.
    * *PAN:* Una Red de Área Personal cubre distancias cortas en torno a un individuo (como conexiones Bluetooth entre un teléfono y audífonos).
    * *WWAN:* Una Red de Área Amplia Inalámbrica hace referencia a la infraestructura celular de datos móviles (como 4G o 5G), no a una conexión privada cifrada punto a punto.

### 3. Clave para el Examen SY0-701
Frase clave para el examen: "Public network" + "encrypted private connections" = `VPN`.

---

## Pregunta 11: Criptografía en tiempo real / Real-time cryptography

### English Version
Which protocol allows secure, real-time transmission of audio and video over an IP network?
* [ ] RTP
* [ ] SIP
* [✅] **SRTP**
* [ ] S/MIME

### Versión en Español
¿Qué protocolo permite la transmisión segura y en tiempo real de audio y video a través de una red IP?
* [ ] RTP
* [ ] SIP
* [✅] **SRTP**
* [ ] S/MIME

### 1. Explicación General
Los flujos de Voz sobre IP (VoIP) y las videoconferencias corporativas son altamente vulnerables a la interceptación ilegal. Sin embargo, los algoritmos de cifrado tradicionales añaden demasiado retraso (latencia), por lo que se requiere un protocolo optimizado para proteger flujos continuos multimedia en tiempo real sin romper la fluidez de la llamada.

### 2. ¿Por qué es la correcta y no el resto?
* **Opción Correcta:** `[SRTP (Secure Real-time Transport Protocol)]` provee cifrado (confidencialidad), protección contra reajuste de paquetes y autenticación al flujo multimedia crudo de audio y video que viaja por la red IP.
* **Análisis de los distractores:**
    * *RTP:* Es el protocolo original estándar para audio/video, pero carece por completo de mecanismos de seguridad; el contenido viaja expuesto en texto plano.
    * *SIP:* El Protocolo de Iniciación de Sesión se encarga exclusivamente de la señalización telefónica (establecer la llamada, timbrar, colgar), pero no transporta los datos multimedia de la voz humana.
    * *S/MIME:* Protocolo diseñado específicamente para firmar y cifrar correos electrónicos con archivos adjuntos, no tiene aplicación en multimedia interactiva.

### 3. Clave para el Examen SY0-701
Conceptos encadenados: "Real-time transmission" + "audio and video" + secure = `SRTP`.

---

## Pregunta 12: Blindaje Inalámbrico Estándar / Standard Wireless Shielding

### English Version
An encryption protocol primarily used in Wi-Fi networks implementing the WPA2 security standard is known as:
* [ ] TKIP
* [✅] **CCMP**
* [ ] WEP
* [ ] AES

### Versión en Español
Un protocolo de cifrado utilizado principalmente en redes Wi-Fi que implementan el estándar de seguridad WPA2 se conoce como:
* [ ] TKIP
* [✅] **CCMP**
* [ ] WEP
* [ ] AES

### 1. Explicación General
La seguridad de las transmisiones de ondas de radio en redes inalámbricas requiere protocolos que cifren los paquetes de datos en el aire. Con el lanzamiento de WPA2, la industria necesitaba un protocolo robusto basado en cifrados por bloques modernos para enterrar las debilidades del pasado.

### 2. ¿Por qué es la correcta y no el resto?
* **Opción Correcta:** `[CCMP]` es el protocolo criptográfico obligatorio estándar de WPA2. Emplea el algoritmo AES operando en modo contador con CBC-MAC para blindar los paquetes de Wi-Fi con máxima seguridad.
* **Análisis de los distractores:**
    * *TKIP:* Fue un protocolo de cifrado temporal lanzado para WPA1 con el fin de parchar el viejo WEP a través de actualizaciones de software, pero hoy está obsoleto y se considera inseguro debido a vulnerabilidades de RC4.
    * *WEP:* El protocolo original de Wi-Fi de los años 90; está completamente roto y se puede vulnerar en segundos. No pertenece a WPA2.
    * *AES:* Es el algoritmo matemático simétrico base subyacente, pero la pregunta pide explícitamente el *protocolo inalámbrico completo* que implementa dicho algoritmo, el cual es CCMP.

### 3. Clave para el Examen SY0-701
Igualdad obligatoria para redes inalámbricas: "Wi-Fi networks" + "WPA2 security standard" = `CCMP`.

---

## Pregunta 13: El Sucesor de SSL / The Successor to SSL

### English Version
Which cryptographic protocol is designed to provide secure communications over a computer network and is the successor to SSL?
* [ ] CCMP
* [✅] **TLS**
* [ ] AES
* [ ] HTTPS

### Versión en Español
¿Qué protocolo criptográfico está diseñado para proporcionar comunicaciones seguras a través de una red informática y es el sucesor de SSL?
* [ ] CCMP
* [✅] **TLS**
* [ ] AES
* [ ] HTTPS

### 1. Explicación General
Secure Sockets Layer (SSL) fue el pionero en asegurar el tráfico de internet, pero sus versiones originales acumularon fallas críticas de diseño. El organismo internacional IETF tomó el control de la tecnología, reescribiendo y estandarizando el protocolo bajo una nueva denominación técnica.

### 2. ¿Por qué es la correcta y no el resto?
* **Opción Correcta:** `[TLS (Transport Layer Security)]` es el heredero directo y evolución de SSL. Las versiones modernas de hoy (TLS 1.2 y 1.3) son las encargadas de asegurar las conexiones mundiales de la capa de transporte.
* **Análisis de los distractores:**
    * *CCMP:* Es un protocolo criptográfico restringido al ámbito de las tramas inalámbricas Wi-Fi (Capa 2), no un protocolo general de transporte de red.
    * *AES:* Es un algoritmo de cifrado simétrico puro (matemáticas), no un protocolo completo de comunicación de red para negociación de sesiones.
    * *HTTPS:* Es el protocolo de aplicación web que *utiliza* un túnel TLS por debajo para asegurar los datos, pero no es el sucesor directo del protocolo de transporte SSL en sí mismo.

### 3. Clave para el Examen SY0-701
Si la pregunta pide textualmente al "successor to SSL", la única respuesta correcta de la industria es `TLS`.

---

## Pregunta 14: Conceptos Básicos Invertidos / Inverted Ciphers Concepts

### English Version
Examples of techniques used to encrypt information include symmetric encryption (also called public-key encryption) and asymmetric encryption. True or False?
* [ ] True
* [✅] **False**

### Versión en Español
Los ejemplos de técnicas utilizadas para cifrar información incluyen el cifrado simétrico (también llamado cifrado de clave pública) y el cifrado asimétrico. ¿Verdadero o Falso?
* [ ] True
* [✅] **False**

### 1. Explicación General
Para aprobar la certificación, es crucial mapear de manera exacta los nombres técnicos alternativos de los dos paradigmas de la criptografía moderna sin confundir sus mecánicas de llaves compartidas o divididas.

### 2. ¿Por qué es la correcta y no el resto?
* **Opción Correcta:** `[False]` debido a que el enunciado afirma falsamente que el cifrado simétrico es el mismo que el de clave pública. La reality técnica es al revés: El cifrado **Simétrico** es de clave secreta/única (*secret-key*), y el cifrado **Asimétrico** es el que se denomina criptografía de clave pública (*public-key*).
* **Análisis de los distractores:**
    * *True:* Es incorrecto debido a que dar por verdadero el texto validaría una definición teórica errónea que reprobaría el examen.

### 3. Clave para el Examen SY0-701
Memoriza las parejas correctas: Simétrico = Llave única = Clave secreta (*Secret Key*). Asimétrico = Par de llaves = Clave pública / privada (*Public Key*). Cualquier cruce de estos términos es `False`.

---

## Pregunta 15: Relación del Par Asimétrico / Asymmetric Pair Relationship

### English Version
In asymmetric encryption, any message encrypted with a public key can only be decrypted by applying the same algorithm and a matching private key (and vice versa).
* [✅] **True**
* [ ] False

### Versión en Español
En el cifrado asimétrico, cualquier mensaje cifrado con una clave pública solo puede descifrarse aplicando el mismo algoritmo y una clave privada correspondiente (y viceversa).
* [✅] **True**
* [ ] False

### 1. Explicación General
El núcleo de la criptografía asimétrica es que las llaves operan como un candado y una llave física única. Están vinculadas matemáticamente mediante funciones trampa unidireccionales: lo que una de las llaves bloquea, únicamente la otra llave del mismo par exacto lo puede desbloquear.

### 2. ¿Por qué es la correcta y no el resto?
* **Opción Correcta:** `[True]` porque el enunciado es una verdad fundamental. Si uso la **clave pública** de un destinatario para cifrar un mensaje, garantizo la *confidencialidad*, ya que solo su **clave privada** correspondiente puede descifrarlo. El "viceversa" también es real: si cifro con mi clave privada, cualquiera con mi clave pública lo descifra, verificando mi identidad (*firma digital*).
* **Análisis de los distractores:**
    * *False:* Sería incorrecto ya que negaría el principio operativo básico sobre el cual se construyen los certificados digitales de todo el planeta.

### 3. Clave para el Examen SY0-701
Principio rector asimétrico: "Encrypted with public -> Decrypted ONLY with matching private" o viceversa es siempre una afirmación verdadera (`True`).

---

## Pregunta 16: Clasificación de Simétricos / Symmetric Classification

### English Version
Which of the following answers are NOT examples of symmetric encryption algorithms? (Select all that apply)
* [✅] **DHE**
* [ ] AES
* [✅] **ECC**
* [ ] DES
* [✅] **RSA**

### Versión en Español
¿Cuáles de las siguientes respuestas NO son ejemplos de algoritmos de cifrado simétrico? (Seleccione todas las que correspondan)
* [✅] **DHE**
* [ ] AES
* [✅] **ECC**
* [ ] DES
* [✅] **RSA**

### 1. Explicación General
Una de las habilidades más evaluadas en el examen CompTIA Security+ es la capacidad de clasificar una lista de siglas criptográficas en sus categorías correctas (Simétricos vs. Asimétricos / Algoritmos de Intercambio).

### 2. ¿Por qué es la correcta y no el resto?
* **Opciones Correctas:** `[DHE, ECC, y RSA]` porque la pregunta pide identificar los que **NO** son simétricos. Estos tres pertenecen estrictamente a la familia de criptografía asimétrica o protocolos de acuerdo de claves públicas.
* **Análisis de los distractores:**
    * *AES:* Es un algoritmo de cifrado simétrico por bloques (el estándar de la industria), por lo que no se selecciona.
    * *DES:* Es un algoritmo de cifrado simétrico por bloques antiguo de 56 bits, por ende queda descartado de la selección.

### 3. Clave para el Examen SY0-701
Memoriza los asimétricos principales para descartar rápido en listas: `RSA`, `ECC`, `DH` / `DHE` / `ECDHE` y `DSA`. Los demás suelen ser simétricos o hashes.

---

## Pregunta 17: Clasificación de Asimétricos / Asymmetric Classification

### English Version
Which of the answers listed below are NOT examples of asymmetric encryption algorithms? (Select all that apply)
* [✅] **AES**
* [ ] RSA
* [✅] **DES**
* [ ] D) ECC
* [✅] **IDEA**
* [✅] **RC4**

### Versión en Español
¿Cuáles de las respuestas enumeradas a continuación NO son ejemplos de algoritmos de cifrado asimétrico? (Seleccione todas las que correspondan)
* [✅] **AES**
* [ ] RSA
* [✅] **DES**
* [ ] ECC
* [✅] **IDEA**
* [✅] **RC4**

### 1. Explicación General
Caso inverso al ítem anterior. Aquí el objetivo es depurar la lista removiendo los algoritmos basados en pares de claves públicas/privadas y aislando los algoritmos de clave compartida única.

### 2. ¿Por qué es la correcta y no el resto?
* **Opciones Correctas:** `[AES, DES, IDEA, y RC4]` son correctas porque **NO** son asimétricos. Todos ellos son algoritmos de cifrado simétrico (AES, DES e IDEA procesan bloques de datos; RC4 procesa flujos continuos de bits).
* **Análisis de los distractores:**
    * *RSA:* Es el algoritmo asimétrico clásico por excelencia basado en factorización de números primos, por ende no se selecciona.
    * *ECC:* Criptografía de Curvas Elípticas, paradigma asimétrico moderno de llaves públicas de alta eficiencia, descartado de la selección.

### 3. Clave para el Examen SY0-701
`AES`, `DES`, `3DES`, `IDEA`, `Blowfish`, `Twofish` y `RC4` son todos miembros del club **Simétrico**.

---

## Pregunta 18: Protección de Llaves / Key Wrapping Concepts

### English Version
The term "KEK" refers to a type of cryptographic key used frequently in key management systems to add an extra layer of security by encrypting and decrypting other cryptographic keys. True or False?
* [✅] **True**
* [ ] False

### Versión en Español
El término "KEK" se refiere a un tipo de clave criptográfica utilizada frecuentemente en los sistemas de gestión de claves para añadir una capa adicional de seguridad al cifrar y descifrar otras claves criptográficas. ¿Verdadero o Falso?
* [✅] **True**
* [ ] False

### 1. Explicación General
En infraestructuras de almacenamiento masivo o nubes de datos, existen miles de llaves que cifran archivos locales (llamadas DEK o *Data Encryption Keys*). Almacenar estas llaves en texto plano dentro del mismo servidor es peligroso, por lo que se implementa una jerarquía donde una llave maestra sella a las demás.

### 2. ¿Por qué es la correcta y no el resto?
* **Opción Correcta:** `[True]` porque el enunciado es completamente verdadero. **KEK** significa *Key Encryption Key* (Clave de Cifrado de Clave). Su función exclusiva en seguridad es realizar el envoltorio de llaves (*key wrapping*), cifrando las llaves operativas de datos para que puedan ser almacenadas o movidas de forma segura.
* **Análisis de los distractores:**
    * *False:* Es incorrecto porque rechazaría una definición de arquitectura de almacenamiento criptográfico que está totalmente estandarizada por la industria.

### 3. Clave para el Examen SY0-701
Si el enunciado describe una clave cuyo rol es explícitamente "encrypting and decrypting other cryptographic keys", la respuesta siempre será `True` bajo el acrónimo de `KEK`.

---

## Pregunta 19: Algoritmos Eficientes en Móviles / Efficient Mobile Cryptography

### English Version
Which of the following asymmetric cryptographic algorithms provides the same level of security as RSA but with smaller key sizes?
* [ ] AES
* [✅] **ECC (Elliptic-Curve Cryptography)**
* [ ] Diffie-Hellman
* [ ] RSA

### Versión en Español
¿Cuál de los siguientes algoritmos criptográficos asimétricos proporciona el mismo nivel de seguridad que RSA pero con tamaños de clave más pequeños?
* [ ] AES
* [✅] **ECC (Criptografía de Curvas Elípticas)**
* [ ] Diffie-Hellman
* [ ] RSA

### 1. Explicación General
Los dispositivos móviles, sensores IoT y tarjetas inteligentes tienen recursos de hardware limitados (batería y CPU). Usar algoritmos asimétricos tradicionales como RSA requiere llaves muy largas (ej. 3072 bits) que ralentizan los cálculos. Para resolver esto, la industria adoptó matemáticas basadas en la estructura algebraica de curvas elípticas sobre campos finitos, logrando la misma resistencia con una fracción del esfuerzo de cómputo.

### 2. ¿Por qué es la correcta y no el resto?
* **Opción Correcta:** `[ECC]` es la respuesta porque una clave ECC de solo 256 bits ofrece una resistencia matemática equivalente a una clave RSA de 3072 bits. Esto reduce drásticamente el consumo de energía y el ancho de banda necesario para negociar conexiones seguras.
* **Análisis de los distractores:**
    * *AES:* Aunque usa llaves pequeñas (128/256 bits), es un algoritmo simétrico, por lo que no puede sustituir funcionalmente el rol asimétrico de RSA.
    * *Diffie-Hellman:* Es un protocolo dedicado estrictamente al intercambio de claves a través de un canal inseguro, no un algoritmo de cifrado general con optimización de llaves frente a RSA.
    * *RSA:* Es el algoritmo base con el que se está comparando el enunciado, por lo que autoseleccionarse carece de sentido lógico.

### 3. Clave para el Examen SY0-701
Relación matemática directa para el examen: "Asymmetric" + "smaller key sizes" (mismo nivel de seguridad que RSA) = `ECC`.

---

## Pregunta 20: Acrónimo de Curvas Elípticas / Elliptic Curve Acronym

### English Version
What is the acronym used for Elliptic-Curve Cryptography?
* [ ] EFS
* [✅] **ECC**
* [ ] Ephemeral
* [ ] ESP

### Versión en Español
¿Cuál es el acrónimo utilizado para la Criptografía de Curvas Elípticas?
* [ ] EFS
* [✅] **ECC**
* [ ] Ephemeral
* [ ] ESP

### 1. Explicación General
El examen Security+ requiere memorizar con total precisión los acrónimos estándar de la industria para evitar confusiones básicas durante las preguntas de escenarios complejos.

### 2. ¿Por qué es la correcta y no el resto?
* **Opción Correcta:** `[ECC]` corresponde exactamente a las siglas en inglés de *Elliptic-Curve Cryptography*.
* **Análisis de los distractores:**
    * *EFS:* Corresponde al *Encrypting File System* de Microsoft Windows (cifrado local de archivos).
    * *Ephemeral:* Es un término técnico (efímero) que describe llaves criptográficas temporales que se destruyen tras terminar una sesión, no un algoritmo en sí.
    * *ESP:* Significa *Encapsulating Security Payload*, un componente de la suite de protocolos IPsec.

### 3. Clave para el Examen SY0-701
Pregunta de reconocimiento directo: Elliptic-Curve Cryptography = `ECC`.

---

## Pregunta 21: El Concepto de Llaves Efímeras / Ephemeral Keys Definition

### English Version
In cryptography, a cryptographic key that is generated for each execution of a key-establishment process is called:
* [✅] **Ephemeral key**
* [ ] Symmetric key
* [ ] Static key
* [ ] Asymmetric key

### Versión en Español
En criptografía, una clave criptográfica que se genera para cada ejecución de un proceso de establecimiento de claves se llama:
* [✅] **Clave efímera (Ephemeral key)**
* [ ] Clave simétrica
* [ ] Clave estática
* [ ] Clave asimétrica

### 1. Explicación General
Si una organización usa la misma clave privada de su certificado de servidor para cifrar todo el tráfico web a lo largo de los años, y un atacante logra robar esa clave en el futuro, podría descifrar de manera retroactiva todas las comunicaciones pasadas grabadas de la red. Para evitar esto, los protocolos modernos generan llaves de sesión temporales que se destruyen inmediatamente después de usarse.

### 2. ¿Por qué es la correcta y no el resto?
* **Opción Correcta:** `[Ephemeral key]` es la definición técnica exacta de una clave de corta vida útil que se genera bajo demanda únicamente para una sesión específica (*each execution*), garantizando el Secreto Perfecto hacia Adelante (PFS).
* **Análisis de los distractores:**
    * *Symmetric key:* Describe la naturaleza de la llave (que es igual para cifrar y descifrar), pero no implica que deba ser temporal o destruirse tras el proceso.
    * *Static key:* Es el opuesto directo; una clave estática se mantiene fija y se reutiliza a lo largo de múltiples sesiones durante meses o años.
    * *Asymmetric key:* Describe un par de llaves pública/privada que típicamente son estáticas y persistentes en un certificado digital.

### 3. Clave para el Examen SY0-701
Indicador textual en el examen: "Generated for each execution" / "temporary" = `Ephemeral key`.

---

## Pregunta 22: Algoritmos de Intercambio de Llaves / Key Exchange Paradigms

### English Version
Which of the cryptographic algorithms listed below is used for secure sharing of cryptographic keys over an insecure channel?
* [ ] AES
* [ ] RSA
* [✅] **Diffie-Hellman**
* [ ] ECC

### Versión en Español
¿Cuál de los algoritmos criptográficos enumerados a continuación se utiliza para compartir de forma segura claves criptográficas a través de un canal inseguro?
* [ ] AES
* [ ] RSA
* [✅] **Diffie-Hellman**
* [ ] ECC

### 1. Explicación General
Dos extraños en internet necesitan comunicarse usando cifrado simétrico (el cual es muy rápido), pero no tienen una forma segura de acordar cuál será la contraseña secreta sin que un espía en la red la intercepte. Para resolver este problema, se requiere un método matemático que permita a ambas partes calcular el mismo secreto compartido de manera independiente sin enviar la clave directamente a través de la red.

### 2. ¿Por qué es la correcta y no el resto?
* **Opción Correcta:** `[Diffie-Hellman]` es un protocolo diseñado específicamente para el acuerdo de claves (*key exchange*). Utiliza aritmética modular para que ambos extremos computen la misma llave secreta simétrica final a la vista de todos, sin que los atacantes puedan deducirla.
* **Análisis de los distractores:**
    * *AES:* Es el algoritmo simétrico que utilizará la llave una vez acordada, pero no tiene la capacidad matemática de crear un canal inicial para compartirla.
    * *RSA:* Aunque se puede usar para el transporte de claves (cifrando la llave simétrica con la clave pública del servidor), su función primaria es el cifrado general y las firmas digitales, no es un protocolo puro de acuerdo simétrico como DH.
    * *ECC:* Es una familia matemática de criptografía asimétrica, no un algoritmo de intercambio de claves por sí solo (se requeriría específicamente su variante ECDH).

### 3. Clave para el Examen SY0-701
Conexión de conceptos clásica de CompTIA: "Sharing cryptographic keys" + "over an insecure channel" = `Diffie-Hellman`.

---

## Pregunta 23: Propiedades del Secreto Perfecto / Perfect Forward Secrecy

### English Version
Which of the following terms refers to a cryptographic property that ensures that a compromise of long-term keys does not compromise past session keys?
* [ ] Non-repudiation
* [✅] **PFS (Perfect Forward Secrecy)**
* [ ] Key wrapping
* [ ] Obfuscation

### Versión en Español
¿Cuál de los siguientes términos se refiere a una propiedad criptográfica que garantiza que el compromiso de claves a largo plazo no comprometa las claves de sesión pasadas?
* [ ] No repudio
* [✅] **PFS (Secreto Perfecto hacia Adelante)**
* [ ] Envoltorio de claves (Key wrapping)
* [ ] Ofuscación

### 1. Explicación General
En el pasado, si un gobierno confiscaba la clave privada principal de una empresa, podía descifrar gigabytes de tráfico de red capturado años atrás. Los criptógrafos crearon una regla de diseño: la clave maestra de largo plazo de un servidor solo debe servir para autenticar la identidad, mientras que el cifrado del tráfico debe depender de llaves efímeras independientes para cada sesión.

### 2. ¿Por qué es la correcta y no el resto?
* **Opción Correcta:** `[PFS (Perfect Forward Secrecy)]` es la propiedad de seguridad exacta que asegura que si un atacante roba la clave privada del servidor hoy, los datos que interceptó la semana pasada siguen estando completamente seguros porque las llaves de sesión pasadas no se derivaron de esa clave robada.
* **Análisis de los distractores:**
    * *Non-repudiation:* El no repudio garantiza que una entidad no pueda negar haber firmado un mensaje o haber realizado una transacción.
    * *Key wrapping:* Es el acto de cifrar una clave con otra (usando una KEK) para almacenamiento seguro, no una propiedad de aislamiento temporal de sesiones.
    * *Obfuscation:* Es el proceso de hacer que el código fuente o un mensaje sea difícil de entender para los humanos, careciendo de propiedades criptográficas matemáticas avanzadas.

### 3. Clave para el Examen SY0-701
Definición de oro para el examen: "Compromise of long-term keys does not compromise past session keys" = `PFS`.

---

## Pregunta 24: Escondiendo Datos en Archivos / Hiding Data Inside Files

### English Version
The practice of hiding a secret message inside a conventional file (such as a digital image) is called:
* [ ] Stegomalware
* [ ] Salt
* [✅] **Steganography**
* [ ] Obfuscation

### Versión en Español
La práctica de ocultar un mensaje secreto dentro de un archivo convencional (como una imagen digital) se llama:
* [ ] Stegomalware
* [ ] Sal (Salt)
* [✅] **Esteganografía (Steganography)**
* [ ] Ofuscación

### 1. Explicación General
Mientras que el cifrado altera el contenido de un mensaje para que sea incomprensible (llamando la atención sobre su existencia), esta disciplina busca pasar desapercibida por completo ocultando el mensaje dentro de los bits menos significativos de un archivo ordinario que parece inofensivo.

### 2. ¿Por qué es la correcta y no el resto?
* **Opción Correcta:** `[Steganography]` es la ciencia de ocultar información para que no se detecte que hay algo oculto en el medio portador (por ejemplo, meter un archivo de texto con contraseñas dentro de los pixeles de una foto `.jpg` de un paisaje).
* **Análisis de los distractores:**
    * *Stegomalware:* Es un término que describe al código malicioso que explota la esteganografía para descargar comandos sin activar las alarmas del antivirus, pero no es el nombre general de la práctica de ocultación de datos.
    * *Salt:* Son datos aleatorios que se inyectan a una contraseña antes de procesarla con un hash para evitar ataques de tablas arcoíris.
    * *Obfuscation:* Hace el contenido confuso y difícil de analizar, pero el archivo sigue siendo visible y sospechoso en su naturaleza, no oculto dentro de otro objeto.

### 3. Clave para el Examen SY0-701
Mapeo rápido de examen: "Hiding a secret message inside a conventional file / digital image" = `Steganography`.

---

## Pregunta 25: Ataques de Fuerza Bruta en Bloques / Block Cipher Exhaustive Search

### English Version
Which of the terms listed below refers to a cryptographic attack where the attacker tries every possible key until the correct one is found?
* [ ] Rainbow table
* [ ] Replay attack
* [✅] **Brute-force attack**
* [ ] Birthday attack

### Versión en Español
¿Cuál de los términos enumerados a continuación se refiere a un ataque criptográfico en el que el atacante prueba todas las claves posibles hasta encontrar la correcta?
* [ ] Tabla Arcoíris (Rainbow table)
* [ ] Ataque de denegación/reproducción (Replay attack)
* [✅] **Ataque de fuerza bruta (Brute-force attack)**
* [ ] Ataque de cumpleaños (Birthday attack)

### 1. Explicación General
Cuando un atacante no encuentra vulnerabilidades de diseño ni errores matemáticos en un algoritmo criptográfico, se ve obligado a recurrir al método de prueba y error a gran escala, probando combinaciones una por una de forma exhaustiva hasta dar con la clave exacta.

### 2. ¿Por qué es la correcta y no el resto?
* **Opción Correcta:** `[Brute-force attack]` define la técnica de adivinación exhaustiva que recorre todo el espacio de claves posibles (*tries every possible key*) de manera secuencial o aleatoria hasta romper el descifrado.
* **Análisis de los distractores:**
    * *Rainbow table:* Es una base de datos precomputada con hashes de contraseñas comunes utilizada para acelerar el descifrado de credenciales, no un intento en vivo de probar todas las llaves posibles de un algoritmo.
    * *Replay attack:* Consiste en capturar un paquete de red legítimo y retransmitirlo después para engañar a un sistema, no involucra adivinación de llaves.
    * *Birthday attack:* Explota la paradoja matemática del cumpleaños para encontrar colisiones en funciones hash (dos entradas distintas que generan el mismo hash), no busca adivinar una clave simétrica por fuerza bruta pura.

### 3. Clave para el Examen SY0-701
Frase clave: "Tries every possible key" = `Brute-force attack`.

---

## Pregunta 26: El Concepto Clave de Colisión / Hash Collision Definition

### English Version
A situation where two different inputs produce the same hash output is known as:
* [ ] Coincidence
* [✅] **Collision**
* [ ] Interception
* [ ] Clustering

### Versión en Español
Una situación en la que dos entradas diferentes producen el mismo resultado hash se conoce como:
* [ ] Coincidencia
* [✅] **Colisión (Collision)**
* [ ] Interceptación
* [ ] Agrupamiento (Clustering)

### 1. Explicación General
Una función hash ideal toma un bloque de datos de cualquier tamaño y genera una huella digital única de longitud fija. Si dos archivos completamente distintos (por ejemplo, un contrato legítimo y un virus) generan la misma huella hash exacta, el algoritmo se considera comprometido y no apto para validar la integridad de los datos.

### 2. ¿Por qué es la correcta y no el resto?
* **Opción Correcta:** `[Collision]` es el término técnico estandarizado globalmente para describir este fallo en la propiedad de resistencia de una función hash. Algoritmos viejos como MD5 y SHA-1 fueron retirados porque los atacantes aprendieron a forzar colisiones de manera controlada.
* **Análisis de los distractores:**
    * *Coincidence:* Es una palabra del lenguaje común que carece de precisión y rigor dentro del vocabulario de la seguridad informática profesional.
    * *Interception:* Es la acción de capturar datos en tránsito por la red, no tiene relación matemática con las propiedades de los hashes.
    * *Clustering:* En bases de datos o analítica se refiere al agrupamiento de datos similares, no al fallo criptográfico de coincidencia de hashes.

### 3. Clave para el Examen SY0-701
Relación fundamental: "Two different inputs = same hash output" = `Collision`.

---

## Pregunta 27: Explotando la Paradoja Matemática / Exploiting Probability Paradox

### English Version
Which cryptographic attack exploits the mathematics behind the probability of finding two random inputs that generate the same hash output?
* [ ] Replay attack
* [ ] Brute-force attack
* [ ] Downgrade attack
* [✅] **Birthday attack**

### Versión en Español
¿Qué ataque criptográfico explota las matemáticas detrás de la probabilidad de encontrar dos entradas aleatorias que generen el mismo resultado hash?
* [ ] Ataque de reproducción (Replay attack)
* [ ] Ataque de fuerza bruta (Brute-force attack)
* [ ] Ataque de degradación (Downgrade attack)
* [✅] **Ataque de cumpleaños (Birthday attack)**

### 1. Explicación General
La paradoja del cumpleaños demuestra que en un grupo de solo 23 personas, la probabilidad de que al menos dos de ellas compartan el mismo día de cumpleaños supera el 50%. En criptografía, esto significa que es mucho más fácil encontrar *dos archivos aleatorios cualesquiera* que tengan el mismo hash, que intentar adivinar qué archivo específico coincide con un hash predeterminado.

### 2. ¿Por qué es la correcta y no el resto?
* **Opción Correcta:** `[Birthday attack]` es el nombre del ataque matemático diseñado específicamente para romper la integridad de las funciones hash buscando colisiones de forma acelerada basándose en estas leyes de probabilidad.
* **Análisis de los distractores:**
    * *Replay attack:* No involucra cálculos matemáticos ni hashes; solo copia y vuelve a enviar tráfico capturado.
    * *Brute-force attack:* Busca adivinar una contraseña o clave simétrica específica probando de forma lineal, no se enfoca en la probabilidad de colisiones cruzadas.
    * *Downgrade attack:* Fuerza a un servidor a abandonar un protocolo seguro (ej. TLS 1.3) y rebajarse a usar una versión antigua y vulnerable (ej. SSL 3.0).

### 3. Clave para el Examen SY0-701
Conector de examen: "Probability of finding two random inputs with same hash" = `Birthday attack`.

---

## Pregunta 28: Degradación de Seguridad / Forcing Vulnerable Protocols

### English Version
A cryptographic attack where an attacker forces a system to abandon a secure mode of operation and resort to an older, less secure protocol is called:
* [✅] **Downgrade attack**
* [ ] Birthday attack
* [ ] Replay attack
* [ ] Brute-force attack

### Versión en Español
Un ataque criptográfico en el que un atacante obliga a un sistema a abandonar un modo de operación seguro y recurrir a un protocolo más antiguo y menos seguro se llama:
* [✅] **Ataque de degradación (Downgrade attack)**
* [ ] Ataque de cumpleaños (Birthday attack)
* [ ] Ataque de reproducción (Replay attack)
* [ ] Ataque de fuerza bruta (Brute-force attack)

### 1. Explicación General
Muchos sistemas modernos mantienen compatibilidad con versiones antiguas para no romper la comunicación con clientes obsoletos. Un atacante metido en medio de la red puede interceptar la negociación inicial y alterar los mensajes para engañar a ambas partes, haciéndoles creer que el otro no soporta los estándares modernos de cifrado y forzándolos a usar un protocolo viejo que el atacante ya sabe cómo romper.

### 2. ¿Por qué es la correcta y no el resto?
* **Opción Correcta:** `[Downgrade attack]` (o ataque de retroceso) describe perfectamente esta manipulación de la negociación donde se fuerza la transición desde un estado seguro hacia uno obsoleto (*older, less secure protocol*). Un ejemplo clásico es forzar conexiones HTTPS a usar versiones vulnerables de TLS o SSL (como en el ataque POODLE).
* **Análisis de los distractores:**
    * *Birthday attack:* Enfocado en colisiones de hashes, no altera configuraciones de protocolos activos en red.
    * *Replay attack:* Reenvía tramas de red guardadas, pero no altera los parámetros criptográficos de la sesión actual de soporte.
    * *Brute-force attack:* Intento masivo de adivinar llaves por medio de cómputo repetitivo, sin modificar capacidades del servidor.

### 3. Clave para el Examen SY0-701
Asociación rápida: "Forces a system to abandon a secure mode" + "older, less secure protocol" = `Downgrade attack`.

---

## Pregunta 29: Introducción a la Computación Cuántica / Intro to Quantum Threat

### English Version
Which of the following terms refers to a type of computing technology that utilizes qubits and has the potential to break many of the cryptographic algorithms currently in use?
* [ ] Centralized computing
* [ ] Edge computing
* [✅] **Quantum computing**
* [ ] Distributed computing

### Versión en Español
¿Cuál de los siguientes términos se refiere a un tipo de tecnología informática que utiliza qubits y tiene el potencial de romper muchos de los algoritmos criptográficos que se utilizan actualmente?
* [ ] Computación centralizada
* [ ] Computación perimetral (Edge computing)
* [✅] **Computación cuántica (Quantum computing)**
* [ ] Computación distribuida

### 1. Explicación General
Las computadoras tradicionales procesan la información usando bits binarios convencionales (que solo pueden ser 0 o 1). Una nueva generación de tecnología de procesamiento aprovecha la física cuántica, permitiendo que sus unidades lógicas existan en múltiples estados al mismo tiempo, lo que les permite resolver ciertos problemas matemáticos complejos a una velocidad inimaginable para la informática clásica.

### 2. ¿Por qué es la correcta y no el resto?
* **Opción Correcta:** `[Quantum computing]` utiliza la superposición y el entrelazamiento cuántico a través de bits cuánticos o *qubits*. Algoritmos cuánticos especializados (como el algoritmo de Shor) pueden factorizar números primos gigantescos en minutos, lo que destruirá la base matemática de algoritmos de clave pública actuales como RSA y ECC.
* **Análisis de los distractores:**
    * *Centralized computing:* Modelo clásico donde un solo servidor central realiza todo el procesamiento de datos ordinarios.
    * *Edge computing:* Paradigma que procesa los datos cerca del lugar donde se generan (en el perímetro de la red) para ahorrar ancho de banda, usando hardware tradicional.
    * *Distributed computing:* Red de computadoras tradicionales que dividen una tarea grande en partes más pequeñas compartiendo carga de trabajo, pero sin capacidades cuánticas.

### 3. Clave para el Examen SY0-701
Indicador de cambio tecnológico: "Utilizes qubits" + "break cryptographic algorithms" = `Quantum computing`.

---

## Pregunta 30: Blindaje para la Era Cuántica / Shielding for the Quantum Era

### English Version
What is the name of a cryptographic standard currently being developed to counter the threat of quantum computing?
* [ ] PKI
* [✅] **PQC (Post-Quantum Cryptography)**
* [ ] HSM
* [ ] ASLR

### Versión en Español
¿Cuál es el nombre de un estándar criptográfico que se está desarrollando actualmente para contrarrestar la amenaza de la computación cuántica?
* [ ] PKI
* [✅] **PQC (Criptografía Post-Cuántica)**
* [ ] HSM
* [ ] ASLR

### 1. Explicación General
Debido a que las computadoras cuánticas del futuro cercano podrán romper los algoritmos de clave pública que protegen los bancos, gobiernos e internet hoy en día, agencias internacionales como el NIST están liderando un proceso global para estandarizar nuevos algoritmos matemáticos que sigan siendo seguros tanto frente a computadoras convencionales como frente a ataques cuánticos.

### 2. ¿Por qué es la correcta y no el resto?
* **Opción Correcta:** `[PQC (Post-Quantum Cryptography)]` (también conocida como criptografía segura contra el análisis cuántico) engloba los nuevos algoritmos criptográficos basados en problemas matemáticos hipercomplejos (como la criptografía basada en retículos) que las computadoras cuánticas no pueden resolver de manera eficiente.
* **Análisis de los distractores:**
    * *PKI:* La Infraestructura de Claves Públicas es el marco actual que gestiona certificados digitales ordinarios y que precisamente necesita ser actualizado para usar algoritmos PQC.
    * *HSM:* Dispositivo físico de hardware corporativo que almacena llaves tradicionales, no un estándar criptográfico de algoritmos de nueva generación.
    * *ASLR:* *Address Space Layout Randomization* es una defensa a nivel de sistema operativo para prevenir ataques de desbordamiento de búfer en la memoria RAM, sin relación alguna con la criptografía de red.

### 3. Clave para el Examen SY0-701
Mapeo cronológico: "Counter the threat of quantum computing" = `PQC`.

---

## Pregunta 31: Concepto Fundamental del No Repudio / Non-Repudiation Definition

### English Version
Which architectural term describes a security service that provides proof of the origin and integrity of data, making it impossible for a sender to deny having sent a message?
* [ ] Accountability
* [ ] Confidentiality
* [ ] Availability
* [✅] **Non-repudiation**

### Versión en Español
¿Qué término arquitectónico describe un servicio de seguridad que proporciona prueba del origen y la integridad de los datos, haciendo imposible que un remitente niegue haber enviado un mensaje?
* [ ] Rendición de cuentas (Accountability)
* [ ] Confidencialidad (Confidentiality)
* [ ] Disponibilidad (Availability)
* [✅] **No repudio (Non-repudiation)**

### 1. Explicación General
En transacciones comerciales, contratos digitales o transferencias bancarias, es vital contar con un mecanismo legal e informático que impida que una persona firme un documento en línea y más tarde intente retractarse afirmando que ella no fue quien realizó dicha acción.

### 2. ¿Por qué es la correcta y no el resto?
* **Opción Correcta:** `[Non-repudiation]` es la propiedad criptográfica lograda a través de las firmas digitales (usando clave privada del autor) que enlaza indisolublemente la identidad de un individuo con el mensaje enviado, otorgando validez legal y técnica absoluta frente a reclamos de falsificación (*impossible for a sender to deny*).
* **Análisis de los distractores:**
    * *Accountability:* Asegura que las acciones de una entidad puedan ser rastreadas e identificadas en los registros de auditoría, pero no ofrece la prueba criptográfica dura de no retractación que ofrece el no repudio.
    * *Confidencialidad:* Se encarga únicamente de ocultar la información ante miradas no autorizadas mediante el cifrado, pero no valida quién la envió.
    * *Disponibilidad:* Garantiza que los sistemas y datos estén listos y accesibles para los usuarios autorizados cuando lo requieran.

### 3. Clave para el Examen SY0-701
Frase clave para identificar la propiedad: "Impossible for a sender to deny having sent a message" = `Non-repudiation`.

---

## Pregunta 32: Autenticación e Integridad Web / Web Cryptographic Validation

### English Version
Digital signatures provide: (Select 2 answers)
* [✅] **Authentication**
* [ ] Confidentiality
* [ ] Availability
* [✅] **Integrity**
* [ ] Obfuscation

### Versión en Español
Las firmas digitales proporcionan: (Seleccione 2 respuestas)
* [✅] **Autenticación (Authentication)**
* [ ] Confidencialidad (Confidentiality)
* [ ] Disponibilidad (Availability)
* [✅] **Integridad (Integrity)**
* [ ] Ofuscación (Obfuscation)

### 1. Explicación General
Una firma digital no oculta el contenido de un archivo. Su funcionamiento consiste en calcular el hash del documento y cifrar ese hash usando la clave privada del autor. Cualquier persona que reciba el archivo puede usar la clave pública del autor para verificar que el contenido coincide perfectamente y saber con total certeza quién lo generó.

### 2. ¿Por qué es la correcta y no el resto?
* **Opciones Correctas:** `[Authentication e Integrity]` porque la firma digital valida la identidad del emisor (**Autenticación**) y garantiza que el archivo no fue modificado por un tercero en el camino (**Integridad**), ya que cualquier cambio alteraría el hash final invalidando la firma.
* **Análisis de los distractores:**
    * *Confidencialidad:* Una firma digital por sí sola deja el texto del mensaje a la vista de cualquiera; se requiere cifrado complementario para lograr confidencialidad.
    * *Disponibilidad:* No influye en el tiempo de actividad o acceso a los servicios de red.
    * *Ofuscación:* No altera la legibilidad del código ni busca esconder datos mediante confusión de sintaxis.

### 3. Clave para el Examen SY0-701
Pilares que sostiene una firma digital: Firma digital = `Authentication` + `Integrity` (+ No repudio). Nunca confidencialidad.

---

## Pregunta 33: Cifrado Granular del Correo / Secure Email Standard

### English Version
A protocol that allows for encrypting and digitally signing email messages is called:
* [ ] HTTPS
* [ ] SRTP
* [✅] **S/MIME**
* [ ] IPsec

### Versión en Español
Un protocolo que permite cifrar y firmar digitalmente mensajes de correo electrónico se llama:
* [ ] HTTPS
* [ ] SRTP
* [✅] **S/MIME (Secure/Multipurpose Internet Mail Extensions)**
* [ ] IPsec

### 1. Explicación General
El correo electrónico tradicional viaja por internet en texto plano a través del protocolo SMTP. Para enviar información confidencial (como datos financieros o médicos) de extremo a extremo entre usuarios específicos, se necesita un estándar que empaquete de forma criptográfica el contenido y los archivos adjuntos dentro del propio cliente de correo.

### 2. ¿Por qué es la correcta y no el resto?
* **Opción Correcta:** `[S/MIME]` es el estándar técnico integrado en la mayoría de los clientes de correo empresarial (como Outlook). Utiliza certificados digitales X.509 para permitir tanto la firma digital (autenticación) como el cifrado (confidencialidad) del cuerpo del correo y sus anexos de forma directa.
* **Análisis de los distractores:**
    * *HTTPS:* Asegura el canal de comunicación entre el navegador web y el servidor, protegiendo la sesión de webmail, pero no cifra el mensaje de forma individual una vez que se guarda o se transfiere entre servidores de correo externos.
    * *SRTP:* Está diseñado exclusivamente para la transmisión en tiempo real de flujos de audio y video en redes IP (VoIP), ajeno al correo electrónico.
    * *IPsec:* Suite de seguridad para túneles a nivel de capa de red (Capa 3); cifra todo el tráfico entre dos routers de sucursal, pero no gestiona firmas ni cifrado individual de mensajes de correo electrónico en la capa de aplicación.

### 3. Clave para el Examen SY0-701
Asociación directa para el examen: "Encrypting and digitally signing email" = `S/MIME`.

---

## Pregunta 34: El Ciclo de Vida de los Certificados / Certs Lifecycle Validation

### English Version
Which of the following answers refers to a trusted third party that issues digital certificates?
* [ ] RA (Registration Authority)
* [ ] CRL (Certificate Revocation List)
* [✅] **CA (Certificate Authority)**
* [ ] PKI (Public Key Infrastructure)

### Versión en Español
¿Cuál de las siguientes respuestas se refiere a un tercero de confianza que emite certificados digitales?
* [ ] RA (Autoridad de Registro)
* [ ] CRL (Lista de Revocación de Certificados)
* [✅] **CA (Autoridad de Certificación)**
* [ ] PKI (Infraestructura de Claves Públicas)

### 1. Explicación General
Para que las transacciones en internet sean seguras, los navegadores web necesitan una forma de verificar que un sitio de comercio electrónico realmente pertenece a la empresa legítima y no a un estafador. Se delega esta verificación en entidades globales altamente auditadas que actúan como "notarios digitales" de confianza para certificar las llaves públicas del mundo.

### 2. ¿Por qué es la correcta y no el resto?
* **Opción Correcta:** `[CA (Certificate Authority)]` es la organización responsable de validar las identidades y firmar digitalmente los certificados para darles validez oficial ante los sistemas operativos del planeta (ej. DigiCert, Let's Encrypt).
* **Análisis de los distractores:**
    * *RA:* La Autoridad de Registro ayuda a la CA validando los documentos y la identidad de los solicitantes, pero la RA **no tiene permitido firmar ni emitir** los certificados finales directamente.
    * *CRL:* Es simplemente un archivo de texto publicado por la CA que contiene el listado de certificados que han sido cancelados o anulados antes de su fecha de vencimiento original.
    * *PKI:* Es el ecosistema global completo (compuesto por leyes, servidores, CAs, RAs, tokens y certificados) encargado de la gestión criptográfica, no la entidad emisora específica por sí misma.

### 3. Clave para el Examen SY0-701
Vínculo conceptual inmediato: "Trusted third party that issues digital certificates" = `CA`.

---

## Pregunta 35: Comprobación Rápida de Estado / Real-Time Certs Status Checking

### English Version
Which of the answers listed below refers to a method for checking the validity of a digital certificate in real-time?
* [ ] CSR
* [ ] CRL
* [✅] **OCSP (Online Certificate Status Protocol)**
* [ ] CA

### Versión en Español
¿Cuál de las respuestas enumeradas a continuación se refiere a un método para verificar la validez de un certificado digital en tiempo real?
* [ ] CSR (Solicitud de Firma de Certificado)
* [ ] CRL (Lista de Revocación de Certificados)
* [✅] **OCSP (Protocolo de Estado de Certificados en Línea)**
* [ ] CA (Autoridad de Certificación)

### 1. Explicación General
Cuando tu navegador web entra a un banco en línea, debe verificar al instante que el certificado digital de ese sitio no haya sido cancelado por robo de claves o hackeo de la empresa. Descargar listas gigantescas de certificados revocados consume demasiado ancho de banda y tiempo, por lo que se requiere un método de consulta rápida y directa.

### 2. ¿Por qué es la correcta y no el resto?
* **Opción Correcta:** `[OCSP]` permite al navegador enviar una consulta ligera con el número de serie del certificado directamente a un servidor respondedor de la CA. Este responde de inmediato con un estado simple: "Válido", "Revocado" o "Desconocido" (*checking in real-time*).
* **Análisis de los distractores:**
    * *CSR:* Es el archivo de solicitud inicial que genera un administrador para pedirle a una CA que le cree un certificado nuevo; no sirve para validar estados de certificados existentes.
    * *CRL:* Aunque sirve para verificar si un certificado fue cancelado, requiere descargar una lista pesada completa de forma periódica, por lo que no se considera una consulta interactiva optimizada en tiempo real.
    * *CA:* Es la entidad que emite el certificado, no el protocolo tecnológico específico de consulta de estado en tiempo real solicitado.

### 3. Clave para el Examen SY0-701
Conector de infraestructura clave: "Checking the validity" + "in real-time" = `OCSP`.

---

## Pregunta 36: El Ecosistema Completo de Llaves / The Complete Management Framework

### English Version
A system composed of hardware, software, people, policies, and procedures needed to create, manage, distribute, use, store, and revoke digital certificates is called:
* [ ] CA (Certificate Authority)
* [ ] RA (Registration Authority)
* [ ] CRL (Certificate Revocation List)
* [✅] **PKI (Public Key Infrastructure)**

### Versión en Español
Un sistema compuesto por hardware, software, personas, políticas y procedimientos necesarios para crear, administrar, distribuir, usar, almacenar y revocar certificados digitales se llama:
* [ ] CA (Autoridad de Certificación)
* [ ] RA (Autoridad de Registro)
* [ ] CRL (Lista de Revocación de Certificados)
* [✅] **PKI (Infraestructura de Claves Públicas)**

### 1. Explicación General
La seguridad basada en criptografía asimétrica no funciona de manera aislada con solo instalar un software. Requiere un marco estructural integral que abarque desde los servidores físicos ultra seguros que guardan las claves raíz, hasta las normativas legales, los ingenieros encargados de la administración y las herramientas de software de los sistemas operativos que confían en ellos.

### 2. ¿Por qué es la correcta y no el resto?
* **Opción Correcta:** `[PKI]` es el término global definitivo que representa a toda la infraestructura (*system composed of hardware, software, people, policies...*) encargada de gobernar el ciclo de vida completo de las claves públicas y los certificados a nivel mundial.
* **Análisis de los distractores:**
    * *CA:* Es simplemente una pieza (la entidad emisora) que opera dentro de toda la gran maquinaria de la PKI.
    * *RA:* Es otro componente secundario de apoyo para la validación de identidades dentro del sistema PKI.
    * *CRL:* Es solo uno de los tantos tipos de archivos o entregables generados por la infraestructura para publicar revocaciones.

### 3. Clave para el Examen SY0-701
Definición holística para recordar: "System composed of hardware, software, people, policies..." = `PKI`.

---

[[ExamCompass - Cuestionarios por Temas|⬅️ Volver a Cuestionarios por Temas]]