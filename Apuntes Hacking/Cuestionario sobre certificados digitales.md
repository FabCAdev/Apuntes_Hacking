---
tags:
  - "formato/apunte"
  - "hacking/fundamental"
  - "examen/test-especifico"
  - "gestion/estado/terminado"
---
Este apunte contiene el análisis detallado del cuestionario temático sobre Certificados Digitales e Infraestructura de Clave Pública (PKI) de la plataforma ExamCompass para la certificación CompTIA Security+ (SY0-701), alineado con las respuestas oficiales del simulador.

---

## Pregunta 1: Concepto de Certificado Digital / Digital Certificate Fundamentals

### English Version
A type of digital document that verifies the identity of an individual, device, service, or organization in online communications is known as:
* [ ] Encryption key
* [✅] **Digital certificate**
* [ ] Identity token
* [ ] Digital signature

### Versión en Español
Un tipo de documento digital que verifica la identidad de un individuo, dispositivo, servicio u organización en las comunicaciones en línea se conoce como:
* [ ] Clave de cifrado (Encryption key)
* [✅] **Certificado digital**
* [ ] Token de identidad (Identity token)
* [ ] Firma digital (Digital signature)

### 1. Explicación General
Un certificado digital es el equivalente a un pasaporte o documento de identidad oficial en el mundo cibernético. Su único propósito técnico es vincular de manera oficial una clave pública con la identidad real de una entidad (un servidor web, una persona, un dispositivo, etc.) bajo el estándar internacional **X.509**.

### 2. ¿Por qué es la correcta y no el resto?
* **Opción Correcta:** `[Digital certificate / Certificado digital]` debido a que respondiste correctamente; es el único documento estructurado que da fe de quién es el dueño de una llave pública.
* **Análisis de los distractores:**
    * *Encryption key:* Es solo el componente matemático para asegurar datos, no contiene metadatos de identidad.
    * *Identity token:* (Como un token JWT) sirve para mantener sesiones activas de usuarios autenticados en aplicaciones web, no para validar infraestructura de llaves.
    * *Digital signature:* Es la acción criptográfica de validar un mensaje, no el documento de identidad.

### 3. Clave para el Examen SY0-701
En el examen, si el enunciado te habla de un **"documento digital"**, **"estándar X.509"** o de **"vincular una clave pública a una identidad"**, la respuesta inequívoca es *Digital Certificate*.

---

## Pregunta 2: El rol de la RA en PKI / Registration Authority Role

### English Version
What is the role of RA in PKI? (Select 2 answers)
* [✅] **Accepting requests for digital certificates**
* [ ] Validating digital certificates
* [✅] **Authenticating the entity making the request**
* [ ] Providing backup source for cryptographic keys
* [ ] Issuing digital certificates

### Versión en Español
¿Cuál es el rol de la RA en la PKI? (Seleccione 2 respuestas)
* [✅] **Aceptar solicitudes de certificados digitales**
* [ ] Validar certificados digitales
* [✅] **Autenticar a la entidad que realiza la solicitud**
* [ ] Proporcionar una fuente de respaldo para claves criptográficas
* [ ] Emitir certificados digitales

### 1. Explicación General
La RA (*Registration Authority* - Autoridad de Registro) actúa como el gestor o la oficina de atención al cliente de la infraestructura PKI. Su trabajo es verificar que los documentos y la identidad de quien pide un certificado sean reales y legítimos. Sin embargo, la RA no tiene el poder de fabricar ni firmar certificados.

### 2. ¿Por qué son las correctas?
* **Opciones Correctas:** `[Aceptar solicitudes...]` y `[Autenticar a la entidad...]`. Respondiste correctamente. La RA es el filtro inicial de seguridad. Revisa la identidad del solicitante y, si todo está en orden, aprueba la petición para derivarla a la CA.
* **Por qué se descartan las otras:**
    * *Validar certificados* en tiempo real es trabajo de los clientes finales (navegadores) usando CRL/OCSP.
    * *Emitir certificados (Issuing)* es una facultad exclusiva y sagrada de la CA.

