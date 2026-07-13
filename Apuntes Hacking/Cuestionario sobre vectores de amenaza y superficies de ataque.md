---
tags:
  - "formato/apunte"
  - "hacking/fundamental"
  - "examen/test-especifico"
  - "gestion/estado/terminado"
---
Este apunte contiene el análisis detallado del cuestionario temático sobre superficies de ataque, vectores de amenaza y canales de entrega de la plataforma ExamCompass para la certificación CompTIA Security+ (SY0-701), alineado con las respuestas oficiales del simulador.

---

## Pregunta 1: Superficie de Ataque vs. Vectores de Amenaza

### English Version
Select the correct statement regarding the difference between cybersecurity attack surfaces and threat vectors.
* [✅] **True**
* [ ] False

### Versión en Español
Seleccione la afirmación correcta con respecto a la diferencia entre superficies de ataque y vectores de amenaza.
* [✅] **Verdadero**
* [ ] Falso

### 1. Explicación General
La superficie de ataque abarca todos los puntos donde un sistema está expuesto y es vulnerable a interacciones externas. El vector de amenaza es la ruta o el mecanismo exacto que el atacante utiliza para viajar a través de esa superficie e infiltrarse en el objetivo.

### 2. ¿Por qué es la correcta y no el resto?
Es **Verdadero** porque el texto técnico mapea con precisión los conceptos fundamentales de CompTIA: las interfaces, puertos abiertos o fallas lógicas/físicas constituyen la superficie (la exposición total), mientras que técnicas como el phishing, el vishing o los exploits de malware actúan como los medios de transporte específicos (los vectores). Marcar "Falso" negaría estas definiciones estándar de la industria.

### 3. Clave para el Examen SY0-701
En el examen, identifique **Superficie** como el mapa total de vulnerabilidades y puntos de contacto (*qué está expuesto*) y **Vector** como el método de transporte, entrega o explotación (*cómo se viaja o se ejecuta el ataque*).

---

## Pregunta 2: Vectores de Acceso Inicial vía Correo Electrónico

### English Version
Identify which of the options refers to a threat vector commonly delivered through email.
* [ ] Phishing / BEC attacks
* [ ] Malicious links
* [ ] Malware attachments
* [✅] **All of the above**

### Versión en Español
Identifique cuál de las opciones se refiere a un vector de amenaza comúnmente entregado a través del correo electrónico.
* [ ] Suplantación de identidad / Ataques BEC
* [ ] Enlaces maliciosos
* [ ] Archivos adjuntos de malware
* [✅] **Todo lo anterior**

### 1. Explicación General
El correo electrónico sigue siendo el vector de acceso inicial más explotado en seguridad corporativa debido a su capacidad intrínseca de combinar tácticas de engaño psicológico con cargas útiles técnicas (payloads).

### 2. ¿Por qué es la correcta y no el resto?
**Todo lo anterior** es la opción correcta debido a que el ecosistema del correo no se limita a una sola categoría de peligro. Puede transportar fraudes financieros puros basados en texto sin archivos (BEC), redirecciones web externas (enlaces maliciosos) o código ejecutable directo camuflado (adjuntos). Seleccionar cualquiera de las otras de forma aislada dejaría el vector de correo incompleto.

### 3. Clave para el Examen SY0-701
CompTIA suele presentar escenarios de correo electrónico donde el atacante mezcla ingeniería social con un componente técnico. Siempre evalúe si el vector de ataque incluye tanto el mensaje manipulado como el medio técnico de ejecución posterior.

---

## Pregunta 3: Amenazas Basadas en Servicios de Mensajería Corta (SMS)

### English Version
Select the specific term used to describe communication-based threats over Short Message Service (SMS).
* [ ] Phishing
* [ ] Vishing
* [✅] **Smishing**
* [ ] Pharming

### Versión en Español
Seleccione el término específico utilizado para describir las amenazas de comunicación a través del Servicio de Mensajes Cortos (SMS).
* [ ] Phishing
* [ ] Vishing
* [✅] **Smishing**
* [ ] Pharming

### 1. Explicación General
Los ataques de ingeniería social reciben nombres y clasificaciones específicas en la taxonomía de seguridad según el canal tecnológico exacto que el atacante elija para interactuar con la víctima.

