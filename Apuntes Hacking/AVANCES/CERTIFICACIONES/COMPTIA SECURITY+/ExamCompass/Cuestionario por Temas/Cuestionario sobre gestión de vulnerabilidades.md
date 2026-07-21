---
tags:
  - "formato/apunte"
  - "hacking/fundamental"
  - "examen/test-especifico"
  - "gestion/estado/terminado"
---
Este apunte contiene el análisis detallado y completo del cuestionario temático de 20 preguntas sobre desarrollo seguro de software, técnicas de análisis de código (SAST/DAST), mitigación de fallas de memoria (ASLR), criptografía y seguridad web de la plataforma ExamCompass para la certificación CompTIA Security+ (SY0-701), alineado con mis respuestas y las oficiales del simulador.

---

## Pregunta 1: Pilares de la Programación Segura

### English Version
Which of the programming aspects listed below are fundamental in the secure application development process? (Select 2 answers)
- [ ] Patch management
- [x] **Input validation**
- [ ] Password protection
- [x] **Error and exception handling**
- [ ] Application whitelisting

### Versión en Español
¿Cuáles de los aspectos de programación que se enumeran a continuación son fundamentales en el proceso de desarrollo de aplicaciones seguras? (Seleccione 2 respuestas)
- [ ] Gestión de parches
- [x] **Validación de entrada**
- [ ] Protección con contraseña
- [x] **Manejo de errores y excepciones**
- [ ] Lista blanca de aplicaciones

### 1. Explicación General
En el marco del desarrollo seguro (*Secure Coding*), la premisa básica que debo seguir como programador es la desconfianza absoluta: debo asumir que los datos provenientes de los usuarios pueden ser maliciosos y que el sistema experimentará fallos inesperados. Los controles fundamentales integrados directamente en el código fuente son el filtrado de entradas y la resiliencia ante excepciones.

### 2. ¿Por qué es la correcta y no el resto?
- **Validación de entrada** y **Manejo de errores/excepciones** impactan directamente la lógica interna del código fuente. El primero sanitiza los datos entrantes para evitar que se interpreten como comandos, y el segundo controla las respuestas del sistema ante fallos para evitar caídas catastróficas.
- **Gestión de parches** y **Lista blanca de aplicaciones:** Son controles operativos y administrativos de la infraestructura del sistema operativo, no aspectos de la lógica de desarrollo o codificación pura del software.

### 3. Clave para el Examen SY0-701
Recuerdo el principio de **Manejo Seguro de Errores**: un error en producción nunca debe desplegar información interna del sistema (como *stack traces*, rutas de directorios, nombres de bases de datos o versiones de software) al usuario final, ya que esto facilita la fase de reconocimiento a un atacante.

---

## Pregunta 2: Defectos por Validación Incorrecta

### English Version
A situation where a web form field accepts data other than expected (e.g., server commands) is an example of:
- [ ] Zero-day vulnerability
- [x] **Improper input validation**
- [ ] Default configuration
- [ ] Improper error handling

### Versión en Español
Una situación en la que un campo de formulario web acepta datos distintos a los esperados (por ejemplo, comandos del servidor) es un ejemplo de:
- [ ] Vulnerabilidad de día cero
- [x] **Validación de entrada incorrecta**
- [ ] Configuración predeterminada
- [ ] Manejo inadecuado de errores

### 1. Explicación General
Cuando una aplicación web procesa ciegamente la información introducida por un usuario en un formulario (como un cuadro de texto o barra de búsqueda) sin someterla a reglas estrictas de formato, longitud o caracteres permitidos, la frontera entre datos e instrucciones se rompe.

### 2. ¿Por qué es la correcta y no el resto?
- **Validación de entrada incorrecta** es el término técnico exacto. Si el sistema espera una cadena de caracteres alfabéticos para un "Nombre" y en su lugar procesa y ejecuta comandos de sistema (como `; rm -rf`), el control de sanitización falló.
- **Zero-day (Día cero):** Se refiere a una falla de software desconocida para el fabricante y para la cual no existe un parche público disponible; no describe la naturaleza del defecto lógico del código.

### 3. Clave para el Examen SY0-701
Para el examen, debo tener claro que **la validación de entrada debe realizarse idealmente en el lado del servidor (Server-side validation)**. La validación en el lado del cliente (vía JavaScript en el navegador) es útil para la experiencia de usuario, pero un atacante la evade fácilmente interceptando y modificando la petición HTTP mediante herramientas de proxy como `OWASP ZAP` o `Burp Suite`.

