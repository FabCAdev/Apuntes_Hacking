---
tags:
  - "formato/apunte"
  - "hacking/fundamental"
  - "examen/test-especifico"
  - "gestion/estado/terminado"
---
Este apunte contiene el análisis detallado del cuestionario temático sobre seguridad inalámbrica, protocolos de autenticación (EAP, SAE, 802.1X) y servicios AAA de la plataforma ExamCompass para la certificación CompTIA Security+ (SY0-701), alineado con las respuestas oficiales del simulador.

---

## Pregunta 1: Fundamentos y Buenas Prácticas de SSID

### English Version
An SSID is a unique identifier (a.k.a. wireless network name) for a WLAN. Wireless networks advertise their presence by regularly broadcasting SSID in a special packet called beacon frame. In wireless networks with disabled security features, knowing the network SSID is enough to get access to the network. SSID also pinpoints the wireless router that acts as a WAP. Wireless routers from the same manufacturer are frequently configured with default (well-known) SSID names. Since multiple devices with the same SSID displayed on the list of available networks create confusion and encourage accidental access by unauthorized users (applies to networks that lack security), changing the default SSID is a recommended practice.  
* [✅] True
* [ ] False

### Versión en Español
Un SSID es un identificador único (también conocido como nombre de red inalámbrica) para una WLAN. Las redes inalámbricas anuncian su presencia transmitiendo regularmente el SSID en un paquete especial llamado trama de baliza (beacon frame). En redes inalámbricas con funciones de seguridad deshabilitadas, conocer el SSID de la red es suficiente para acceder a ella. El SSID también identifica el enrutador inalámbrico que actúa como WAP. Los enrutadores inalámbricos del mismo fabricante se configuran con frecuencia con nombres de SSID predeterminados (bien conocidos). Dado que varios dispositivos con el mismo SSID en la lista de redes disponibles crean confusión y fomentan el acceso accidental de usuarios no autorizados (se aplica a redes que carecen de seguridad), cambiar el SSID predeterminado es una práctica recomendada.
* [✅] Verdadero
* [ ] Falso

### 1. Explicación General
El SSID (*Service Set Identifier*) es el nombre legible por humanos que se le asigna a una red inalámbrica. Los puntos de acceso (WAP) transmiten este identificador de manera constante a través de paquetes de control conocidos como *beacon frames* (tramas de baliza) para que cualquier dispositivo dentro del alcance pueda listar la red y solicitar la conexión.

### 2. ¿Por qué es la correcta y no el resto?
El enunciado es completamente **Verdadero**. Mantener el SSID de fábrica (como "Linksys", "Netgear" o "Default") revela de forma directa la marca y potencialmente el modelo del hardware, permitiendo a los atacantes buscar vulnerabilidades específicas del firmware o intentar contraseñas de administración predeterminadas. Además, en redes abiertas, SSIDs idénticos facilitan ataques de suplantación.

### 3. Clave para el Examen SY0-701
CompTIA enfatiza que **ocultar el SSID (SSID Broadcasting Disabled) no es una medida de seguridad efectiva**. Es un ejemplo clásico de *seguridad por oscuridad*. Un atacante con un sniffer de paquetes (como `Wireshark` o `airodump-ng`) puede interceptar las tramas de asociación o desconexión (*probe requests/responses*) cuando un usuario legítimo se conecta a la red, revelando el SSID oculto en segundos.

---

## Pregunta 2: Negociación de Parámetros Inalámbricos

### English Version
For a wireless client to be able to connect to a network, the security type (e.g., WEP, WPA, WPA2, or WPA3) and encryption type (e.g., TKIP or AES) settings on the connecting host must match the corresponding wireless security settings on a WAP.  
* [✅] True
* [ ] False

### Versión en Español
Para que un cliente inalámbrico pueda conectarse a una red, los ajustes del tipo de seguridad (por ejemplo, WEP, WPA, WPA2 o WPA3) y del tipo de cifrado (por ejemplo, TKIP o AES) en el host de conexión deben coincidir con los ajustes de seguridad inalámbrica correspondientes en un WAP.
* [✅] Verdadero
* [ ] Falso

