---
tags:
  - "formato/apunte"
  - "hacking/fundamental"
  - "examen/test-especifico"
  - "gestion/estado/terminado"
---
# 🛡️ Cuestionario sobre Controles de Seguridad (ExamCompass)

Este apunte contiene el análisis detallado del cuestionario temático sobre controles de seguridad de la plataforma ExamCompass para la certificación CompTIA Security+ (SY0-701), alineado con las respuestas oficiales del simulador.

---

## Pregunta 1: Características de los Controles Técnicos

### English Version
Which of the following answers can be used to describe technical security controls? (Select 3 answers)
* [ ] Focused on protecting material assets
* [✅] **Sometimes called logical security controls**
* [✅] **Executed by computer systems (instead of people)**
* [ ] Also known as administrative controls
* [✅] **Implemented with technology**
* [ ] Primarily implemented and executed by people (as opposed to computer systems)

### Versión en Español
¿Cuál de las siguientes respuestas se puede utilizar para describir los controles de seguridad técnicos? (Seleccione 3 respuestas)
* [ ] Centrados en la protección de activos materiales
* [✅] **A veces llamados controles de seguridad lógicos**
* [✅] **Ejecutados por sistemas informáticos (en lugar de personas)**
* [ ] También conocidos como controles administrativos
* [✅] **Implementados con tecnología**
* [ ] Principalmente implementados y ejecutados por personas (a diferencia de los sistemas informáticos)

### 1. Explicación General
Los controles técnicos son las salvaguardas y mecanismos de protección que se ejecutan directamente dentro de los sistemas informáticos a través de hardware, software o firmware. Su función principal es aplicar reglas lógicas automatizadas para restringir accesos, proteger datos y monitorear amenazas sin depender de la intervención humana directa en cada evento.

### 2. ¿Por qué es la correcta y no el resto?
* **Opciones Correctas:** `[Sometimes called logical security controls / Executed by computer systems / Implemented with technology]` definen la naturaleza del control: requiere tecnología para existir, es sinónimo de control "lógico" en seguridad informática y la ejecución de la regla corre a cargo de la CPU y los sistemas informáticos, no de un operario humano.
* **Análisis de los distractores:**
    * *Focused on protecting material assets:* Esto describe a los controles físicos.
    * *Also known as administrative controls:* Es falso, ya que corresponden a los controles gerenciales.
    * *Primarily implemented and executed by people:* Esto describe a los controles operacionales.

### 3. Clave para el Examen SY0-701
Se debe recordar la igualdad conceptual para el examen: Technical = Logical. Cada vez que el control involucre configuraciones de software, sistemas operativos o reglas automáticas de red, la categoría obligatoria es técnica.

---

## Pregunta 2: Ejemplos de Controles Técnicos

### English Version
Which of the answers listed below refer to examples of technical security controls? (Select 3 answers)
* [ ] Security audits
* [✅] **Encryption**
* [ ] Organizational security policy
* [✅] **IDSs**
* [ ] Configuration management
* [✅] **Firewalls**

### Versión en Español
¿Cuáles de las respuestas enumeradas a continuación se referieren a ejemplos de controles de seguridad técnicos? (Seleccione 3 respuestas)
* [ ] Auditorías de seguridad
* [✅] **Cifrado (Encryption)**
* [ ] Política de seguridad organizacional
* [✅] **IDSs (Sistemas de Detección de Intrusos)**
* [ ] Gestión de configuración
* [✅] **Firewalls (Cortafuegos)**

### 1. Explicación General
Para identificar ejemplos de controles técnicos, se deben buscar herramientas tangibles de TI que operen mediante algoritmos informáticos, software activo o inspección automatizada de datos en tránsito o en reposo.

### 2. ¿Por qué es la correcta y no el resto?
* **Opciones Correctas:** `[Encryption / IDSs / Firewalls]` aplican tecnología automatizada. El cifrado utiliza algoritmos lógicos para proteger la información; un IDS analiza paquetes de red de forma automatizada mediante firmas de software; un firewall bloquea o permite tráfico según reglas de puertos o direcciones IP.
* **Análisis de los distractores:**
    * *Security audits:* Es una revisión humana de cumplimiento (operacional o gerencial).
    * *Organizational security policy:* Es un documento escrito (gerencial).
    * *Configuration management:* Es un proceso administrativo de control de cambios.