### 2. ¿Por qué es la correcta y no el resto?
**Smishing** es el término correcto porque nace directamente de la fusión conceptual de *SMS* y *Phishing*. Las otras opciones se descartan por sus medios: *Phishing* se asocia al formato general (correo electrónico), *Vishing* se realiza exclusivamente mediante llamadas de voz y *Pharming* consiste en manipular servidores DNS o archivos `hosts` locales para redirigir tráfico legítimo.

### 3. Clave para el Examen SY0-701
Si el enunciado de una pregunta menciona el uso de teléfonos celulares, mensajes de texto, SMS o enlaces de mensajería celular para engañar a un usuario simulando alertas bancarias o de paquetería, la respuesta técnica obligatoria es Smishing.

---

## Pregunta 4: Vectores de Riesgo en Plataformas de Mensajería Instantánea

### English Version
Choose the answer that represents a potential threat vector within instant messaging platforms.
* [ ] Spoofing / Account hijacking
* [ ] Malware distribution
* [ ] Malicious links/attachments
* [✅] **All of the above**

### Versión en Español
Elija la respuesta que represente un vector de amenaza potencial dentro de las plataformas de mensajería instantánea.
* [ ] Ataques de suplantación / Secuestro de cuentas
* [ ] Distribución de malware
* [ ] Enlaces/archivos adjuntos maliciosos
* [✅] **Todo lo anterior**

### 1. Explicación General
Las plataformas de mensajería instantánea modernas (como Slack, Teams o WhatsApp) han ampliado la superficie de ataque corporativa al permitir comunicaciones directas que a menudo saltan o evaden los filtros perimetrales tradicionales del correo electrónico.

### 2. ¿Por qué es la correcta y no el resto?
**Todo lo anterior** es la opción correcta porque estas herramientas permiten el despliegue de ataques complejos en cadena: un atacante secuestra una cuenta legítima mediante robo de tokens o ingeniería social (*account hijacking*), y desde esa identidad comprometida procede a distribuir malware o enviar enlaces maliciosos aprovechando la relación de confianza establecida.

### 3. Clave para el Examen SY0-701
El peligro crítico de la mensajería instantánea en los entornos empresariales es la **confianza implícita**. Los usuarios tienden a hacer clic en enlaces internos de Teams o Slack mucho más rápido y con menos sospecha que en los del correo tradicional.

---

## Pregunta 5: Vectores de Amenaza Basados en Imágenes

### English Version
Select the three (3) options that represent threat vectors directly associated with images.
* [✅] **Steganography**
* [ ] BEC attacks
* [✅] **Image spoofing (deepfakes)**
* [ ] Brand spoofing
* [✅] **Images with embedded malware**

### Versión en Español
Seleccione las tres (3) respuestas que se refieren a ejemplos de vectores de amenazas basados en imágenes. (Seleccione 3 respuestas)
* [✅] **Esteganografía**
* [ ] Ataques BEC
* [✅] **Suplantación de imágenes (deepfakes)**
* [ ] Suplantación de marca
* [✅] **Imágenes con malware incrustado**

### 1. Explicación General
Los archivos de imagen pueden ser utilizados como vectores tanto de manera técnica (ocultando código en sus metadatos o píxeles) como de manera visual/psicológica (manipulando el contenido de la imagen para evadir controles o engañar humanos).

### 2. ¿Por qué es la correcta y no el resto?
* **Esteganografía:** Oculta datos binarios dentro de los bits de menor peso de los píxeles de una imagen sin alterar su apariencia.
* **Imágenes con malware:** Aprovechan vulnerabilidades de desbordamiento de búfer en los códecs de los visores de imágenes para ejecutar código local.
* **Deepfakes:** Altera el vector visual para saltar controles de identidad biométricos o engañar personal mediante ingeniería social de video/foto.
* Los ataques *BEC* y la *Suplantación de marca* se descartan porque son fraudes de identidad basados en procesos corporativos, no en la estructura o manipulación de un archivo gráfico.

### 3. Clave para el Examen SY0-701
Cuando el examen describa el acto de ocultar información confidencial, malware o comandos de un servidor C2 dentro de un archivo de imagen aparentemente inofensivo (como un `.png` o `.jpg`) para evadir los sistemas DLP, la respuesta técnica obligatoria es **Esteganografía**.

---

## Pregunta 6: Categorización de Vectores Basados en Archivos

### English Version
Identify the comprehensive option that categorizes file-based threat vectors.
* [ ] Malicious macros / PDF exploits
* [ ] Compressed archives (ZIP, RAR) / Executables
* [ ] Infected images or web scripts
* [✅] **All of the above**

