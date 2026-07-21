---
tags:
  - "formato/apunte"
  - "hacking/fundamental"
  - "examen/test-especifico"
  - "gestion/estado/progreso"
---
Este apunte contiene la tercera sección del análisis de los cuestionarios temáticos de ExamCompass para la certificación CompTIA Security+ (SY0-701). Se enfoca exhaustivamente en la seguridad de contraseñas, criptografía aplicada a credenciales (Salting/Key Stretching) y vectores de ataque de autenticación, contrastando mis respuestas con las oficiales del simulador.

---

## Pregunta 1: Factores de Fortaleza de una Contraseña

### English Version
The two factors considered important for creating secure passwords are: (Select 2 answers)
- [x] **Password length**
- [ ] Minimum password age
- [ ] Password history
- [x] **Password complexity**
- [ ] Maximum password age

### Versión en Español
Los dos factores que se consideran importantes para crear contraseñas seguras son: (Seleccione 2 respuestas)
- [x] **Longitud de la contraseña**
- [ ] Edad mínima de la contraseña
- [ ] Historial de contraseñas
- [x] **Complejidad de la contraseña**
- [ ] Edad máxima de la contraseña

### 1. Explicación General
La resistencia de una credencial secreta contra intentos de descifrado automatizado depende directamente de su aleatoriedad y del espacio de búsqueda que un adversario debe recorrer. La longitud y la complejidad definen el tamaño de dicho espacio matemático.

### 2. ¿Por qué es la correcta y no el resto?
- **Password Length y Complexity:** Son atributos técnicos intrínsecos de la contraseña. La **longitud** incrementa el exponente de las combinaciones posibles de forma exponencial, mientras que la **complejidad** expande la base de caracteres disponibles.
- **Políticas de Antigüedad e Historial:** Son controles administrativos y directrices del sistema operativo, pero no alteran la robustez criptográfica de la cadena de caracteres en sí misma.

### 3. Clave para el Examen SY0-701
`Longitud + Complejidad = Contraseña Robusta`. El estándar actual de la industria (e.g., directrices NIST) y CompTIA priorizan la **longitud** (passphrases largas) por encima de la complejidad pura para neutralizar ataques modernos de fuerza bruta.

---

## Pregunta 2: Estándar de Complejidad de Contraseñas