### 1. Explicación General
El establecimiento de un enlace Wi-Fi seguro requiere un proceso de negociación inicial (*handshake*). El cliente y el punto de acceso deben acordar de forma simétrica tanto el protocolo de autenticación como el algoritmo criptográfico para el intercambio de claves y el cifrado posterior del tráfico de datos.

### 2. ¿Por qué es la correcta y no el resto?
El enunciado es estrictamente **Verdadero**. Si un punto de acceso está configurado para operar únicamente con WPA2 utilizando cifrado AES, y un cliente intenta iniciar una sesión configurado con WPA clásico y TKIP, el WAP rechazará la solicitud de asociación durante la fase de validación de capacidades criptográficas.

### 3. Clave para el Examen SY0-701
Los WAPs permiten configurar modos de transición (como WPA2/WPA3 mixto) para soportar dispositivos antiguos. Sin embargo, desde la perspectiva de la seguridad, estos modos mixtos amplían la superficie de ataque al permitir ataques de degradación (*downgrade attacks*), donde un atacante fuerza al cliente a comunicarse usando el protocolo más débil disponible.

---

## Pregunta 3: Seguridad en Emparejamiento Bluetooth

### English Version
Which of the following answers refers to a security feature used in Bluetooth device pairing?
* [ ] SAE
* [✅] **PIN**
* [ ] MFA
* [ ] ACL

### Versión en Español
¿Cuál de las siguientes respuestas se refiere a una función de seguridad utilizada en el emparejamiento de dispositivos Bluetooth?
* [ ] SAE
* [✅] **PIN**
* [ ] MFA
* [ ] ACL

### 1. Explicación General
El proceso de emparejamiento (*pairing*) en Bluetooth establece un enlace confiable y cifrado entre dos dispositivos independientes de corto alcance. Para evitar la conexión no autorizada de dispositivos espía, el estándar utiliza mecanismos de autenticación basados en una clave de acceso temporal o estática.

### 2. ¿Por qué es la correcta y no el resto?
* **PIN** (*Personal Identification Number*) es el método clásico y nativo de emparejamiento. Exige ingresar o confirmar un código numérico coincidente en las pantallas de ambos dispositivos para validar la legitimidad del enlace físico.
* **SAE:** Es un mecanismo de autenticación exclusivo de redes inalámbricas Wi-Fi (específicamente WPA3-Personal).
* **MFA:** Autenticación de múltiples factores; es un concepto macro de gestión de identidad, no un control integrado de bajo nivel del protocolo de emparejamiento Bluetooth.
* **ACL:** Lista de control de acceso; se utiliza para el filtrado de paquetes de red o asignación de permisos sobre archivos.

### 3. Clave para el Examen SY0-701
Asocia Bluetooth con dos vectores de ataque críticos que CompTIA evalúa frecuentemente:
* **Bluejacking:** El envío de mensajes no solicitados o spam a dispositivos cercanos a través de Bluetooth. Es molesto, pero no compromete los datos.
* **Bluesnarfing:** El acceso y robo no autorizado de información personal (contactos, correos, imágenes) desde un dispositivo a través de una conexión Bluetooth vulnerable. Este sí representa un compromiso de confidencialidad severo.

---

## Pregunta 4: Seguridad Wi-Fi en Entornos SOHO (WPA3-SAE)

### English Version
Which of the following solutions would offer the strongest security for a small network that lacks an authentication server?
* [✅] **WPA3-SAE**
* [ ] WPA2-Enterprise
* [ ] WPA2-PSK
* [ ] WPA3-Enterprise

### Versión en Español
¿Cuál de las siguientes soluciones ofrecería la mayor seguridad para una red pequeña que carece de un servidor de autenticación?
* [✅] **WPA3-SAE**
* [ ] WPA2-Enterprise
* [ ] WPA2-PSK
* [ ] WPA3-Enterprise

### 1. Explicación General
En entornos SOHO (*Small Office / Home Office*) donde no se dispone de una infraestructura de servidores centralizada para validar identidades, se debe emplear un modo basado en llaves compartidas locales. El estándar de seguridad más moderno y robusto diseñado para este propósito es WPA3-Personal.