---

## Pregunta 3: Contramedidas ante Inyecciones de Código

### English Version
Which of the following answers refers to a countermeasure against code injection?
- [ ] Fuzzing
- [x] **Input validation**
- [ ] Code signing
- [ ] Normalization

### Versión en Español
Indicación: ¿Cuál de las siguientes respuestas se refiere a una contramedida contra la inyección de código?
- [ ] Fuzzing
- [x] **Validación de entrada**
- [ ] Firma de código
- [ ] Normalización

### 1. Explicación General
Las vulnerabilidades de inyección (SQLi, *Command Injection*, *Cross-Site Scripting*) ocurren porque los datos proveídos por el usuario malicioso alteran la estructura sintáctica de los comandos que la aplicación envía al motor de ejecución. Neutralizar estos metacaracteres antes de su procesamiento es la defensa principal.

### 2. ¿Por qué es la correcta y no el resto?
- **Validación de entrada** detiene la inyección al filtrar, rechazar o escapar caracteres especiales peligrosos (como `'`, `"`, `;`, `<`, `>`).
- **Fuzzing:** Es una técnica ofensiva de pruebas de software, no un control defensivo de mitigación en entornos de producción.
- **Firma de código:** Garantiza la identidad del autor y la integridad del archivo binario, pero no previene que una aplicación legítima contenga errores de programación en sus formularios web.

### 3. Clave para el Examen SY0-701
Junto con la validación de entrada, asocio de inmediato el término **Consultas Parametrizadas (Parameterized Queries / Prepared Statements)**. Es la contramedida más eficaz evaluada en el examen para mitigar la inyección SQL, ya que separa físicamente el código SQL de los datos proporcionados por el usuario.

---

## Pregunta 4: Atributos de Seguridad en Cookies HTTP

### English Version
The term "Secure cookie" refers to an HTTP cookie type transmitted over an encrypted HTTPS connection, which helps prevent the cookie from being intercepted or tampered with during transmission.
- [x] True
- [ ] False

### Versión en Español
El término "cookie segura" se refiere a un tipo de cookie HTTP que se transmite a través de una conexión HTTPS cifrada, lo que ayuda a evitar que la cookie sea interceptada o manipulada durante la transmisión.
- [x] Verdadero
- [ ] Falso

### 1. Explicación General
Las cookies web almacenan con frecuencia identificadores únicos de sesión (*session tokens*). Si un usuario transmite estos datos sobre un canal de comunicación no cifrado (HTTP plano), cualquier adversario situado en el mismo segmento de red local podría capturar la cookie mediante un ataque de *sniffing* y suplantar la identidad del usuario.

### 2. ¿Por qué es la correcta y no el resto?
El enunciado es **Verdadero**. El atributo `Secure` inyectado en la cabecera HTTP le prohíbe explícitamente al navegador web enviar dicha cookie si el canal de comunicación se degrada a HTTP claro; la cookie solo viajará si se ha establecido un túnel TLS/HTTPS activo.

### 3. Clave para el Examen SY0-701
CompTIA evalúa dos atributos críticos para blindar cookies web que debo dominar:
- **Secure:** Restringe la transmisión exclusivamente a conexiones cifradas HTTPS (protección contra intercepción de red / *sniffing*).
- **HttpOnly:** Impide que los scripts del lado del cliente (como JavaScript) accedan a la cookie. Es el control fundamental para neutralizar el robo de sesiones mediante ataques de Cross-Site Scripting (XSS).

---

## Pregunta 5: Análisis de Código Estático (SAST)

### English Version
Which of the terms listed below refers to an automated or manual code review process aimed at discovering logic and syntax errors in the application source code?
- [ ] Input validation
- [ ] Dynamic code analysis
- [ ] Fuzzing
- [x] **Static code analysis**

### Versión en Español
¿Cuál de los términos que se enumeran a continuación se refiere a un proceso de revisión de código automatizado o manual destinado a descubrir errores de lógica y sintaxis en el código fuente de la aplicación?
- [ ] Validación de entrada
- [ ] Análisis de código dinámico
- [ ] Fuzzing
- [x] **Análisis de código estático**

### 1. Explicación General
Evaluar la calidad y la postura de seguridad del software antes del proceso de compilación o empaquetamiento final es un paso inicial crucial en el ciclo de vida de desarrollo seguro (SDLC). Analizar la estructura textual del código fuente ayuda a detectar malas prácticas de manera temprana.