### 3. Clave para el Examen SY0-701
Si la solución de seguridad requiere código, firmware o poder de procesamiento informático para aplicar la protección directamente en los sistemas de información, se clasifica como un ejemplo técnico.

---

## Pregunta 3: Características de los Controles Gerenciales (Managerial)

### English Version
Which of the following answers refer to the characteristic features of managerial security controls? (Select 3 answers)
* [✅] **Also known as administrative controls**
* [ ] Sometimes referred to as logical security controls
* [✅] **Focused on reducing the risk of security incidents**
* [ ] Executed by computer systems (instead of people)
* [✅] **Documented in written policies**
* [ ] Focused on protecting material assets

### Versión en Español
¿Cuál de las siguientes respuestas se refiere a las características de los controles de seguridad gerenciales? (Seleccione 3 respuestas)
* [✅] **También conocidos como controles administrativos**
* [ ] A veces denominados controles de seguridad lógicos
* [✅] **Centrados en reducir el riesgo de incidentes de seguridad**
* [ ] Ejecutados por sistemas informáticos (en lugar de personas)
* [✅] **Documentados en políticas escritas**
* [ ] Centrados en la protección de activos materiales

### 1. Explicación General
Los controles gerenciales representan la capa estratégica, de gobernanza y legal de la seguridad en una organización. Son diseñados e impuestos por la dirección corporativa para establecer la postura de riesgo global del negocio.

### 2. ¿Por qué es la correcta y no el resto?
* **Opciones Correctas:** `[Also known as administrative controls / Focused on reducing risk / Documented in written policies]` toman la batuta de la antigua denominación "administrativa", se plasman formalmente en manuales y políticas de cumplimiento obligatorio y buscan mitigar el riesgo general mediante la planeación estratégica.
* **Análisis de los distractores:**
    * *Logical security controls / Executed by computer systems:* Pertenece a la definición de controles técnicos.
    * *Focused on protecting material assets:* Pertenece a la definición de controles físicos.

### 3. Clave para el Examen SY0-701
Se debe asociar la palabra *Managerial* con la alta dirección de la empresa. Si el escenario del examen habla de presupuestos, cumplimiento legal, marcos de gobernanza (NIST, ISO) o estrategias organizacionales, se está ante un control gerencial.

---

## Pregunta 4: Ejemplos de Controles Gerenciales

### English Version
Examples of managerial security controls include: (Select 3 answers)
* [ ] Configuration management
* [ ] Data backups
* [✅] **Organizational security policy**
* [✅] **Risk assessments**
* [✅] **Security awareness training**

### Versión en Español
Los ejemplos de controles de seguridad gerenciales incluyen: (Seleccione 3 respuestas)
* [ ] Gestión de configuración
* [ ] Copias de seguridad de datos
* [✅] **Política de seguridad organizacional**
* [✅] **Evaluaciones de riesgo (Risk assessments)**
* [✅] **Capacitación en concientización sobre seguridad (Security awareness training)**

### 1. Explicación General
Son los instrumentos, metodologías e iniciativas globales dictadas por los líderes de la empresa para educar a la organización completa, documentar las reglas operativas y cuantificar el impacto de las amenazas.

### 2. ¿Por qué es la correcta y no el resto?
* **Opciones Correctas:** `[Organizational security policy / Risk assessments / Security awareness training]` representan directrices humanas y organizacionales. Las políticas dictan la ley interna de la empresa; las evaluaciones calculan el impacto del riesgo; el entrenamiento de concientización es un programa corporativo dirigido al factor humano.
* **Análisis de los distractores:**
    * *Configuration management & Data backups:* Son tareas técnicas prácticas ejecutadas de forma rutinaria por el área de sistemas.

### 3. Clave para el Examen SY0-701
Se debe tener cuidado con el entrenamiento de usuarios (*Security awareness training*). Aunque los usuarios realizan la acción práctica de estudiar, el programa corporativo se considera un control *Managerial* debido a que proviene de una decisión e iniciativa puramente administrativa de la dirección.

