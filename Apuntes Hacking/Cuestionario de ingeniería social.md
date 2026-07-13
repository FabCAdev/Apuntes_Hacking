---
tags:
  - "formato/apunte"
  - "hacking/fundamental"
  - "examen/test-especifico"
  - "gestion/estado/terminado"
---
Este apunte contiene el análisis detallado del cuestionario temático sobre ingeniería social de la plataforma ExamCompass para la certificación CompTIA Security+ (SY0-701), alineado con las respuestas oficiales del simulador.

---

## Pregunta 1: Definición General de Phishing

### English Version
A social engineering technique whereby attackers, under the guise of a legitimate request, attempt to gain access to confidential information is commonly known as:
* [✅] **Phishing**
* [ ] Smishing
* [ ] Pharming
* [ ] Impersonation

### Versión en Español
Una técnica de ingeniería social mediante la cual los atacantes, bajo el disfraz de una solicitud legítima, intentan obtener acceso a información confidencial se conoce comúnmente como:
* [✅] **Suplantación de identidad (Phishing)**
* [ ] Smishing
* [ ] Farmacia (Pharming)
* [ ] Suplantación de identidad (Impersonation)

### 1. Explicación General
El phishing es el término raíz y la técnica general de ingeniería social que utiliza la comunicación digital fraudulenta, simulando una entidad de total confianza, con el fin de manipular al receptor para que entregue credenciales, datos financieros o ejecute código dañino.

### 2. ¿Por qué es la correcta y no el resto?
**Phishing** es correcta por ser la categoría general solicitada en la definición. *Smishing* se descarta porque se limita estrictamente a la mensajería de texto celular (SMS). *Farmacia (Pharming)* se descarta porque no es una solicitud directa al usuario, sino una manipulación técnica subyacente de la resolución de nombres (DNS o archivos hosts) para redirigir tráfico web. *Suplantación de identidad (Impersonation)* suele referirse a un rol adoptado en interacciones directas o físicas, no a la mecánica general de la solicitud fraudulenta digital.

### 3. Clave para el Examen SY0-701
Cuando el escenario del examen describa un ataque masivo basado en un engaño digital fraudulento que busca capturar información confidencial simulando legitimidad, la respuesta por defecto es Phishing.

---

## Pregunta 2: Ingeniería Social por Canales de Voz (Vishing)

### English Version
The practice of using a telephone system to manipulate the user into disclosing confidential information is known as:
* [ ] Whaling
* [ ] Spear phishing
* [✅] **Vishing**
* [ ] Pharming

### Versión en Español
La práctica de utilizar un sistema telefónico para manipular al usuario y lograr que revele información confidencial se conoce como:
* [ ] Ballenero (Whaling)
* [ ] Suplantación de identidad dirigida (Spear phishing)
* [✅] **Vishing**
* [ ] Farmacia (Pharming)

### 1. Explicación General
Los ataques de ingeniería social se ramifican y nombran según el canal de transmisión física o técnica empleado. Cuando el canal es la voz interactiva, la industria aplica una nomenclatura específica.

### 2. ¿Por qué es la correcta y no el resto?
**Vishing (Voice Phishing)** es la única opción correcta porque utiliza llamadas telefónicas (tradicionales o VoIP) para ejecutar el engaño de viva voz. *Whaling* se descarta porque se dirige de forma exclusiva a altos ejecutivos corporativos (CEOs, CFOs) mediante correos sofisticados. *Spear phishing* se enfoca de forma personalizada en un individuo o grupo pequeño, normalmente por escrito. *Pharming* se descarta por completo al ser un ataque a la resolución de direcciones de red.

### 3. Clave para el Examen SY0-701
Cualquier escenario donde el atacante interactúe mediante la voz, use sistemas automáticos de respuesta interactiva (IVR) falsos o llame directamente a un centro de soporte (*Help Desk*) simula ser un ataque de Vishing.

---

## Pregunta 3: Ataques Basados en Mensajería de Texto (Smishing)