### 2. ¿Por qué es la correcta y no el resto?
* **WPA3-SAE** es la opción idónea. SAE (*Simultaneous Authentication of Equals*) es el protocolo de autenticación subyacente en WPA3-Personal. Ofrece la máxima protección criptográfica disponible sin requerir servidores adicionales.
* **WPA2/WPA3-Enterprise:** Se descartan automáticamente porque requieren de forma obligatoria un servidor centralizado (como RADIUS/802.1X), el cual el enunciado especifica que no existe.
* **WPA2-PSK:** Utiliza una clave precompartida tradicional que es altamente vulnerable a ataques de diccionario e interceptación fuera de línea (*offline cracking*) si el atacante captura el intercambio inicial de cuatro vías (*4-way handshake*).

### 3. Clave para el Examen SY0-701
Grábate el beneficio principal de **SAE**: implementa un protocolo de intercambio de claves autenticado por contraseña (*PAKE - Password-Authenticated Key Exchange*). Esto significa que **WPA3-SAE es inmune a ataques de diccionario pasivos y fuera de línea**. Incluso si un atacante captura el tráfico de inicio de sesión, no puede descifrarlo por fuerza bruta ni comprometer sesiones pasadas (ofrece *Forward Secrecy*).

---

## Pregunta 5: Arquitectura WPA2/WPA3 Enterprise

### English Version
What are the characteristic features of WPA2/WPA3 Enterprise mode? (Select 3 answers)
* [✅] Suitable for large corporate networks
* [ ] IEEE 802.1D
* [ ] Does not require an authentication server
* [✅] IEEE 802.1X
* [ ] Suitable for all types of wireless LANs
* [✅] Requires RADIUS authentication server

### Versión en Español
¿Cuáles son las características del modo WPA2/WPA3 Enterprise? (Seleccione 3 respuestas)
* [✅] Adecuado para grandes redes corporativas
* [ ] IEEE 802.1D
* [ ] No requiere un servidor de autenticación
* [✅] IEEE 802.1X
* [ ] Adecuado para todos los tipos de LAN inalámbricas
* [✅] Requiere un servidor de autenticación RADIUS

### 1. Explicación General
El modo Enterprise (Empresarial) está diseñado para delegar el control de acceso a una infraestructura central de TI. En lugar de utilizar una única contraseña estática compartida por toda la organización, cada usuario se autentica de forma individual utilizando sus credenciales corporativas (como cuentas de Active Directory/LDAP) o certificados digitales.

### 2. Análisis de Fallo y Descarte
* **Mi error aquí:** Marcar *IEEE 802.1D*. Este estándar pertenece al ámbito del switching clásico (define el funcionamiento de puentes de red y el protocolo *Spanning Tree* para evitar bucles), por lo que no tiene ninguna relación con la seguridad Wi-Fi corporativa.
* **Por qué son correctas las otras:** La tríada técnica empresarial obligatoria para asegurar redes corporativas requiere: **Aptitud para grandes redes**, adopción del estándar de control de acceso **IEEE 802.1X** y el requerimiento de un servidor **RADIUS** centralizado.

### 3. Clave para el Examen SY0-701
Fijo esta equivalencia inmediata en mi mente para el examen: **Enterprise Mode = 802.1X = Servidor RADIUS**. Si un caso de estudio me plantea la necesidad de revocar de inmediato el acceso Wi-Fi a un empleado despedido, de manera individual y sin afectar al resto de la organización, la solución obligatoria es un esquema Enterprise (802.1X).

---

## Pregunta 6: Protocolo de Cifrado Nativo en WPA3

### English Version
What is the name of the encryption protocol primarily used in Wi-Fi networks implementing the WPA3 security standard?
* [ ] AES-CCMP
* [ ] CBC-MAC
* [✅] **AES-GCMP**
* [ ] WPA-TKIP

### Versión en Español
¿Cuál de los siguientes acrónimos se refiere a un método de autenticación de clientes utilizado en el modo WPA3 Personal?
* [ ] AES-CCMP
* [ ] CBC-MAC
* [✅] **AES-GCMP**
* [ ] WPA-TKIP

