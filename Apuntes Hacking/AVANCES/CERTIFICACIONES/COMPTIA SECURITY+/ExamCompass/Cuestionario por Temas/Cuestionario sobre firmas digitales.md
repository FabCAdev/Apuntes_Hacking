---
tags:
  - "formato/apunte"
  - "hacking/fundamental"
  - "examen/test-especifico"
  - "gestion/estado/terminado"
---
Este apunte contiene el análisis detallado del cuestionario temático sobre certificados digitales e infraestructura PKI de la plataforma ExamCompass para la certificación CompTIA Security+ (SY0-701), alineado con las respuestas oficiales del simulador.

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
* [ ] Clave de cifrado
* [✅] **Certificado digital**
* [ ] Token de identidad
* [ ] Firma digital

### 1. Explicación General
Un certificado digital es el equivalente a un documento de identidad oficial en el entorno cibernético. Su único propósito técnico es vincular una clave pública con la identidad real de una entidad (un servidor web, una persona o un dispositivo) bajo el estándar internacional X.509, garantizando que la llave pertenece a quien dice ser.

### 2. ¿Por qué es la correcta y no el resto?
* **Opción Correcta:** `[Digital certificate / Certificado digital]` debido a que constituye el único documento estructurado y firmado por una entidad de confianza (CA) que da fe de la titularidad de una llave pública.
* **Análisis de los distractores:**
    * *Encryption key:* Representa únicamente el componente matemático para cifrar o descifrar datos, careciendo de metadatos de identidad.
    * *Identity token:* Se utiliza para mantener sesiones activas de usuarios autenticados en aplicaciones web (como un token JWT), no para validar la infraestructura de llaves.
    * *Digital signature:* Es el resultado de la acción criptográfica de validar un mensaje o documento, no el documento de identidad en sí mismo.

### 3. Clave para el Examen SY0-701
Cuando el enunciado mencione un "documento digital", el "estándar X.509" o la acción de "vincular una clave pública a una identidad", la respuesta de examen siempre es un Certificado Digital.

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
¿Cuál de las respuestas que aparecen a continuación se refiere a un protocolo que permite consultar bajo demanda el estado de revocación de un certificado digital?
* [✅] **Aceptar solicitudes de certificados digitales**
* [ ] Validar certificados digitales
* [✅] **Autenticar a la entidad que realiza la solicitud**
* [ ] Proporcionar una fuente de respaldo para claves criptográficas
* [ ] Emitir certificados digitales

### 1. Explicación General
La RA (Registration Authority) actúa como el brazo administrativo u oficina de atención dentro de la infraestructura PKI. Su función consiste en verificar que los documentos y la identidad del solicitante sean reales y legítimos antes de pasar la petición a la CA. Al ser solo un intermediario de validación, carece de la facultad de fabricar o firmar certificados.

### 2. ¿Por qué es la correcta y no el resto?
* **Opciones Correctas:** `[Accepting requests... / Authenticating the entity...]` debido a que la RA opera como el filtro inicial de seguridad. Recibe la petición, valida la identidad del solicitante cara a cara o mediante documentos oficiales y aprueba el trámite.
* **Análisis de los distractores:**
    * *Validating digital certificates:* La validación de certificados vigentes en tiempo real corresponde a los clientes finales (como los navegadores web) mediante tecnologías como CRL o consultas OCSP.
    * *Providing backup source...:* El respaldo de claves criptográficas (Key Escrow) es ejecutado por servidores de almacenamiento seguro o módulos HSM.
    * *Issuing digital certificates:* La emisión (fabricación y firma) de certificados es una facultad exclusiva de la CA.

### 3. Clave para el Examen SY0-701
Utiliza la analogía de que la RA es la oficina gubernamental local donde entregas tus papeles físicos, mientras que la CA es la fábrica central que imprime tu pasaporte. La RA nunca emite (*issue*) ni firma certificados.

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
La CA (Certificate Authority) representa la máxima autoridad y el núcleo de confianza dentro de una infraestructura PKI. Es la entidad encargada de gestionar el ciclo de vida completo de los certificados: desde su creación mediante firma criptográfica hasta su eventual revocación si las llaves se ven comprometidas.

