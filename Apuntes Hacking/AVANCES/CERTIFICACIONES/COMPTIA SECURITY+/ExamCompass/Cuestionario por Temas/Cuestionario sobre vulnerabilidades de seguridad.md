---
tags:
  - "formato/apunte"
  - "hacking/fundamental"
  - "examen/test-especifico"
  - "gestion/estado/terminado"
---
Este apunte contiene el análisis detallado del cuestionario temático sobre vulnerabilidades del sistema operativo, memoria y aplicaciones de la plataforma ExamCompass para la certificación CompTIA Security+ (SY0-701), alineado con las respuestas oficiales del simulador.

---

## Pregunta 1: Definición de Inyección de Memoria

### English Version
Which type of application attack relies on introducing external code into the address space of a running program?
* [ ] Buffer overflow
* [✅] **Memory injection**
* [ ] Replay attack
* [ ] Pointer dereference

### Versión en Español
¿Qué tipo de ataque a aplicaciones se basa en introducir código externo en el espacio de direcciones de un programa en ejecución?
* [ ] Desbordamiento de búfer (Buffer overflow)
* [✅] **Inyección de memoria (Memory injection)**
* [ ] Ataque de repetición (Replay attack)
* [ ] Desreferencia de puntero (Pointer dereference)

### 1. Explicación General
La inyección de memoria es una técnica avanzada de explotación mediante la cual un proceso malicioso inyecta código ejecutable (shellcode) o una biblioteca directamente en el espacio de direcciones lógicas asignado a un subproceso legítimo que ya está corriendo en el sistema.

### 2. ¿Por qué es la correcta y no el resto?
**Inyección de memoria** es la respuesta correcta porque describe con precisión el acto de insertar y ejecutar código en un espacio de memoria dinámico y activo. *Desbordamiento de búfer* se descarta porque consiste en saturar la capacidad de almacenamiento de datos de un búfer fijo para sobrescribir la pila (stack) o el montón (heap); aunque puede llevar a la ejecución de código, la técnica puramente definida por introducir código en un espacio de ejecución existente es la inyección de memoria. *Ataque de repetición* es una amenaza de red, y la *desreferencia de puntero* ocurre cuando el software intenta leer una ubicación de memoria inválida o nula.

### 3. Clave para el Examen SY0-701
Cuando una pregunta del examen describa la manipulación directa de la memoria de un proceso en ejecución para forzarlo a hospedar y procesar código malicioso externo de manera sigilosa, busque el concepto de Memory Injection.

---

## Pregunta 2: Definición de Biblioteca de Enlace Dinámico (DLL)

### English Version
A collection of precompiled functions designed to be used by more than one Microsoft Windows application simultaneously to save system resources is known as:
* [✅] **DLL**
* [ ] API
* [ ] EXE
* [ ] INI

### Versión en Español
Una colección de funciones precompiladas diseñada para ser utilizada por más de una aplicación de Microsoft Windows simultáneamente para ahorrar recursos del sistema se conoce como:
* [✅] **DLL**
* [ ] API
* [ ] EXE
* [ ] INI

### 1. Explicación General
En el entorno operativo Windows, las bibliotecas de enlace dinámico son componentes de software modular que permiten a múltiples programas compartir código y recursos lógicos idénticos para realizar tareas estándar (como dibujar ventanas o procesar redes) sin duplicar archivos en memoria.

### 2. ¿Por qué es la correcta y no el resto?
**DLL (Dynamic Link Library)** cumple de forma exacta con la definición de biblioteca de funciones precompiladas de Windows. *API* se descarta porque representa la interfaz conceptual de programación o el contrato lógico de comunicación, no el archivo precompilado que guarda las funciones. *EXE* representa un archivo ejecutable principal (un programa independiente). *INI* es un formato de archivo de texto plano utilizado para configuraciones de inicialización de software, no contiene código ejecutable ni funciones.

### 3. Clave para el Examen SY0-701
Comprender qué es una DLL es el prerrequisito arquitectónico necesario para entender ataques complejos de secuestro y manipulación de procesos de Windows en la memoria del sistema.

---

## Pregunta 3: Concepto de Inyección de DLL

### English Version
Which of the answers listed below refers to an application attack that relies on executing a library of code?
* [ ] Memory leak
* [✅] **DLL injection**
* [ ] Pointer dereference
* [ ] Buffer overflow

### Versión en Español
¿Cuál de las respuestas enumeradas a continuación se refiere a un ataque a aplicaciones que se basa en la ejecución de una biblioteca de código?
* [ ] Fuga de memoria (Memory leak)
* [✅] **Inyección de DLL (DLL injection)**
* [ ] Desreferencia de puntero (Pointer dereference)
* [ ] Desbordamiento de búfer (Buffer overflow)