---

## Pregunta 5: Características de los Controles Operacionales

### English Version
Which of the answers listed below can be used to describe operational security controls (Select 3 answers)
* [ ] Also known as administrative controls
* [✅] **Focused on the day-to-day procedures of an organization**
* [ ] Executed by computer systems (instead of people)
* [✅] **Used to ensure that the equipment continues to work as specified**
* [ ] Focused on managing risk
* [✅] **Primarily implemented and executed by people (as opposed to computer systems)**

### Versión en Español
¿Cuáles de las respuestas enumeradas a continuación se pueden utilizar para describir los controles de seguridad operacionales? (Seleccione 3 respuestas)
* [ ] También conocidos como controles administrativos
* [✅] **Centrados en los procedimientos diarios de una organización**
* [ ] Ejecutados por sistemas informáticos (en lugar de personas)
* [✅] **Utilizados para garantizar que el equipo siga funcionando según lo especificado**
* [ ] Centrados en la gestión del riesgo
* [✅] **Implementados y ejecutados principalmente por personas (a diferencia de los sistemas informáticos)**

### 1. Explicación General
Los controles operacionales son aquellos procedimientos prácticos y manuales que las personas ejecutan regularmente para mantener la infraestructura tecnológica estable, segura y operativa. A diferencia de las políticas estratégicas o los sistemas automáticos, la seguridad operacional recae directamente sobre las tareas físicas y lógicas del personal de TI.

### 2. ¿Por qué es la correcta y no el resto?
* **Opciones Correctas:** `[Focused on day-to-day / Ensure equipment works as specified / Executed by people]` se basan en rutinas diarias, aseguran que los servidores y equipos mantengan su estado de operación óptimo conforme a los manuales, y su ejecución depende completamente de la acción manual o supervisión de un humano en lugar de un software aislado.
* **Análisis de los distractores:**
    * *Administrative controls:* Es sinónimo de controles gerenciales.
    * *Executed by computer systems:* Esto define a un control técnico.
    * *Focused on managing risk:* Es el enfoque macro y estratégico de la categoría gerencial.

### 3. Clave para el Examen SY0-701
La frase insignia en esta sección es *"Day-to-day"* (Día a día) combinado con la intervención de personas. Si el control describe a un administrador siguiendo un manual de mantenimiento o ejecutando tareas recurrentes de soporte técnico, se clasifica como operacional.

---

## Pregunta 6: Ejemplos de Controles Operacionales

### English Version
Which of the following examples fall into the category of operational security controls? (Select 3 answers)
* [ ] Risk assessments
* [✅] **Configuration management**
* [✅] **System backups**
* [ ] Authentication protocols
* [✅] **Patch management**

### Versión en Español
¿Cuáles de los siguientes ejemplos entran en la categoría de controles de seguridad operacionales? (Seleccione 3 respuestas)
* [ ] Evaluaciones de riesgo
* [✅] **Gestión de configuración (Configuration management)**
* [✅] **Respaldos de sistema (System backups)**
* [ ] Protocolos de autenticación
* [✅] **Gestión de parches (Patch management)**

### 1. Explicación General
Estos ejemplos engloban las actividades de mantenimiento higiénico de TI. No son simples líneas de código autónomas, sino flujos de trabajo programados e implementados por los administradores de sistemas para garantizar la integridad operativa.

### 2. ¿Por qué es la correcta y no el resto?
* **Opciones Correctas:** `[Configuration management / System backups / Patch management]` configuran el proceso estructurado de actualizar sistemas (parches), verificar que la información se guarde con éxito (backups) y mantener el inventario de configuraciones sin variaciones no autorizadas.
* **Análisis de los distractores:**
    * *Risk assessments:* Control netamente gerencial.
    * *Authentication protocols:* Es código informático automatizado, por lo tanto, técnico.

### 3. Clave para el Examen SY0-701
Para CompTIA, los procesos repetitivos de administración como *Patch Management* y *Backups* se clasifican primordialmente como *Operational* porque requieren gobernanza humana diaria para verificar que los planes se cumplan en la realidad.

---