### 1. Explicación General
Con la llegada de cada generación de seguridad inalámbrica, los algoritmos de confidencialidad e integridad de datos evolucionan para responder a la capacidad de cómputo moderna y mitigar las vulnerabilidades descubiertas en los cifrados anteriores.

### 2. ¿Por qué es la correcta y no el resto?
* **AES-GCMP** (*Galois/Counter Mode Protocol*) es el protocolo criptográfico robusto y nativo de WPA3. A diferencia de sus predecesores, calcula el cifrado y la autenticación de integridad de los datos de forma paralela y simétrica, haciéndolo mucho más eficiente y seguro.
* **AES-CCMP:** Es el protocolo de cifrado simétrico base utilizado por el estándar WPA2. Aunque WPA3 mantiene compatibilidad retrospectiva con este, GCMP es su estándar mandatorio de alta seguridad.
* **WPA-TKIP:** Un protocolo completamente obsoleto (*deprecated*) creado únicamente como parche temporal para mitigar las fallas de WEP; hoy en día está prohibido debido a debilidades estructurales.

### 3. Clave para el Examen SY0-701
CompTIA exige asociar directamente las parejas de protocolos y sus respectivos cifrados: **WPA2 se vincula con CCMP**, mientras que **WPA3 se vincula con GCMP**. Si una pregunta menciona niveles de protección criptográfica de grado gubernamental o militar en redes inalámbricas, apunta directo a GCMP.

---

## Pregunta 7: Autenticación en WPA3-Personal

### English Version
Which of the following acronyms refers to a client authentication method used in WPA3 Personal mode?
* [✅] **SAE**
* [ ] IKE
* [ ] PSK
* [ ] AES

### Versión en Español
¿Cuál del los siguientes de refiere a una estrategia de respaldo que se basa en la creación y el mantenimiento de copias de datos en tiempo real o casi en tiempo real en un sistema separado?
* [✅] **SAE**
* [ ] IKE
* [ ] PSK
* [ ] AES

### 1. Explicación General
El método de autenticación determina el mecanismo de verificación que el cliente inalámbrico y el punto de acceso ejecutan en los primeros instantes de la conexión para demostrar que conocen la clave correcta, sin llegar a transmitir dicha clave en texto plano ni exponerla de forma matemática directa por el aire.

### 2. ¿Por qué es la correcta y no el resto?
* **SAE** (*Simultaneous Authentication of Equals*) es el mecanismo oficial que reemplaza al viejo sistema PSK en el modo personal de WPA3, protegiendo al sistema contra interceptaciones maliciosas.
* **PSK:** *Pre-Shared Key* (Clave precompartida). Es el método de autenticación de WPA2-Personal, el cual quedó expuesto a ataques de fuerza bruta fuera de línea a través de la captura del handshake.
* **IKE:** Protocolo de intercambio de claves de Internet, utilizado para el establecimiento de túneles VPN IPsec, no para conexiones Wi-Fi de área local.
* **AES:** Es el algoritmo de cifrado simétrico encargado de empaquetar los datos cifrados, no un método de autenticación o validación de identidad.

### 3. Clave para el Examen SY0-701
Cuidado con confundir la función de cada acrónimo: **SAE autentica** (valida que el cliente conoce la clave e impide ataques de diccionario fuera de línea), mientras que **AES-GCMP cifra** (mantiene la confidencialidad de la información mientras viaja por las ondas de radio).

---

## Pregunta 8: Características Operativas del Protocolo RADIUS

### English Version
What are the characteristic features of RADIUS? (Select 3 answers)
* [✅] Primarily used for network access
* [ ] Encrypts the entire payload of the access-request packet
* [✅] Combines authentication and authorization
* [✅] Encrypts only the password in the access-request packet
* [ ] Primarily used for device administration
* [ ] Separates authentication and authorization

### Versión en Español
¿Cuáles son las características de RADIUS? (Seleccione 3 respuestas)
* [✅] Se utiliza principalmente para el acceso a la red
* [ ] Cifra toda la carga útil del paquete de solicitud de acceso
* [✅] Combina autenticación y autorización
* [✅] Cifra solo la contraseña en el paquete de solicitud de acceso
* [ ] Se utiliza principalmente para la administración de dispositivos
* [ ] Separa la autenticación y la autorización