### 1. Explicación General
La inyección de DLL es una variante específica de la inyección de memoria en la que un atacante obliga a un proceso legítimo de Windows a cargar y ejecutar una biblioteca de enlace dinámico (.dll) maliciosa externa dentro de su propio contexto de seguridad.

### 2. ¿Por qué es la correcta y no el resto?
**Inyección de DLL** es la única opción que cumple estrictamente con el requisito de "ejecutar una biblioteca de código". *Desbordamiento de búfer* se descarta porque ataca los límites de almacenamiento de datos de una variable en memoria, no la carga estructurada de una biblioteca. *Fuga de memoria* es un fallo de desarrollo donde el programa olvida liberar memoria asignada, y la *desreferencia de puntero* es una falla de direccionamiento lógico.

### 3. Clave para el Examen SY0-701
Si el enunciado del examen detalla que un malware intenta evadir la detección de un sistema EDR obligando a un proceso nativo del sistema operativo (como explorer.exe o svchost.exe) a cargar una biblioteca externa no autorizada, el ataque es DLL Injection.

---

## Pregunta 4: Mecánica del Desbordamiento de Búfer

### English Version
A type of exploit in which an application overwrites the contents of a memory area it should not have access to is called:
* [ ] DLL injection
* [✅] **Buffer overflow**
* [ ] Memory leak
* [ ] Privilege escalation

### Versión en Español
Un tipo de exploit en el que una aplicación sobrescribe el contenido de un área de memoria a la que no debería tener acceso se denomina:
* [ ] Inyección de DLL (DLL injection)
* [✅] **Desbordamiento de búfer (Buffer overflow)**
* [ ] Fuga de memoria (Memory leak)
* [ ] Escalada de privilegios (Privilege escalation)

### 1. Explicación General
Un desbordamiento de búfer ocurre cuando un programa recibe más volumen de datos del que está diseñado para almacenar en un búfer específico, provocando que el excedente de información se desborde y sobrescriba los bloques de memoria adyacentes.

### 2. ¿Por qué es la correcta y no el resto?
**Desbordamiento de búfer** es la respuesta correcta porque describe con exactitud la vulnerabilidad de entrada de datos que "sobrescribe" el contenido de la memoria fuera de los límites reservados. *Inyección de DLL* carga una biblioteca entera de forma legítima para el proceso. *Fuga de memoria* no sobrescribe nada, solo agota la memoria libre. La *escalada de privilegios* es un objetivo de control de accesos que puede ser consecuencia de un desbordamiento, pero no es la falla técnica de memoria en sí.

### 3. Clave para el Examen SY0-701
Las fallas de Buffer Overflow son causadas por una validación deficiente de la longitud de las entradas en lenguajes como C o C++. En el examen, se mitigan mediante funciones de validación de límites de entrada (bounds checking) y mecanismos como ASLR y DEP.

---

## Pregunta 5: Definición de Condición de Carrera

### English Version
A malfunction in a preprogrammed sequential access to a shared resource is described as:
* [✅] **Race condition**
* [ ] Concurrency error
* [ ] Multithreading
* [ ] Synchronization error

### Versión en Español
Un mal funcionamiento en el acceso secuencial preprogramado a un recurso compartido se describe como:
* [✅] **Condición de carrera (Race condition)**
* [ ] Error de concurrencia (Concurrency error)
* [ ] Multiprocesamiento (Multithreading)
* [ ] Error de sincronización (Synchronization error)

### 1. Explicación General
Una condición de carrera se produce cuando dos o más subprocesos de software intentan acceder y modificar un recurso compartido simultáneamente de manera que el resultado final depende exclusivamente del orden y la velocidad de ejecución de dichos subprocesos.

### 2. ¿Por qué es la correcta y no el resto?
**Condición de carrera** es el término técnico preciso que define esta falla secuencial específica. *Error de concurrencia* y *Error de sincronización* son clasificaciones conceptuales genéricas que abarcan múltiples tipos de fallas (como bloqueos mutuos o deadlocks), pero no definen el fallo de acceso secuencial preprogramado. *Multiprocesamiento* es una característica legítima de los procesadores modernos para ejecutar hilos en paralelo.

### 3. Clave para el Examen SY0-701
La Race Condition ocurre cuando los desarrolladores no implementan mecanismos de bloqueo o exclusión mutua (mutex) en recursos críticos compartidos, permitiendo que un atacante altere el flujo normal de operaciones mediante ejecuciones veloces.