### Versión en Español
¿Cuál de las respuestas que aparecen a continuación se refiere a un vector de amenaza basado en archivos?
* [ ] Explotación de archivos PDF / Macros maliciosas en documentos
* [ ] Archivos comprimidos (ZIP, RAR) / Archivos ejecutables maliciosos
* [ ] Imágenes infectadas / Scripts maliciosos en páginas web
* [✅] **Todo lo anterior**

### 1. Explicación General
Un vector basado en archivos aprovecha cualquier formato o contenedor del sistema de archivos que un sistema operativo o aplicación deba procesar, leer o ejecutar de forma local en el host del usuario.

### 2. ¿Por qué es la correcta y no el resto?
**Todo lo anterior** es la única opción completa debido a que los atacantes modifican y empaquetan amenazas en múltiples extensiones de archivo (`.pdf`, `.docm`, `.zip`, `.exe`) para eludir las firmas estáticas de los antivirus tradicionales. Las opciones individuales solo describen formatos aislados y no la totalidad del vector.

### 3. Clave para el Examen SY0-701
Preste especial atención a las **Macros maliciosas en archivos de Office**. Se consideran un vector basado en archivos crítico porque ejecutan scripts automáticos (como PowerShell o VBA) en el momento exacto en que el usuario habilita el contenido del documento.

---

## Pregunta 7: Vectores de Ataque mediante Canales Telefónicos (Voz)

### English Version
Choose the specific threat vector term utilized for voice-over-telephony scams.
* [ ] Smishing
* [ ] Pharming
* [✅] **Vishing**
* [ ] Phishing

### Versión en Español
¿Cuál de las siguientes opciones de respuesta es un ejemplo de un tipo de vector de amenaza típico para la comunicación por voz?
* [ ] Smishing
* [ ] Farmacia (Pharming)
* [✅] **Vishing**
* [ ] Suplantación de identidad (Phishing)

### 1. Explicación General
El uso de canales telefónicos tradicionales o de voz sobre IP (VoIP) permite a los atacantes aplicar técnicas de urgencia, intimidación y autoridad mediante la interacción humana directa en tiempo real.

### 2. ¿Por qué es la correcta y no el resto?
**Vishing** es la respuesta correcta ya que proviene del concepto *Voice Phishing*. Las demás opciones se descartan por sus canales específicos de entrega: *Smishing* requiere mensajería corta SMS, *Pharming* altera registros DNS o archivos locales, y *Phishing* se asocia principalmente al formato escrito de correo electrónico.

### 3. Clave para el Examen SY0-701
Si una pregunta describe a un atacante llamando por teléfono a un empleado de la mesa de ayuda (*Help Desk*) simulando ser un alto ejecutivo enfadado que olvidó su contraseña para forzar un restablecimiento inmediato, el vector es Vishing.

---

## Pregunta 8: Vectores Asociados a Dispositivos de Almacenamiento Extraíbles

### English Version
Select the two (2) threat vectors directly related to the deployment of removable storage devices.
* [ ] Pretexting
* [  ] **Malware delivery**
* [ ] Watering hole attacks
* [  ] **Data exfiltration**
* [ ] Social engineering attacks

### Versión en Español
Ejemplos de vectores de amenaza directamente relacionados con el uso de dispositivos extraíbles incluyen: (Seleccione 2 respuestas)
* [ ] Pretextos (Pretexting)
* [  ] **Entrega de malware**
* [ ] Ataques en los abrevaderos (Watering hole)
* [  ] **Exfiltración de datos**
* [ ] Ataques de ingeniería social

### 1. Explicación General
Los medios de almacenamiento extraíbles (como las memorias USB o discos externos) son vectores físicos altamente peligrosos porque saltan por completo las defensas perimetrales y los firewalls de la red corporativa al conectarse directamente en la zona de confianza interna.

### 2. ¿Por qué es la correcta y no el resto?
Las dos opciones seleccionadas operan en los dos sentidos del riesgo técnico de hardware: sirven como vector de entrada para la **entrega de malware** (al conectarse físicamente e iniciar la ejecución de controladores o archivos) y como vector de salida para la **exfiltración de datos** (copiar archivos confidenciales saltándose la monitorización de red). *Pretexting*, *Watering hole* y los ataques generales de ingeniería social son vectores lógicos o psicológicos basados en red o interacción humana, no en hardware local.