### 1. Explicación General
RADIUS (*Remote Authentication Dial-In User Service*) es un protocolo de red clásico de la arquitectura AAA (Autenticación, Autorización y Auditoría). Se utiliza de forma masiva para centralizar la validación de usuarios que buscan ingresar a la infraestructura de red a través de conexiones Wi-Fi empresariales, puertos de switches (*802.1X*) o túneles VPN.

### 2. ¿Por qué falló tu respuesta?
Elegiste que *cifra toda la carga útil* y que *separa la autenticación y autorización*. Esos atributos corresponden en realidad a **TACACS+** (un protocolo propietario de Cisco diseñado específicamente para la administración de dispositivos de red). 

Las características reales de RADIUS seleccionadas de forma correcta reflejan que **se usa para el acceso a la red**, une los procesos lógicos de **autenticación y autorización** en un solo paso de comunicación para agilizar el rendimiento, y por herencia histórica **solo cifra el campo de la contraseña**, dejando el campo del nombre de usuario visible en texto plano dentro del paquete de solicitud de acceso (*Access-Request*).

### 3. Clave para el Examen SY0-701
Esta tabla comparativa es una fija en el examen de CompTIA y debes dominarla:

| Atributo | RADIUS | TACACS+ |
|---|---|---|
| **Propósito principal** | Acceso de usuarios a la red (Wi-Fi 802.1X, VPN) | Administración de dispositivos (comandos en routers/switches) |
| **Arquitectura** | Combina Autenticación y Autorización | Separa Autenticación de la Autorización |
| **Cifrado** | Solo cifra el campo de la *contraseña* | Cifra la *totalidad* del paquete (toda la carga útil) |
| **Capa de Transporte** | UDP (puertos 1812 / 1813) | TCP (puerto 49) |

---

## Pregunta 9: Jerarquía de Seguridad Inalámbrica

### English Version
Which of the wireless encryption schemes listed below offers the highest level of protection?
* [ ] WPS
* [✅] **WPA3**
* [ ] AES
* [ ] TKIP

### Versión en Español
¿Cuál de los esquemas de cifrado inalámbrico enumerados a continuación ofrece el nivel más alto de protección?
* [ ] WPS
* [✅] **WPA3**
* [ ] AES
* [ ] TKIP

### 1. Explicación General
La evolución de los estándares dictados por la *Wi-Fi Alliance* progresa de manera lineal y cronológica, donde cada nueva especificación soluciona los fallos de diseño estructural y las debilidades matemáticas descubiertas en las tecnologías de las generaciones previas.

### 2. ¿Por qué es la correcta y no el resto?
* **WPA3** es la respuesta correcta al consolidar el nivel más alto de protección comercial disponible hoy en día, haciendo obligatorios el uso de SAE para el entorno personal, 802.1X protegido para el empresarial y cifrado AES-GCMP de forma nativa.
* **WPS:** *Wi-Fi Protected Setup*. No es un cifrado, sino un mecanismo de emparejamiento rápido por botón o PIN de 8 dígitos que es críticamente vulnerable a ataques de fuerza bruta automatizados. Debe desactivarse en entornos corporativos.
* **TKIP / WEP:** Protocolos obsoletos e inseguros que pueden ser vulnerados en minutos por herramientas básicas de auditoría.
* **AES:** Es un algoritmo base de cifrado simétrico de bloques, no representa un estándar o esquema integral de arquitectura inalámbrica completo por sí solo.

### 3. Clave para el Examen SY0-701
Si una pregunta te pide ordenar o seleccionar el protocolo de mayor seguridad para mitigar riesgos, recuerda la jerarquía de peor a mejor: `WEP` < `WPA` < `WPA2` < `WPA3`.

---

## Pregunta 10: Protocolos Heredados y Riesgo de Proveedor (LEAP)

### English Version
Which of the following answers refers to a deprecated wireless authentication protocol developed by Cisco?
* [ ] PEAP
* [ ] EAP-TTLS
* [✅] **LEAP**
* [ ] EAP-TLS