### English Version
Which of the following answers refers to a social engineering attack that exploits SMS or text messages to trick recipients into taking harmful actions?
* [ ] Pharming
* [ ] Phishing
* [ ] Quishing
* [✅] **Smishing**

### Versión en Español
¿Cuál de las siguientes respuestas se refiere a un ataque de ingeniería social que explota los mensajes SMS o de texto para engañar a los destinatarios y lograr que realicen acciones perjudiciales?
* [ ] Farmacia (Pharming)
* [ ] Suplantación de identidad (Phishing)
* [ ] Quishing
* [✅] **Smishing**

### 1. Explicación General
Los dispositivos móviles han fragmentado las vías de acceso de ingeniería social, forzando la creación de términos específicos para cada protocolo de mensajería del terminal.

### 2. ¿Por qué es la correcta y no el resto?
**Smishing** es la opción correcta porque combina las siglas de *SMS (Short Message Service)* con *Phishing*. *Phishing* se descarta por ser el concepto madre general, no el específico para mensajes de texto. *Quishing* se descarta porque es un ataque que utiliza códigos QR fraudulentos impresos o digitales. *Pharming* se descarta por ser una manipulación del enrutamiento web.

### 3. Clave para el Examen SY0-701
Si la pregunta del examen especifica explícitamente el uso de SMS, alertas de texto celular o enlaces enviados al teléfono móvil por mensajería de texto, la respuesta mandatoria es Smishing.

---

## Pregunta 4: Definición de Información Falsa Involuntaria

### English Version
Which of the terms listed below refers to false or misleading information that is spread unintentionally?
* [ ] Astroturfing
* [ ] Misinformation
* [ ] Psychological manipulation
* [✅] **Disinformation** *(Nota: Evaluado bajo las restricciones y la plantilla del test de origen)*

### Versión en Español
¿Cuál de los términos que se enumeran a continuación se refiere a información falsa o engañosa que se difunde involuntariamente?
* [ ] Césped artificial (Astroturfing)
* [ ] Desinformación *(Evaluado como incorrecto en el test tradicional, pero marcado como sistema correcto/omisión en esta plantilla)*
* [ ] Manipulación psicológica
* [✅] **Desinformación**

### 1. Explicación General
Existe una delgada línea técnica en la doctrina de seguridad y operaciones de información entre la falsedad propagada con conocimiento del daño y aquella compartida por error o desconocimiento de su falta de veracidad.

### 2. ¿Por qué es la correcta y no el resto?
En el estándar estricto de la lengua inglesa, *Misinformation* es involuntaria y *Disinformation* es deliberada. Sin embargo, en diversas traducciones de exámenes técnicos, la diferenciación puede tornarse ambigua o cruzada según la plantilla de evaluación del simulador de origen. *Astroturfing* se descarta porque es la creación de una falsa impresión de apoyo popular espontáneo a una campaña. *Manipulación psicológica* es el proceso general, no la información en sí misma.

### 3. Clave para el Examen SY0-701
En las preguntas sobre operaciones de influencia (*Influence Campaigns*), se debe diferenciar el vector de la intención. Si el objetivo es desestabilizar mediante datos falsos creados a propósito, la respuesta técnica estándar apunta a campañas de Desinformación.

---

## Pregunta 5: Información Falsa Deliberada (Disinformation)

### English Version
Which of the following terms best describes deliberately false or misleading information that is spread with the intent to deceive or manipulate?
* [✅] **Disinformation**
* [ ] Hoax
* [ ] Psychological manipulation
* [ ] Manipulation

### Versión en Español
¿Cuál de los siguientes términos describe mejor la información deliberadamente falsa o engañosa que se difunde con la intención de engañar o manipular?
* [✅] **Desinformación**
* [ ] Engaño (Hoax)
* [ ] Manipulación psicológica
* [ ] Manipulación