### 3. Clave para el Examen SY0-701
Grábate esta analogía para CompTIA: La RA es la ventanilla gubernamental local donde entregas tus documentos físicos para el pasaporte; la CA es la fábrica central blindada que imprime y sella el pasaporte oficial. **La RA nunca emite (issue) ni firma certificados.**

---

## Pregunta 3: Tercero de confianza (CA) / Certificate Authority Core

### English Version
Which of the answers listed below refers to a trusted third party responsible for issuing, revoking, and managing digital certificates?
* [ ] RA
* [ ] DN
* [✅] **CA**
* [ ] CSP

### Versión en Español
¿Cuál de las respuestas que aparecen a continuación se refiere a un tercero de confianza responsable de emitir, revocar y gestionar certificados digitales?
* [ ] RA
* [ ] DN
* [✅] **CA**
* [ ] CSP

### 1. Explicación General
La CA (*Certificate Authority* - Autoridad de Certificación) es la máxima autoridad dentro de una infraestructura PKI. Es la entidad de absoluta confianza encargada de gestionar el ciclo de vida completo de los certificados: desde su creación (firma criptográfica) hasta su revocación si las llaves se ven comprometidas.

### 2. ¿Por qué es la correcta?
* **Opción Correcta:** `[CA]` debido a que respondiste correctamente. Es el tercero de confianza (*trusted third party*) que firma digitalmente los certificados utilizando su clave privada raíz o intermedia para otorgarles validez global.
* **Análisis de los distractores:**
    * *RA:* Solo registra e identifica identidades.
    * *DN (Distinguished Name):* Es una cadena de texto estructurada para identificar un objeto único dentro del certificado.
    * *CSP (Cryptographic Service Provider):* Es una librería de software que contiene funciones criptográficas.

### 3. Clave para el Examen SY0-701
Si la pregunta del examen menciona expresiones clave como **"Issuing" (Emitir)**, **"Revoking" (Revocar)** o **"Trusted third party" (Tercero de confianza)**, la respuesta obligatoria es CA.

---

## Pregunta 4: Publicación periódica de revocaciones (CRL) / Certificate Revocation Lists

### English Version
Which of the following answers refers to a means for periodic publication of all digital certificates that have been revoked?
* [✅] **CRL**
* [ ] OSPF
* [ ] RA
* [ ] CSR

### Versión en Español
¿Cuál de las siguientes respuestas se refiere a un medio para la publicación periódica de todos los certificados digitales que han sido revocados?
* [✅] **CRL**
* [ ] OSPF
* [ ] RA
* [ ] CSR

### 1. Explicación General
Cuando la clave privada de un certificado es robada o se compromete por un atacante, ese certificado debe cancelarse inmediatamente antes de su fecha de vencimiento original. La CRL (*Certificate Revocation List*) es una "lista negra" que la CA publica en internet de forma periódica conteniendo todos los certificados revocados.

### 2. ¿Por qué es la correcta?
* **Opción Correcta:** `[CRL]` debido a que respondiste correctamente. La palabra clave en el enunciado es **"periodic publication" (publicación periódica)**. Los clientes descargan este archivo completo para revisar si el certificado del sitio web al que entran está en la lista de cancelados.
* **Análisis de los distractores:**
    * *OSPF:* Es un protocolo de enrutamiento de redes (Capa 3).
    * *CSR:* Es la solicitud técnica para pedir un certificado.

### 3. Clave para el Examen SY0-701
Asocia siempre la palabra CRL con **"List"** (Lista completa/archivo masivo) y **"Periodic"** (Actualización por tiempos o intervalos). Su gran desventaja en los escenarios de examen es que consume mucho ancho de banda y puede quedar desactualizada entre publicaciones (periodo de latencia).

---

## Pregunta 5: Consulta de revocación bajo demanda (OCSP) / Online Certificate Status Protocol

### English Version
Which of the answers listed below refers to a protocol that enables on-demand querying of the revocation status of a digital certificate?
* [ ] CSP
* [✅] **OCSP**
* [ ] DN
* [ ] CRL

