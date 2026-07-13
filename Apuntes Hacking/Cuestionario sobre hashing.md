---
tags:
  - "formato/apunte"
  - "hacking/fundamental"
  - "examen/test-especifico"
  - "gestion/estado/terminado"
---
Este apunte contiene el análisis detallado del cuestionario temático sobre funciones hash de la plataforma ExamCompass para la certificación CompTIA Security+ (SY0-701), alineado con las respuestas oficiales del simulador.

---

## Pregunta 1: Concepto fundamental de una función Hash / Fundamental Hash Concept

### English Version
A hash function is a mathematical algorithm that maps data of arbitrary size to a fixed-size hash value, typically represented as a short string of characters. The output of the hash function, also known as a digest or checksum, provides a unique representation of the original input data. The functionality of hash functions relies on the fact that if any changes occur to the data after the original hash has been generated, the new hash value calculated after modifying the content will be different from the original result, as hash functions are designed to be sensitive to changes in the input data.
* [✅] **True**
* [ ] False

### Versión en Español
Una función hash es un algoritmo matemático que asigna datos de tamaño arbitrario a un valor hash de tamaño fijo, generalmente representado como una cadena corta de caracteres. El resultado de la función hash, también conocido como resumen o suma de verificación, proporciona una representación única de los datos de entrada originales. La funcionalidad de las funciones hash se basa en el hecho de que si se produce algún cambio en los datos después de que se haya generado el hash original, el nuevo valor hash calculado tras la modificación del contenido será diferente del resultado original, ya que las funciones hash están diseñadas para ser sensibles a los cambios en los datos de entrada.
* [✅] **Verdadero**
* [ ] Falso

### 1. Explicación General
Una función hash es una operación matemática de una sola vía (*one-way function*): es increíblemente rápido pasar de un archivo (sin importar si pesa 1 KB o 10 TB) a su resumen hash, pero es matemáticamente imposible reconstruir el archivo original a partir de ese código. Además, son deterministas: el mismo archivo exacto siempre dará exactamente el mismo resultado hash.

### 2. ¿Por qué es la correcta y no el resto?
* **Opción Correcta:** `[True / Verdadero]` debido a que el enunciado describe a la perfección el comportamiento del "efecto avalancha" (*avalanche effect*). Si alteras un solo bit, una coma, un espacio o cambias una mayúscula por minúscula en un documento masivo, el hash resultante cambiará por completo de forma radical y caótica. Esto es lo que permite verificar de inmediato que un archivo no ha sido manipulado.

### 3. Clave para el Examen SY0-701
Conceptos clave que CompTIA usará para describir un hash: "Fixed-size output" (salida de tamaño fijo) y su objetivo principal en la triada CIA, que es garantizar la **Integridad (Integrity)**.

---

## Pregunta 2: Aplicaciones prácticas de las funciones Hash / Practical Applications of Hashes

### English Version
Hash functions are used in various applications, including:
* [ ] Cryptography / Data integrity verification
* [ ] Password verification and storage / Digital signatures
* [ ] Blockchain technology
* [✅] **All of the above**

### Versión en Español
Las funciones hash se utilizan en diversas aplicaciones, entre las que se incluyen:
* [ ] Criptografía / Verificación de la integridad de los datos
* [ ] Verificación y almacenamiento de contraseñas / Firmas digitales
* [ ] Tecnología blockchain
* [✅] **Todo lo anterior**

### 1. Explicación General
Los hashes son la herramienta multiusos de la seguridad informática moderna. No están limitados a un solo software; son el mecanismo subyacente que valida que las descargas de internet sean seguras, que las bases de datos no guarden contraseñas expuestas y que los bloques de transacciones sean inmutables.

### 2. ¿Por qué es la correcta y no el resto?
* **Opción Correcta:** `[All of the above / Todo lo anterior]` porque cada una de las opciones describe un caso de uso crítico en producción:
    * *Almacenamiento de contraseñas:* Los sistemas operativos modernos nunca guardan tu contraseña real; guardan su hash de forma segura.
    * *Firmas digitales:* El emisor genera el hash de un documento y luego cifra ese hash con su clave privada, asegurando no repudio e integridad.
    * *Blockchain:* Cada bloque lleva inyectado el hash del bloque anterior; si alguien intenta alterar el pasado, la cadena completa se rompe al instante.

### 3. Clave para el Examen SY0-701
Si en el examen te presentan un escenario donde necesitas asegurar que un administrador de base de datos malicioso no pueda leer las contraseñas de los usuarios, la solución técnica requerida siempre es **"Hashing and salting passwords"**.

---

## Pregunta 3: Algoritmos hash obsoletos (MD5) / Legacy Hash Algorithms

### English Version
Which of the answers listed below refers to a cryptographic hash function that has been widely used in the past, but is now considered obsolete for security-sensitive applications due to known vulnerabilities?
* [✅] **MD5**
* [ ] SHA
* [ ] CRC
* [ ] HMAC

