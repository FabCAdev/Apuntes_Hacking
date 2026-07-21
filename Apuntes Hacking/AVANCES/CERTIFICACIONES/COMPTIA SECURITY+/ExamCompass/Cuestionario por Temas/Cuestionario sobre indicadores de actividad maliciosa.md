---
tags:
  - "formato/apunte"
  - "analisis/forense"
  - "examen/test-especifico"
  - "gestion/estado/terminado"
---
Este apunte contiene el análisis detallado del sexto bloque del cuestionario temático sobre análisis forense, indicadores de compromiso y detección de anomalías en logs de la plataforma ExamCompass para la certificación CompTIA Security+ (SY0-701), alineado con las respuestas oficiales del simulador.

---

## Pregunta 1: Evidencia Forense e Indicadores de Compromiso (IoC)

### English Version
A type of forensic evidence that can be used to detect unauthorized access attempts or other malicious activities is called:
* [ ] CVE
* [✅] **IoC**
* [ ] AIS
* [ ] OSINT

### Versión en Español
Un tipo de evidencia forense que puede utilizarse para detectar intentos de acceso no autorizado u otras actividades maliciosas se denomina:
* [ ] CVE
* [✅] **IoC (Indicador de Compromiso)**
* [ ] AIS
* [ ] OSINT

### 1. Explicación General
Un IoC (*Indicator of Compromise* / Indicador de Compromiso) es cualquier rastro o evidencia digital residual en una red o sistema operativo que sugiere, con un alto nivel de confianza, que se ha producido una intrusión o una actividad maliciosa. Ejemplos de IoC incluyen firmas de archivos conocidos (hashes MD5/SHA256 de malware), direcciones IP sospechosas, URLs de servidores de comando y control (C2) o entradas de registro de Windows alteradas.

### 2. ¿Por qué es la correcta y no el resto?
**IoC** es el término forense exacto para "pistas o evidencias de intrusión". *CVE (Common Vulnerabilities and Exposures)* es un catálogo público de vulnerabilidades de software conocidas. *AIS (Automated Indicator Sharing)* es una tecnología que sirve para compartir estos indicadores rápidamente entre organizaciones de forma automatizada. *OSINT (Open Source Intelligence)* es la metodología de recolectar datos de fuentes de acceso público para ciberinteligencia.

### 3. Clave para el Examen SY0-701
Para el examen, piensa en los IoCs como "la escena del crimen digital". Si un analista de seguridad de un SOC encuentra un hash de archivo malicioso en un servidor, ese hash es un IoC que sirve para buscar otras máquinas comprometidas dentro de la infraestructura.

---

## Pregunta 2: Interpretación de Bloqueos de Cuenta

### English Version
What type of malicious activity could an account lockout indicate?
* [ ] Attempting to deliver malicious content
* [ ] DoS attack
* [ ] Account compromise
* [✅] **Password brute-force attempt**

### Versión en Español
¿Qué tipo de actividad maliciosa podría indicar el bloqueo de una cuenta?
* [ ] Intentar entregar contenido malicioso
* [ ] Ataque DoS
* [ ] Compromiso de cuenta
* [✅] **Intento de fuerza bruta de contraseña**

### 1. Explicación General
Las políticas de bloqueo de cuenta (*Account Lockout Policies*) son medidas de seguridad pasivas en los sistemas operativos y servicios de identidad (como Active Directory). Bloquean temporalmente una cuenta de usuario tras un número predeterminado de intentos fallidos de inicio de sesión (por ejemplo, 3 o 5 intentos).

### 2. ¿Por qué es la correcta y no el resto?
Un aumento repentino en los eventos de bloqueo de cuentas de usuarios es un indicador clásico de que un atacante (o un script automatizado) está ejecutando un ataque de fuerza bruta o de adivinación de contraseñas contra el portal de login. No indica compromiso de cuenta, ya que el hecho de que esté bloqueada significa que el atacante precisamente falló en entrar y el sistema lo contuvo de manera preventiva.

### 3. Clave para el Examen SY0-701
En Security+, la política de *Account Lockout* es un control de seguridad preventivo que frena los ataques de adivinación de contraseñas de manera eficiente, pero a su vez puede ser explotada de forma maliciosa para causar una denegación de servicio (DoS) a los usuarios legítimos al bloquearles sus cuentas de trabajo a propósito.