### 2. ¿Por qué es la correcta y no el resto?
- **Análisis de código estático** (conocido como SAST - *Static Application Security Testing*) escanea el código "en reposo" o "código muerto". Actúa como una revisión de planos arquitectónicos buscando patrones de funciones vulnerables o debilidades de sintaxis sin necesidad de poner en marcha la aplicación.
- **Análisis dinámico (DAST):** Requiere obligatoriamente que la aplicación esté compilada y activa para interactuar con ella mediante entradas y respuestas.

### 3. Clave para el Examen SY0-701
Diferencia operativa clave: El análisis estático tiene acceso completo al código fuente (*White-box testing*) y encuentra la línea exacta del error, pero es propenso a generar falsos positivos al no evaluar el comportamiento real en memoria.

---

## Pregunta 6: Pruebas Dinámicas de Seguridad (DAST)

### English Version
Dynamic code analysis allows detecting flaws in the application without actually executing the application code.
- [ ] True
- [x] False

### Versión en Español
El análisis dinámico del código permite detectar fallos en la aplicación sin necesidad de ejecutar realmente el código de la misma.
- [ ] Verdadero
- [x] Falso

### 1. Explicación General
El análisis de código dinámico adopta una perspectiva externa de tipo "caja negra" (*Black-box testing*). Para identificar fallas que solo ocurren bajo carga real de trabajo, interacciones lógicas o consumo de memoria, requiere monitorizar el comportamiento activo del programa.

### 2. ¿Por qué es la correcta y no el resto?
El enunciado es rotundamente **Falso**. Por definición computacional, el análisis dinámico exige que el software esté compilado, desplegado y ejecutándose en un entorno controlado para poder enviarle peticiones y analizar sus respuestas en tiempo real.

### 3. Clave para el Examen SY0-701
El análisis dinámico (DAST) destaca en la identificación de fallas de autenticación, problemas en los flujos lógicos del negocio, malas configuraciones del servidor web subyacente y fugas de memoria (*memory leaks*) que el escaneo estático del texto fuente no puede predecir con exactitud.

---

## Pregunta 7: Análisis Estático vs. Errores en Tiempo de Ejecución

### English Version
The term "static code analysis" refers to the process of detecting runtime errors in an application.
- [ ] True
- [x] False

### Versión en Español
El término "análisis de código estático" se refiere al proceso de detección de errores en tiempo de ejecución de una aplicación.
- [ ] Verdadero
- [x] Falso

### 1. Explicación General
Los errores en tiempo de ejecución (*runtime errors*) son aquellas anomalías que se manifiestan exclusivamente cuando el binario del programa está cargado en la memoria RAM interactuando con variables del sistema operativo (por ejemplo, condiciones de carrera o desbordamientos lógicos dinámicos).

### 2. Análisis de Fallo y Descarte
- **Mi error aquí:** Marqué el enunciado como *Verdadero*, cruzando los conceptos. El análisis estático jamás detectará un error en tiempo de ejecución porque la aplicación no está corriendo durante su análisis.
- **Por qué es Falso:** El escaneo estático lee archivos de texto plano buscando malas prácticas sintácticas. El término técnico correcto para capturar fallas en tiempo de ejecución es **análisis de código dinámico (DAST)**.

### 3. Clave para el Examen SY0-701
Establezco esta regla nemotécnica rápida para evitar confusiones en el examen:
- **Estático = Escritorio / Estacionado:** El código es texto quieto, se evalúa la sintaxis y la estructura.
- **Dinámico = Desplegado / En Movimiento:** El código está vivo en memoria, se evalúa el comportamiento y las respuestas.

---

## Pregunta 8: Criptografía y Firma de Código (Code Signing)

### English Version
What is the purpose of code signing? (Select 2 answers)
- [ ] Disables code reuse
- [x] **Confirms the application's source of origin**
- [ ] Allows the installation of the application
- [x] **Validates the application's integrity**
- [ ] Protects the application against unauthorized use

### Versión en Español
¿Cuál es el propósito de la firma de código? (Seleccione 2 respuestas)
- [ ] Deshabilita la reutilización de código
- [x] **Confirma la fuente de origen de la aplicación**
- [ ] Permite la instalación de la aplicación
- [x] **Valida la integridad de la aplicación**
- [ ] Protege la aplicación contra el uso no autorizado.

