---
tags:
  - "formato/apunte"
  - "analisis/forense"
  - "examen/test-especifico"
  - "gestion/estado/terminado"
---
Este apunte contiene el análisis detallado del cuestionario temático sobre seguridad de datos, privacidad, criptografía y control de accesos de la plataforma ExamCompass para la certificación CompTIA Security+ (SY0-701), alineado con las respuestas oficiales del simulador.

---

## Pregunta 1: Definición de Información de Identificación Personal (PII)

### English Version
Which of the answers listed below refers to any type of information relating to an individual that can be used to uniquely identify that person?
* [ ] FI
* [ ] Biometrics
* [ ] ID
* [✅] **PII**

### Versión en Español
¿Cuál de las respuestas que aparecen a continuación se refiere a cualquier tipo de información relativa a un individuo que pueda utilizarse para identificar de forma unívoca a esa persona?
* [ ] FI
* [ ] Biometría
* [ ] IDENTIFICACIÓN
* [✅] **PII (Personally Identifiable Information)**

### 1. Explicación General
Las siglas **PII** (*Personally Identifiable Information* / Información de Identificación Personal) representan cualquier dato que, por sí solo o combinado con otra información relevante, pueda identificar, contactar o localizar de manera única a un individuo específico. Ejemplos comunes incluyen nombres completos, números de seguridad social, direcciones de correo electrónico, números de teléfono y registros financieros.

### 2. ¿Por qué es la correcta y no el resto?
* **PII** es el término estándar de la industria que engloba toda la categoría de datos de identidad personal de forma unívoca.
* **Biometría:** Es solo un subconjunto o tipo específico de datos (huellas dactilares, reconocimiento de iris) que puede usarse como PII, pero no es el término general.
* **IDENTIFICACIÓN (ID):** Es un término demasiado genérico que puede referirse a un identificador de proceso, de máquina o de base de datos, y no necesariamente a una persona natural.
* **FI (Financial Information):** Se limita únicamente a datos bancarios, sin cubrir la totalidad de la identidad del individuo.

### 3. Clave para el Examen SY0-701
Para Security+, la clasificación y el inventario de PII son pasos críticos en el gobierno de datos. Las organizaciones deben aplicar controles estrictos de seguridad para cumplir con las normativas globales, pues la pérdida de PII conlleva multas severas y pérdida de reputación.

---

## Pregunta 2: Regulación de Privacidad de la Unión Europea (GDPR)

### English Version
Which of the following regulations governs the personal data privacy of EU citizens?
* [ ] FI
* [ ] HIPAA
* [ ] PCI DSS
* [✅] **GDPR**

### Versión en Español
¿Cuál de las siguientes disposiciones regula la privacidad de los datos personales de los ciudadanos de la UE?
* [ ] FI
* [ ] HIPAA
* [ ] PCI DSS
* [✅] **RGPD (Reglamento General de Protección de Datos)**

### 1. Explicación General
El **RGPD** (*Reglamento General de Protección de Datos* / GDPR en inglés) es un marco legal estricto de la Unión Europea que entró en vigor en 2018. Su objetivo es proteger la privacidad de los datos de todos los residentes de la UE y regula cómo las empresas recopilan, almacenan, procesan y destruyen dichos datos, aplicando incluso a empresas fuera de Europa si procesan datos de ciudadanos comunitarios.

### 2. ¿Por qué es la correcta y no el resto?
* **RGPD** es el único reglamento de la lista creado por la Unión Europea para la protección global de la privacidad personal de sus ciudadanos.
* **HIPAA:** Es una ley federal exclusivamente estadounidense enfocada en proteger la información médica y de salud.
* **PCI DSS:** No es una ley gubernamental, sino un estándar de seguridad de la industria de tarjetas de pago para proteger transacciones y datos bancarios.
* **FI:** No representa un estándar o reglamento de privacidad reconocido.

### 3. Clave para el Examen SY0-701
El RGPD introduce el concepto del *"Derecho al olvido" (Right to be Forgotten)* y exige la notificación obligatoria de brechas de seguridad dentro de las 72 horas posteriores a su detección. Es un clásico del examen para evaluar el cumplimiento (*compliance*) global.

---

## Pregunta 3: Protección de la Privacidad Médica (HIPAA)

### English Version
The Health Insurance Portability and Accountability Act (HIPAA) provides privacy protection for:
* [ ] Personally Identifiable Information
* [ ] PI
* [✅] **Protected Health Information**
* [ ] PIV

### Versión en Español
La Ley de Portabilidad y Responsabilidad del Seguro Médico de EE. UU. (HIPAA) brinda protección de la privacidad para:
* [ ] Información de identificación personal
* [ ] PI
* [✅] **Información de salud protegida (Protected Health Information - PHI)**
* [ ] PIV