---

## Pregunta 3: Control de Accesos Simultáneos (Concurrent Sessions)

### English Version
Which of the terms listed below most accurately describes a situation where a single account is used from multiple locations/devices at the same time?
* [ ] Spraying attack
* [✅] **Concurrent session usage**
* [ ] Single Sign-On (SSO)
* [ ] Impossible travel

### Versión en Español
¿Cuál de los términos que se enumeran a continuación describe con mayor precisión una situación en la que se utiliza una sola cuenta desde múltiples ubicaciones/dispositivos al mismo tiempo?
* [ ] Ataque de rociado (Spraying attack)
* [✅] **Uso de sesiones concurrentes (Concurrent session usage)**
* [ ] Inicio de sesión único (SSO)
* [ ] Viaje imposible (Impossible travel)

### 1. Explicación General
Las sesiones concurrentes ocurren cuando una misma credencial o identidad mantiene conexiones activas simultáneamente desde diferentes terminales o direcciones IP de manera paralela.

### 2. ¿Por qué es la correcta y no el resto?
**Uso de sesiones concurrentes** describe de forma directa y literal el evento de accesos paralelos. Se diferencia de *Viaje imposible* en que este último se enfoca en la velocidad del cambio de posición física en un marco temporal (pueden ser sesiones consecutivas pero demasiado rápidas), mientras que las sesiones concurrentes son estrictamente simultáneas (mismo segundo, dos lugares).

### 3. Clave para el Examen SY0-701
Para mitigar este riesgo de uso compartido de credenciales o secuestro de sesión, los administradores de seguridad deben aplicar límites estrictos de sesiones concurrentes en las políticas de seguridad (por ejemplo, restringir el acceso a una sola sesión activa por usuario).

---

## Pregunta 4: Mitigación Perimetral y Contenido Bloqueado

### English Version
Which of the following terms refers to an indicator of malicious activity in a situation where a firewall or other security measure prevents an attempt to deliver a malicious payload or perform an unauthorized action?
* [ ] DoS attack
* [ ] Resource inaccessibility
* [✅] **Blocked content**
* [ ] Excessive consumption of system resources

### Versión en Español
¿Cuál de los siguientes términos se refiere a un indicador de actividad maliciosa en una situación en la que un cortafuegos u otra medida de seguridad impide un intento de entregar una carga útil maliciosa o realizar una acción no autorizada?
* [ ] Ataque DoS
* [ ] Inaccesibilidad de los recursos
* [✅] **Contenido bloqueado (Blocked content)**
* [ ] Consumo excesivo de recursos del sistema

### 1. Explicación General
Cuando un sistema de seguridad como un firewall de red, un filtro de correo electrónico o un proxy web intercepta y detiene de forma activa tráfico dañino (como un correo con malware o una petición SQL Injection), registra ese evento en sus logs bajo la categoría de Contenido bloqueado (*Blocked content*).

### 2. ¿Por qué falló tu respuesta?
Elegiste *Consumo excesivo de recursos del sistema*. El consumo excesivo de CPU o RAM ocurre típicamente durante ataques volumétricos, DoS, minería de criptomonedas no autorizada o desbordamientos de búfer. No describe la acción específica de un control defensivo de red (como un cortafuegos) interceptando y previniendo la entrega de malware o solicitudes sospechosas antes de que afecten al sistema interno; esa métrica de bloqueo preventivo se denomina simplemente **Contenido bloqueado**.

### 3. Clave para el Examen SY0-701
Para el examen, si los logs de seguridad muestran picos masivos de *Blocked Content*, el analista del SOC sabe que la red está siendo escaneada o atacada activamente, pero que los controles defensivos perimetrales (firewall, IPS) están haciendo su trabajo y neutralizando las amenazas antes de que penetren en la intranet.

---

## Pregunta 5: Detección Geoespacial: Viaje Imposible

### English Version
Which of the terms listed below most accurately describes a situation where an account is accessed from a location where it is physically impossible for the user to be?
* [ ] Login time restrictions
* [✅] **Impossible travel**
* [ ] Concurrent session usage
* [ ] Out-of-cycle logging

### Versión en Español
¿Cuál de los términos que se enumeran a continuación describe con mayor precisión una situación en la que se accede a una cuenta desde una ubicación en la que es físicamente imposible que el usuario se encuentre?
* [ ] Restricciones de tiempo de inicio de sesión
* [✅] **Viaje imposible (Impossible travel)**
* [ ] Uso de sesiones concurrentes
* [ ] Registro fuera de ciclo