### 1. Explicación General
Las campañas de influencia modernas emplean la inyección maliciosa de datos fabricados en los canales de comunicación de una empresa o sociedad para alterar la toma de decisiones y generar caos operativo o reputacional.

### 2. ¿Por qué es la correcta y no el resto?
**Desinformación (Disinformation)** es la respuesta correcta porque el enunciado estipula la presencia de un elemento crítico: la intención deliberada de engañar. Un *Engaño (Hoax)* suele ser una falsedad aislada (como una falsa alerta de virus); la *Manipulación psicológica* y la *Manipulación* general son metodologías de persuasión, no la clasificación formal de los datos falsos propagados.

### 3. Clave para el Examen SY0-701
Cuando CompTIA introduce escenarios de ataques a la reputación corporativa o alteración de elecciones y decisiones mediante noticias falsas estructuradas intencionalmente por actores estatales o competidores, el término correcto es Desinformación.

---

## Pregunta 6: Ataques Basados en el Fraude de Identidad

### English Version
Which type of social engineering attack relies on identity fraud?
* [ ] Pretexting
* [ ] Spear phishing
* [ ] Tailgating
* [✅] **Impersonation**

### Versión en Español
¿Qué tipo de ataque de ingeniería social se basa en el fraude de identidad?
* [ ] Pretextos (Pretexting)
* [ ] Phishing selectivo (Spear phishing)
* [ ] Seguir de cerca (Tailgating)
* [✅] **Suplantación de identidad (Impersonation)**

### 1. Explicación General
La adopción de un rol falso o de una identidad legítima que no pertenece al atacante es la base para romper las barreras de desconfianza naturales del personal de una organización.

### 2. ¿Por qué es la correcta y no el resto?
**Suplantación de identidad (Impersonation)** es correcta porque define el acto puro de pretender ser otra persona específica (un inspector de incendios, un auditor, un técnico de soporte). *Pretexting* se descarta porque es la creación de la historia o el escenario de fondo, no el fraude de identidad en sí mismo. *Spear phishing* es un método de entrega digital por correo, y *Tailgating* es un ataque físico de acceso sin autorización.

### 3. Clave para el Examen SY0-701
La *Suplantación de identidad (Impersonation)* en el examen suele presentarse en interacciones directas donde el atacante asume una posición de autoridad para intimidar al empleado de menor rango y forzar el salto de los protocolos de verificación.

---

## Pregunta 7: Clasificación de Ataques BEC (Business Email Compromise)

### English Version
A BEC (Business Email Compromise) attack is an example of:
* [ ] Smishing
* [✅] **Phishing**
* [ ] Vishing
* [ ] Pharming

### Versión en Español
Un ataque BEC es un ejemplo de:
* [ ] Smishing
* [✅] **Suplantación de identidad (Phishing)**
* [ ] Vishing
* [ ] Farmacia (Pharming)

### 1. Explicación General
El fraude de Compromiso de Correo Electrónico Corporativo (BEC) consiste en interceptar o suplantar cuentas de correo electrónico de ejecutivos o proveedores legítimos para desviar transferencias monetarias o solicitar pagos fraudulentos.

### 2. ¿Por qué es la correcta y no el resto?
Es un tipo especializado de **Phishing** porque el vehículo exclusivo de ejecución e ingeniería social es el correo electrónico. Se descartan *Smishing* (SMS), *Vishing* (Llamada de voz) y *Pharming* (Enrutamiento web fraudulento) debido a que ninguno de estos canales aloja la naturaleza técnica original de un ataque BEC.

### 3. Clave para el Examen SY0-701
El ataque BEC es altamente peligroso porque muchas veces no contiene enlaces maliciosos ni malware; se fundamenta puramente en texto con ingeniería social financiera sofisticada enviado desde dominios suplantados (*spoofed*) o cuentas comprometidas legítimas.

---

## Pregunta 8: Creación de Escenarios Ficticios (Pretexting)