### 1. Explicación General
La ley estadounidense HIPAA exige la protección de la **PHI** (*Protected Health Information* / Información de Salud Protegida). Esto abarca cualquier dato médico creado, guardado o transmitido por proveedores de salud, aseguradoras o clínicas de compensación, incluyendo historiales clínicos, diagnósticos, resultados de laboratorio y facturación médica.

### 2. ¿Por qué es la correcta y no el resto?
* **Información de salud protegida (PHI)** es la categoría jurídica exacta definida y regulada bajo el mando de HIPAA.
* **Información de identificación personal (PII):** Aunque la PHI es técnicamente un tipo de PII, HIPAA fue redactada específicamente para salvaguardar la información relacionada con la salud (PHI), no la PII general (como licencias de conducir ordinarias).
* **PI (Personal Information) / PIV (Personal Identity Verification):** "PI" es una denominación genérica, y "PIV" es un estándar de tarjetas de identificación del gobierno de EE. UU. para acceso físico y lógico; ninguno de los dos describe los datos sanitarios de HIPAA.

### 3. Clave para el Examen SY0-701
CompTIA asocia directamente HIPAA con **PHI**. Si en un caso práctico del examen se habla de hospitales, historiales clínicos o software de telemedicina, el tipo de dato que debes buscar proteger obligatoriamente es la PHI.

---

## Pregunta 4: Estándar de Seguridad de Tarjetas de Pago (PCI DSS)

### English Version
The purpose of PCI DSS is to provide protection for:
* [✅] **Credit cardholder data**
* [ ] Licensed software
* [ ] User passwords
* [ ] Personal health information

### Versión en Español
El propósito de PCI DSS es brindar protección para:
* [✅] **Datos del titular de la tarjeta de crédito (Credit cardholder data)**
* [ ] Software con licencia
* [ ] Contraseñas de usuario
* [ ] Información personal sobre salud

### 1. Explicación General
El estándar **PCI DSS** (*Payment Card Industry Data Security Standard*) es una norma de seguridad global unificada creada por las principales marcas de tarjetas de pago (Visa, Mastercard, Amex, etc.). Su propósito es prevenir el fraude mediante la protección de los datos sensibles de los titulares de tarjetas durante el almacenamiento, procesamiento y transmisión de las transacciones de pago.

### 2. ¿Por qué es la correcta y no el resto?
* **Datos del titular de la tarjeta de crédito (CHD / Cardholder Data)** es el enfoque exclusivo de la normativa PCI DSS.
* **Software con licencia:** Se gestiona mediante acuerdos de licencia de software (EULA) y gestión de activos de TI (SAM).
* **Contraseñas de usuario:** Su protección se rige por políticas internas de control de acceso, IAM y hashing de contraseñas.
* **Información personal sobre salud (PHI):** Está regulada por HIPAA, no por las marcas de tarjetas de crédito.

### 3. Clave para el Examen SY0-701
Cualquier escenario en el examen que involucre un comercio electrónico, procesamiento de pagos o bases de datos de transacciones de tarjetas requiere el cumplimiento inmediato del estándar PCI DSS y la técnica de **Tokenización** para mitigar el riesgo en el almacenamiento de estos datos.

---

## Pregunta 5: Métodos de Cifrado para Datos en Reposo

### English Version
Which of the answers listed below refer to encryption methods used to protect data at rest? (Select all that apply)
* [✅] **FDE**
* [✅] **SED**
* [ ] IPsec
* [ ] TLS
* [ ] VPN
* [✅] **EFS**

### Versión en Español
¿Cuál o cuáles de las respuestas que aparecen a continuación se referieren a los métodos de cifrado utilizados para proteger los datos en reposo? (Seleccione todas las opciones que correspondan)
* [✅] **FDE (Full Disk Encryption)**
* [✅] **SED (Self-Encrypting Drive)**
* [ ] IPsec
* [ ] TLS
* [ ] VPN
* [✅] **EFS (Encrypting File System)**

### 1. Explicación General
Los datos en reposo (*data at rest*) son aquellos almacenados estáticamente en un medio físico persistente. Para protegerlos de accesos físicos no autorizados (como el robo de una laptop), se emplean técnicas de cifrado de sistemas de archivos, discos completos o chips físicos que impiden la lectura de los bloques de almacenamiento sin la llave criptográfica adecuada.

### 2. ¿Por qué son las correctas y no el resto?
* **FDE (Full Disk Encryption):** Cifra el disco duro entero, sector por sector, protegiendo todo el sistema operativo y los datos almacenados.
* **SED (Self-Encrypting Drive):** Es un disco que cuenta con un chip controlador de hardware dedicado que cifra y descifra automáticamente los datos sin consumir recursos de la CPU principal.
* **EFS (Encrypting File System):** Es una característica de los sistemas de archivos (como NTFS en Windows) que permite cifrar archivos y carpetas individuales de forma transparente para el usuario.
* **IPsec, TLS y VPN:** Son protocolos estrictamente diseñados para proteger datos en tránsito a través de canales de red de comunicaciones, no archivos estáticos.