### 1. Explicación General
El viaje imposible (*Impossible travel*) es una alerta de correlación geoespacial basada en el tiempo. Si un usuario inicia sesión en su oficina en la Ciudad de México a las 9:00 AM y luego inicia otra sesión desde París a las 9:15 AM, la distancia geográfica entre ambos puntos es imposible de recorrer en ese periodo temporal.

### 2. ¿Por qué es la correcta y no el resto?
**Viaje imposible** es el término estándar de la industria (utilizado por herramientas de monitoreo como Microsoft Defender for Cloud Apps o SIEMs) para esta anomalía matemática de tiempo y espacio.

### 3. Clave para el Examen SY0-701
Esta alerta suele indicar que la contraseña del usuario ha sido robada y un atacante extranjero está usando sus credenciales, o que el usuario legítimo está utilizando una Red Privada Virtual (VPN) con un servidor de salida en el extranjero.

---

## Pregunta 6: Telemetría y Registro Fuera de Ciclo

### English Version
The term "out-of-cycle logging" refers to cases where systems or applications generate logs outside of their regular intervals or in abnormal volumes, which could indicate malicious activity.
* [✅] **True**
* [ ] False

### Versión en Español
El término "registro fuera de ciclo" (out-of-cycle logging) se refiere a los casos en que los sistemas o las aplicaciones generan registros fuera de sus intervalos regulares o en volúmenes anormales, lo que podría indicar actividad maliciosa.
* [✅] **Verdadero**
* [ ] Falso

### 1. Explicación General
La mayoría de los sistemas operativos, servicios empresariales e infraestructura de red generan bitácoras de logs con un ritmo periódico predecible (línea base). Un cambio dramático en la frecuencia de estos eventos indica una anomalía de comportamiento.

### 2. ¿Por qué es la correcta y no el resto?
Es **Verdadero** porque define con precisión el comportamiento inusual de telemetría. Un pico masivo o el reporte de logs en horas de la madrugada (fuera de la ventana operativa normal) puede indicar que un script automatizado está escaneando la red o exfiltrando bases de datos.

### 3. Clave para el Examen SY0-701
Los sistemas SIEM modernos utilizan el análisis de comportamiento de usuarios y entidades (UEBA) para detectar automáticamente estas desviaciones de "fuera de ciclo" comparando los flujos de logs activos contra el comportamiento histórico habitual de la organización.

---

## Pregunta 7: Técnicas de Evasión: Registros Faltantes (Missing Logs)

### English Version
Which of the following would indicate an attempt to hide evidence of malicious activity?
* [ ] Account lockout
* [ ] Resource inaccessibility
* [✅] **Missing logs**
* [ ] Concurrent session usage

### Versión en Español
¿Cuál de las siguientes opciones indicaría un intento de ocultar pruebas de actividad maliciosa?
* [ ] Bloqueo de cuenta
* [ ] Inaccesibilidad de los recursos
* [✅] **Registros faltantes (Missing logs)**
* [ ] Uso de sesiones concurrentes

### 1. Explicación General
Una vez que los atacantes comprometen un sistema de forma exitosa, una de sus prioridades principales es la fase de Borrado de Huellas (*Clearing tracks*). Para ello, intentan apagar los servicios de auditoría del sistema operativo o eliminar directamente los archivos de logs que registraron sus comandos y accesos ilegítimos.

### 2. ¿Por qué es la correcta y no el resto?
Los **Registros faltantes** (o huecos temporales inexplicables en los logs) son una señal de alerta de que alguien con altos privilegios los modificó o borró a propósito para encubrir sus pasos. Ninguno de los otros conceptos se asocia a la destrucción intencionada de evidencias de auditoría.

### 3. Clave para el Examen SY0-701
Para mitigar e identificar inmediatamente los registros faltantes, las empresas deben configurar sus sistemas para enviar y duplicar sus logs en tiempo real hacia un servidor centralizado de recolección de logs inaccesible para los atacantes (ej. syslog server o SIEM con almacenamiento WORM - *Write Once, Read Many*).

---

[[ExamCompass - Cuestionarios por Temas|⬅️ Volver a Cuestionarios por Temas]]