### 1. Explicación General
La firma de código (*Code Signing*) aprovecha los componentes de una infraestructura de clave pública (PKI). El desarrollador calcula el hash del binario ejecutable y lo cifra utilizando su clave privada corporativa, estampando un sello digital de autenticidad.

### 2. ¿Por qué es la correcta y no el resto?
- **Confirma la fuente de origen** al garantizar la autenticidad (sé exactamente qué entidad o desarrollador firmó el archivo a través del certificado de clave pública).
- **Valida la integridad** porque si un atacante inyecta malware o modifica un solo byte del binario tras la firma, el hash divergerá y el sistema operativo romperá la confianza del archivo bloqueando su ejecución.

### 3. Clave para el Examen SY0-701
La firma de código proporciona la propiedad de **No repudio**. El creador del software no puede negar la autoría o publicación de una versión específica del programa si este fue validado con su clave privada legítima (a menos que demuestre un compromiso previo de sus llaves maestras).

---

## Pregunta 9: Concepto y Aplicación de Fuzzing

### English Version
The practice of finding vulnerabilities in an application by feeding it incorrect data is called:
- [ ] Normalization
- [ ] Hardening
- [ ] Dynamic code analysis
- [x] **Fuzzing**

### Versión en Español
La práctica de encontrar vulnerabilidades en una aplicación introduciéndole datos incorrectos se denomina:
- [ ] Normalización
- [ ] Endurecimiento
- [ ] Análisis de código dinámico
- [x] **Fuzzing**

### 1. Explicación General
Para auditar la robustez de las interfaces de entrada de una aplicación y descubrir fallas ocultas que congelen el sistema, los especialistas automatizan pruebas que inyectan datos inesperados de manera masiva.

### 2. ¿Por qué es la correcta y no el resto?
- **Fuzzing** (*Fuzz testing*) es el término preciso para el envío masivo y automatizado de datos aleatorios, malformados o inválidos hacia los puntos de entrada de un programa con el fin de provocar bloqueos, fugas de memoria o excepciones no controladas.
- **Normalización:** Proceso de optimización de bases de datos para mitigar redundancias, o la estandarización de entradas de texto.
- **Endurecimiento (Hardening):** Es la eliminación de servicios innecesarios y configuraciones por defecto para reducir la superficie de ataque de un sistema operativo.

### 3. Clave para el Examen SY0-701
El Fuzzing es una técnica ofensiva de primer nivel para descubrir **vulnerabilidades de día cero (Zero-days)** y fallos lógicos complejos que los desarrolladores no previeron en los casos de prueba convencionales del software.

---

## Pregunta 10: Aislamiento de Procesos (Sandboxing)

### English Version
In computer security, a mechanism for the secure execution of untested code or untrusted applications is called:
- [ ] Sideloading
- [ ] Virtualization
- [x] **Sandboxing**
- [ ] Stress testing

### Versión en Español
En seguridad informática, un mecanismo para la ejecución segura de código no probado o aplicaciones no confiables se denomina:
- [ ] Carga lateral
- [ ] Virtualización
- [x] **Sandboxing**
- [ ] Pruebas de estrés

### 1. Explicación General
Cuando se necesita analizar muestras de malware capturadas o verificar el comportamiento de binarios experimentales que podrían comprometer la estabilidad del sistema, se recurre a entornos con restricciones lógicas extremas.

### 2. ¿Por qué es la correcta y no el resto?
- **Sandboxing** (Entorno de pruebas aislado) confina la ejecución del programa en una burbuja lógica. El proceso tiene prohibido escribir en el disco físico real, alterar las llaves del registro base o comunicarse con el segmento de red local. Si el código despliega malware, el impacto queda contenido en la caja de arena.
- **Sideloading:** Proceso de instalar aplicaciones empaquetadas omitiendo los repositorios o tiendas oficiales del sistema operativo.
- **Virtualización:** Concepto general que permite abstraer hardware para ejecutar sistemas operativos completos (máquinas virtuales), mientras que el *sandboxing* apunta específicamente al aislamiento de aplicaciones individuales sospechosas.

### 3. Clave para el Examen SY0-701
Los sistemas de protección avanzados como los cortafuegos de correo electrónico modernos o soluciones **EDR (Endpoint Detection and Response)** utilizan motores de *sandboxing* automáticos en la nube para detonar y observar archivos adjuntos antes de permitir su entrega al buzón de los usuarios finales.