### 3. Clave para el Examen SY0-701
Los dispositivos USB son el vector por excelencia para atacar sistemas aislados de internet (entornos **Air-Gapped**), infectando equipos o robando información confidencial sin dejar rastro en los logs de los firewalls perimetrales.

---

## Pregunta 9: Vectores de Software Basados en el Cliente (Client-Based)

### English Version
Select all options that correspond strictly to client-based software threat vectors.
* [✅] **Drive-by download via web browser**
* [✅] **Malicious macro**
* [ ] Network protocol or device vulnerability
* [✅] **USB-based attack**
* [✅] **Infected executable file**
* [✅] **Malicious attachment in email application**

### Versión en Español
¿Cuáles de las respuestas que aparecen a continuación se refieren a vectores de amenazas de software basados en el cliente? (Seleccione todas las opciones que correspondan)
* [✅] **Descarga automática a través del navegador web (Drive-by download)**
* [✅] **Macro maliciosa**
* [ ] Vulnerabilidad en un protocolo de red o dispositivo
* [✅] **Ataque basado en USB**
* [✅] **Archivo ejecutable infectado**
* [✅] **Archivo adjunto malicioso en la aplicación de correo electrónico**

### 1. Explicación General
Un vector basado en el cliente requiere de forma obligatoria que una aplicación o programa de software que se ejecuta localmente en la máquina del usuario final (el lado del cliente) procese, interprete o ejecute el código malicioso enviado por el atacante.

### 2. ¿Por qué es la correcta y no el resto?
* **Opciones Correctas [✓]:** Los navegadores web (que interpretan scripts y ejecutan *drive-by downloads*), las aplicaciones de correo (que abren adjuntos), las suites de oficina (que ejecutan macros) y el propio sistema operativo host (que procesa archivos ejecutables y sistemas de archivos USB) son software cliente expuesto a la interacción del usuario.
* **Opción Descartada:** Una vulnerabilidad en un protocolo de red o dispositivo (como una falla en un servicio SSH o un firmware de router) es un vector del lado del servidor o de la infraestructura; el atacante la explota enviando paquetes directamente a un puerto de escucha remota sin requerir acciones del usuario.

### 3. Clave para el Examen SY0-701
Para identificar vectores basados en el cliente, busque siempre elementos que requieran la interacción o el procesamiento local por parte de una aplicación instalada en la estación de trabajo del usuario (endpoint).

---

## Pregunta 10: Vectores de Amenaza Sin Agente (Agentless)

### English Version
Select the two (2) answers that refer to agentless software threat vectors.
* [✅] **Phishing email**
* [ ] Malicious USB drive
* [✅] **Network protocol vulnerability**
* [ ] Infected macro
* [ ] Packet sniffing

### Versión en Español
¿Cuáles de las siguientes respuestas se refieren a vectores de amenazas de software sin agente (Agentless)? (Seleccione 2 respuestas)
* [✅] **Correo electrónico de phishing**
* [ ] Unidad USB maliciosa
* [✅] **Vulnerabilidad del protocolo de red**
* [ ] Macro infectada
* [ ] Análisis de paquetes (Packet sniffing)

### 1. Explicación General
Los vectores "sin agente" (*agentless*) operan directamente sobre los canales de comunicación, servicios nativos y los protocolos estándar del sistema. No requieren de la preinstalación de un software intermediario ni de código residente del atacante en el host final para manifestar la amenaza.

### 2. ¿Por qué es la correcta y no el resto?
* **Opciones Correctas:** El correo electrónico de phishing (que viaja sobre el protocolo nativo SMTP) y las vulnerabilidades en protocolos de red (como fallas en los servicios SMB o RDP) aprovechan la arquitectura de red existente; el atacante interactúa directamente con servicios estándar abiertos.
* **Opciones Descartadas:** Las unidades USB y las macros infectadas requieren de la interacción directa con hardware y software ejecutable local. El *Packet sniffing* se descarta por ser una técnica de reconocimiento pasivo (escucha de tráfico), no un vector de inyección de exploits o software.

### 3. Clave para el Examen SY0-701
Lo "sin agente" se aprovecha de las funciones y puertos que ya están corriendo legítimamente en la red. Si el atacante explota un servicio expuesto externamente de forma remota sin requerir la inyección previa de código persistente en el objetivo, está usando un vector *agentless*.