---

## Pregunta 6: La Vulnerabilidad de Tiempo TOC/TOU

### English Version
A type of vulnerability where the state of a resource is verified at one point in time but may change before the resource is actually used is referred to as:
* [ ] TOC
* [✅] **TOC/TOU**
* [ ] TOU
* [ ] TSIG

### Versión en Español
Un tipo de vulnerabilidad en la que el estado de un recurso se verifica en un momento dado pero puede cambiar antes de que el recurso se utilice realmente se denomina:
* [ ] TOC
* [✅] **TOC/TOU**
* [ ] TOU
* [ ] TSIG

### 1. Explicación General
Las vulnerabilidades TOC/TOU (Tiempo de Comprobación a Tiempo de Uso) son una subcategoría de las condiciones de carrera que ocurren cuando un programa realiza una verificación de seguridad sobre un recurso (como un archivo) y, en la fracción de segundo previa a que el sistema use dicho recurso, un atacante modifica el recurso verificado por uno malicioso.

### 2. ¿Por qué es la correcta y no el resto?
**TOC/TOU (Time-of-Check to Time-of-Use)** es la denominación correcta que une ambas fases temporales del fallo de lógica. *TOC (Time of Check)* y *TOU (Time of Use)* por sí solas describen solo fragmentos de la ventana temporal del ataque y no la vulnerabilidad completa. *TSIG (Transaction Signature)* es un protocolo criptográfico de seguridad utilizado para autenticar actualizaciones de zonas en servidores DNS.

### 3. Clave para el Examen SY0-701
Si el escenario del examen describe que un sistema valida los privilegios de un archivo de texto de manera exitosa, pero un atacante reemplaza ese archivo mediante un enlace simbólico rápido justo antes de que el sistema lo ejecute, está ante un vector TOC/TOU.

---

## Pregunta 7: Vectores para Actualizaciones Maliciosas

### English Version
A malicious application update can be enabled through various means, including:
* [ ] Unsigned application code
* [ ] Unencrypted update channel (HTTP vs HTTPS)
* [ ] Fake update website
* [ ] Compromised software development process
* [✅] **All of the above**

### Versión en Español
La introducción de una actualización maliciosa en el código de una aplicación puede habilitarse a través de varios medios, incluidos:
* [ ] Código de aplicación no firmado
* [ ] Canal de actualización no cifrado (HTTP vs HTTPS)
* [ ] Sitio web de actualizaciones falso
* [ ] Proceso de desarrollo de software comprometido
* [✅] **Todo lo anterior**

### 1. Explicación General
Los ataques de actualización maliciosa secuestran la cadena de confianza establecida entre el cliente y el desarrollador para inyectar troyanos dentro de los flujos legítimos de mantenimiento del software.

### 2. ¿Por qué es la correcta y no el resto?
**Todo lo anterior** es la respuesta correcta porque cada una de las vulnerabilidades listadas permite un vector diferente de inyección: la falta de firmas digitales impide verificar el origen del código; el tráfico HTTP permite ataques On-path para alterar el paquete en tránsito; los sitios web falsos usan typosquatting para engañar al usuario; y un entorno de desarrollo comprometido da origen a un ataque directo a la cadena de suministro.

### 3. Clave para el Examen SY0-701
Para proteger los canales de actualización contra amenazas, es mandatorio el uso exclusivo de cifrado de red en tránsito (HTTPS/TLS) acoplado con la firma criptográfica obligatoria del código fuente (Code Signing).

---

## Pregunta 8: Clasificación de Vulnerabilidades del Sistema Operativo

### English Version
Which of the following answers does not refer to a common type of OS-based vulnerability?
* [ ] Access control and permissions vulnerabilities
* [ ] Vulnerabilities in installed applications, system utilities, and device drivers
* [ ] Memory-related vulnerabilities
* [ ] Patch and update management vulnerabilities
* [ ] Vulnerabilities related to system/security misconfigurations
* [ ] Network-related vulnerabilities
* [✅] **All of the above answer choices are examples of OS-based vulnerabilities**

### Versión en Español
¿Cuál de las siguientes respuestas no se refiere a un tipo común de vulnerabilidad basada en el sistema operativo?
* [ ] Vulnerabilidades de control de acceso y permisos
* [ ] Vulnerabilidades en aplicaciones instaladas, utilidades del sistema y controladores de dispositivos
* [ ] Vulnerabilidades relacionadas con la memoria
* [ ] Vulnerabilidades de gestión de parches y actualizaciones
* [ ] Vulnerabilidades relacionadas con malas configuraciones del sistema/seguridad
* [ ] Vulnerabilidades relacionadas con la red
* [✅] **Todas las opciones de respuesta anteriores son ejemplos de vulnerabilidades basadas en el sistema operativo**