### English Version
Which of the answers below refers to a social engineering technique where an attacker creates a fictitious scenario or situation to trick the victim into revealing confidential information?
* [ ] Role playing
* [ ] Credential harvesting
* [✅] **Pretexting**
* [ ] Watering hole attack

### Versión en Español
¿Cuál de las respuestas que aparecen a continuación se refiere a una técnica de ingeniería social en la que un atacante crea un escenario o situación ficticia para engañar a la víctima y lograr que revele información confidencial?
* [ ] Interpretación (Role playing)
* [ ] Recopilación de credenciales (Credential harvesting)
* [✅] **Pretexto (Pretexting)**
* [ ] Ataque al abrevadero (Watering hole)

### 1. Explicación General
Para que un engaño sea exitoso, los ingenieros sociales construyen arquitecturas narrativas que otorguen credibilidad y contexto lógico a las peticiones inusuales que realizan a las víctimas.

### 2. ¿Por qué es la correcta y no el resto?
**Pretexto (Pretexting)** es el término formal para el diseño y ejecución de la historia ficticia de fondo. *Interpretación* es un método de entrenamiento, no un ataque. *Recopilación de credenciales* es el objetivo técnico final de muchos ataques, no la creación del escenario. El *Ataque al abrevadero* es una técnica pasiva de compromiso de sitios web específicos frecuentados por los objetivos.

### 3. Clave para el Examen SY0-701
Si la pregunta enfatiza que el atacante hizo una investigación previa para armar una historia elaborada, un guion o una situación ficticia creíble antes de pedir los datos, la respuesta correcta es Pretexting.

---

## Pregunta 9: Plataformas Utilizadas en Ataques Watering Hole

### English Version
Which of the following terms refers to a common platform for watering hole attacks?
* [ ] Mail gateways
* [✅] **Websites**
* [ ] PBX systems
* [ ] Web browsers

### Versión en Español
¿Cuál delos siguientes términos se refiere a una plataforma común para ataques de tipo "watering hole"?
* [ ] Pasarelas de correo (Mail gateways)
* [¼] **Sitios web**
* [ ] Sistemas PBX
* [ ] Navegadores web

### 1. Explicación General
El ataque de abrevadero (*Watering Hole*) imita la estrategia de los depredadores en la naturaleza: en lugar de buscar a la presa individualmente, infectan el lugar exacto al que el grupo objetivo acude con regularidad por necesidad o interés común.

### 2. ¿Por qué es la correcta y no el resto?
Los **Sitios web** constituyen el activo infectado donde el atacante aloja el exploit de descarga automática. Las *Pasarelas de correo* procesan mensajes entrantes/salientes, no albergan abrevaderos. Los *Sistemas PBX* controlan telefonía de voz. Los *Navegadores web* son la herramienta cliente que visita el sitio, pero la plataforma comprometida donde se monta la trampa es el sitio web en sí mismo.

### 3. Clave para el Examen SY0-701
En un ataque de *Watering Hole*, el adversario no envía correos directos al objetivo; en su lugar, compromete un sitio web de un tercero legítimo que sabe que los empleados de la organización víctima visitan con frecuencia debido a su nicho industrial.

---

## Pregunta 10: Clonación de Identidad Corporativa (Brand Spoofing)

### English Version
A fake website that mimics a legitimate online retailer, designed to steal user login credentials, is an example of:
* [ ] Malicious software
* [✅] **Brand spoofing**
* [ ] Identity fraud
* [ ] Watering hole attack

### Versión en Español
Un sitio web falso que imita a un minorista en línea legítimo, diseñado para robar las credenciales de inicio de sesión del usuario, es un ejemplo de:
* [ ] Software malicioso (Malware)
* [✅] **Suplantación de marca (Brand spoofing)**
* [ ] Fraude de identidad (Identity fraud)
* [ ] Ataque al abrevadero (Watering hole)

### 1. Explicación General
La explotación visual de logotipos, tipografías y la identidad corporativa de marcas reconocidas globalmente busca neutralizar el estado de alerta defensivo de los consumidores en internet.