### 3. Clave para el Examen SY0-701
CompTIA suele presentar la pérdida física de dispositivos (ej. un empleado olvida su laptop en un taxi) como una amenaza común. La única solución efectiva para garantizar que los datos confidenciales sigan protegidos en este escenario es haber implementado previamente FDE o SED.

---

## Pregunta 6: Métodos de Cifrado para Datos en Tránsito

### English Version
Encryption methods used to protect data in transit include: (Select all that apply)
* [ ] NFS
* [✅] **VPN**
* [ ] SED
* [✅] **IPsec**
* [ ] FDE
* [✅] **TLS**

### Versión en Español
Los métodos de cifrado utilizados para proteger los datos en tránsito incluyen: (Seleccione todos los que correspondan)
* [ ] NFS
* [✅] **VPN**
* [ ] SED
* [✅] **IPsec**
* [ ] FDE
* [✅] **TLS**

### 1. Explicación General
Los datos en tránsito (*data in transit / motion*) se encuentran viajando activamente a través de redes cableadas o inalámbricas públicas o privadas. Para evitar ataques de intermediarios (Ataques On-Path / Man-in-the-Middle) y de rastreo de paquetes (*sniffing*), se deben encapsular dentro de túneles criptográficos y sesiones cifradas seguras.

### 2. ¿Por qué son las correctas y no el resto?
* **VPN (Virtual Private Network):** Crea una conexión cifrada de extremo a extremo a través de internet para transportar datos corporativos de manera segura.
* **IPsec (Internet Protocol Security):** Suite de protocolos utilizada para autenticar y cifrar paquetes IP en la capa de red, comúnmente en túneles VPN sitio a sitio.
* **TLS (Transport Layer Security):** El estándar de la capa de transporte que asegura la comunicación web (HTTPS), el correo electrónico y otras transmisiones de aplicaciones.
* **SED y FDE:** Son tecnologías exclusivas para datos estáticos en almacenamiento físico (en reposo).
* **NFS (Network File System):** Es un protocolo para compartir archivos en red, pero de forma nativa no cifra el tráfico a menos que sea integrado con Kerberos o túneles cifrados auxiliares.

### 3. Clave para el Examen SY0-701
En Security+, recuerda que TLS reemplazó por completo al antiguo e inseguro SSL. Cuando veas escenarios de comercio electrónico o portales de inicio de sesión de usuarios, la respuesta correcta para asegurar ese tráfico web siempre involucrará el uso de **TLS**.

---

## Pregunta 7: Estados de los Datos: Datos en Uso

### English Version
Which of the following data states typically requires the data to be processed unencrypted?
* [ ] Data in motion
* [ ] Data at rest
* [ ] Data in transit
* [✅] **Data in use**

### Versión en Español
¿Cuál de los siguientes estados de datos normalmente requiere que los datos se procesen sin cifrar?
* [ ] Datos en movimiento
* [ ] Datos en reposo
* [ ] Datos en tránsito
* [✅] **Datos en uso (Data in use)**

### 1. Explicación General
Los **datos en uso** (*data in use*) son aquellos que están siendo procesados activamente por la unidad central de procesamiento (CPU) del sistema, almacenados temporalmente en la memoria de acceso aleatorio (RAM) o en los registros internos del procesador. El hardware moderno de cómputo convencional no puede ejecutar operaciones matemáticas ni lógicas sobre información cifrada, por lo que el sistema operativo debe cargarlos descifrados en memoria para su procesamiento.

### 2. ¿Por qué es la correcta y no el resto?
* **Datos en uso** es la respuesta correcta porque la CPU requiere datos legibles para realizar cálculos de manera inmediata.
* **Datos en reposo / en movimiento / en tránsito:** En todos estos estados es altamente recomendado e ideal que los datos permanezcan cifrados de principio a fin, ya que no se están ejecutando operaciones de procesamiento directo sobre ellos.

### 3. Clave para el Examen SY0-701
El estado de "datos en uso" es especialmente vulnerable a ataques de extracción de memoria física, como *Memory Dumping*, o ataques físicos tipo *Cold Boot Attack* (lectura de la RAM justo después de apagar el equipo). Para mitigar riesgos en entornos altamente confidenciales, CompTIA introduce tecnologías emergentes como la computación confidencial y el aislamiento de memoria.

---

## Pregunta 8: Datos No Legibles por Humanos (Non-Human-Readable)

### English Version
Which of the answers listed below refer to examples of non-human-readable data types? (Select 2 answers)
* [✅] **Binary code**
* [ ] XML files
* [✅] **Machine language**
* [ ] HTML code
* [ ] SQL queries