### 2. ¿Por qué es la correcta y no el resto?
* **Opción Correcta:** `[CA]` por ser el tercero de confianza (*trusted third party*) que firma digitalmente los certificados utilizando su propia clave privada para otorgarles validez global ante cualquier sistema operativo.
* **Análisis de los distractores:**
    * *RA:* Se limita a registrar y verificar las identidades, sin poseer capacidad de firma de infraestructura.
    * *DN (Distinguished Name):* Es una cadena de texto estructurada (como `CN=www.google.com`) utilizada para identificar un objeto único dentro del certificado.
    * *CSP (Cryptographic Service Provider):* Hace referencia a una librería de software o proveedor que contiene funciones criptográficas para el sistema operativo.

### 3. Clave para el Examen SY0-701
Si la pregunta del examen incluye expresiones clave como "Issuing" (Emitir), "Revoking" (Revocar) o "Trusted third party" (Tercero de confianza), la respuesta obligatoria es la CA.

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
Cuando la clave privada de un certificado es robada, el certificado debe cancelarse inmediatamente antes de su fecha de vencimiento original. La CRL (Certificate Revocation List) es una "lista negra" que la CA publica en internet con todos los certificados revocados para que los navegadores sepan en quién no confiar.

### 2. ¿Por qué es la correcta y no el resto?
* **Opción Correcta:** `[CRL]` debido a que el enunciado especifica una *"periodic publication"* (publicación periódica). Consiste en un archivo completo que los clientes descargan para revisar si el certificado del sitio web al que acceden se encuentra cancelado.
* **Análisis de los distractores:**
    * *OSPF:* Es un protocolo de enrutamiento dinámico de redes en Capa 3, ajeno a la seguridad PKI.
    * *RA:* Es la entidad administrativa encargada del registro de identidades.
    * *CSR:* Es la solicitud técnica inicial para pedir un certificado a la CA, no un medio de revocación.

### 3. Clave para el Examen SY0-701
Debes asociar el término CRL con "List" (Lista completa/archivo masivo) y "Periodic" (Actualización por intervalos de tiempo). Su gran desventaja es el periodo de latencia (si se actualiza cada 24 horas, un certificado robado hace 1 hora pasará como válido).

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
Debido a que descargar la lista completa (CRL) se volvió ineficiente por el crecimiento de internet, se diseñó OCSP. En lugar de bajarse todo el archivo de la lista negra, el navegador web realiza una consulta rápida en tiempo real al servidor de la CA sobre un certificado específico y este le responde inmediatamente su estado.

### 2. ¿Por qué es la correcta y no el resto?
* **Opción Correcta:** `[OCSP]` porque el enunciado resalta *"on-demand querying"* (consulta bajo demanda o en tiempo real). Permite una verificación rápida mediante peticiones individuales, devolviendo respuestas puntuales como "Válido" o "Revocado".
* **Análisis de los distractores:**
    * *CSP:* Es una librería de funciones criptográficas de software.
    * *DN:* Es el nombre distintivo que compone los campos de identidad del certificado.
    * *CRL:* No opera bajo demanda interactiva, sino que consiste en un archivo estático que se descarga por completo de forma periódica.

### 3. Clave para el Examen SY0-701
Si el escenario plantea la verificación del estado de un certificado utilizando un protocolo basado en consultas en tiempo real (Query) de manera interactiva y veloz, la respuesta correcta es OCSP.

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
Esta pregunta evalúa el rendimiento práctico de OCSP frente a la arquitectura de CRL. Descargar un archivo masivo (CRL) para validar una sola firma o sitio web resulta muy lento, mientras que enviar un paquete de red mínimo para verificar un único certificado toma milisegundos.

### 2. ¿Por qué es la correcta y no el resto?
* **Opción Correcta:** `[OCSP]` por representar la optimización más moderna para realizar verificaciones de certificados individuales sin penalizar el tráfico de red ni la velocidad de carga de la página.
* **Análisis de los distractores:**
    * *CRL:* Es un método más lento debido a que requiere la descarga y el procesamiento de toda la lista acumulada de exclusiones.
    * *CSR y DN:* No constituyen herramientas ni protocolos de validación de revocación; el primero es una solicitud de firma y el segundo es un campo de identidad.