### Versión en Español
¿Cuál de las respuestas que aparecen a continuación se refiere a un protocolo que permite consultar bajo demanda el estado de revocación de un certificado digital?
* [ ] CSP
* [✅] **OCSP**
* [ ] DN
* [ ] CRL

### 1. Explicación General
Como descargar la lista completa (CRL) se volvió muy ineficiente debido al crecimiento exponencial de internet, se diseñó el protocolo OCSP (*Online Certificate Status Protocol*). En lugar de descargar todo el archivo de la lista negra, el navegador le hace una pregunta rápida en tiempo real al servidor de la CA sobre un certificado específico.

### 2. ¿Por qué es la correcta?
* **Opción Correcta:** `[OCSP]` debido a que respondiste correctamente. La frase clave es **"on-demand querying" (consulta bajo demanda o en tiempo real)**. Es una verificación de un solo certificado mediante peticiones rápidas, en lugar de procesar una lista completa.

### 3. Clave para el Examen SY0-701
Si el escenario del examen te pide verificar el estado de un certificado utilizando un protocolo de red basado en **consultas en tiempo real (Query)** de forma interactiva, la respuesta correcta es OCSP.

---

## Pregunta 6: La forma más rápida de validar un certificado / Fast Validation Options

### English Version
What is the fastest way to check the validity of a single digital certificate?
* [ ] CSR
* [ ] DN
* [ ] CRL
* [✅] **OCSP**

### Versión en Español
¿Cuál es la forma más rápida de comprobar la validez de un único certificado digital?
* [ ] CSR
* [ ] DN
* [ ] CRL
* [✅] **OCSP**

### 1. Explicación General
Esta pregunta refuerza el rendimiento práctico de OCSP frente a la arquitectura de CRL. Descargar un archivo de varios megabytes (CRL) para validar una sola página web es sumamente ineficiente para el rendimiento del navegador. Enviar un paquete de red diminuto para verificar un único certificado toma milisegundos.

### 2. ¿Por qué es la correcta?
* **Opción Correcta:** `[OCSP]` debido a que respondiste correctamente. Representa la optimización más moderna para realizar verificaciones de certificados individuales sin penalizar el tráfico de red ni la velocidad de carga de la página.

### 3. Clave para el Examen SY0-701
Aprende el concepto de **"OCSP Stapling"** para el examen. Es una optimización donde el propio servidor web le pide la validación firmada a la CA con antelación (la grapa) y se la entrega directamente al navegador del usuario durante el saludo TLS (*TLS handshake*), ahorrando conexiones extra a servidores de terceros y protegiendo la privacidad del cliente.

---

## Pregunta 7: Características de Certificados Autofirmados / Self-Signed Certificates Features

### English Version
Which of the following answers can be used to describe self-signed digital certificates? (Select 3 answers)
* [ ] Backed by a well-known and trusted third party
* [✅] **Not trusted by default by web browsers and other applications**
* [✅] **Used in trusted environments, such as internal networks and development environments**
* [ ] Suitable for websites and other applications that are accessible to the public
* [ ] Trusted by default by web browsers and other applications
* [✅] **Not backed by a well-known and trusted third party**

### Versión en Español
¿Cuáles de las siguientes respuestas pueden utilizarse para describir los certificados digitales autofirmados? (Seleccione 3 respuestas)
* [ ] Respaldado por un tercero de confianza y bien conocido
* [✅] **No son confiables por defecto por los navegadores web y otras aplicaciones**
* [✅] **Utilizados en entornos de confianza, como redes internas y entornos de desarrollo**
* [ ] Adecuados para sitios web y otras aplicaciones accesibles al público
* [ ] Confiables por defecto por los navegadores web y otras aplicaciones
* [✅] **No están respaldados por un tercero de confianza y bien conocido**

### 1. Explicación General
Un certificado autofirmado (*Self-signed*) es aquel donde una entidad o un servidor genera su propio certificado y él mismo lo firma, sin acudir a una autoridad externa oficial pública. Piensa en esto como una credencial de identificación hecha en casa: sirve para laboratorios internos, pero el resto de las entidades no la aceptarán por defecto porque carece de respaldo institucional oficial.