### Versión en Español
¿Cuál de las respuestas que aparecen a continuación se refiere a una función hash criptográfica que se ha utilizado ampliamente en el pasado, pero que ahora se considera obsoleta para aplicaciones sensibles a la seguridad debido a vulnerabilidades conocidas?
* [✅] **MD5**
* [ ] SHA
* [ ] CRC
* [ ] HMAC

### 1. Explicación General
En criptografía, cuando dos entradas de datos completamente distintas generan por accidente o manipulación el mismo valor hash de salida, ocurre un desastre llamado colisión (*collision*). Si un algoritmo es vulnerable a colisiones provocadas de forma intencional en segundos, pierde toda su utilidad de seguridad, ya que un atacante podría hacer pasar un archivo con malware por uno legítimo compartiendo el mismo hash.

### 2. ¿Por qué es la correcta y no el resto?
* **Opción Correcta:** `[MD5]` (Message Digest 5) genera un hash de 128 bits. Actualmente está completamente roto y obsoleto para la seguridad porque las capacidades de cómputo actuales permiten forzar colisiones criptográficas con extrema facilidad.
* **Análisis de los distractores:**
    * *SHA:* Sus familias modernas (SHA-2 y SHA-3) siguen siendo el estándar seguro de la industria.
    * *CRC:* Es un código de redundancia cíclica usado en redes para detectar errores físicos accidentales, no tiene propiedades criptográficas contra ataques.
    * *HMAC:* Es una estructura de autenticación de mensajes que usa una clave, no un algoritmo hash base por sí solo.

### 3. Clave para el Examen SY0-701
Regla estricta de CompTIA: `MD5` y `SHA-1` se consideran algoritmos débiles u obsoletos (*weak/legacy*). Si un escenario exige proteger datos críticos o firmas digitales, nunca debes elegirlos.

---

## Pregunta 4: La familia de algoritmos seguros (SHA) / Secure Hash Algorithm Family

### English Version
Which of the following following answers refers to a family of cryptographic hash functions designed for various security-related applications, including digital signatures, password storage, secure communications, and data integrity verification?
* [ ] RSA
* [ ] AES
* [ ] PKCS
* [✅] **SHA**

### Versión en Español
¿Cuál de las siguientes respuestas se refiere a una familia de funciones hash criptográficas diseñadas para diversas aplicaciones relacionadas con la seguridad, incluidas las firmas digitales, el almacenamiento de contraseñas, las comunicaciones seguras y la verificación de la integridad de los datos?
* [ ] RSA
* [ ] AES
* [ ] PKCS
* [✅] **SHA**

### 1. Explicación General
Diseñada originalmente por la Agencia de Seguridad Nacional (NSA) de EE. UU. y publicada por el NIST, esta familia de funciones fue estructurada específicamente para superar las debilidades que fueron apareciendo en los algoritmos de la vieja escuela como MD5. Es la suite reglamentaria obligatoria para la gran mayoría de los estándares gubernamentales y bancarios del mundo.

### 2. ¿Por qué es la correcta y no el resto?
* **Opción Correcta:** `[SHA]` (Secure Hash Algorithm) es una familia completa de funciones. Aunque SHA-1 ya no es seguro, las versiones dentro de SHA-2 (como SHA-256 o SHA-512) y SHA-3 son el motor de integridad actual de internet.
* **Análisis de los distractores:**
    * *RSA:* Es un algoritmo de cifrado asimétrico (par de llaves pública/privada), no una función hash.
    * *AES:* Es el estándar de cifrado simétrico por bloques para confidencialidad de datos.
    * *PKCS:* Significa *Public-Key Cryptography Standards*, son especificaciones y protocolos de la industria, no un algoritmo de compresión hash.

### 3. Clave para el Examen SY0-701
Cuando una pregunta se refiera de forma genérica a la "family of cryptographic hash functions" estándar activa para proteger certificados TLS o firmas de código, tu mente debe ir directo a `SHA`.

---

## Pregunta 5: El nivel más alto de seguridad (SHA-3) / Next-Gen Hashing Standards

### English Version
Which of the hash functions listed below offers the highest level of security?
* [ ] MD5
* [✅] **SHA-3**
* [ ] RIPEMD-160
* [ ] HMAC

### Versión en Español
¿Cuál de las funciones hash que se enumeran a continuación ofrece el mayor nivel de seguridad?
* [ ] MD5
* [✅] **SHA-3**
* [ ] RIPEMD-160
* [ ] HMAC

### 1. Explicación General
A pesar de que la familia SHA-2 sigue siendo completamente segura y masivamente utilizada hoy en día, los criptógrafos del NIST decidieron lanzar un concurso internacional para diseñar una arquitectura hash totalmente nueva. El objetivo era tener un plan de respaldo ultraavanzado por si en el futuro alguien descubría una vulnerabilidad matemática teórica en el diseño de SHA-2.