## Pregunta 7: Definición de Controles Físicos

### English Version
Which of the answers listed below refers to security controls designed to deter, detect, and prevent unauthorized access, theft, damage, or destruction of material assets?
* [ ] Managerial security controls
* [✅] **Physical security controls**
* [ ] Technical security controls
* [ ] Operational security controls

### Versión en Español
¿Cuál de las respuestas enumeradas a continuación se refiere a los controles de seguridad diseñados para disuadir, detectar y prevenir el acceso no autorizado, robo, daño o destrucción de activos materiales?
* [ ] Controles de seguridad gerenciales
* [✅] **Controles de seguridad físicos**
* [ ] Controles de seguridad técnicos
* [ ] Controles de seguridad operacionales

### 1. Explicación General
Los controles físicos representan todas las barreras tangibles instaladas en el mundo real tridimensional para resguardar la infraestructura, los edificios y el hardware contra accesos indebidos o desastres.

### 2. ¿Por qué es la correcta y no el resto?
* **Opción Correcta:** `[Physical security controls]` responde directamente a la definición del resguardo de *"material assets"* (activos materiales). Los controles físicos son los únicos capaces de evitar que una persona toque, robe o destruya físicamente un equipo informático.
* **Análisis de los distractores:** Las categorías gerenciales, técnicas y operacionales operan a nivel lógico, documental o de flujos de procesos cibernéticos, no sobre elementos tridimensionales.

### 3. Clave para el Examen SY0-701
Si la medida de seguridad se puede ver y tocar físicamente en las instalaciones de la empresa, su categoría por excelencia es física.

---

## Pregunta 8: Lo que NO es un Control Físico

### English Version
Which of the following examples do not fall into the category of physical security controls? (Select 3 answers)
* [ ] Lighting
* [ ] Access control vestibules
* [✅] **Data backups**
* [ ] Fencing/Bollards/Barricades
* [✅] **Firewalls**
* [ ] Security guards
* [✅] **Asset management**

### Versión en Español
¿Cuáles de los siguientes ejemplos no entran en la categoría de controles de seguridad físicos? (Seleccione 3 respuestas)
* [ ] Iluminación (Lighting)
* [ ] Esclusas de acceso (Access control vestibules)
* [✅] **Copias de seguridad de datos (Data backups)**
* [ ] Cercas/Bolardos/Barricadas
* [✅] **Firewalls (Cortafuegos)**
* [ ] Guardias de seguridad
* [✅] **Gestión de activos (Asset management)**

### 1. Explicación General
Aquí se solicita separar los mecanismos lógicos y de procesos de aquellos elementos físicos instalados en el perímetro o dentro de los edificios de la corporación.

### 2. ¿Por qué es la correcta y no el resto?
* **Opciones Correctas:** `[Data backups / Firewalls / Asset management]` operan fuera de la barrera perimetral tangible. Los respaldos y firewalls viven en la capa lógica/técnica de los sistemas de TI, mientras que el control de inventario de activos es un proceso procedimental (operacional).
* **Análisis de los distractores:** La iluminación, exclusas (*access control vestibules*), cercas y guardias son objetos y personas físicas ubicadas en el entorno tangible.

### 3. Clave para el Examen SY0-701
Se debe aprender a reconocer el término *Access control vestibules* (las denominadas esclusas de doble puerta). Es una respuesta recurrente de CompTIA para denotar una contramedida física contra la intrusión perimetral.

---

## Pregunta 9: Ejemplos de Controles Preventivos

### English Version
What are the examples of preventive security controls? (Select 3 answers)
* [✅] **Encryption**
* [ ] IDS
* [ ] Sensors
* [✅] **Firewalls**
* [ ] Warning signs
* [✅] **AV software**

### Versión en Español
¿Cuáles son los ejemplos de controles de seguridad preventivos? (Seleccione 3 respuestas)
* [✅] **Cifrado (Encryption)**
* [ ] IDS (Sistema de detección de intrusos)
* [ ] Sensores
* [✅] **Firewalls (Cortafuegos)**
* [ ] Señales de advertencia (Warning signs)
* [✅] **AV software (Software Antivirus)**