### 1. Explicación General
La superficie de ataque de un sistema operativo (SO) es masiva debido a que actúa como el puente de orquestación entre la infraestructura de red, el hardware de memoria, las configuraciones del usuario y todas las aplicaciones instaladas.

### 2. ¿Por qué es la correcta y no el resto?
La opción **Todas las opciones de respuesta anteriores son ejemplos...** es la correcta porque la pregunta pide identificar cuál de ellas no pertenece a la categoría. Dado que el control de accesos, los controladores, la gestión de memoria, la política de parches, las configuraciones del sistema y las conexiones de red forman parte integral de las responsabilidades directas de un sistema operativo moderno, todas constituyen ejemplos válidos de su superficie de riesgo.

### 3. Clave para el Examen SY0-701
Para asegurar un sistema operativo frente a esta matriz de vulnerabilidades diversificada, la estrategia del examen exige aplicar metodologías de Endurecimiento del Sistema (OS Hardening).

---

## Pregunta 9: Inyección de Comandos en Bases de Datos (SQLi)

### English Version
Which of the answers listed below refers to a security vulnerability that enables inserting malicious code into input fields, such search bars or login forms, to execute unauthorized commands on a database?  
* [ ] RCE
* [✅] **SQLi**
* [ ] XSS
* [ ] CSRF

### Versión en Español
¿Cuál de las respuestas enumeradas a continuación se refiere a una vulnerabilidad de seguridad que permite insertar código malicioso en campos de entrada para ejecutar comandos no autorizados en una base de datos?
* [ ] RCE
* [✅] **SQLi**
* [ ] XSS
* [ ] CSRF

### 1. Explicación General
La inyección SQL ocurre cuando los datos de entrada proporcionados por el usuario no son sanitizados ni validados adecuadamente por la aplicación web, permitiendo que caracteres especiales de control modifiquen la estructura de la consulta SQL original que se envía al motor de base de datos.

### 2. ¿Por qué es la correcta y no el resto?
**SQLi (SQL Injection)** es la única respuesta correcta ya que su objetivo y blanco exclusivo es el intérprete de comandos de la base de datos de respaldo (backend). *RCE* es la ejecución remota de código en el sistema operativo host general. *XSS (Cross-Site Scripting)* ataca a los navegadores de los usuarios finales que visitan la web. *CSRF* obliga al navegador de una víctima autenticada a enviar solicitudes HTTP no deseadas a una aplicación web.

### 3. Clave para el Examen SY0-701
La contramedida técnica más efectiva recomendada por CompTIA para mitigar por completo la vulnerabilidad de inyección SQL es la implementación estricta de Consultas Parametrizadas (Parameterized Queries / Prepared Statements) y la validación de entradas.

---

## Pregunta 10: Firmas de Ataque SQLi en Consultas

### English Version
Which of the following indicates an SQL injection attack attempt?
* [ ] DELETE FROM itemDB WHERE itemID = '1';
* [✅] **SELECT * FROM users WHERE userName = 'Alice' AND password = '' OR '1' = '1';**
* [ ] DROP TABLE itemDB;
* [ ] SELECT * FROM users WHERE email = 'example@example.com' AND password = '';

### Versión en Español
¿Cuál de las siguientes respuestas indica un intento de ataque de inyección SQL?
* [ ] DELETE FROM itemDB WHERE itemID = '1';
* [✅] **SELECT * FROM users WHERE userName = 'Alice' AND password = '' OR '1' = '1';**
* [ ] DROP TABLE itemDB;
* [ ] SELECT * FROM users WHERE email = 'example@example.com' AND password = '';

### 1. Explicación General
Los atacantes utilizan operadores lógicos y tautologías matemáticas (afirmaciones que siempre resultan verdaderas, como '1'='1') para anular las cláusulas de validación de contraseñas de las aplicaciones web.

### 2. ¿Por qué es la correcta y no el resto?
La opción que contiene **OR '1' = '1'** es el ejemplo perfecto de ataque de inyección SQL porque busca forzar a la base de datos a retornar un valor verdadero sin importar qué contraseña se escriba, otorgando acceso no autorizado a las cuentas. Las opciones de *DELETE* y *DROP TABLE* son comandos legítimos y completos de administración de bases de datos que no muestran la manipulación de una cadena de entrada de una aplicación. La última opción es una consulta de verificación estándar sin alteración maliciosa.