### Versión en Español
¿Cuáles de las respuestas que aparecen a continuación se refieren a ejemplos de tipos de datos no legibles por humanos? (Seleccione 2 respuestas)
* [✅] **Código binario (Binary code)**
* [ ] Archivos XML
* [✅] **Lenguaje de máquina (Machine language)**
* [ ] Código HTML
* [ ] Consultas SQL

### 1. Explicación General
Los datos no legibles por humanos (*non-human-readable*) son flujos estructurados puramente para la interpretación del hardware, las computadoras y los microprocesadores. Generalmente consisten en secuencias de unos y ceros (binario) o instrucciones compiladas que carecen de caracteres alfabéticos estructurados que un humano promedio pueda comprender de manera directa.

### 2. ¿Por qué son las correctas y no el resto?
* **Código binario** es la base lógica de las computadoras representativa de transistores encendidos/apagados, imposible de ser leída fluidamente por un humano.
* **Lenguaje de máquina** son las instrucciones nativas compiladas de bajo nivel que ejecuta la CPU directamente, representadas en formato hexadecimal o binario puro.
* **XML, HTML y SQL:** Son formatos de datos estructurados basados en texto plano que utilizan palabras del idioma inglés estándar (como `<p>`, `<name>`, `SELECT * FROM`). Aunque tienen una sintaxis de programación, son perfectamente legibles y comprensibles por humanos.

### 3. Clave para el Examen SY0-701
Es vital comprender que el malware sofisticado a menudo se entrega en formatos compilados y ofuscados (código binario/lenguaje de máquina) para evadir la inspección analítica de firmas de antivirus tradicionales, requiriendo herramientas de ingeniería inversa para decodificarlos.

---

## Pregunta 9: Rol de Gobernanza de Privacidad (DPO)

### English Version
Which of the following answers refers to a person or role responsible for overseeing and ensuring compliance with data protection laws and policies within an organization?
* [ ] CTO
* [✅] **DPO**
* [ ] CIO
* [ ] CSO

### Versión en Español
¿Cuál de las siguientes respuestas se refiere a una persona o función responsable de supervisar y garantizar el cumplimiento de las leyes y políticas de protección de datos dentro de una organización?
* [ ] CTO
* [✅] **DPO (Delegado de Protección de Datos)**
* [ ] CIO
* [ ] CSO

### 1. Explicación General
El **DPO** (*Data Protection Officer* / Delegado de Protección de Datos) es un rol de liderazgo de seguridad e infraestructura legal, exigido de manera obligatoria por marcos regulatorios como el RGPD (GDPR). Su función es actuar de forma independiente para asesorar a la junta directiva sobre el cumplimiento normativo de la privacidad de los datos, capacitar al personal y servir como punto de contacto principal entre la organización y las autoridades supervisoras.

### 2. ¿Por qué es la correcta y no el resto?
* **DPO** es el puesto de trabajo específico definido en la ley para la gobernanza exclusiva de la privacidad de datos personales.
* **CTO (Chief Technology Officer):** Enfocado en la estrategia de adquisición de tecnología y desarrollo de productos tecnológicos comerciales.
* **CIO (Chief Information Officer):** Responsable de la infraestructura de TI de la empresa, la conectividad y la productividad de los sistemas.
* **CSO (Chief Security Officer):** Encargado de la seguridad integral global de la compañía (incluida la seguridad física), aunque delega la gestión específica de datos personales al DPO.

### 3. Clave para el Examen SY0-701
Cuando una pregunta del examen hable del cumplimiento normativo a gran escala y de la auditoría interna del uso de los datos personales recopilados de clientes, la figura del **DPO** es siempre la respuesta correcta de gobernanza.

---

## Pregunta 10: Funcionalidad de Localización por Hardware (GPS)

### English Version
The built-in functionality of a mobile device that allows the use of location-based applications is known as:
* [ ] WPS
* [ ] GSM
* [ ] SIM
* [✅] **GPS**

### Versión en Español
La funcionalidad integrada de un dispositivo móvil que permite el uso de aplicaciones de localización se conoce como:
* [ ] WPS
* [ ] GSM
* [ ] SIM
* [✅] **GPS (Global Positioning System)**

### 1. Explicación General
El **GPS** (*Global Positioning System* / Sistema de Posicionamiento Global) es un receptor de hardware integrado de forma nativa en casi todos los teléfonos móviles actuales. No emite señales, sino que escucha pasivamente las microondas electromagnéticas emitidas por un mínimo de 4 satélites en órbita terrestre. Al medir con alta precisión el retraso de viaje de estas señales, el chip calcula de manera autónoma las coordenadas geográficas del usuario.