---

## Pregunta 11: Manejo de Excepciones en Arquitecturas Windows (SEH)

### English Version
Which of the following answers refers to a Windows-specific feature for handling exceptions, errors, and abnormal conditions in software?
- [ ] EPC
- [x] **SEH**
- [ ] EH
- [ ] EXR

### Versión en Español
¿Cuál de las siguientes respuestas se refiere a una característica específica de Windows para el manejo de excepciones, errores y condiciones anormales en el software?
- [ ] EPC
- [x] **SEH**
- [ ] EH
- [ ] EXR

### 1. Explicación General
El sistema operativo Microsoft Windows provee un marco arquitectónico a bajo nivel para permitir que el software desarrollado en lenguajes como C o C++ capture fallas críticas a nivel de aplicación o hardware sin colapsar la sesión completa del usuario.

### 2. ¿Por qué es la correcta y no el resto?
- **SEH** (*Structured Exception Handling*) es el mecanismo nativo y propietario de Windows encargado de estructurar el control de condiciones anómalas mediante rutinas lógicas (`__try` y `__except`).
- Los demás acrónimos (*EPC, EH, EXR*) no corresponden a tecnologías estándar o características evaluadas en el control de excepciones de sistemas Windows en el ámbito de seguridad de aplicaciones.

### 3. Clave para el Examen SY0-701
A nivel técnico avanzado, debo saber que los atacantes intentan explotar desbordamientos de búfer en la pila para sobrescribir los punteros de los controladores SEH (*SEH Overwrite Attack*), logrando desviar la ejecución del hilo del programa hacia código malicioso personalizado (*shellcode*).

---

## Pregunta 12: Aleatorización de Memoria (ASLR)

### English Version
Address Space Layout Randomization (ASLR) is an operating system security technique that randomizes the location of key data areas in memory. The goal of ASLR is to prevent attackers from predicting the location of specific code or data in memory, which adds a layer of protection against memory-based attacks such as buffer overflows.
- [x] True
- [ ] False

### Versión en Español
La aleatorización del espacio de direcciones (ASLR, por sus siglas en inglés) es una técnica de seguridad del sistema operativo que aleatoriza la ubicación de áreas de datos clave en la memoria. El objetivo de ASLR es evitar que los atacantes predigan la ubicación de código o datos específicos en la memoria, lo que añade una capa de protección contra ataques basados ​​en la memoria, como los desbordamientos de búfer.
- [x] **Verdadero**
- [ ] Falso

### 1. Explicación General
En sistemas operativos antiguos, las funciones esenciales y las librerías dinámicas se cargaban invariablemente en las mismas coordenadas exactas de la memoria RAM. Esto permitía a los desarrolladores de exploits escribir instrucciones fijas que apuntaban de forma consistente a esas direcciones para secuestrar el flujo del sistema.

### 2. ¿Por qué es la correcta y no el resto?
El enunciado es completamente **Verdadero**. ASLR reordena aleatoriamente el mapa de direcciones de la memoria RAM cada vez que el equipo arranca o el programa se inicia. Al alterar la ubicación de la pila (*stack*) y el montón (*heap*), un ataque de desbordamiento de búfer basado en direcciones estáticas fallará y provocará el cierre seguro del programa en lugar de ejecutar código malicioso.

### 3. Clave para el Examen SY0-701
ASLR trabaja en tándem con **DEP (Data Execution Prevention / bit NX/XD)**. Mientras que ASLR oculta la ubicación de los componentes en la memoria RAM, DEP etiqueta explícitamente ciertas regiones de memoria como no ejecutables, impidiendo que el procesador ejecute instrucciones inyectadas en zonas destinadas únicamente a almacenar datos.

---

## Pregunta 13: Mitigación de Automatización (CAPTCHA)

### English Version
A type of user identification mechanism used as a countermeasure against automated software (such as network bots) is known as:
- [ ] MFA
- [x] **CAPTCHA**
- [ ] SSO
- [ ] NIDS

### Versión en Español
Un tipo de mecanismo de identificación de usuario utilizado como contramedida contra software automatizado (como los bots de red) se conoce como:
- [ ] MFA
- [x] **CAPTCHA**
- [ ] SSO
- [ ] NIDS