### 3. Clave para el Examen SY0-701
Domina también el concepto de OCSP Stapling (Grapado OCSP). Es una optimización donde el propio servidor web solicita la validación firmada a la CA con antelación y se la "grapa" directamente al navegador del usuario durante el saludo TLS, ahorrando conexiones adicionales.

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
Un certificado autofirmado (Self-signed) es aquel generado y firmado por la propia entidad o servidor, sin recurrir a una CA externa oficial. Equivale a una credencial de identificación de fabricación propia: es útil para entornos internos, pero los sistemas externos no la aceptarán por defecto al carecer de un respaldo institucional precargado.

### 2. ¿Por qué es la correcta y no el resto?
* **Opciones Correctas:** Describen con precisión la naturaleza de la autofirma. Al no encontrarse en el almacén de confianza de los sistemas operativos, provocan advertencias de seguridad en los navegadores, pero resultan idóneos para implementar conexiones cifradas HTTPS de forma interna y sin costos.
* **Análisis de los distractores:** Se descartan debido a que describen la operación de los certificados comerciales o de PKI pública emitidos por una CA acreditada.

### 3. Clave para el Examen SY0-701
Si un escenario indica que una empresa busca reducir costos en servidores de prueba, laboratorios de investigación o entornos de desarrollo interno (*testing/development/lab*), la solución adecuada son los Certificados Autofirmados.

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
* [ ] Certificado de cliente
* [ ] Certificado EV
* [ ] Certificado de servidor
* [ ] Certificado comodín
* [✅] **Ninguno de los anteriores**

### 1. Explicación General
Los certificados se clasifican habitualmente en la industria por su función técnica (Client, Server), su alcance de nombres (Wildcard) o por sus niveles de validación legal (EV). Ninguno de estos términos describe de forma inherente la identidad de la entidad firmante o la naturaleza matemática de la autofirma.

### 2. ¿Por qué es la correcta and no el resto?
* **Opción Correcta:** `[None of the above / Ninguno de los anteriores]` porque, aunque un certificado autofirmado puede cumplir la función de un certificado de servidor, no es un sinónimo directo de este. El término técnico preciso en la arquitectura de seguridad cuando se habla del anclaje maestro es *Self-signed Root Certificate*.
* **Análisis de los distractores:** *Client, EV, Server, Wildcard* describen tipos funcionales o niveles de validación de certificados que, por norma general, son emitidos por una CA legítima y no autofirmados por un sistema local de forma genérica.

### 3. Clave para el Examen SY0-701
No confundas el rol del certificado (su propósito de uso, como un *Server Certificate* para HTTPS) con la entidad que lo firmó. Un certificado puede ser de servidor y estar autofirmado, pero un concepto no equivale al otro.

---

## Pregunta 9: Certificados Comerciales vs. Autofirmados / CA-Issued vs. Self-Signed

### English Version
Third-party digital certificates, issued by trusted CAs, are automatically trusted by most browsers and operating systems, involve a cost, and require validation of the applicant's identity. In contrast, self-signed certificates, issued by the entity to itself, are not automatically trusted, are free to create and use, and do not require validation by a CA.
* [✅] **True**
* [ ] False

### Versión en Español
Los certificados digitales de terceros, emitidos por CAs de confianza, son confiables automáticamente por la mayoría de los navegadores y sistemas operativos, implican un costo y requieren la validación de la identidad del solicitante. En cambio, los certificados autofirmados, emitidos por la propia entidad para sí misma, no son confiables automáticamente, son gratuitos de crear y usar, y no requieren la validación de una CA.
* [✅] **Verdadero**
* [ ] Falso

### 1. Explicación General
Esta pregunta delimita el alcance operativo, el nivel de confianza que otorgan de manera automatizada los sistemas informáticos y el impacto financiero de ambas opciones criptográficas dentro de la industria.

### 2. ¿Por qué es la correcta y no el resto?
* **Opción Correcta:** `[True / Verdadero]` dado que plasma con precisión el funcionamiento del ecosistema: los certificados de CA pública tienen un costo, validan la identidad del solicitante y son transparentes para el usuario final. Los autofirmados son gratuitos y rápidos de generar, pero disparan alertas de seguridad si se exponen al público.