### 2. ¿Por qué falló tu respuesta en el simulador?
Elegiste **WPS** (*Wi-Fi Protected Setup*). Esta es una tecnología de configuración de red inalámbrica diseñada para simplificar la conexión de dispositivos domésticos a un punto de acceso inalámbrico (generalmente mediante el ingreso de un PIN de 8 dígitos o pulsando un botón físico). Debido a graves fallas de diseño que permitían ataques de fuerza bruta rápidos, su uso está totalmente desaconsejado en entornos de seguridad corporativos y no tiene ninguna relación directa con el hardware de posicionamiento satelital.

### 3. Clave para el Examen SY0-701
En Security+, el GPS habilita el concepto clave de **Geocercado** (*Geofencing*), que permite a las soluciones de seguridad móvil delimitar áreas geográficas virtuales (ej. "las oficinas corporativas") y restringir los privilegios del dispositivo cuando está fuera de dicho perímetro para prevenir fugas de información.

---

## Pregunta 11: Control de Fronteras Virtuales (Geocercado)

### English Version
Which of the answers listed below refers to a technology that provides control over the use of a mobile device within a designated area?
* [✅] **Geofencing**
* [ ] Captive portal
* [ ] Honeypot
* [ ] Geolocation

### Versión en Español
¿Cuál de las respuestas que aparecen a continuación se refiere a una tecnología que proporciona control sobre el uso de un dispositivo móvil dentro de un área designada?
* [✅] **Geocercado (Geofencing)**
* [ ] Portal cautivo
* [ ] Mielero (Honeypot)
* [ ] Geolocalización

### 1. Explicación General
El **Geocercado** (*Geofencing*) consiste en establecer fronteras o perímetros virtuales sobre una zona geográfica real (utilizando datos del GPS, Wi-Fi o datos celulares del dispositivo móvil). Cuando el dispositivo entra o sale de este límite virtual predefinido, un software de gestión corporativo (como un MDM) activa de manera automatizada acciones o restricciones preestablecidas de seguridad.

### 2. ¿Por qué es la correcta y no el resto?
* **Geocercado** es el único término que denota la imposición de acciones o de un control de seguridad dinámico basado en límites de área específicos.
* **Geolocalización:** Es simplemente el acto analítico pasivo de identificar y registrar la posición geográfica de un objeto o persona en un mapa, sin aplicar reglas o bloqueos automatizados de control.
* **Portal cautivo:** Es una página web forzada que se le muestra a los usuarios antes de otorgarles acceso a una red Wi-Fi pública para aceptar términos de uso o autenticarse.
* **Mielero (Honeypot):** Es un sistema trampa expuesto intencionalmente para atraer y analizar las técnicas de los atacantes en un entorno controlado.

### 3. Clave para el Examen SY0-701
El geocercado se utiliza comúnmente en entornos BYOD (*Bring Your Own Device*) de alta seguridad. Un escenario clásico en el examen es deshabilitar la cámara trasera del teléfono o forzar que el cliente VPN se conecte tan pronto como el dispositivo físico gruce la puerta de entrada de la empresa.

---

## Pregunta 12: Criptografía Reversible (Cifrado)

### English Version
Which of the following options converts plain text data into ciphertext using an algorithm and a key?
* [✅] **Encryption**
* [ ] Masking
* [ ] Tokenization
* [ ] Obfuscation

### Versión en Español
¿Cuál de las siguientes opciones convierte datos en texto plano en texto cifrado utilizando un algoritmo y una clave?
* [✅] **Cifrado (Encryption)**
* [ ] Enmascaramiento
* [ ] Tokenización
* [ ] Ofuscación

### 1. Explicación General
El **Cifrado** (*Encryption*) es un proceso matemático reversible que toma un mensaje comprensible (texto plano) y lo transforma en una cadena ininteligible (texto cifrado) aplicando operaciones matemáticas rigurosas (algoritmo como AES) combinadas con un secreto matemático (clave criptográfica). El texto original solo se recupera aplicando el proceso inverso con la llave correcta.

### 2. ¿Por qué es la correcta y no el resto?
* **Cifrado** es el único proceso de protección criptográfica estricta que utiliza tanto un algoritmo estandarizado de clave pública/privada como llaves específicas para habilitar la reversibilidad.
* **Enmascaramiento:** Es puramente de carácter estático o dinámico para visualización visual (ej. reemplazar caracteres por asteriscos), no es un proceso basado en operaciones de llave criptográfica.
* **Tokenización:** Reemplaza los datos sensibles con un token sintético aleatorio consultable en una base de datos de bóveda segura, sin ejecutar operaciones de cifrado directamente sobre la cadena de caracteres originales.
* **Ofuscación:** Solo hace que el código o el texto sea extremadamente difícil de entender para los análisis de ingeniería inversa, pero no requiere algoritmos criptográficos ni llaves secretas y carece de seguridad matemática real.