### 3. Clave para el Examen SY0-701
Aprenda a identificar firmas de texto de inyección SQL clásicas en los registros (logs) del examen. Las comillas simples sueltas ('), los guiones dobles de comentarios (--) y las condiciones OR 1=1 son indicadores definitivos de SQLi.

---

## Pregunta 11: Anatomía de un Ataque Cross-Site Scripting (XSS)

### English Version
Which of the answers listed below describe the characteristics of a cross-site scripting attack? (Select 3 answers)
* [✅] **Exploits the trust a user's web browser has in a website**
* [✅] **A malicious script is injected into a trusted website**
* [✅] **User's browser executes attacker's script**
* [ ] Exploits the trust a website has in the user's web browser  
* [ ] A user is tricked by an attacker into submitting unauthorized web requests  
* [ ] Website executes attacker's requests  

### Versión en Español
¿Cuáles de las respuestas enumeradas a continuación describen las características de un ataque de cross-site scripting (XSS)? (Seleccione 3 respuestas)  
* [✅] **Explota la confianza que el navegador web de un usuario tiene en un sitio web.**
* [✅] **Se inyecta un script malicioso en un sitio web de confianza.**
* [✅] **El navegador del usuario ejecuta el script del atacante.**
* [ ] Explota la confianza que un sitio web tiene en el navegador web del usuario.
* [ ] Un atacante engaña a un usuario para que envíe solicitudes web no autorizadas.
* [ ] El sitio web ejecuta las solicitudes del atacante.

### 1. Explicación General
El ataque XSS (Secuestro de Sitios Cruzados) consiste en incrustar código de scripting (generalmente JavaScript) dentro de las páginas web que ven otros usuarios, con el fin de que sus navegadores locales ejecuten dicho código bajo el contexto de seguridad de la sesión legítima del sitio.

### 2. ¿Por qué es la correcta y no el resto?
Las tres opciones marcadas con [✅] definen la anatomía exacta de XSS: el script malicioso se aloja o refleja en la web de confianza, el navegador confía en ese sitio y descarga el script, y finalmente la máquina de la víctima ejecuta las instrucciones (robando cookies de sesión). Las opciones descartadas describen el flujo opuesto y corresponden en realidad a la definición técnica de un ataque de Falsificación de Solicitud en Sitios Cruzados (CSRF).

### 3. Clave para el Examen SY0-701
Recuerde la diferencia clave de objetivos: XSS inyecta código que corre en el navegador del usuario víctima, mientras que CSRF aprovecha la sesión abierta del usuario para forzar el envío de comandos no deseados directamente hacia el servidor web.

---

## Pregunta 12: Definición de Fin de Vida Útil (EOL)

### English Version
Which of the terms listed below refers to a situation in which a product or service may no longer receive security patches or other updates, making it more vulnerable to attack?
* [✅] **EOL**
* [ ] ALM
* [ ] EOS
* [ ] SDLC

### Versión en Español
¿Cuál delos términos enumerados a continuación se refiere a una situación en la que un producto o servicio ya no recibe parches de seguridad u otras actualizaciones, haciéndolo más vulnerable a ataques?
* [✅] **EOL**
* [ ] ALM
* [ ] EOS
* [ ] SDLC

### 1. Explicación General
El ciclo de vida comercial de un componente de hardware o software tiene un hito en el cual el fabricante cesa todo esfuerzo técnico de mantenimiento, suspendiendo la creación de soluciones ante fallas de seguridad emergentes.

### 2. ¿Por qué es la correcta y no el resto?
**EOL (End of Life - Fin de la Vida Útil)** es el estándar de la industria que marca el cese formal de parches de seguridad. *ALM* es la Gestión del Ciclo de Vida de las Aplicaciones (un marco organizativo general). *EOS (End of Sale)* indica que un producto deja de venderse al público, pero puede seguir recibiendo parches de soporte por un tiempo determinado. *SDLC* es el Ciclo de Vida de Desarrollo de Software.

### 3. Clave para el Examen SY0-701
Operar activos en estado EOL aumenta drásticamente el riesgo empresarial. Si un sistema operativo es marcado como EOL, los atacantes buscarán exploits conocidos públicamente con la certeza de que no habrá parches para frenar la intrusión.

---

## Pregunta 13: Vulnerabilidad Crítica del Hardware Heredado (Legacy)

### English Version
What is the main vulnerability related to legacy hardware?
* [ ] Compatibility issues
* [✅] **Lack of security updates and patches**
* [ ] Worn-out physical components
* [ ] Lack of skilled personnel to run it and maintain it

### Versión en Español
¿Cuál es la principal vulnerabilidad relacionada con el hardware heredado (Legacy)?
* [ ] Problemas de compatibilidad
* [✅] **Falta de actualizaciones de seguridad y parches**
* [ ] Componentes físicos desgastados
* [ ] Falta de personal calificado para ejecutarlo y mantenerlo

### 1. Explicación General
El hardware heredado (Legacy) continúa realizando funciones operativas críticas en muchas empresas, pero al no tener soporte activo del proveedor, su firmware se vuelve inmune a las correcciones de vulnerabilidades modernas.

### 2. ¿Por qué es la correcta y no el resto?
La **Falta de actualizaciones de seguridad y parches** es la respuesta correcta desde la perspectiva de ciberseguridad, ya que describe la vulnerabilidad lógica que deja al hardware expuesto a exploits permanentes. Los *problemas de compatibilidad*, los *componentes físicos desgastados* y la *falta de personal* son problemas operativos, de ingeniería de hardware o de recursos humanos, no la debilidad de seguridad primaria que explotan los atacantes de red.

### 3. Clave para el Examen SY0-701
Cuando una corporación está obligada a mantener hardware Legacy por razones de producción y no puede actualizarlo, la contramedida mandatoria del examen es implementar Segmentación de Red estricta para aislar dichos dispositivos de internet.

---

## Pregunta 14: Mecánica de Escape de Máquina Virtual (VM Escape)

### English Version
The term "VM escape" refers to the process of breaking out of the boundaries of a guest operating system installation to access the primary hypervisor controlling all the virtual machines on the host machine.  
* [✅] **True**
* [ ] False

### Versión en Español
El término "VM escape" (escape de máquina virtual) se refiere al proceso de romper los límites de la instalación de un sistema operativo invitado para acceder al hipervisor principal que controla todas las máquinas virtuales en la máquina host.
* [✅] **Verdadero**
* [ ] Falso

### 1. Explicación General
El aislamiento es el pilar de la virtualización. Si un atacante alojado dentro de una máquina virtual invitada (guest) logra explotar una falla en el software de virtualización para interactuar directamente con el hipervisor base del host, rompe este aislamiento por completo.

### 2. ¿Por qué es la correcta y no el resto?
Es **Verdadero** porque define con precisión técnica el ataque de escape de máquina virtual. Lograr esto otorga al atacante el control potencial sobre el resto de las máquinas virtuales vecinas que comparten el mismo hardware físico. Marcar "Falso" ignoraría uno de los riesgos de infraestructura virtual y nube más críticos de la industria.

### 3. Clave para el Examen SY0-701
El VM Escape representa la vulnerabilidad más severa en entornos de nube e infraestructura virtualizada, ya que compromete la confidencialidad e integridad multi-inquilino (multi-tenancy).

---

## Pregunta 15: Riesgo de Reutilización de Recursos en Virtualización

### English Version
Which of the following answers refers to a virtualization-related vulnerability where virtualized assets allocated to one VM are improperly isolated and can be accessed or compromised by another VM?
* [✅] **Resource reuse**
* [ ] Privilege escalation
* [ ] Resource exhaustion
* [ ] Concurrent session usage

### Versión en Español
¿Cuál de las siguientes respuestas se refiere a una vulnerabilidad relacionada con la virtualización en la que los activos virtualizados asignados a una VM no están aislados adecuadamente y pueden ser accedidos o comprometidos por otra VM?
* [✅] **Reutilización de recursos (Resource reuse)**
* [ ] Escalada de privilegios (Privilege escalation)
* [ ] Agotamiento de recursos (Resource exhaustion)
* [ ] Uso de sesiones concurrentes (Concurrent session usage)

### 1. Explicación General
Cuando el hipervisor reasigna bloques de memoria caché, almacenamiento o ciclos de CPU que fueron utilizados por una máquina virtual a una máquina virtual distinta sin haber limpiado o sanitizado previamente los remanentes de datos binarios, expone información residual confidencial.

### 2. ¿Por qué es la correcta y no el resto?
**Reutilización de recursos** es el término técnico formal para este fallo de limpieza de memoria en la virtualización. La *escalada de privilegios* es ganar accesos superiores en el sistema pero no describe el traspaso de datos entre VMs por falta de sanitización. El *agotamiento de recursos* es un ataque de denegación de servicio (DoS) por consumo masivo de hardware. El *uso de sesiones concurrentes* es una métrica de acceso de usuarios.

### 3. Clave para el Examen SY0-701
El riesgo de Resource Reuse se mitiga asegurando que el hipervisor aplique políticas estrictas de borrado seguro y sobreescritura de los bloques de memoria física antes de asignarlos a un entorno virtual diferente.

---

## Pregunta 16: Vulnerabilidades Comunes de la Infraestructura Cloud

### English Version
Which of the answers listed below refers to a cloud-related vulnerability type?
* [ ] Insecure APIs
* [ ] Poor access controls
* [ ] Lack of security updates
* [ ] Misconfigured cloud storage
* [ ] Shadow IT / Malicious insiders
* [✅] **All of the above**

### Versión en Español
¿Cuál de las respuestas enumeradas a continuación se refiere a un tipo de vulnerabilidad relacionada con la nube?
* [ ] APIs inseguras
* [ ] Controles de acceso deficientes
* [ ] Falta de actualizaciones de seguridad
* [ ] Almacenamiento en la nube mal configurado
* [ ] Shadow IT / Insiders maliciosos
* [✅] **Todo lo anterior**

### 1. Explicación General
Las implementaciones en la nube (IaaS, PaaS, SaaS) introducen vectores de riesgo específicos vinculados a la automatización, la exposición pública perimetral de interfaces y la responsabilidad compartida de las configuraciones lógicas.

### 2. ¿Por qué es la correcta y no el resto?
**Todo lo anterior** es la opción correcta porque todas las respuestas describen fallas nativas de la nube: las APIs controlan la nube y si son inseguras exponen los datos; los accesos deficientes rompen el principio de mínimo privilegio; el almacenamiento mal configurado (como cubos S3 abiertos públicamente) causa fugas de información masivas; y el Shadow IT implica que los empleados desplieguen servicios en la nube sin la autorización del departamento de seguridad.

### 3. Clave para el Examen SY0-701
En entornos de nube, el eslabón más débil no suele ser el proveedor (AWS, Azure, GCP), sino los errores de malas configuraciones (Misconfigurations) realizados por los propios clientes al desplegar los recursos.

---

## Pregunta 17: Instalación de Software por Carga Lateral (Sideloading)

### English Version
The practice of installing mobile apps from websites and app stores other than the official marketplaces is referred to as:
* [ ] Jailbreaking
* [ ] Rooting
* [✅] **Sideloading**
* [ ] Carrier unlocking

### Versión en Español
La práctica de instalar aplicaciones móviles desde sitios web y tiendas de aplicaciones distintas a los mercados oficiales se conoce como:
* [ ] Jailbreaking
* [ ] Rooting
* [✅] **Carga lateral (Sideloading)**
* [ ] Desbloqueo de operador (Carrier unlocking)

### 1. Explicación General
Los sistemas operativos móviles modernos restringen de manera nativa la instalación de software a sus tiendas oficiales para garantizar que el código pase por un proceso previo de revisión y firma de seguridad. Romper este flujo controlado introduce software sin verificar.

### 2. ¿Por qué es la correcta y no el resto?
**Carga lateral (Sideloading)** es la respuesta correcta porque define específicamente la acción de descargar e instalar paquetes de aplicaciones (.apk o .ipa) desde fuentes externas ajenas al control oficial del ecosistema. *Jailbreaking* y *Rooting* implican la modificación del sistema operativo para obtener privilegios administrativos, mas no son el nombre del acto de instalar el software externo. *Desbloqueo de operador* desvincula el modem celular del dispositivo de una telefónica específica.

### 3. Clave para el Examen SY0-701
El Sideloading representa un riesgo severo de infección por malware debido a que las aplicaciones obtenidas en repositorios de terceros carecen de los controles de seguridad y escaneos de vulnerabilidades automatizados de las tiendas oficiales.

---

## Pregunta 18: Modificaciones de Seguridad en Dispositivos Apple (Jailbreaking)

### English Version
Which of the following terms is used to describe the process of removing software restrictions imposed by Apple on its iOS operating system?
* [ ] Sideloading
* [ ] Rooting
* [✅] **Jailbreaking**
* [ ] Carrier unlocking

### Versión en Español
¿Cuál de los siguientes términos se utiliza para describir el proceso de eliminar las restricciones de software impuestas por Apple en su sistema operativo iOS?
* [ ] Carga lateral (Sideloading)
* [ ] Rooting
* [✅] **Jailbreaking**
* [ ] Desbloqueo de operador (Carrier unlocking)

### 1. Explicación General
El jailbreaking es un proceso de escalada de privilegios diseñado específicamente para dispositivos de la manzana que ejecutan iOS. Su objetivo principal es eludir los controles de seguridad del fabricante (como el entorno de aislamiento de aplicaciones o *sandbox* y la verificación de firmas de código) para permitir la personalización profunda del sistema y la instalación de software no autorizado.

### 2. ¿Por qué es la correcta y no el resto?
**Jailbreaking** es la respuesta correcta debido a que es el término técnico y comercial exclusivo para la plataforma iOS de Apple. *Rooting* se descarta por estar estrictamente ligado a dispositivos basados en Android. *Sideloading* es el acto de instalar apps de fuentes externas (lo cual se facilita enormemente tras hacer jailbreak, pero no es el proceso de liberación del sistema operativo). *Desbloqueo de operador* solo elimina las trabas de red de telefonía celular para usar cualquier tarjeta SIM.

### 3. Clave para el Examen SY0-701
Un dispositivo que ha pasado por el proceso de jailbreaking pierde su modelo de seguridad por defecto, dejando expuesta la información corporativa en tránsito y en reposo. Para mitigar este riesgo, las políticas corporativas deben exigir el bloqueo de estos terminales mediante herramientas de MDM/UEM.

---

## Pregunta 19: Modificaciones de Seguridad en Dispositivos Android (Rooting)

### English Version
The term "Rooting" refers to the capability of gaining administrative access to the operating system and system applications on:
* [✅] **Android devices**
* [ ] iOS devices
* [ ] Microsoft devices
* [ ] All types of mobile devices

### Versión en Español
El término "Rooting" se refiere a la capacidad de obtener acceso administrativo al sistema operativo y a las aplicaciones del sistema en:
* [✅] **Dispositivos Android**
* [ ] Dispositivos iOS
* [ ] Dispositivos Microsoft
* [ ] Todo tipo de dispositivos móviles

### 1. Explicación General
El sistema operativo Android está construido sobre la arquitectura de un kernel de Linux. En la terminología nativa de Linux, el superusuario o administrador que posee el control absoluto de todo el sistema de archivos y las configuraciones de raíz del entorno se conoce formalmente como "root".

### 2. ¿Por qué es la correcta y no el resto?
**Dispositivos Android** es la opción correcta porque el concepto de "Rooting" deriva directamente de la obtención de privilegios de este usuario root de Linux/Android. *Dispositivos iOS* se descarta porque su proceso análogo se conoce estrictamente como Jailbreaking. *Dispositivos Microsoft* y *Todo tipo de dispositivos móviles* se descartan debido a la imprecisión técnica respecto a la plataforma origen de donde nace este vocablo informático.

### 3. Clave para el Examen SY0-701
A nivel organizativo, el Rooting compromete severamente la postura de seguridad de la empresa. Permite que aplicaciones potencialmente maliciosas alteren archivos críticos de sistema que normalmente estarían fuertemente protegidos en modo de solo lectura.

---

## Pregunta 20: Explotación de Amenazas Desconocidas (Zero-Day)

### English Version
A type of attack aimed at exploiting vulnerability that is present in already released software but unknown to the software developer is known as:
* [ ] On-path attack
* [ ] IV attack
* [✅] **Zero-day attack**
* [ ] Replay attack

### Versión en Español
Un tipo de ataque destinado a explotar una vulnerabilidad que está presente en el software ya lanzado pero que el desarrollador del software desconoce se conoce como:
* [ ] Ataque en ruta (On-path attack)
* [ ] Ataque IV (IV attack)
* [✅] **Ataque de día cero (Zero-day attack)**
* [ ] Ataque de repetición (Replay attack)

### 1. Explicación General
Las fallas de seguridad del software que son descubiertas y explotadas por actores maliciosos antes de que el fabricante del producto tenga conocimiento de su existencia (y, por lo tanto, antes de que pueda desarrollar y publicar un parche de mitigación) representan riesgos críticos de intrusión.

### 2. ¿Por qué es la correcta y no el resto?
**Ataque de día cero (Zero-day)** es el concepto exacto que define una brecha explotada donde el desarrollador tiene "cero días" de ventaja para combatirla mediante parches oficiales. *Ataque en ruta* es una amenaza de interceptación e interrupción de red (Man-in-the-Middle). *Ataque IV* explota debilidades en los vectores de inicialización de cifrados inalámbricos antiguos como WEP. *Ataque de repetición* reenvía capturas de datos válidas previas para evadir una autenticación de red legítima.

### 3. Clave para el Examen SY0-701
Dado que no existen parches disponibles para detener una amenaza de tipo Zero-day, la estrategia de defensa requerida por el examen se basa en el despliegue de soluciones de análisis de comportamiento y heurística a través de sistemas EDR/NDR para detectar las anomalías de explotación en tiempo real.

---

[[ExamCompass - Cuestionarios por Temas|⬅️ Volver a Cuestionarios por Temas]]