### 2. ¿Por qué es la correcta y no el resto?
**Suplantación de marca (Brand spoofing)** es el término de diseño exacto para la clonación visual de la identidad de un negocio o corporativo con fines maliciosos. El *Fraude de identidad* suele asociarse con robar y usar los datos de una persona real. El *Software malicioso* requiere la inyección de binarios de código, mientras que aquí se trata de un sitio web estático clonado. El *Ataque al abrevadero* no busca imitar una marca comercial para el público general, sino infectar un sitio específico para un grupo cerrado.

### 3. Clave para el Examen SY0-701
El uso ilegal de logotipos, colores corporativos y marcas de empresas masivas (como bancos, pasarelas de pago o minoristas) para crear portales falsos de autenticación se denomina conceptualmente Brand Spoofing.

---

## Pregunta 11: Secuestro de URL mediante Errores de Escritura (Typosquatting)

### English Version
Typosquatting involves registering domain names with slight misspellings of popular sites to exploit user typographical errors, host phishing sites, or distribute malware.
* [✅] **True**
* [ ] False

### Versión en Español
El término "typosquatting" se refiere a una práctica engañosa que consiste en el registro deliberado de nombres de dominio con errores ortográficos o ligeras variaciones que se asemejan mucho a nombres de dominio populares...
* [✅] **Verdadero**
* [ ] Falso

### 1. Explicación General
El error humano al teclear rápidamente una dirección en la barra URL de un navegador es una vulnerabilidad conductual que los atacantes monetizan comprando dominios parecidos.

### 2. ¿Por qué es la correcta y no el resto?
Es **Verdadero** debido a que la descripción del enunciado define de manera exacta todas las ramificaciones operativas del typosquatting: captura de tráfico residual, redirección publicitaria engañosa, alojamiento de páginas espejo para robo de credenciales o descarga automática de malware. Indicar "Falso" contradice la definición técnica internacional del término.

### 3. Clave para el Examen SY0-701
Si el escenario describe que un usuario escribió accidentalmente `goolge.com` o `microsoft-security.com` en lugar del dominio real y cayó en un portal de fraude, la técnica aplicada por el atacante se cataloga como Typosquatting (también denominado secuestro de URL).

---

## Pregunta 12: Indicadores de Compromiso en Correos Electrónicos

### English Version
In email communication, which signs can help recognize a phishing attempt?
* [ ] Message contains spelling/grammar errors
* [ ] Message requests personal information
* [ ] Message includes a call to action with urgency
* [ ] Message includes suspicious links/attachments
* [✅] **Any of the above**

### Versión en Español
En la comunicación por correo electrónico, ¿qué señales pueden ayudar a reconocer un intento de phishing?
* [ ] El mensaje contiene errores ortográficos y gramaticales.
* [ ] El mensaje solicita información personal.
* [ ] El mensaje incluye un llamado a la acción con un sentido de urgencia.
* [ ] El mensaje incluye enlaces o archivos adjuntos sospechosos.
* [✅] **Cualquiera de las anteriores**

### 1. Explicación General
Los correos de phishing masivos exhiben múltiples indicadores de compromiso lógicos y conductuales debido a su necesidad de forzar acciones rápidas en la víctima antes de que intervengan los controles técnicos.

### 2. ¿Por qué es la correcta y no el resto?
**Cualquiera de las anteriores** es la respuesta correcta porque el phishing es multifacético. Un solo correo fraudulento puede manifestar uno, varios o todos estos indicadores de manera simultánea para presionar psicológicamente al usuario (urgencia) o explotar su sistema (adjuntos). Marcar una sola opción descartaría los otros vectores válidos de detección.

### 3. Clave para el Examen SY0-701
Los tres pilares clásicos para detectar phishing en escenarios de examen son: sentido de urgencia artificial, solicitud inusual de credenciales/datos y direcciones URL que no coinciden exactamente con el dominio legítimo de la organización remitente.

---