### 3. Clave para el Examen SY0-701
Para el examen, se deben asociar siempre los certificados emitidos por CAs comerciales con entornos de Producción (Production) y aplicaciones de cara al cliente público (*Public-facing*).

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
El modelo jerárquico de la PKI se basa en el principio de "herencia de confianza". En la cúspide de la pirámide estructural se ubica la Root CA. Si el sistema operativo o navegador confía en dicha Root CA, por extensión confiará automáticamente en las entidades descendientes (Intermediate CAs) y en los certificados finales.

### 2. ¿Por qué es la correcta y no el resto?
* **Opción Correcta:** `[True / Verdadero]` porque describe fielmente cómo se hereda y se traza la validez criptográfica hacia atrás hasta alcanzar el anclaje principal (Root CA) a través de la Cadena de Confianza (*Chain of Trust*).

### 3. Clave para el Examen SY0-701
Para proteger la validez absoluta de esta infraestructura, las organizaciones implementan una Offline Root CA. Esta máquina raíz se mantiene completamente desconectada de la red y resguardada bajo estricta seguridad física para evitar que un ataque remoto comprometa toda la empresa.

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
* [ ] Modelo de CA única
* [ ] Modelo jerárquico (*Hierarchical model*)
* [ ] Modelo de malla (*Mesh model*)
* [ ] Modelo de red de confianza (*Web of trust model*)
* [ ] Modelo de cadena de confianza (*Chain of trust model*)
* [ ] Modelo de puente (*Bridge model*)
* [ ] Modelo híbrido (*Hybrid model*)
* [✅] **Todos los anteriores**

### 1. Explicación General
Dependiendo de la escala de una corporación, de si se están unificando los sistemas de dos empresas distintas tras una fusión, o de si se trabaja en un entorno descentralizado, el diseño de las relaciones de confianza de la PKI cambia para adaptarse a las necesidades del negocio.

### 2. ¿Por qué es la correcta y no el resto?
* **Opción Correcta:** `[All of the above / Todos los anteriores]` porque todos los modelos listados existen formalmente en la arquitectura de seguridad. El *Hierarchical* es el estándar web. El modelo *Web of Trust* es el modelo descentralizado típico de PGP/GPG donde los propios usuarios se firman entre sí.
* **El modelo Bridge:** Está diseñado para interconectar de forma cruzada dos PKIs corporativas independientes a través de una CA "puente".

### 3. Clave para el Examen SY0-701
Presta especial atención al *Bridge Model*. Si CompTIA plantea un escenario de fusión (*merger*) entre dos empresas que necesitan confiar en los certificados mutuos sin alterar o subordinar sus CAs raíces individuales, la respuesta técnica clave es el modelo de puente.

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
Para habilitar HTTPS en un servidor web, el paso inicial consiste en configurar un paquete estructurado de datos de forma local. Este bloque empaqueta los datos de la organización junto con la clave pública generada por el servidor, y se envía firmado electrónicamente a la CA para que valide la información.