### 3. Clave para el Examen SY0-701
Asegúrate de comprender que el cifrado puede ser Simétrico (misma llave para cifrar y descifrar, rápido y para grandes volúmenes de datos en disco) o Asimétrico (par de llaves pública y privada, utilizado para intercambio de claves y firmas digitales).

---

## Pregunta 13: Algoritmos Unidireccionales de Integridad (Hashing)

### English Version
Which of the answers listed below refers to a technique that allows input data to be converted into a fixed-size string, making it difficult to reverse or retrieve the original data?
* [ ] Obfuscation
* [ ] Tokenization
* [✅] **Hashing**
* [ ] Encryption

### Versión en Español
¿Cuál de las respuestas que aparecen a continuación se refiere a una técnica que permite convertir los datos de entrada en una cadena de tamaño fijo, lo que dificulta revertir o recuperar los datos originales?
* [ ] Ofuscación
* [ ] Tokenización
* [✅] **Hashing**
* [ ] Cifrado

### 1. Explicación General
El **Hashing** es un algoritmo matemático unidireccional (*one-way*) que procesa un bloque de datos de entrada de cualquier tamaño y devuelve una huella digital única (hash) de longitud fija. Una propiedad fundamental del hashing seguro es la resistencia a preimágenes: es computacionalmente imposible revertir el hash final para deducir el texto original.

### 2. ¿Por qué es la correcta y no el resto?
* **Hashing** cumple exactamente con la condición de ser irreversible por diseño matemático y de producir una salida de longitud fija invariable (ej. SHA-256 siempre generará 256 bits sin importar si el input es una letra o un libro completo).
* **Cifrado:** Es bidireccional y reversible por definición utilizando una clave, y la longitud del texto cifrado crece en función del tamaño de los datos de entrada.
* **Ofuscación:** Se puede revertir fácilmente mediante técnicas de desofuscación automatizadas.
* **Tokenización:** No tiene tamaño de salida fijo estandarizado y requiere mapeo directo en una tabla relacional para almacenamiento de tokens.

### 3. Clave para el Examen SY0-701
El propósito principal del hashing es garantizar la **Integridad** de la información (verificar que los archivos no hayan sido alterados o modificados por atacantes). Los algoritmos de hashing recomendados actualmente para el examen son SHA-2 (SHA-256) y SHA-3, mientras que MD5 y SHA-1 se consideran obsoletos y vulnerables.

---

## Pregunta 14: Definición y Propósito del Enmascaramiento de Datos

### English Version
Which of the following answers refer to data masking? (Select 2 answers)
* [✅] **Replaces sensitive data with fictitious or modified data, retaining its original format**
* [✅] **Allows data manipulation in environments where actual values are not needed**
* [ ] Transforms data into an unreadable format using an encryption algorithm and key
* [ ] Creates a unique fixed-length string from the original data
* [ ] Replaces sensitive data with a non-sensitive identifier that has no meaning or value outside the specific system

### Versión en Español
¿Cuáles de las siguientes respuestas se referieren al enmascaramiento de datos? (Seleccione 2 respuestas)
* [✅] **Reemplaza los datos confidenciales con datos ficticios o modificados, conservando su formato original**
* [✅] **Permite la manipulación de datos en entornos donde no se necesitan los valores reales**
* [ ] Transforma los datos a un formato ilegible mediante un algoritmo y una clave de cifrado.
* [ ] Crea una cadena única de longitud fija a partir de los datos originales.
* [ ] Reemplaza los datos confidenciales con un identificador no confidencial que no tiene significado ni valor fuera del sistema específico.

### 1. Explicación General
El **Enmascaramiento de Datos** (*Data Masking*) es el proceso de crear una versión estructuralmente similar de los datos originales pero alterando los valores confidenciales (por ejemplo, reemplazando caracteres de números de tarjetas, ofuscando nombres por equivalentes ficticios). Se utiliza principalmente para que equipos de desarrollo, control de calidad (QA) o analistas de soporte puedan probar bases de datos con estructuras reales sin riesgo de exponer información real de clientes.

### 2. ¿Por qué son las correctas y no el resto?
* **Reemplazar con datos ficticios conservando el formato** y **permitir la manipulación en entornos de prueba** son las dos definiciones operativas de esta técnica para prevenir fugas de información en entornos no seguros de desarrollo de software.
* **Transformar datos con algoritmo y clave:** Es la definición del Cifrado.
* **Crear una cadena de longitud fija:** Es la definición del Hashing.
* **Reemplazar con un identificador sin valor fuera del sistema:** Es la definición de la Tokenización.

### 3. Clave para el Examen SY0-701
Recuerda la diferencia en los casos de uso: el enmascaramiento se aplica para la no divulgación interna en escenarios de desarrollo, lo que reduce drásticamente el alcance y la superficie de ataque del cumplimiento de normas (*compliance*) en servidores que no necesitan datos auténticos de producción.

---