### 1. Explicación General
En este apartado se evalúa la funcionalidad o tipo de objetivo del control. Los controles preventivos están diseñados para impedir activamente que un incidente de seguridad llegue a ocurrir, bloqueando la amenaza antes de que logre impactar o dañar los activos.

### 2. ¿Por qué es la correcta y no el resto?
* **Opciones Correctas:** `[Encryption / Firewalls / AV software]` detienen la amenaza antes del impacto. El cifrado previene la fuga de información si los datos son interceptados de manera ilegítima; el firewall bloquea proactivamente puertos maliciosos no deseados; el antivirus frena y elimina malware antes de su ejecución destructiva.
* **Análisis de los distractores:**
    * *IDS & Sensors:* Reaccionan identificando el problema una vez iniciado, por lo que son detectivos.
    * *Warning signs:* Buscan desanimar al atacante únicamente a nivel psicológico (disuasorios).

### 3. Clave para el Examen SY0-701
Si la herramienta tiene la capacidad técnica de denegar el acceso o neutralizar por completo el peligro antes de que se consume la brecha, su función es *Preventive*.

---

## Pregunta 10: Ejemplos de Controles Disuasorios (Deterrent)

### English Version
Examples of deterrent security controls include: (Select 3 answers)
* [✅] **Warning signs**
* [ ] Sensors
* [✅] **Lighting**
* [ ] Video surveillance
* [ ] Security audits
* [✅] **Fencing/Bollards**

### Versión en Español
Los ejemplos de controles de seguridad disuasorios incluyen: (Seleccione 3 respuestas)
* [✅] **Señales de advertencia (Warning signs)**
* [ ] Sensores
* [ ] Videovigilancia (CCTV)
* [✅] **Iluminación (Lighting)**
* [ ] Auditorías de seguridad
* [✅] **Cercas/Bolardos (Fencing/Bollards)**

### 1. Explicación General
Un control disuasorio busca desalentar o desanimar psicológicamente a un posible atacante, enviando una señal clara de que el entorno está protegido o monitoreado para que desista de su intento.

### 2. ¿Por qué es la correcta y no el resto?
* **Opciones Correctas:** `[Warning signs / Lighting / Fencing/Bollards]` actúan de forma disuasoria. Las advertencias legales intimidan; una iluminación intensa disuade a delincuentes que buscan el amparo de la oscuridad; las cercas y bolardos imponen una barrera visible que comunica dificultad de acceso.
* **Análisis de los distractores:**
    * *Sensors:* Son de tipo detectivo.
    * *Video surveillance:* Aunque tiene un efecto disuasivo visual secundario, su función principal para la lógica de CompTIA es grabar y auditar, clasificándose como detectivo.
    * *Security audits:* Es una revisión operativa de cumplimiento.

### 3. Clave para el Examen SY0-701
Los elementos de seguridad perimetral exterior visibles suelen agruparse bajo la función *Deterrent* en el simulador porque actúan como la primera línea psicológica de defensa ante intrusos.

---

## Pregunta 11: Controles Detectivos (Detective)

### English Version
Which of the answers listed below refer(s) to detective security control(s)? (Select all that apply)
* [ ] Lighting
* [✅] **Log monitoring**
* [ ] Sandboxing
* [✅] **Security audits**
* [✅] **CCTV**
* [✅] **IDS**
* [✅] **Vulnerability scanning**

### Versión en Español
¿Cuáles de las respuestas enumeradas a continuación se refieren a controles de seguridad detectivos? (Seleccione todo lo que corresponda)
* [ ] Iluminación (Lighting)
* [✅] **Monitoreo de registros (Log monitoring)**
* [ ] Sandboxing
* [✅] **Auditorías de seguridad (Security audits)**
* [✅] **CCTV (Videovigilancia)**
* [✅] **IDS (Sistema de detección de intrusos)**
* [✅] **Escaneo de vulnerabilidades (Vulnerability scanning)**

### 1. Explicación General
Los controles detectivos están diseñados para descubrir, alertar o documentar actividades maliciosas, fallas o configuraciones erróneas durante su ejecución o inmediatamente después de que sucedieron. Su labor es traer visibilidad y encender alarmas.