### Versión en Español
¿Cuál de las siguientes respuestas se refiere a un protocolo de autenticación inalámbrica obsoleto desarrollado por Cisco?
* [ ] PEAP
* [ ] EAP-TTLS
* [✅] **LEAP**
* [ ] EAP-TLS

### 1. Explicación General
En los primeros años del despliegue inalámbrico empresarial, ante el colapso de la seguridad de WEP, ciertos fabricantes desarrollaron extensiones propietarias cerradas para subsanar los riesgos rápidamente. Sin embargo, el paso del tiempo reveló fallas estructurales severas en estos parches propietarios, obligando a su desuso.

### 2. ¿Por qué es la correcta y no el resto?
* **LEAP** (*Lightweight Extensible Authentication Protocol*) fue la solución propietaria desarrollada por Cisco. Hoy en día está completamente obsoleta (*deprecated*) debido a que es vulnerable a ataques de diccionario dinámicos dirigidos contra el protocolo de autenticación MS-CHAPv2 modificado que utiliza por debajo.
* **EAP-TLS / PEAP / EAP-TTLS:** Son protocolos basados en estándares de la industria completamente abiertos, vigentes y seguros que utilizan túneles TLS fuertemente cifrados para proteger las credenciales.

### 3. Clave para el Examen SY0-701
Cuando veas **LEAP** listado en una pregunta de CompTIA, trátalo de inmediato como un indicador de **riesgo tecnológico heredado (legacy risk)**. La respuesta orientada a la remediación técnica siempre consistirá en migrar la infraestructura hacia protocolos abiertos basados en certificados de clave pública, como PEAP o EAP-TLS.

---

## Pregunta 11: Encapsulación y Túneles TLS en Autenticación (PEAP)

### English Version
Which of the answers listed below refers to an open standard wireless network authentication protocol that enhances security by encapsulating authentication process within an encrypted TLS tunnel?
* [✅] **PEAP**
* [ ] EAP
* [ ] LEAP
* [ ] RADIUS

### Versión en Español
¿Cuál de las respuestas enumeradas a continuación se refiere a un protocolo de autenticación de red inalámbrica de estándar abierto que mejora la seguridad al encapsular el proceso de autenticación dentro de un túnel TLS cifrado?
* [✅] **PEAP**
* [ ] EAP
* [ ] LEAP
* [ ] RADIUS

### 1. Explicación General
Para proteger las credenciales de los usuarios e impedir que sean capturadas del aire en un entorno corporativo 802.1X, el protocolo debe envolver de forma segura la fase de autenticación. Esto se logra levantando primero una sesión cifrada segura (un túnel TLS) utilizando un certificado digital instalado del lado del servidor.

### 2. Análisis de Fallo y Descarte
* **Mi error aquí:** Caer en la trampa común de elegir *RADIUS*. RADIUS es el servidor de backend (o el servicio de red) que aloja y procesa la base de datos de identidades, pero no es el protocolo criptográfico encargado de negociar y construir la encapsulación del túnel inalámbrico desde el cliente Wi-Fi.
* **Por qué la correcta es PEAP:** El protocolo específico encargado de encapsular el flujo de autenticación dentro de un túnel TLS seguro es **PEAP** (*Protected Extensible Authentication Protocol*).

### 3. Clave para el Examen SY0-701
CompTIA evalúa minuciosamente las diferencias de despliegue entre las variantes de EAP. Grabo esta distinción para el examen:
* **EAP-TLS:** Requiere la instalación de certificados digitales **tanto en el servidor de autenticación como en cada uno de los dispositivos clientes** (Máxima seguridad, pero infraestructura de PKI muy costosa).
* **PEAP:** **Solo requiere un certificado digital en el servidor**. El dispositivo cliente valida al servidor mediante este certificado y luego el usuario puede autenticarse de forma segura transmitiendo sus credenciales tradicionales (usuario y contraseña) por dentro del túnel protegido.

---

[[ExamCompass - Cuestionarios por Temas|⬅️ Volver a Cuestionarios por Temas]]