### 2. ¿Por qué es la correcta y no el resto?
* **Opción Correcta:** `[CSR - Certificate Signing Request]` por tratarse del formato estandarizado (PKCS#10) que contiene los metadatos de identidad del solicitante y su clave pública listos para ser procesados por la CA.
* **Análisis de los distractores:**
    * *OID:* Consiste en un identificador de objetos criptográficos representado por números separados por puntos.
    * *CRL:* Es el archivo que contiene la lista negra de revocación.
    * *DN:* Es el nombre distinguido en texto legible que compone los campos de identidad individuales dentro de la solicitud.

### 3. Clave para el Examen SY0-701
Principio vital de seguridad: Al generar un CSR, la clave privada **NUNCA sale del servidor local**. El archivo CSR únicamente distribuye la clave pública e información de identidad. Si un escenario insinúa que debes transferir la clave privada a la CA, descarta esa opción de inmediato.

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
* [ ] Certificado de firma raíz
* [ ] Certificado de Nombre Alternativo del Sujeto (SAN)
* [ ] Certificado de Validación Extendida (EV)
* [✅] **Certificado comodín (Wildcard)**

### 1. Explicación General
Un certificado Wildcard (comodín) implementa un carácter expansivo (un asterisco `*`) en su diseño de nombre. Al emitirse para un dominio base con la estructura `*.tuempresa.com`, protegerá automáticamente cualquier subdominio directo de primer nivel bajo esa misma raíz, evitando la necesidad de adquirir o gestionar certificados individuales.

### 2. ¿Por qué es la correcta y no el resto?
* **Opción Correcta:** `[Wildcard certificate]` debido a que cubre de forma automatizada entornos que compartan la misma raíz, como `correo.tuempresa.com` o `dev.tuempresa.com`.
* **Análisis de los distractores:** *Subject Alternative Name (SAN)* se descarta porque, aunque un certificado SAN técnicamente puede dar soporte a subdominios listándolos manualmente uno a uno, la clave del enunciado radica en cubrir subdominios que cuelgan del mismo árbol raíz de manera dinámica e ilimitada.

### 3. Clave para el Examen SY0-701
Si la pregunta en CompTIA exige proteger una cantidad indeterminada, dinámica o creciente de subdominios que comparten exactamente la misma raíz de dominio (ej. `*.dominio.com`), la opción correcta es un Wildcard Certificate.

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
* [ ] Certificado comodín (Wildcard)
* [✅] **Certificado de Nombre Alternativo del Sujeto (SAN)**
* [ ] Certificado de firma raíz

### 1. Explicación General
Los certificados SAN (Subject Alternative Name) permiten insertar un listado estructurado de múltiples dominios, nombres de host o subdominios completamente diferentes dentro del campo de extensiones de un único certificado digital X.509, ideal para unificar la gestión criptográfica de infraestructuras corporativas diversas.

### 2. ¿Por qué es la correcta y no el resto?
* **Opción Correcta:** `[Subject Alternative Name (SAN) certificate]` puesto que el enunciado especifica *"multiple domain names"* (múltiples nombres de dominio diferentes). Un certificado SAN puede listar dominios totalmente inconexos en el mismo documento (ej. `empresaA.com`, `empresaB.net`, `tiendita.org`).
* **Análisis de los distractores:**
    * *Extended Validation (EV):* Describe el nivel de escrutinio e investigación legal exhaustiva que la CA realiza sobre la empresa antes de la emisión, pero no define la cantidad técnica de dominios.
    * *Wildcard certificate:* Está estrictamente limitado a una sola raíz; no puede proteger marcas o extensiones distintas de manera simultánea.

### 3. Clave para el Examen SY0-701
Regla de diferenciación definitiva en el examen: Si se solicita proteger subdominios ilimitados de un mismo dominio base $\rightarrow$ Wildcard. Si se solicita proteger dominios completamente distintos en un solo certificado $\rightarrow$ SAN (Multi-Domain).

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
Un OID (Object Identifier) es una cadena estandarizada de números enteros separados por puntos (como por ejemplo `2.5.4.3`) que opera como un identificador universal e inequívoco en criptografía, certificados X.509 y directorios LDAP para definir tipos de objetos y atributos.

### 2. ¿Por qué es la correcta y no el resto?
* **Opción Correcta:** `[OID]` porque garantiza que cualquier sistema operativo o navegador interprete con exactitud qué elemento técnico se está describiendo dentro de un certificado, independientemente del idioma. Existen OIDs asignados globalmente para indicar que un campo contiene el Common Name (CN) o que el algoritmo es SHA-256.
* **Análisis de los distractores:**
    * *DN:* Es el nombre distinguido en texto legible, no el identificador numérico de registro del objeto.
    * *GUID:* Es un identificador único global utilizado principalmente por sistemas operativos de Microsoft para componentes de software, no para la arquitectura interna de objetos PKI.

### 3. Clave para el Examen SY0-701
Si en el examen se presenta una pregunta sobre la arquitectura interna de un certificado digital que describa una cadena jerárquica de números separados por puntos, la respuesta correcta hace referencia a un OID.

---

[[ExamCompass - Cuestionarios por Temas|⬅️ Volver a Cuestionarios por Temas]]