### 1. Explicación General
Los atacantes emplean scripts automatizados (*bots*) para realizar ataques de fuerza bruta masivos, inyección de spam en formularios o ataques de relleno de credenciales (*credential stuffing*). Se requiere un control de capa de aplicación capaz de evaluar si quien interactúa posee rasgos computacionales exclusivamente humanos.

### 2. ¿Por qué es la correcta y no el resto?
- **CAPTCHA** (*Completely Automated Public Turing test to tell Computers and Humans Apart*) plantea desafíos cognitivos (lógicos o visuales) sencillos para un humano pero difíciles de interpretar y procesar por scripts automatizados tradicionales, mitigando el abuso en formularios web.
- **MFA:** Autenticación multifactor; valida la identidad legítima de un usuario a través de múltiples canales, pero no está diseñado para distinguir humanos de bots en un acceso público general.
- **SSO:** *Single Sign-On* (Inicio de sesión único); centraliza la autenticación entre múltiples plataformas.
- **NIDS:** Sistema de detección de intrusos en la red; analiza el tráfico del segmento buscando firmas de ataques a nivel de paquetes.

### 3. Clave para el Examen SY0-701
Integrar CAPTCHAs en las pasarelas de inicio de sesión o formularios de contacto es un control defensivo de software fundamental en la capa de aplicación para contrarrestar ataques automatizados web de fuerza bruta.

---

## Pregunta 14: Verificación y Normalización de Entradas

### English Version
Which of the following terms refers to a process that ensures string data matches an expected format before it is processed by the application?
- [ ] Obfuscation
- [ ] Code signing
- [x] **Input validation**
- [ ] Data minimization

### Versión en Español
¿Cuál de los siguientes términos se refiere a un proceso que garantiza que los datos de cadena coincidan con un formato esperado antes de que sean procesados por la aplicación?
- [ ] Ofuscación
- [ ] Firma de código
- [x] **Validación de entrada**
- [ ] Minimización de datos

### 1. Explicación General
Cuando los sistemas reciben campos abiertos de texto plano, la aplicación debe pasar esas cadenas por un embudo de filtrado que garantice que no contienen caracteres prohibidos.

### 2. ¿Por qué es la correcta y no el resto?
- **Validación de entrada** comprueba el formato exacto mediante expresiones regulares (por ejemplo, validar que un correo electrónico tenga una estructura `@` y un dominio válido) descartando cualquier otra cosa.
- **Ofuscación:** Modificación del código fuente para volverlo ilegible a la ingeniería inversa humana, manteniendo intacta su funcionalidad computacional.
- **Minimización de datos:** Principio de privacidad de la información que dicta que solo deben recopilarse los datos personales estrictamente necesarios para cumplir el objetivo del negocio.

### 3. Clave para el Examen SY0-701
Relaciono esto inmediatamente con los conceptos de **Listas Blancas (Allow-list)** vs. **Listas Negras (Block-list)**. Para el examen, la validación de entrada basada en listas blancas (especificar exactamente qué se permite) es infinitamente superior y más segura que intentar adivinar y bloquear lo que podría ser dañino.

---

## Pregunta 15: Entornos de Ciclo de Vida del Software (SDLC)

### English Version
In secure software development, the environment where code is written and initially tested by developers is called:
- [x] **Development**
- [ ] Staging
- [ ] Production
- [ ] Testing

### Versión en Español
En el desarrollo de software seguro, el entorno donde los desarrolladores escriben y prueban inicialmente el código se denomina:
- [x] **Desarrollo (Development)**
- [ ] Preproducción (Staging)
- [ ] Producción
- [ ] Pruebas (Testing)

### 1. Explicación General
El ciclo de vida de desarrollo de sistemas exige una segregación estricta de funciones y entornos técnicos para impedir que fallas de programación o vulnerabilidades experimentales comprometan datos reales o la disponibilidad operativa de la empresa.

### 2. ¿Por qué es la correcta y no el resto?
- El entorno de **Desarrollo** es el ecosistema local o centralizado donde los ingenieros de software construyen las primeras líneas de código fuente.
- **Staging (Preproducción):** Réplica idéntica del entorno productivo donde se validan las integraciones finales antes del despliegue masivo.
- **Producción:** El entorno vivo y crítico donde los clientes reales consumen los servicios del negocio; los desarrolladores jamás deben tener acceso de escritura directo aquí.