### 2. Análisis de las respuestas correctas
* **[Not trusted by default...]:** Al no estar firmados por una CA pública oficial preinstalada en el almacén de confianza del sistema operativo (como DigiCert o Let's Encrypt), los navegadores web mostrarán de inmediato una pantalla de alerta roja de seguridad.
* **[Used in trusted environments...]:** Son ideales para entornos de desarrollo locales o laboratorios internos de pruebas, ya que permiten simular conexiones cifradas HTTPS sin costo monetario.
* **[Not backed by a well-known...]:** Por definición técnica, no cuentan con el aval de un tercero de confianza.

### 3. Corrigiendo el Desliz Técnico
* *¿Por qué fallaron tus elecciones originales?* Habías marcado las opciones que indicaban que estaban respaldados por CAs conocidas y que eran confiables por defecto. Recuerda que eso describe exactamente lo opuesto: los certificados comerciales o de PKI pública. Los autofirmados carecen de esa raíz de confianza pública.

### 4. Clave para el Examen SY0-701
Si un escenario de CompTIA menciona que una empresa busca reducir costos en servidores de prueba, laboratorios de investigación o entornos de desarrollo interno (**testing/development/lab**), la solución adecuada son los *Self-signed certificates*. Si la aplicación está expuesta a clientes en Internet, usarlos es inaceptable.

---

## Pregunta 8: Otro nombre para Certificados Autofirmados / Terminology

### English Version
A self-signed digital certificate is also referred to as:
* [ ] Client certificate
* [ ] EV certificate
* [ ] Server certificate
* [ ] Wildcard certificate
* [✅] **None of the above**

### Versión en Español
Un certificado digital autofirmado también se conoce como:
* [ ] Certificado de cliente (Client certificate)
* [ ] Certificado EV (EV certificate)
* [ ] Certificado de servidor (Server certificate)
* [ ] Certificado comodín (Wildcard certificate)
* [✅] **Ninguno de los anteriores**

### 1. Explicación General
Los certificados se clasifican comúnmente en la industria por su función técnica (*Client, Server*), su alcance de nombres (*Wildcard*) o por sus niveles de validación legal (*EV*). Ninguno de estos términos describe de forma inherente la identidad de la entidad firmante o la naturaleza matemática de la autofirma.

### 2. ¿Por qué es la correcta?
* **Opción Correcta:** `[None of the above / Ninguno de los anteriores]` debido a que respondiste correctamente. Aunque un certificado autofirmado puede cumplir la función de un certificado de servidor (*Server certificate*), no es un sinónimo directo de este. El término técnico preciso en la arquitectura de seguridad es **Self-signed Root Certificate** o certificado raíz de anclaje propio.

---

## Pregunta 9: Certificados Comerciales vs. Autofirmados / CA-Issued vs. Self-Signed

### English Version
Third-party digital certificates, issued by trusted CAs, are automatically trusted by most browsers and operating systems, involve a cost, and require validation of the applicant's identity. In contrast, self-signed certificates, issued by the entity to itself, are not automatically trusted, are free to create and use, and do not require validation by a CA.
* [✅] **True**
* [ ] False

### Versión en Español
Los certificados digitales de terceros, emitidos por CAs de confianza, son confiables automáticamente por la mayoría de los navegadores y sistemas operativos, implican un costo y requieren la validación de la identidad del solicitante. In cambio, los certificados autofirmados, emitidos por la propia entidad para sí misma, no son confiables automáticamente, son gratuitos de crear y usar, y no requieren la validación de una CA.
* [✅] **Verdadero**
* [ ] Falso

### 1. Explicación General
Esta pregunta de Verdadero/Falso resume de manera clara el contraste teórico que se evalúa en el examen, delimitando el alcance operativo, de confianza y financiero de ambas opciones criptográficas.

### 2. ¿Por qué es la correcta?
* **Opción Correcta:** `[True / Verdadero]` debido a que respondiste correctamente. La afirmación plasma con precisión las ventajas e inconvenientes del ecosistema de confianza de la PKI pública frente a la autogestión de certificados locales.

---

## Pregunta 10: Raíz de Confianza (Root of Trust) / Root CA Concepts

### English Version
In the context of digital certificates, the term "Root of trust" refers to the highest level of trust within a PKI system. It is typically represented by a root CA, which is a trusted third party that serves as the foundation for the entire PKI. All other entities in the PKI hierarchy, including intermediate CAs and end-entities (such as web servers, email servers, user devices, IoT devices, and individual users), derive their trust from this root...
* [✅] **True**
* [ ] False

### Versión en Español
En el contexto de los certificados digitales, el término "Raíz de confianza" se refiere al nivel más alto de confianza dentro de un sistema PKI. Normalmente está representado por una CA raíz, que es un tercero de confianza que sirve como base para toda la PKI. Todas las demás entidades de la jerarquía de la PKI, incluidas las CA intermedias y las entidades finales (como servidores web, servidores de correo electrónico, dispositivos de usuario, dispositivos IoT e usuarios individuales), derivan su confianza de esta raíz...
* [✅] **Verdadero**
* [ ] Falso

### 1. Explicación General
El modelo jerárquico de la PKI funciona bajo un principio de "herencia de confianza". En la cúspide de la pirámide se encuentra la **Root CA**. Si tu sistema operativo confía en la Root CA, por extensión confiará automáticamente en las entidades descendientes (*Intermediate CAs*) y en los certificados finales (*End-entities*) de las páginas web que visitas. A esta estructura lineal se le conoce como **Cadena de Confianza (Chain of Trust)**.

### 2. ¿Por qué es la correcta?
* **Opción Correcta:** `[True / Verdadero]` debido a que respondiste correctamente. El texto describe fielmente cómo se hereda y se traza la validez criptográfica hacia atrás hasta llegar al anclaje principal.

### 3. Clave para el Examen SY0-701
Para proteger la validez absoluta de esta infraestructura, las organizaciones implementan una **Offline Root CA** (CA Raíz fuera de línea). Esta máquina raíz se mantiene completamente desconectada de la red y resguardada bajo estricta seguridad física. Solo se enciende de forma controlada para emitir certificados a las CAs intermedias (*Intermediate CAs*), que son las que se quedan conectadas a internet (*Online*) lidiando con la emisión del día a día. Esto evita que un ataque de red comprometa la raíz completa de la infraestructura corporativa.

---

## Pregunta 11: Modelos de Confianza PKI / Trust Models Architecture

### English Version
Which of the answers listed below refers to a PKI trust model?
* [ ] Single CA model
* [ ] Hierarchical model (root CA + intermediate CAs)
* [ ] Mesh model (cross-certifying CAs)
* [ ] Web of trust model (all CAs function as root CAs)
* [ ] Chain of trust model (multiple CAs in a sequential chain)
* [ ] Bridge model (cross-certifying between separate PKIs)
* [ ] Hybrid model (combining aspects of different models)
* [✅] **All of the above**

### Versión en Español
¿Cuál de las respuestas que aparecen a continuación se refiere a un modelo de confianza PKI?
* [ ] Modelo de CA única (Single CA model)
* [ ] Modelo jerárquico (Hierarchical model - root CA + intermediate CAs)
* [ ] Modelo de malla (Mesh model - cross-certifying CAs)
* [ ] Modelo de red de confianza (Web of trust model)
* [ ] Modelo de cadena de confianza (Chain of trust model)
* [ ] Modelo de puente (Bridge model - cross-certifying between separate PKIs)
* [ ] Modelo híbrido (Hybrid model)
* [✅] **Todos los anteriores**

### 1. Explicación General
Dependiendo de la escala de una corporación, de si se están unificando los sistemas de dos empresas distintas tras una fusión, o de si se trabaja en un entorno descentralizado (como PGP), el diseño de las relaciones de confianza criptográfica cambia para adaptarse a las necesidades del negocio.

### 2. ¿Por qué es la correcta?
* **Opción Correcta:** `[All of the above / Todos los anteriores]` debido a que respondiste correctamente. Todos los modelos listados existen formalmente en el diseño de arquitecturas de seguridad de red. Desde el clásico *Hierarchical* hasta el modelo *Bridge* (diseñado para interconectar de forma cruzada dos PKIs corporativas independientes sin que una deba someterse a la jerarquía de la otra).

---

## Pregunta 12: Solicitud de Certificado (CSR) / Certificate Signing Requests

### English Version
Which of the following answers refers to a cryptographic file generated by an entity requesting a digital certificate from a CA?
* [ ] OID
* [✅] **CSR**
* [ ] DN
* [ ] CRL

### Versión en Español
¿Cuál de las siguientes respuestas se refiere a un archivo criptográfico generado por una entidad que solicita un certificado digital a una CA?
* [ ] OID
* [✅] **CSR**
* [ ] DN
* [ ] CRL

### 1. Explicación General
Cuando necesitas habilitar HTTPS en un servidor web, el paso inicial es configurar un paquete estructurado de datos local. Este bloque empaqueta los datos de la compañía junto con la clave pública del servidor y se envía firmado electrónicamente a la CA para su validación.

### 2. ¿Por qué es la correcta?
* **Opción Correcta:** `[CSR]` (*Certificate Signing Request*). Respondiste correctamente. Es el formato estandarizado que contiene los metadatos de identidad del solicitante y su clave pública listos para ser procesados por la CA.
* **Análisis de los distractores:**
    * *OID:* Es un identificador de objetos.
    * *CRL:* Es el archivo de la lista negra de revocación.
    * *DN:* Es el nombre distintivo que compone los campos de identidad.

### 3. Clave para el Examen SY0-701
Principio vital de seguridad: **Al generar un CSR, la clave privada NUNCA sale del servidor local.** El archivo CSR únicamente distribuye la clave pública e información de identidad. Si un escenario de CompTIA te insinúa que debes transferir tu clave privada a la CA para que fabriquen el certificado, esa opción es un grave error de seguridad.

---

## Pregunta 13: Subdominios dentro de un dominio primario / Wildcard Certificates

### English Version
A type of digital certificate that can be used to secure multiple subdomains within a primary domain is called:
* [ ] Root signing certificate
* [ ] Subject Alternative Name (SAN) certificate
* [ ] Extended Validation (EV) certificate
* [✅] **Wildcard certificate**

### Versión en Español
Un tipo de certificado digital que se puede utilizar para asegurar múltiples subdominios dentro de un dominio primario se denomina:
* [ ] Certificado de firma raíz (Root signing certificate)
* [ ] Certificado de Nombre Alternativo del Sujeto (SAN)
* [ ] Certificado de Validación Extendida (EV)
* [✅] **Certificado comodín (Wildcard certificate)**

### 1. Explicación General
Un certificado Wildcard (comodín) implementa un carácter expansivo (asterisco) en su diseño. Al emitirse para un dominio base con la estructura `*.tuempresa.com`, protegerá automáticamente cualquier subdominio directo de primer nivel bajo esa misma raíz sin necesidad de reemitir el certificado.

### 2. Corrigiendo el Desliz Técnico
* *¿Por qué falló tu elección original?* Elegiste SAN, lo cual es un error común porque un certificado SAN técnicamente puede dar soporte a subdominios listándolos de forma manual uno a uno. Sin embargo, la clave del enunciado radica en la expresión: **"multiple subdomains within a primary domain"** (múltiples subdominios dentro de un dominio primario). Cuando la necesidad operativa busca cubrir subdominios que cuelgan del mismo árbol raíz de manera dinámica y escalable, la solución idónea es un *Wildcard*.
* Protegerá de forma automatizada entornos como `correo.tuempresa.com`, `ventas.tuempresa.com` o `dev.tuempresa.com`.

### 3. Clave para el Examen SY0-701
Si la pregunta en CompTIA te exige proteger una cantidad indeterminada, dinámica o creciente de subdominios que **comparten exactamente la misma raíz de dominio**, la opción correcta es **Wildcard**.

---

## Pregunta 14: Múltiples nombres de dominios diferentes / Subject Alternative Name (SAN)

### English Version
Which digital certificate type allows to secure multiple domain names or subdomains with a single certificate?
* [ ] Extended Validation (EV) certificate
* [ ] Wildcard certificate
* [✅] **Subject Alternative Name (SAN) certificate**
* [ ] Root signing certificate

### Versión en Español
¿Qué tipo de certificado digital permite asegurar múltiples nombres de dominio o subdominios con un solo certificado?
* [ ] Certificado de Validación Extendida (EV)
* [ ] Certificado comodín (Wildcard certificate)
* [✅] **Certificado de Nombre Alternativo del Sujeto (SAN)**
* [ ] Certificado de firma raíz (Root signing certificate)

### 1. Explicación General
Los certificados SAN (*Subject Alternative Name*) permiten insertar un listado estructurado de múltiples dominios, nombres de host o subdominios dentro del campo de extensiones de un único certificado digital X.509. Esto permite unificar la gestión criptográfica de infraestructuras empresariales diversas bajo un mismo archivo.

### 2. Corrigiendo el Desliz Técnico
* *¿Por qué falló tu elección original?* Seleccionaste EV (*Extended Validation*). Los certificados EV describen el nivel de escrutinio e investigación legal exhaustiva que la CA realiza sobre la empresa antes de emitir (para mitigar fraudes o phishing), pero no definen la cantidad técnica de dominios que puede contener el archivo.
* La respuesta correcta era SAN, puesto que el enunciado especificaba **"multiple domain names"** (múltiples nombres de dominio diferentes). Un certificado Wildcard está estrictamente limitado a una sola raíz; no puede proteger marcas o extensiones distintas de manera simultánea (ej. `empresaA.com` y `empresaB.net`), mientras que un certificado SAN sí puede listar dominios totalmente inconexos en el mismo documento.

### 3. Clave para el Examen SY0-701
Aprende a diferenciarlos con esta regla de oro en el examen:
* Si te piden proteger subdominios ilimitados de un mismo dominio base (ej: `*.google.com`) ➔ **Wildcard**.
* Si te piden proteger dominios completamente distintos en un solo certificado (ej: `google.com`, `youtube.com`, `android.com`) ➔ **SAN** (también denominado en la industria como *Multi-Domain* o certificado UCC).

---

## Pregunta 15: Identificador de objetos PKI (OID) / Object Identifiers

### English Version
Which of the answers listed below refers to an identifier used for PKI objects?
* [✅] **OID**
* [ ] DN
* [ ] SAN
* [ ] GUID

### Versión en Español
¿Cuál de las respuestas listadas a continuación se refiere a un identificador utilizado para objetos PKI?
* [✅] **OID**
* [ ] DN
* [ ] SAN
* [ ] GUID

### 1. Explicación General
Un OID (*Object Identifier* - Identificador de Objeto) es una cadena estandarizada de números enteros separados por puntos (como por ejemplo `2.5.4.3`) que opera como un código de barras o identificador universal e inequívoco en criptografía y telecomunicaciones.

### 2. ¿Para qué sirve?
Garantiza que cualquier sistema operativo, navegador o software del mundo entienda con exactitud qué elemento técnico se está describiendo dentro de una estructura ASN.1 (como el certificado X.509) sin importar las barreras del idioma o la plataforma. Por ejemplo, hay un OID asignado globalmente para indicar de forma estricta que un campo de texto contiene el *Common Name* (CN) o que el algoritmo de firma empleado es `SHA-256`.

### 3. Clave para el Examen SY0-701
Si en el examen encuentras una pregunta sobre la arquitectura interna de un certificado digital que describa una **cadena jerárquica de números separados por puntos** (por ejemplo, `1.3.6.1.4.1...`), la respuesta correcta hace referencia a un OID.

---

[[ExamCompass - Cuestionarios por Temas|⬅️ Volver a Cuestionarios por Temas]]