---

## Pregunta 11: Explotación de Vulnerabilidades Conocidas

### English Version
Select all components for which the exploitation of known vulnerabilities represents a critical threat vector.
* [✅] **Legacy systems/applications**
* [✅] **Unsupported systems/applications**
* [ ] Recently released systems/applications
* [ ] Systems/applications with zero-day vulnerabilities

### Versión en Español
La explotación de vulnerabilidades conocidas es un vector de amenaza común para: (Seleccione todas las opciones que correspondan)
* [✅] **Sistemas/aplicaciones heredados (Legacy)**
* [✅] **Sistemas/aplicaciones no compatibles (Unsupported)**
* [ ] Sistemas/aplicaciones de reciente lanzamiento
* [ ] Sistemas/aplicaciones con vulnerabilidad de día cero

### 1. Explicación General
Cuando el software llega al final de su ciclo de vida útil (EOL), los fabricantes cesan el desarrollo de parches de seguridad, provocando que cualquier fallo descubierto y publicado en bases de datos de vulnerabilidades (CVE) se convierta en una puerta abierta permanente para los atacantes.

### 2. ¿Por qué es la correcta y no el resto?
Los sistemas heredados (*Legacy*) y los no compatibles/sin soporte (*Unsupported*) son las respuestas correctas ya que ambos carecen de mantenimiento activo; las vulnerabilidades conocidas permanecen ahí para siempre. Las aplicaciones de reciente lanzamiento cuentan con parches activos, y los ataques de día cero (*Zero-day*) explotan fallas que aún no son públicas, lo que contradice el enunciado de vulnerabilidades "conocidas".

### 3. Clave para el Examen SY0-701
En el examen de CompTIA, los términos *Legacy* y *Unsupported* equivalen a sistemas totalmente indefensos ante exploits antiguos e indexados públicamente. La única mitigación real si no se pueden actualizar o reemplazar es aislarlos de la red mediante segmentación.

---

## Pregunta 12: Tecnologías Inalámbricas Obsoletas como Vectores de Riesgo

### English Version
Select all wireless technologies that are considered potential threat vectors due to legacy architectural flaws.
* [✅] **WPS**
* [ ] WAP
* [ ] WPA
* [ ] WAF
* [ ] WPA2
* [✅] **WEP**

### Versión en Español
¿Cuáles de las tecnologías inalámbricas que se enumeran a continuación se consideran vectores de amenaza potenciales y deben evitarse debido a sus vulnerabilidades conocidas? (Seleccione todas las opciones que correspondan)
* [✅] **WPS**
* [ ] WAP
* [ ] WPA
* [ ] WAF
* [ ] WPA2
* [✅] **WEP**

### 1. Explicación General
Los protocolos de cifrado y autenticación inalámbricos antiguos fueron diseñados con debilidades estructurales matemáticas que permiten romper su seguridad de forma automatizada en cuestión de minutos.

### 2. ¿Por qué es la correcta y no el resto?
* **WEP:** Utiliza claves estáticas con vectores de inicialización (IV) extremadamente cortos (24 bits), lo que permite deducir la clave mediante el análisis estadístico de paquetes capturados en redes con tráfico.
* **WPS:** Posee un mecanismo de autenticación por PIN de 8 dígitos dividido internamente en dos bloques independientes, lo que reduce las combinaciones y lo hace vulnerable a ataques de fuerza bruta rápidos.
* *WPA* y *WPA2* se descartan por ser estándares seguros (WPA3 es el ideal actual); *WAP* es el acrónimo del hardware físico (Punto de Acceso Inalámbrico), no de un protocolo; y *WAF* es un Firewall de Aplicaciones Web.

### 3. Clave para el Examen SY0-701
WEP es considerado el protocolo inalámbrico más inseguro e indefendible. Cualquier pregunta del examen que exija elevar la seguridad de una infraestructura inalámbrica obsoleta requerirá desactivar WEP/WPS y realizar la transición hacia WPA2/WPA3 en modo empresarial.

---

## Pregunta 13: Vectores Exclusivos de Infraestructuras Cableadas (Physical Layer)

### English Version
Identify the threat vector that is uniquely characteristic of physical, wired network infrastructures.
* [ ] ARP spoofing
* [ ] VLAN hopping
* [  ] **Wiretapping**
* [ ] Port sniffing
* [ ] All of the above