## Pregunta 13: Protocolo del Usuario Final ante Phishing

### English Version
What would be an appropriate user response to an email phishing attempt? (Select all that apply)
* [✅] **Do not reply to the message or provide personal info**
* [✅] **Report the message to the IT/Security department**
* [✅] **Delete the message from the inbox**
* [✅] **Do not click on links or download attachments**
* [ ] Forward the message to the sender to verify legitimacy
* [ ] Open the attachment in a sandbox environment to test

### Versión en Español
¿Cuál sería una respuesta apropiada de un usuario ante un intento de phishing por correo electrónico? (Seleccione todas las opciones que correspondan)
* [✅] **No responder al mensaje ni proporcionar ninguna información personal.**
* [✅] **Informar del mensaje al departamento de TI o de seguridad, si procede.**
* [✅] **Eliminar el mensaje de la bandeja de entrada.**
* [✅] **No hacer clic en ningún enlace ni descargar ningún archivo adjunto en el mensaje.**
* [ ] Reenviar el mensaje al remitente para verificar su legitimidad.
* [ ] Abrir el archivo adjunto en un entorno de pruebas para comprobar su seguridad.

### 1. Explicación General
El manejo seguro de incidentes sospechosos por parte de los usuarios finales mitiga la propagación interna de amenazas y alimenta los sistemas de inteligencia defensiva de la organización.

### 2. ¿Por qué es la correcta y no el resto?
Las cuatro opciones marcadas con [✓] componen el protocolo estándar de contención pasiva y reporte. Las dos opciones finales se descartan rotundamente: *Reenviar al remitente original* es inútil y valida que la cuenta del usuario está activa frente al atacante; e *instruir a un usuario final a abrir código en una sandbox* viola las políticas de seguridad corporativas, ya que las tareas de análisis técnico pertenecen de forma exclusiva a los analistas del SOC o ingenieros de seguridad.

### 3. Clave para el Examen SY0-701
Ante la detección de un correo sospechoso en la estación de trabajo, la acción prioritaria recomendada por CompTIA es el aislamiento del correo (no interactuar) junto con el reporte inmediato al canal oficial de seguridad (ej. botón de reporte de phishing o mesa de ayuda).

---

## Pregunta 14: La Mitigación Principal frente a la Ingeniería Social

### English Version
What is the best countermeasure against social engineering attacks?
* [ ] Situational awareness
* [ ] Implicit deny policy
* [✅] **User education**
* [ ] Strong security controls

### Versión en Español
¿Cuál es la mejor contramedida contra los ataques de ingeniería social?
* [ ] Conciencia situacional
* [ ] Política de denegación implícita
* [✅] **Educación del usuario**
* [ ] Fuertes controles de seguridad

### 1. Explicación General
Dado que la ingeniería social no ataca principalmente el código o el hardware, sino las debilidades cognitivas, sesgos de confianza y vulnerabilidades psicológicas humanas, el parche de seguridad debe aplicarse sobre el propio comportamiento de las personas.

### 2. ¿Por qué es la correcta y no el resto?
**Educación del usuario** (programas continuos de concientización y entrenamiento en seguridad) es la contramedida más efectiva porque dota al personal de la capacidad crítica para identificar y rechazar los engaños. Las políticas de denegación implícita y los fuertes controles de seguridad técnicos (como firewalls o MFA) son indispensables para la defensa en profundidad, pero no impiden que un humano engañado tome el teléfono o valide un acceso de forma manual. La conciencia situacional es el estado mental deseado, pero se alcanza precisamente a través de la educación formal.

### 3. Clave para el Examen SY0-701
El ser humano es catalogado como el "eslabón más débil" de la cadena de custodia de la información. Por tanto, para mitigar riesgos de ingeniería social, la respuesta correcta del examen siempre orbitará en torno a **Security Awareness Training** (Capacitación en Concienciación de Seguridad).

---

[[ExamCompass - Cuestionarios por Temas|⬅️ Volver a Cuestionarios por Temas]]