### 2. ¿Por qué es la correcta y no el resto?
* **Opciones Correctas:** `[Todas las opciones marcadas con ✅]` se orientan a la identificación. El monitoreo de logs detecta actividad inusual; las auditorías de seguridad descubren brechas de cumplimiento técnico u operativo; el CCTV registra visualmente intrusiones; el IDS levanta banderas ante firmas maliciosas de red; el escáner detecta vulnerabilidades activas expuestas.
* **Análisis de los distractores:**
    * *Lighting:* Control estrictamente disuasorio.
    * *Sandboxing:* Es un aislamiento técnico enfocado en prevención y análisis.

### 3. Clave para el Examen SY0-701
No se debe olvidar que las auditorías (*Security audits*) y los escaneos de vulnerabilidades entran en esta categoría porque su función es "encontrar" lo que está mal en el sistema. *Detection* equivale a identificar el problema.

---

## Pregunta 12: Controles Correctivos (Corrective)

### English Version
Which of the following answers refer(s) to corrective security control(s)? (Select all that apply)
* [✅] **Recovering data from backup copies**
* [✅] **Applying software updates and patches to fix vulnerabilities**
* [✅] **Developing and implementing IRPs to respond to and recover from security incidents**
* [ ] Regularly reviewing logs for anomalies or patterns indicative of attacks
* [✅] **Activating and executing DRPs to restore operations after a major incident**

### Versión en Español
¿Cuáles de las siguientes respuestas se refieren a controles de seguridad correctivos? (Seleccione todo lo que corresponda)
* [✅] **Recuperación de datos a partir de copias de seguridad**
* [✅] **Aplicar actualizaciones de software y parches para corregir vulnerabilidades**
* [✅] **Desarrollar e implementar IRPs (Planes de Respuesta a Incidentes) para responder y recuperarse de incidentes de seguridad**
* [ ] Revisar periódicamente los registros en busca de anomalías o patrones indicativos de ataques
* [✅] **Activar y ejecutar DRPs (Planes de Recuperación ante Desastres) para restaurar operaciones después de un incidente mayor**

### 1. Explicación General
Los controles correctivos se activan después de que un ataque o falla vulneró las defensas de la organización. Tienen como meta mitigar el impacto negativo, reparar la infraestructura afectada y devolver el negocio a su estado operativo seguro habitual.

### 2. ¿Por qué es la correcta y no el resto?
* **Opciones Correctas:** `[Recovering from backups / Applying patches / IRPs / DRPs]` corrigen el impacto de la brecha. Restaurar respaldos recupera la información perdida; parchar remedia la vulnerabilidad explotada; los planes IRP y DRP guían las actividades obligadas para mitigar daños y levantar servicios caídos.
* **Análisis de los distractores:**
    * *Regularly reviewing logs:* Es una actividad continua de monitoreo y descubrimiento, por lo que es Detective.

### 3. Clave para el Examen SY0-701
Si la respuesta describe acciones orientadas a la recuperación, reparación, contención de incidentes o remediación de fallas post-brecha, la función del control es correctiva.

---

## Pregunta 13: Controles Compensatorios (Compensating)

### English Version
Which of the answers listed below refer(s) to compensating security control(s)? (Select all that apply)
* [✅] **Backup power systems**
* [ ] Video surveillance
* [✅] **MFA**
* [✅] **Application sandboxing**
* [✅] **Network segmentation**

### Versión en Español
¿Cuáles de las respuestas enumeradas a continuación se refieren a controles de seguridad compensatorios? (Seleccione todo lo que corresponda)
* [✅] **Sistemas de energía de respaldo (Backup power systems)**
* [ ] Videovigilancia (Video surveillance)
* [✅] **MFA (Autenticación de Múltiples Factores)**
* [✅] **Sandboxing de aplicaciones (Application sandboxing)**
* [✅] **Network segmentation (Segmentación de red)**

### 1. Explicación General
Un control compensatorio actúa como un Plan B o una medida alternativa cuando no es posible implementar un control de seguridad primario ideal (debido a limitaciones técnicas, costos excesivos o incompatibilidades). Su objetivo es balancear y compensar esa vulnerabilidad para que el nivel de riesgo permanezca bajo control.