### Versión en Español
¿Cuál de las respuestas que aparecen a continuación se refiere a un vector de amenaza característico únicamente de las redes cableadas?
* [ ] Suplantación de ARP (ARP spoofing)
* [ ] Salto de VLAN (VLAN hopping)
* [  ] **Intercepción de cables (Wiretapping)**
* [ ] Olfateo de puertos (Port sniffing)
* [ ] Todo lo anterior

### 1. Explicación General
A diferencia de las redes inalámbricas donde las señales se propagan libremente por el aire, las redes cableadas confinan los datos a un medio físico conductor (cobre o fibra óptica), introduciendo el riesgo de alteración o acceso físico directo sobre la infraestructura de cables.

### 2. ¿Por qué es la correcta y no el resto?
**Intercepción de cables (Wiretapping)** es la única opción correcta porque requiere la conexión o el empalme físico de herramientas o hardware de escucha directamente sobre los hilos conductores de cobre o filamentos de fibra para extraer las señales eléctricas o de luz. Los ataques de *ARP*, *VLAN hopping* y *Port sniffing* se ejecutan a nivel lógico mediante software, lo que significa que pueden aplicarse indistintamente en entornos cableados o inalámbricos una vez dentro de la red.

### 3. Clave para el Examen SY0-701
Si el vector de ataque exige que el intruso manipule físicamente los cables en canaletas, falsos techos o armarios de telecomunicaciones (paneles de parcheo IDF/MDF) para clonar el tráfico de datos, la respuesta técnica es **Wiretapping**.

---

## Pregunta 14: Vectores de Ataque sobre Protocolos Bluetooth

### English Version
Determine the validity of the statement regarding Bluetooth vector attacks (bluesmacking, bluejacking, bluesnarfing, bluebugging).
* [✅] **True**
* [ ] False

### Versión en Español
Algunos ejemplos de vectores de amenaza relacionados con la comunicación Bluetooth incluyen: bluesmacking, bluejacking, bluesnarfing y bluebugging.
* [✅] **Verdadero**
* [ ] Falso

### 1. Explicación General
El protocolo de comunicación inalámbrica de corto alcance Bluetooth cuenta con su propia taxonomía de vectores de ataque lógicos, diseñados para explotar el descubrimiento de dispositivos y el intercambio de paquetes por proximidad física.

### 2. ¿Por qué es la correcta y no el resto?
Es **Verdadero** debido a que el texto asocia con total precisión los nombres técnicos oficiales de la industria con las mecánicas del protocolo: *Bluesmacking* (Denegación de servicio mediante paquetes ping masivos), *Bluejacking* (envío de mensajes o tarjetas de contacto no solicitadas), *Bluesnarfing* (acceso no autorizado y robo de datos del dispositivo) y *Bluebugging* (toma de control total de los comandos del teléfono). Marcar "Falso" negaría esta terminología de examen.

### 3. Clave para el Examen SY0-701
Memorice la diferencia crítica entre los dos términos más preguntados: **Bluejacking es molesto pero inofensivo** (solo introduce datos/mensajes en la pantalla de la víctima), mientras que **Bluesnarfing es un ataque de robo** (extrae de forma no autorizada información como contactos, SMS o fotos).

---

## Pregunta 15: Explotación de Puntos de Entrada Lógicos de Red

### English Version
Choose the network asset state that most likely leads to unauthorized access via entry point exploitation.
* [ ] Outdated antivirus software
* [ ] Browser cookies
* [  ] **Open service ports**
* [ ] Insufficient logging and monitoring

### Versión en Español
¿Cuál de las respuestas que se enumeran a continuación se refiere a la causa más probable de un acceso no autorizado provocado por la explotación de un punto de entrada específico de la red?
* [ ] Software antivirus obsoleto
* [ ] Cookies del navegador
* [  ] **Abrir puertos de servicio**
* [ ] Registro y monitoreo insuficientes

### 1. Explicación General
En redes, los puntos de entrada lógicos se establecen mediante la apertura de puertos en las interfaces. Si un puerto está abierto y expone a internet un servicio expuesto que cuenta con fallas de configuración o exploits conocidos, el atacante puede interactuar directamente con él desde el exterior para forzar el acceso.