### English Version
A secure password that meets complexity requirements should contain: (Choose the best answer)
- [ ] Uppercase letters (A-Z)
- [ ] Digits (0-9)
- [ ] Non-alphanumeric characters if permitted (e.g., !,@,#,$)
- [ ] Lowercase letters (a-z)
- [x] **A combination of characters from at least 3 character groups**

### Versión en Español
Una contraseña segura que cumpla con el requisito de complejidad debe contener: (Seleccione la mejor respuesta)
- [ ] Letras mayúsculas (A-Z)
- [ ] Dígitos (0-9)
- [ ] Caracteres no alfanuméricos si están permitidos (por ejemplo, !,@,#,$)
- [ ] Letras minúsculas (a-z)
- [x] **Una combinación de caracteres de al menos 3 grupos de caracteres**

### 1. Explicación General
El requisito técnico de complejidad en los directorios de identidad corporativos (como Microsoft Active Directory) busca romper la predictibilidad de las contraseñas creadas por usuarios humanos forzando la dispersión de caracteres.

### 2. ¿Por qué es la correcta y no el resto?
La opción de **una combinación de al menos 3 grupos** es la mejor respuesta porque engloba la política estándar del mercado. Las demás opciones individuales representan únicamente subconjuntos aislados que no satisfacen la regla global de complejidad por sí solas.

### 3. Clave para el Examen SY0-701
Para CompTIA, los 4 grupos de caracteres reconocidos son: *Mayúsculas, Minúsculas, Números y Símbolos especiales*. Una política clásica de complejidad exige obligatoriamente caracteres de al menos 3 de estas categorías.

---

## Pregunta 3: Evaluación Práctica de Complejidad

### English Version
Which of the following passwords is the most complex?
- [ ] T$7C52WL4SU
- [ ] GdL3tU8wxYz
- [ ] @TxBL$nW@Xt
- [x] **G$L3tU8wY@z**

### Versión en Español
¿Cuál de las siguientes contraseñas es la más compleja?
- [ ] T$7C52WL4SU
- [ ] GdL3tU8wxYz
- [ ] @TxBL$nW@Xt
- [x] **G$L3tU8wY@z**

### 1. Explicación General
La evaluación de complejidad requiere un análisis visual minucioso para identificar cuántas categorías o familias de caracteres diferentes coexisten en la misma cadena.

### 2. ¿Por qué es la correcta y no el resto?
- **`G$L3tU8wY@z`:** Es la única contraseña de la lista que incorpora de manera efectiva elementos de **los 4 grupos disponibles**: Mayúsculas (`G`, `Y`), Minúsculas (`t`, `u`, `w`, `z`), Números (`3`, `8`) y Símbolos (`$`, `@`).
- Las opciones restantes carecen de al menos uno de los grupos fundamentales (por ejemplo, carecen de minúsculas o de números).

### 3. Clave para el Examen SY0-701
En ejercicios visuales de contraseñas, realiza un check rápido de los 4 grupos. La ganadora siempre será la que presente mayor diversidad de conjuntos criptográficos representados.

---

## Pregunta 4: Mitigación de Reutilización de Credenciales

### English Version
Which password policy would be most effective at reducing the risk of a security breach across multiple accounts?
- [ ] Password Expiration Policy
- [ ] Minimum Password Age Policy
- [x] **Password Reuse Policy**
- [ ] Maximum Password Age Policy

### Versión en Español
¿Qué política de contraseñas sería la más eficaz para disminuir el riesgo de una brecha de seguridad en múltiples cuentas?
- [ ] Política de caducidad de contraseñas
- [ ] Política de antigüedad mínima de contraseñas
- [x] **Política de reutilización de contraseñas**
- [ ] Política de antigüedad máxima de contraseñas

### 1. Explicación General
El hábito de los usuarios de reciclar la misma contraseña en diferentes plataformas web (personales y corporativas) genera un riesgo sistémico severo conocido como *Credential Stuffing*. Si un sitio web de terceros sufre una fuga de información, los atacantes usarán esos mismos datos para asaltar cuentas corporativas automáticamente.

### 2. ¿Por qué es la correcta y no el resto?
- **Password Reuse Policy:** Impide directamente que un empleado configure una contraseña idéntica a las utilizadas previamente o en sistemas paralelos mediante el almacenamiento en memoria de un historial de contraseñas previas.
- Las políticas de expiración y antigüedad regulan la vida útil del secreto en un único sistema, pero no controlan la duplicación trans-plataforma.

### 3. Clave para el Examen SY0-701
Asociación de defensa en el examen: `Credential Stuffing / Password Recycling ➡️ Mitigación: Password Reuse / History Policy`.

---

## Pregunta 5: Política de Expiración

### English Version
Which password policy requires a mandatory password change after a specified period of time?
- [x] **Password Expiration Policy**
- [ ] Password History Policy
- [ ] Minimum Password Age Policy
- [ ] Password Reuse Policy

### Versión en Español
¿Qué política de contraseñas exige un cambio de contraseña obligatorio después de un tiempo determinado?
- [x] **Política de caducidad de contraseñas**
- [ ] Política de historial de contraseñas
- [ ] Política de antigüedad mínima de contraseñas
- [ ] Política de reutilización de contraseñas

### 1. Explicación General
Para limitar el tiempo de utilidad de una credencial potencialmente comprometida sin el conocimiento de la organización, los administradores configuran límites temporales de validez activa.

### 2. ¿Por qué es la correcta y no el resto?
- **Password Expiration Policy (Caducidad):** Invalida el estado de la contraseña una vez transcurrido el temporizador del sistema, forzando una redirección hacia el módulo de actualización de credenciales.

### 3. Clave para el Examen SY0-701
`Expiration = Ciclo de vida máximo`. Aunque las tendencias modernas de ciberseguridad mitigan su uso continuo debido a que causan frustración en el usuario (provocando que elijan contraseñas predecibles), sigue siendo un concepto central evaluado bajo el control administrativo clásico.

---

## Preguntas 6 y 7: Antigüedad de Contraseñas (Minimum vs. Maximum Age)

### English Version
- **Minimum Password Age Policy:** Determines the period during which a password must be used before a user can change it. (Prevents immediate recycling).
- **Maximum Password Age Policy:** Determines the period of time a password can be used before the system requires the user to change it.

### Versión en Español
- **Política de Antigüedad Mínima:** Define el tiempo que el usuario debe conservar su contraseña actual antes de que el sistema le permita modificarla. **(Evita que el usuario salte el historial de contraseñas cambiando su clave muchas veces seguidas en un solo día)**.
- **Política de Antigüedad Máxima:** Define el tiempo límite de uso antes de que expire de forma obligatoria.

### 1. Análisis de los Enunciados del Simulador
- El enunciado de la Pregunta 6 es **Falso** porque asigna la definición de *Maximum* al concepto de *Minimum*.
- El enunciado de la Pregunta 7 es **Falso** porque asigna la definición de *Minimum* al concepto de *Maximum*.

### 2. Clave para el Examen SY0-701
Memoriza este contraste técnico:
- `Minimum Age` ➡️ Restringe e impide cambios inmediatos (Protege al Historial de Contraseñas).
- `Maximum Age` ➡️ Obliga y demanda un cambio periódico.

---

## Pregunta 8: Herramientas de Gestión de Identidad (Password Manager)

### English Version
Which of the following refers to a software tool specifically designed to store and manage login credentials?
- [ ] BitLocker
- [x] **Password Manager**
- [ ] Key Escrow
- [ ] Password Vault

### Versión en Español
¿Cuál de las respuestas que aparecen a continuación se refiere a una herramienta de software diseñada específicamente para almacenar y gestionar credenciales de inicio de sesión?
- [ ] BitLocker
- [x] **Administrador de contraseñas**
- [ ] Depósito de llaves
- [ ] Bóveda de contraseñas

### 1. Explicación General
El uso de bóvedas cifradas de software permite descentralizar la memorización humana de contraseñas complejas, facilitando el uso de una clave única y masiva para cada aplicación o servicio web.

### 2. ¿Por qué es la correcta y no el resto?
- **Password Manager:** Término general de la industria para las aplicaciones (como 1Password o Bitwarden) orientadas al usuario final.
- **BitLocker:** Herramientas de cifrado de volumen completo (*Full Disk Encryption*).
- **Key Escrow:** Custodia de llaves de descifrado por parte de terceros de confianza.
- **Password Vault:** Suele ser la base de datos interna o el componente de almacenamiento centralizado dentro de un entorno PAM de nivel empresarial.

---

## Pregunta 9: Autenticación Sin Contraseña (Passwordless)

### English Version
Which technology cannot be used as a passwordless authentication method?
- [ ] Biometrics
- [ ] Hardware Tokens
- [ ] QR Codes
- [ ] OTP
- [ ] Passwords
- [x] **All of the above can be used for passwordless authentication**

### Versión en Español
¿Cuál de las siguientes tecnologías no se puede utilizar como método de autenticación sin contraseña?
- [ ] Biometría
- [ ] Tokens de hardware
- [ ] Códigos QR
- [ ] OTP
- [ ] Contraseñas
- [x] **Todo lo anterior puede utilizarse como medio para la autenticación sin contraseña**

### 1. Explicación General
El ecosistema *Passwordless* busca erradicar el factor de conocimiento textual tradicional (contraseñas) debido a su alta vulnerabilidad frente a la ingeniería social y la reutilización, sustituyéndolo por factores de posesión o inherencia.

### 2. ¿Por qué es la correcta y no el resto?
**Todo lo anterior puede utilizarse** porque la arquitectura moderna (como los estándares FIDO2 / WebAuthn) integra biometría (huella, rostro), tokens criptográficos físicos (YubiKeys), códigos QR dinámicos y contraseñas de un solo uso (OTP) para validar la legitimidad del acceso sin que el usuario digite una clave maestra tradicional en un formulario.

---

## Pregunta 10: Ocultación de Datos (Data Masking)

### English Version
Replacing password characters in a password field with a series of asterisks is an example of:
- [x] **Data Masking**
- [ ] Tokenization
- [ ] Anonymization
- [ ] Pseudonymization

### Versión en Español
Reemplazar los caracteres de contraseña en un campo de contraseña con una serie de asteriscos es un ejemplo de:
- [x] **Enmascaramiento de datos**
- [ ] Tokenización
- [ ] Anonimización
- [ ] Pseudoanonimización

### 1. Explicación General
El enmascaramiento en interfaces de usuario busca neutralizar una técnica física de espionaje conocida como *Shoulder Surfing* (observar por encima del hombro del operador).

### 2. ¿Por qué es la correcta y no el resto?
- **Data Masking:** Modifica u oculta la representación visual del dato en tiempo real para proteger su confidencialidad visual inmediata.
- **Tokenization:** Sustituye el dato por un token de referencia aleatorio en bases de datos.
- **Anonymization:** Remueve la vinculación de identidad de forma irreversible.

---

## Preguntas 11, 12 y 13: Protección Criptográfica de Hashes (Salting)

### English Version
Which cryptographic technique adds random data to a password before hashing to prevent rainbow tables from being effective?
- [ ] Data Masking
- [ ] 2FA
- [ ] Key Stretching
- [x] **Salting**

### Versión en Español
¿Qué técnica criptográfica añade datos pseudoaleatorios a una contraseña antes del proceso de hash para anular la efectividad de las tablas arcoíris?
- [x] **Salazón (Salting)**

### 1. Análisis Técnico Detallado
Una sal (**Salt**) es una cadena aleatoria única generada por el sistema que se concatena a la contraseña en texto plano del usuario antes de computar el algoritmo Hash. Esto garantiza que dos usuarios que elijan exactamente la misma clave (ej. `Password123!`) tengan **hashes completamente diferentes almacenados en la base de datos**.

### 2. ¿Por qué destruye las Rainbow Tables?
Las *Rainbow Tables* son bases de datos precalculadas que contienen millones de correspondencias entre textos planos y sus respectivos hashes con el fin de agilizar ataques offline. Al inyectar un valor aleatorio (*Salt*) por cada registro, el atacante se ve forzado a recalcular la tabla completa para cada usuario individual, inutilizando la ventaja del pre-cómputo.

### 3. Clave para el Examen SY0-701
Asociación directa obligatoria: `Rainbow Tables ➡️ Mitigación: Salting`.

---

## Pregunta 14: Mitigación de Fuerza Bruta (Key Stretching)

### English Version
Key stretching is a cryptographic technique used to make a weak password more secure against brute-force attacks by increasing the computational time required to hash it.
- [x] **True**
- [ ] False

### Versión en Español
El estiramiento de claves (Key Stretching) es una técnica criptográfica para robustecer contraseñas frente a ataques de fuerza bruta al incrementar intencionalmente el costo computacional del cálculo hash.
- [x] **Verdadero**
- [ ] Falso

### 1. Explicación General
El hardware moderno (GPUs de alta potencia) puede procesar miles de millones de hashes de tipo MD5 o SHA-256 por segundo. **Key Stretching** contrarresta esto forzando al procesador a ejecutar la función hash miles o millones de veces en bucle (*iteraciones*), añadiendo un retraso artificial de milisegundos que no afecta al usuario legítimo, pero ralentiza destructivamente al atacante masivo.

### 2. Clave para el Examen SY0-701
Debo reconocer los algoritmos de Key Stretching más consultados en CompTIA: **PBKDF2**, **bcrypt**, **scrypt**, y **Argon2**.

---

## Pregunta 15: Configuración Inicial de Sistemas (Default Credentials)

### English Version
Changing default credentials upon the deployment of a new device or software is a critical initial hardening step.
- [x] **True**
- [ ] False

### Versión en Español
Cambiar las credenciales predeterminadas al desplegar un nuevo dispositivo o software es un paso crítico e inicial de endurecimiento (Hardening).
- [x] **Verdadero**
- [ ] Falso

### 1. Explicación General
Los fabricantes configuran credenciales genéricas (ej. `admin` / `admin`) de fábrica en routers, firewalls e interfaces IoT. Estas credenciales están documentadas en manuales públicos de Internet.

### 2. Clave para el Examen SY0-701
El primer paso de **Hardening** de cualquier infraestructura de red es remover, deshabilitar o sustituir de inmediato todas las combinaciones predeterminadas de fábrica.

---

## Pregunta 16: Ataques de Movimiento Lateral (Pass the Hash)

### English Version
An attack that allows an attacker to authenticate using a hash without obtaining the plaintext password is known as:
- [x] **Pass the Hash (PtH)**
- [ ] Replay Attack
- [ ] Brute Force Attack
- [ ] Password Spraying

### Versión en Español
Una técnica que permite a un atacante autenticarse en un servidor remoto utilizando directamente el valor hash capturado, sin requerir descifrarlo a texto plano, se conoce como:
- [x] **Pass the Hash**
- [ ] Ataque de repetición
- [ ] Ataque de fuerza bruta
- [ ] Ataque por pulverización

### 1. Explicación General
En protocolos de autenticación de red heredados (como NTLM), el sistema valida la identidad contrastando directamente hashes. Si un atacante compromete la memoria LSASS de un sistema Windows comprometido y extrae el hash de la clave de un Administrador, puede inyectar ese hash directamente en las solicitudes de red para acceder a otros servidores locales.

### 2. Clave para el Examen SY0-701
`Pass-the-Hash = Autenticación directa mediante el Hash capturado` (Movimiento Lateral dentro de la red interna).

---

## Preguntas 17 y 18: Evasión de Bloqueos (Password Spraying)

### English Version
Which password attack tests a single, common password against multiple user accounts to bypass account lockout policies?
- [ ] Birthday Attack
- [ ] Replay Attack
- [x] **Password Spraying**
- [ ] Dictionary Attack

### Versión en Español
¿Qué ataque de contraseña prueba una única clave común contra múltiples cuentas de usuario diferentes para evadir las políticas de bloqueo de cuenta?
- [x] **Ataque por pulverización (Password Spraying)**

### 1. Explicación General
Un ataque de diccionario convencional prueba miles de claves contra *un solo usuario*, lo cual detona inmediatamente la política de **Account Lockout** tras 3 o 5 intentos fallidos, bloqueando la cuenta y alertando al SOC. El **Password Spraying** invierte el vector: toma una contraseña común (ej: `Welcome2026!`) y la prueba una sola vez contra cientos de nombres de usuario diferentes.

### 2. ¿Por qué evade las políticas de bloqueo?
Al realizar un único intento por cuenta en cada ciclo de tiempo, el sistema operativo no detecta una anomalía de fuerza bruta por cuenta individual, manteniendo los umbrales de seguridad limpios y permitiendo al atacante pasar desapercibido.

### 3. Clave para el Examen SY0-701
Ecuación conceptual de CompTIA: `Evadir Bloqueos de Cuenta (Account Lockout Bypass) + Probar una clave contra muchos usuarios = Password Spraying`.

---

## Pregunta 19: Fuerza Bruta Tradicional

### English Version
An attack that systematically tries all possible character combinations until the correct one is found is known as a Brute Force Attack.
- [x] **Brute Force Attack**

### Versión en Español
El ataque que prueba sistemáticamente cada combinación matemática posible de caracteres hasta dar con la correcta es un Ataque de Fuerza Bruta.

### 1. Clave para el Examen SY0-701
La fuerza bruta pura no discrimina ni utiliza diccionarios inteligentes; avanza matemáticamente combinando caracteres (`aaa`, `aab`, `aac`...) lo cual la vuelve altamente ruidosa y costosa en tiempo.

---

## Pregunta 20: Análisis de Entorno (Offline Password Cracking)

### English Version
An offline password cracking attack does not trigger account lockout policies because it occurs outside the target authentication system.
- [x] **True**
- [ ] False

### Versión en Español
Un ataque de descifrado de contraseñas fuera de línea (Offline) no detona las políticas de bloqueo de cuenta porque ocurre fuera del sistema de autenticación objetivo.
- [x] **Verdadero**
- [ ] Falso

### 1. Explicación General
- **Ataques Online:** El atacante interactúa directamente con el servidor de la empresa (formularios de login). Cada intento es procesado por el sistema, permitiendo registrar logs y bloquear la cuenta.
- **Ataques Offline:** El atacante ha extraído previamente la base de datos de hashes (ej. un archivo `NTDS.dit` o volcado SQL) y la traslada a sus propios servidores de hackeo. El descifrado se ejecuta localmente contra su propio hardware. El sistema de la víctima no tiene idea de que el ataque está ocurriendo, por lo que **los bloqueos de cuenta son completamente ineficaces**.

---

[[ExamCompass - Cuestionarios por Temas|⬅️ Volver a Cuestionarios por Temas]]