### 2. ¿Por qué es la correcta y no el resto?
* **Opciones Correctas:** `[Backup power / MFA / Sandboxing / Network segmentation]` actúan como contrapesos de fallas o vulnerabilidades. Los sistemas de energía compensan la caída de la red eléctrica general. Por su parte, el MFA, Sandboxing y la Segmentación de red son recursos utilizados en el simulador para compensar debilidades severas de software heredado u obsoleto (si un servidor antiguo no se puede parchar ni actualizar, se le aísla mediante segmentación y se le exige MFA para mitigar dicho riesgo).
* **Análisis de los distractores:**
    * *Video surveillance:* Su uso nativo es registrar eventos perimetrales y es puramente detectivo; no actúa como un control compensatorio alternativo directo dentro de esta lógica de sistemas.

### 3. Clave para el Examen SY0-701
Se debe asociar Compensating = Amortiguador o Plan B. Si el examen describe un escenario donde no se puede aplicar la solución perfecta por restricciones técnicas o presupuestales, cualquier control alternativo que se agregue para cubrir el hueco se categorizará como compensatorio.

---

## Pregunta 14: Definición de Controles Directivos (Directive)

### English Version
The term "Directive security controls" refers to the category of security controls that are implemented through policies and procedures.
* [✅] **True**
* [ ] False

### Versión en Español
El término "controles de seguridad directivos" se refiere a la categoría de controles de seguridad que se implementan a través de políticas y procedimientos.
* [✅] **Verdadero**
* [ ] Falso

### 1. Explicación General
Los controles directivos tienen la función de guiar, gobernar y normar obligatoriamente la conducta de los empleados de la organización a través de mandatos oficiales, lineamientos y regulaciones internas escritas.

### 2. ¿Por qué es la correcta y no el resto?
* **Opción Correcta [Verdadero]:** Es la definición conceptual exacta. Su fuerza radica en la autoridad administrativa y legal de las políticas corporativas, obligando a los individuos a seguir un estándar específico bajo amenaza de sanciones internas.

### 3. Clave para el Examen SY0-701
Existe una diferencia sutil: los controles *Deterrent* (disuasorios) apelan al miedo psicológico del atacante externo. Los controles *Directive* (directivos) imponen mandatos de cumplimiento obligatorio a nivel normativo para el personal interno de la empresa.

---

## Pregunta 15: Ejemplos de Controles Directivos

### English Version
Which of the following terms fall into the category of directive security controls? (Select 2 answers)
* [✅] **IRP**
* [✅] **AUP**
* [ ] IDS
* [ ] MFA
* [ ] IPS

### Versión en Español
¿Cuáles de los siguientes términos entran en la categoría de controles de seguridad directivos? (Seleccione 2 respuestas)
* [✅] **IRP (Plan de Respuesta a Incidentes)**
* [✅] **AUP (Política de Uso Aceptable)**
* [ ] IDS
* [ ] MFA
* [ ] IPS

### 1. Explicación General
Los ejemplos directivos se traducen en directrices documentales rígidas que le indican detalladamente a los colaboradores de la corporación cómo deben actuar o qué límites tienen prohibido cruzar.

### 2. ¿Por qué es la correcta y no el resto?
* **Opciones Correctas:** `[IRP / AUP]` son documentos mandatorios. La AUP regula de forma contractual y punitiva el uso correcto de los equipos de la empresa por parte del personal. El IRP le impone al personal técnico el protocolo estricto e ineludible que deben ejecutar de forma obligatoria ante una brecha.
* **Análisis de los distractores:**
    * *IDS, MFA, IPS:* Son herramientas lógicas y de software automatizadas, lo que los convierte en controles puramente técnicos.

### 3. Clave para el Examen SY0-701
La AUP (*Acceptable Use Policy*) es la respuesta insignia en CompTIA cuando se requiere un ejemplo claro de control directivo. Es fundamental recordarla para escenarios de cumplimiento de empleados.

---

[[ExamCompass - Cuestionarios por Temas|⬅️ Volver a Cuestionarios por Temas]]