### 3. Clave para el Examen SY0-701
Un principio de cumplimiento auditado en la certificación es que **los datos confidenciales de producción jamás deben copiarse hacia entornos de desarrollo** para realizar pruebas de software, debido al alto riesgo de fuga de datos en ambientes con menores controles de seguridad.

---

## Pregunta 16: El Rol de QA y Entornos de Pruebas

### English Version
Which software development environment is used by Quality Assurance (QA) engineers to perform comprehensive functional and security testing before a release?
- [ ] Development
- [ ] Production
- [x] **Testing**
- [ ] Staging

### Versión en Español
¿Qué entorno de desarrollo de software utilizan los ingenieros de Control de Calidad (QA) para realizar pruebas funcionales y de seguridad integrales antes de un lanzamiento?
- [ ] Desarrollo
- [ ] Producción
- [x] **Pruebas (Testing)**
- [ ] Preproducción (Staging)

### 1. Explicación General
Una vez que el equipo de desarrollo concluye una característica de software, el código debe ser migrado hacia un área neutral de control de calidad para verificar de forma independiente que cumple con los requerimientos técnicos y que no introduce nuevas fallas de seguridad (*regresiones*).

### 2. ¿Por qué es la correcta y no el resto?
- El entorno de **Pruebas (Testing)** está diseñado específicamente para que los ingenieros de QA ejecuten casos de prueba lógicos, escaneos de vulnerabilidades automatizados y validaciones funcionales complejas sin interferir con las tareas de codificación diaria de los desarrolladores.
- **Producción** está totalmente fuera de los límites para pruebas experimentales agresivas de QA debido al peligro latente de causar una denegación de servicio (DoS).

### 3. Clave para el Examen SY0-701
En este entorno se implementan de forma rigurosa las pruebas de **Caja Negra (Black-box)** y de **Caja Gris (Gray-box)** para simular ataques externos reales antes de certificar que el paquete de software es seguro para su avance en el pipeline.

---

## Pregunta 17: Entorno de Preproducción (Staging)

### English Version
A production-like environment used to test installation, configuration, and deployment scripts before they are applied to the live environment is called:
- [ ] Development
- [x] **Staging**
- [ ] Sandbox
- [ ] Testing

### Versión en Español
Un entorno similar al de producción que se utiliza para probar los scripts de instalación, configuración y despliegue antes de aplicarlos al entorno real se denomina:
- [ ] Desarrollo
- [x] **Preproducción (Staging)**
- [ ] Sandbox
- [ ] Pruebas (Testing)

### 1. Explicación General
El último paso de verificación técnica antes del lanzamiento al mercado consiste en desplegar el software en un entorno espejo para garantizar que las configuraciones de red, las migraciones de bases de datos y la arquitectura física responderán exactamente igual en producción.

### 2. ¿Por qué es la correcta y no el resto?
- **Staging** actúa como el ensayo general. Su infraestructura, parches de sistemas operativos y variables de entorno clonan con exactitud el ecosistema productivo real. Si un script de instalación falla en Staging, fallará en producción.
- **Sandbox:** Es una técnica de aislamiento temporal de procesos, no una fase macro de la topología de despliegue del SDLC.

### 3. Clave para el Examen SY0-701
El paso exitoso del código a través de los entornos sigue un orden lineal crítico e irreversible para mantener la integridad del software: **Desarrollo ➡️ Pruebas ➡️ Staging ➡️ Producción**.

---

## Pregunta 18: Prevención de Ejecución de Datos (DEP / bit NX)

### English Version
Which of the following security concepts prevents a processor from executing code in non-executable memory regions, such as the stack or heap?
- [ ] ASLR
- [ ] SEH
- [x] **DEP**
- [ ] Fuzzing

### Versión en Español
¿Cuál de los siguientes conceptos de seguridad impide que un procesador ejecute código en regiones de memoria no ejecutables, como la pila o el montón?
- [ ] ASLR
- [ ] SEH
- [x] **DEP**
- [ ] Fuzzing

### 1. Explicación General
Para tomar el control de un servidor vulnerado, los ciberdelincuentes explotan desbordamientos de búfer introduciendo comandos ejecutables cifrados (*shellcode*) dentro de campos que almacenan datos de usuario simples en la memoria RAM, forzando al procesador del equipo a procesar e iniciar esa lógica maliciosa.