## Pregunta 15: Tokenización y Bóvedas de Referencia (Token Vault)

### English Version
Which of the answers listed below refers to a situation where sensitive data is stored in a separate location and can be retrieved with a non-sensitive replacement that can also be processed in the same way as the original data without the risk of revealing the original data content?
* [ ] Masking
* [ ] Obfuscation
* [ ] Encryption
* [✅] **Tokenization**

### Versión en Español
¿Cuál de las respuestas que se enumeran a continuación se refiere a una situación en la que los datos confidenciales se almacenan en una ubicación separada y se pueden recuperar con un reemplazo no confidencial que también se puede procesar de la misma manera que los datos originales sin el riesgo de revelar el contenido de los datos originales?
* [ ] Enmascaramiento
* [ ] Ofuscación
* [ ] Cifrado
* [✅] **Tokenización**

### 1. Explicación General
La **Tokenización** toma un dato sensible (como el número PAN de una tarjeta de crédito o el número de seguro social) y lo sustituye por un equivalente llamado "Token" que es un dato sin valor intrínseco. El dato real se envía y almacena de forma segura en una bóveda central de datos fuertemente defendida (*Token Vault*). El resto del sistema procesa el Token como si fuera el dato real, eliminando el riesgo si el servidor secundario es vulnerado.

### 2. ¿Por qué es la correcta y no el resto?
* **Tokenización** describe el uso de sistemas independientes que reemplazan valores lógicos con índices que solo tienen significado en la base de datos de control central, manteniendo la funcionalidad de procesamiento intacta.
* **Enmascaramiento:** Modifica permanentemente el texto plano visualmente para prevenir visualización en pantallas, sin buscar que sea recuperado de forma dinámica para transacciones bancarias directas.
* **Cifrado:** Transforma los datos en sí mismos usando criptografía en lugar de almacenarlos en otra base de datos de referencia (bóveda).
* **Ofuscación:** Simplemente hace el código ilegible, sin alterar la arquitectura de almacenamiento de los datos sensibles en tránsito o reposo.

### 3. Clave para el Examen SY0-701
En sistemas de pagos móviles modernos como Apple Pay o Google Pay, la Tokenización es la tecnología clave que permite que tu celular pague en la tienda sin compartir jamás tu número real de tarjeta con la terminal de cobro.

---

## Pregunta 16: Protección de Propiedad Intelectual mediante Ofuscación

### English Version
Which of the following options modifies data or code so that it is difficult to understand or reverse engineer, but without necessarily encrypting or hiding the data?
* [ ] Tokenization
* [ ] Encryption
* [✅] **Obfuscation**
* [ ] Hashing

### Versión en Español
¿Cuál de las siguientes opciones modifica datos o código para que sean difíciles de entender o de aplicar ingeniería inversa, pero sin necesariamente cifrar u ocultar los datos?
* [ ] Tokenización
* [ ] Cifrado
* [✅] **Ofuscación**
* [ ] Hashing

### 1. Explicación General
La **Ofuscación** (*Obfuscation*) es el proceso de complicar deliberadamente el código fuente, la estructura de programación o los datos para dificultar que un humano lo entienda, realice ingeniería de software inversa o analice su flujo de ejecución. No cifra el archivo ni necesita claves; el software puede ejecutarse de forma nativa tal como está, pero un analista que intente leer el código se encontrará con variables renombradas a caracteres caóticos e instrucciones confusas.

### 2. ¿Por qué es la correcta y no el resto?
* **Ofuscación** es el término de ingeniería de software para dificultar el análisis visual sin emplear técnicas formales de cifrado criptográfico.
* **Cifrado:** Bloquea completamente el acceso al archivo completo, haciéndolo inejecutable hasta que sea descifrado por una clave autorizada.
* **Tokenización / Hashing:** Tienen propósitos transaccionales e integridad de datos respectivamente, no están diseñados para el empaquetado seguro y distribución de lógica de software comercial.

### 3. Clave para el Examen SY0-701
La ofuscación es un método de doble filo. Las empresas de software legítimas la usan para proteger su propiedad intelectual contra la piratería, mientras que los atacantes la utilizan constantemente para camuflar el código de sus troyanos y evadir la detección de las herramientas heurísticas de seguridad de los firewalls y endpoints.

---

## Pregunta 17: Ventajas de la Segmentación de Red

### English Version
Which of the answers listed below refer to the advantages of segmentation as a method to protect data? (Select 3 answers)
* [✅] **Improves security by limiting the spread of cyber attacks**
* [✅] **Helps organizations comply with regulatory data requirements by isolating and protecting specific types of data**
* [ ] Provides security for data in transit by using encryption
* [ ] Ensures data recovery in the event of accidental deletion or system failures
* [✅] **Provides better control over user access to sensitive data**