### 2. ¿Por qué es la correcta y no el resto?
**Abrir puertos de servicio** es la respuesta correcta porque representa el punto de entrada lógico directo que un atacante puede escanear y explotar desde internet de forma remota (por ejemplo, un puerto expuesto `3389` de RDP). El software obsoleto procesa el malware pero no abre la red por sí mismo; las cookies controlan sesiones web locales; y la falta de monitoreo impide ver la intrusión, pero no constituye el punto de entrada físico o lógico.

### 3. Clave para el Examen SY0-701
Cerrar los puertos innecesarios (principios de deshabilitar servicios no requeridos) y aplicar reglas estrictas de firewalls perimetrales es la principal contramedida arquitectónica para reducir el tamaño de la **superficie de ataque externa** de una organización.

---

## Pregunta 16: El Impacto de las Credenciales Predeterminadas (Default Credentials)

### English Version
Evaluate the statement regarding the impact of default administrator credentials on an organization's attack surface.
* [✅] **True**
* [ ] False

### Versión en Español
Dejar las credenciales predeterminadas sin modificar amplía la superficie de ataque al proporcionar un punto de entrada fácil para el acceso no autorizado.
* [✅] **Verdadero**
* [ ] Falso

### 1. Explicación General
Los fabricantes configuran sus equipos nuevos (como routers, switches o cámaras IP) con nombres de usuario y contraseñas de fábrica genéricos y simples para facilitar el despliegue inicial. Estas combinaciones son de conocimiento público y están indexadas en listas en internet.

### 2. ¿Por qué es la correcta y no el resto?
Es **Verdadero** debido a que mantener las credenciales predeterminadas crea una vulnerabilidad crítica de control de acceso; cualquier atacante que realice un escaneo de red e identifique el panel de gestión del dispositivo podrá tomar el control administrativo inmediato mediante fuerza bruta simple o diccionarios estándar, sin necesidad de escribir exploits complejos.

### 3. Clave para el Examen SY0-701
Cambiar los nombres de usuario de fábrica y sustituir las contraseñas predeterminadas (*default credentials*) es la primera tarea obligatoria de la línea base de endurecimiento de seguridad (**Hardening**) al instalar cualquier elemento de infraestructura tecnológica en la red corporativa.

---

## Pregunta 17: Vectores de Riesgo en MSP y Cadena de Suministro

### English Version
Select the two (2) threat vectors that commonly propagate through Managed Service Providers (MSPs) and supply chain vendors.
* [ ] Compliance breaches
* [  ] **Malware propagation**
* [ ] Operational disruptions
* [  ] **Social engineering techniques**

### Versión en Español
¿Cuáles de las siguientes respuestas se refieren a vectores de amenazas comunes que afectan a los MSP, vendedores y proveedores en la cadena de suministro? (Seleccione 2 respuestas)
* [ ] Infracciones de cumplimiento (Compliance breaches)
* [ ] Daños a la reputación de la marca
* [  ] **Propagación de malware**
* [ ] Interrupciones operativas
* [  ] **Técnicas de ingeniería social**

### 1. Explicación General
Los ataques a la cadena de suministro (*Supply Chain Attacks*) explotan las relaciones de confianza técnica y operativa que existen entre una organización y sus proveedores externos (como los Proveedores de Servicios Gestionados o MSP), quienes suelen tener credenciales legítimas y túneles VPN directos hacia el interior de las redes de sus clientes.

### 2. ¿Por qué es la correcta y no el resto?
Las dos opciones seleccionadas son las correctas porque representan los vectores reales técnicos y lógicos que se ejecutan durante la intrusión: los atacantes comprometen primero al proveedor externo utilizando **técnicas de ingeniería social** (phishing dirigido a sus administradores) para robar sus accesos y, una vez dentro de las consolas de administración del MSP, despliegan y automatizan la **propagación de malware** (como ransomware en masa) hacia la infraestructura conectada de los clientes finales. Las opciones de cumplimiento, reputación e interrupción operativa constituyen el impacto o las consecuencias del ataque, no los vectores técnicos utilizados para consumarlo.

### 3. Clave para el Examen SY0-701
Para mitigar el riesgo de vectores en la cadena de suministro y MSP, el examen requerirá la implementación del principio de **Privilegio Mínimo**, auditorías de seguridad a terceros (Vendor Assessment) y la exigencia de Autenticación de Múltiples Factores (MFA) obligatoria en todas las conexiones remotas entrantes de proveedores.

---

[[ExamCompass - Cuestionarios por Temas|⬅️ Volver a Cuestionarios por Temas]]