### 2. ¿Por qué es la correcta y no el resto?
- **DEP** (*Data Execution Prevention* / Prevención de Ejecución de Datos) es la tecnología de hardware y software que marca zonas específicas de la memoria (como el *stack* y el *heap*) con el atributo binario de **No Ejecutable (NX / XD)**. Si el procesador detecta un intento de ejecutar código en esas áreas protegidas, bloquea el hilo de inmediato y emite una excepción de violación de acceso de memoria.
- **ASLR:** Cambia de lugar los datos en la memoria RAM, pero no modifica sus propiedades de ejecución.

### 3. Clave para el Examen SY0-701
Debo asimilar que **DEP y ASLR no se reemplazan, sino que se complementan**. Mientras ASLR le complica al atacante saber *dónde* está la memoria, DEP le prohíbe ejecutar su malware si logra inyectarlo en las áreas de almacenamiento de datos de la memoria RAM.

---

## Pregunta 19: Modelado de Amenazas (Threat Modeling)

### English Version
The practice of identifying, quantifying, and prioritizing potential security risks and vulnerabilities in an application's design is known as:
- [ ] Code obfuscation
- [ ] Secure coding
- [x] **Threat modeling**
- [ ] Vulnerability scanning

### Versión en Español
La práctica de identificar, cuantificar y priorizar los posibles riesgos de seguridad y vulnerabilidades en el diseño de una aplicación se conoce como:
- [ ] Ofuscación de código
- [ ] Codificación segura
- [x] **Modelado de amenazas**
- [ ] Escaneo de vulnerabilidades

### 1. Explicación General
Para diseñar contramedidas efectivas en el desarrollo de software, es imperativo analizar los diagramas de arquitectura lógicos de la aplicación en las etapas iniciales de planificación, anticipando cómo un adversario atacaría los flujos lógicos.

### 2. ¿Por qué es la correcta y no el resto?
- **Modelado de amenazas** (*Threat Modeling*) es el ejercicio preventivo y estructurado enfocado en mapear los vectores de ataque del diseño antes de escribir el software. Utiliza metodologías como **STRIDE** (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege).
- **Escaneo de vulnerabilidades:** Es un análisis automatizado posterior que busca fallas ya conocidas en sistemas activos, no una fase abstracta de evaluación de diseño de la lógica del negocio.

### 3. Clave para el Examen SY0-701
El modelado de amenazas se ejecuta de forma óptima durante la fase de **Diseño y Requerimientos** del ciclo de vida del software (SDLC). Es mucho más económico y seguro corregir un error estructural en un diagrama de flujo de diseño que parchar una vulnerabilidad grave en producción.

---

## Pregunta 20: Reutilización Segura de Código y Terceros

### English Version
When developing secure software, incorporating third-party open-source libraries without verification introduces risks related to:
- [ ] Insufficient input validation
- [ ] Improper error handling
- [x] **Software supply chain vulnerabilities**
- [ ] Lack of code obfuscation

### Versión en Español
Al desarrollar software seguro, la incorporación de bibliotecas de código abierto de terceros sin verificación introduce riesgos relacionados con:
- [ ] Validación de entrada insuficiente
- [ ] Manejo inadecuado de errores
- [x] **Vulnerabilidades en la cadena de suministro de software**
- [ ] Falta de ofuscación de código

### 1. Explicación General
Los equipos modernos de programación no escriben todo desde cero; importan cientos de paquetes y librerías prefabricadas de código abierto a través de repositorios públicos (como NPM, PyPI, NuGet) para acelerar sus flujos de entregas.

### 2. ¿Por qué es la correcta y no el resto?
- Importar dependencias sin supervisión directa impacta la **Cadena de Suministro de Software (Software Supply Chain)**. Si una librería de terceros tiene fallas de seguridad conocidas o es suplantada maliciosamente por un actor malintencionado (*Typosquatting*), tu propia aplicación heredará automáticamente ese agujero de seguridad.
- Las opciones de validación de entrada o manejo de errores se enfocan en la lógica nativa escrita en casa, no en los componentes externos heredados.

### 3. Clave para el Examen SY0-701
Para defenderme de estos ataques, el examen evalúa herramientas de análisis tipo **SCA (Software Composition Analysis)**. Estas herramientas automatizadas auditan el árbol de dependencias del software construyendo una lista de materiales de software (**SBOM - Software Bill of Materials**) para alertar inmediatamente si alguna librería externa contiene vulnerabilidades críticas conocidas (CVEs).

---

[[ExamCompass - Cuestionarios por Temas|⬅️ Volver a Cuestionarios por Temas]]