### 2. ¿Por qué es la correcta y no el resto?
* **Opción Correcta:** `[SHA-3]` está basado en un diseño matemático innovador llamado "construcción de esponja" (*sponge construction*). Representa la generación criptográfica más moderna, sofisticada y resistente contra criptoanálisis avanzado disponible en esa lista.
* **Análisis de los distractores:**
    * *MD5:* Está completamente roto.
    * *RIPEMD-160:* Es un algoritmo antiguo con un tamaño de salida menor (160 bits), lo que ofrece matemáticamente menor resistencia que los bloques robustos de SHA-3.
    * *HMAC:* Es un método de construcción de autenticación combinada, no el algoritmo hash base puro por sí solo.

### 3. Clave para el Examen SY0-701
Si CompTIA te pide identificar la función hash pura más moderna y con el mayor nivel de seguridad técnica incorporada dentro de las opciones, la respuesta es `SHA-3`.

---

## Pregunta 6: Autenticidad e Integridad con llaves (HMAC) / Keyed-Hash Message Authentication

### English Version
Which of the following options combines a cryptographic hash function with a secret key to provide a mean of verifying both the authenticity and the integrity of a message or data?
* [ ] MD5
* [ ] DSA
* [✅] **HMAC**
* [ ] DES

### Versión en Español
¿Cuál de las siguientes opciones combina una función hash criptográfica con una clave secreta para proporcionar un medio de verificación tanto de la autenticidad como de la integridad de un mensaje o dato?
* [ ] MD5
* [ ] DSA
* [✅] **HMAC**
* [ ] DES

### 1. Explicación General
Un hash estándar (como SHA-256) te dice si un archivo fue modificado en el camino (integridad), pero no te dice quién lo envió. Si un atacante intercepta un mensaje, modifica el texto y calcula un hash totalmente nuevo sobre ese texto modificado, el receptor creerá que el mensaje es válido porque el hash cuadra. Para evitar esto, necesitamos que el proceso incluya una clave secreta compartida que solo el emisor legítimo y el receptor conozcan.

### 2. ¿Por qué es la correcta y no el resto?
* **Opción Correcta:** `[HMAC]` (Hash-based Message Authentication Code) hace exactamente lo descrito: inyecta una clave simétrica secreta dentro del cálculo matemático del hash. Esto garantiza dos cosas simultáneamente: **Integridad** (los datos no cambiaron) y **Autenticidad** (quien lo mandó posee la clave secreta).
* **Análisis de los distractores:**
    * *MD5:* Es solo un hash base desprotegido sin capacidad de inyección de claves simétricas.
    * *DSA:* Se utiliza para firmas digitales asimétricas complejas, no es un código hash simétrico de autenticación rápida.
    * *DES:* Es un algoritmo obsoleto de cifrado de datos (confidencialidad), no una función hash.

### 3. Clave para el Examen SY0-701
Definición imperativa para el examen: "Hash function + secret key" = `HMAC`. Se usa masivamente en protocolos como IPsec y TLS para asegurar que los paquetes de red no sean alterados ni inyectados por terceros en tránsito.

---

## Pregunta 7: Verificación de errores no criptográfica (CRC) / Non-Cryptographic Checksums

### English Version
Which of the answers listed below refers to a non-cryptographic hash function often used for error checking?
* [ ] MD5
* [✅] **CRC**
* [ ] SHA
* [ ] RIPEMD

### Versión en Español
¿Cuál de las respuestas que aparecen a continuación se refiere a una función hash no criptográfica que se utiliza a menudo para la comprobación de errores?
* [ ] MD5
* [✅] **CRC**
* [ ] SHA
* [ ] RIPEMD

### 1. Explicación General
No todas las funciones de verificación necesitan ser complejas, ultra seguras y resistentes a ataques de hackers. Cuando un disco duro copia un archivo de un sector a otro, o cuando una tarjeta de red envía paquetes de datos por un cable de cobre, pueden ocurrir errores físicos debido a interferencias eléctricas. Para detectar si se cayó un bit en el camino de forma accidental, se necesita un cálculo matemático ultrarrápido y ligero que se ejecute a nivel de hardware.

### 2. ¿Por qué es la correcta y no el resto?
* **Opción Correcta:** `[CRC]` (Cyclic Redundancy Check / Verificación de Redundancia Cíclica) es una función matemática diseñada exclusivamente para detectar errores accidentales en la transmisión de datos o almacenamiento. No es criptográfica; un atacante puede alterar los datos y falsificar el CRC fácilmente, pero para lo que fue diseñada (errores de hardware o ruido en la línea), es sumamente eficiente y rápida.
* **Análisis de los distractores:** `MD5`, `SHA` y `RIPEMD` son funciones explícitamente criptográficas, diseñadas con barreras complejas para ser inmunes a la manipulación maliciosa de datos.

### 3. Clave para el Examen SY0-701
Si el enunciado del examen menciona verificación de errores rutinarios de red o de almacenamiento físico y recalca que la función es **"non-cryptographic"** (no criptográfica), la respuesta es siempre `CRC`.

---

[[ExamCompass - Cuestionarios por Temas|⬅️ Volver a Cuestionarios por Temas]]