### Versión en Español
¿Cuáles de las respuestas que aparecen a continuación se refieren a las ventajas de la segmentación como método para proteger los datos? (Seleccione 3 respuestas)
* [✅] **Mejora la seguridad al limitar la propagación de ciberataques**
* [✅] **Ayuda a las organizaciones a cumplir con los requisitos reglamentarios de datos aislando y protegiendo tipos de datos específicos**
* [ ] Proporciona seguridad para los datos en tránsito mediante el uso de cifrado.
* [ ] Garantiza la recuperación de datos en caso de eliminación accidental o fallos del sistema.
* [✅] **Proporciona un mejor control sobre el acceso del usuario a datos confidenciales**

### 1. Explicación General
La **Segmentación de Red** es una arquitectura de seguridad que consiste en dividir una red física de gran tamaño en subredes lógicas o zonas de seguridad aisladas más pequeñas (por ejemplo, mediante el uso de VLANs, firewalls de próxima generación o directivas SDN). Esto limita estrictamente qué sistemas pueden comunicarse entre sí.

### 2. ¿Por qué son las correctas y no el resto?
* **Mejorar la seguridad al limitar la propagación (Movimiento Lateral):** Si un atacante compromete un equipo en una red de invitados segmentada, no puede saltar directamente hacia la red de servidores de producción de la empresa.
* **Aislamiento para cumplimiento normativo (Compliance):** Si los datos de tarjetas (PCI DSS) se aíslan en una única subred pequeña, solo esa zona requiere auditorías complejas y controles estrictos, reduciendo drásticamente el alcance y costo del compliance.
* **Mejor control sobre el acceso de usuarios:** Facilita aplicar listas de control de acceso (ACLs) y políticas granulares para asegurar que solo los usuarios autorizados (por ejemplo, el departamento de finanzas) alcancen servidores de nóminas.
* **Cifrado de datos en tránsito:** Se logra con protocolos como TLS/IPsec, no mediante topologías de segmentación física o lógica.
* **Recuperación ante fallos/eliminación:** Es el propósito de los respaldos (Backups) y de la redundancia, no de la segmentación de redes.

### 3. Clave para el Examen SY0-701
En las arquitecturas modernas de **Confianza Cero (Zero Trust Architecture)**, la **Microsegmentación** es un principio central. Consiste en llevar la segmentación de red hasta el nivel de sistemas corporativos individuales o cargas de trabajo virtuales para inspeccionar y autorizar estrictamente cada flujo de comunicación (Norte-Sur y Este-Oeste).

---

## Pregunta 18: Mecanismos de Control de Acceso

### English Version
ACL, FACL, DAC, MAC, and RBAC are access control mechanisms that can be used to manage user permissions and protect the confidentiality, integrity, and availability of data.
* [✅] **True**
* [ ] False

### Versión en Español
ACL, FACL, DAC, MAC y RBAC son mecanismos de control de acceso que se pueden utilizar para gestionar los permisos de los usuarios y proteger la confidencialidad, la integridad y la disponibilidad de los datos.
* [✅] **Verdadero**
* [ ] Falso

### 1. Explicación General
Los modelos y mecanismos de control de acceso regulan de manera estricta qué usuarios o sistemas (sujetos) pueden leer, escribir, modificar o ejecutar recursos e información (objetos) dentro de un sistema informático, garantizando la confidencialidad, integridad y disponibilidad (Tríada CIA).

### 2. ¿Por qué es la correcta y no el resto?
**Verdadero** es la respuesta correcta porque todas las siglas mencionadas corresponden a frameworks, protocolos o especificaciones técnicas de control de acceso:
* **ACL (Access Control List):** Listas de control de acceso tradicionales a nivel de red (puertos/IPs) o archivos.
* **FACL (File Access Control List):** Listas extendidas para el control de archivos y carpetas específicas en sistemas operativos tipo Unix/Linux.
* **DAC (Discretionary Access Control):** Modelo donde el propietario del archivo decide de forma discrecional quién tiene permisos sobre él.
* **MAC (Mandatory Access Control):** El modelo más restrictivo, donde el sistema operativo compara etiquetas de clasificación de seguridad (ej. "Top Secret") con los niveles de acreditación del usuario para permitir el acceso.
* **RBAC (Role-Based Access Control):** Asigna permisos basados en los roles o perfiles laborales de los usuarios dentro de la estructura corporativa.

### 3. Clave para el Examen SY0-701
Conocer la definición exacta de cada uno de estos modelos es crítico para el dominio de Identidad y Acceso (IAM). El examen tiende a confrontar escenarios gubernamentales o militares (que requieren obligatoriamente **MAC**) con escenarios empresariales dinámicos (donde se suele preferir **RBAC** o **ABAC** basado en atributos).

---

[[ExamCompass - Cuestionarios por Temas|⬅️ Volver a Cuestionarios por Temas]]