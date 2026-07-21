---
tags:
  - "formato/apunte"
  - "hacking/fundamental"
  - "examen/test-especifico"
  - "gestion/estado/terminado"
---
Este apunte contiene el análisis detallado del cuestionario temático sobre actores de amenazas, vectores de ataque y perfiles de riesgo de la plataforma ExamCompass para la certificación CompTIA Security+ (SY0-701), alineado con las respuestas oficiales del simulador.

---

## Pregunta 1: Matriz de Vectores de Ataque / Threat Actor Attack Vectors (Matching)

### English Version
The reader must match each type of threat actor with its corresponding common attack vector attribute (the source location from which the risk is introduced).
* Nation-state: **External**
* Script Kiddie: **Internal/External**
* Hacktivist: **External**
* Insider Threat: **Internal**
* Organized Crime: **External**
* Shadow IT: **Internal**

### Versión en Español
El lector debe relacionar cada tipo de actor de amenazas con su atributo de vector de ataque común correspondiente (ubicación de origen desde donde se introduce el riesgo).
* Estado-nación: **Externo**
* Atacante inexperto (Script Kiddie): **Interno/Externo**
* Hacktivista: **Externo**
* Amenaza interna (Insider Threat): **Interno**
* Delincuencia organizada: **Externo**
* Tecnología de la sombra (Shadow IT): **Interno**

### 1. Explicación General
El vector de ataque define el punto de origen desde el cual un actor de amenazas inicia sus actividades de riesgo con respecto al perímetro de la organización. Los actores se clasifican en externos (fuera del perímetro), internos (con acceso legítimo dentro de la red) o híbridos.

### 2. ¿Por qué es la correcta y no el resto?
* **Script Kiddie (Interno/Externo):** Es el único actor de naturaleza dual en esta matriz. La mayoría actúa de forma externa lanzando scripts automatizados desde internet, pero un estudiante dentro de una red escolar o un empleado menor en su cubículo representa un vector interno.
* **Hacktivistas, Estado-nación y Delincuencia organizada:** Carecen de credenciales o accesos autorizados, por lo que atacan obligatoriamente desde el exterior a través de redes públicas.
* **Insider Threat y Shadow IT:** El riesgo proviene de personal que ya se encuentra contratado por la organización. Aunque las herramientas de Shadow IT residan en nubes públicas, el vector es interno porque es el propio empleado quien introduce el riesgo a los activos corporativos.

### 3. Clave para el Examen SY0-701
Para el examen, el único actor que comparte de forma explícita ambas ubicaciones en la definición de vectores es el Script Kiddie (Interno/Externo). Recordar esta excepción permite descartar el resto de las opciones de forma inmediata.

---

## Pregunta 2: Matriz de Recursos y Financiación / Threat Actor Resources and Funding (Matching)

### English Version
The reader must associate each type of threat actor with its corresponding material resources and financial backing attribute.
* Nation-state: **High resources and funding**
* Script Kiddie: **Low resources and funding**
* Hacktivist: **Low-to-medium resources and funding**
* Insider Threat: **Low-to-high resources and funding**
* Organized Crime: **Medium-to-high resources and funding**
* Shadow IT: **Low-to-medium resources and funding**

### Versión en Español
El lector debe asociar cada tipo de actor de amenazas con su atributo de recursos materiales y respaldo financiero correspondiente.
* Estado-nación: **Altos recursos y financiación**
* Atacante inexperto (Script Kiddie): **Escasos recursos y financiación**
* Hacktivista: **Recursos y financiación bajos a medios**
* Amenaza interna (Insider Threat): **Recursos y financiación de bajos a altos**
* Delincuencia organizada: **Recursos y financiación de nivel medio a alto**
* Tecnología de la sombra (Shadow IT): **Recursos y financiación bajos a medios**

### 1. Explicación General
La matriz de financiamiento mide la capacidad económica que respalda las actividades de un actor. Los presupuestos determinan el alcance de la infraestructura de ataque, la adquisición de exploits comerciales y el tiempo que pueden sostener una operación.

### 2. ¿Por qué es la correcta y no el resto?
* **Nation-state (Altos):** Cuenta de forma exclusiva con el presupuesto gubernamental de un país soberano, lo que le otorga recursos masivos.
* **Script Kiddie (Escasos):** Carece de capital de inversión y depende de utilidades gratuitas disponibles en internet.
* **Insider Threat (Bajos a altos):** El rango es amplio debido a que el actor puede ser un usuario administrativo común (recursos bajos) o un directivo de TI con control total sobre presupuestos y sistemas críticos (recursos altos).
* **Organized Crime (Medio a alto):** Financian sus operaciones de manera corporativa mediante las ganancias obtenidas de extorsiones y fraudes electrónicos previos.

### 3. Clave para el Examen SY0-701
El concepto de Estado-nación es el único vinculado al término "Altos" (High) de manera exclusiva y absoluta. Ninguna corporación criminal o amenaza interna iguala el nivel presupuestal de un gobierno en los escenarios de CompTIA.

---

## Pregunta 3: Matriz de Nivel de Sofisticación Técnica / Threat Actor Sophistication Levels (Matching)

### English Version
The reader must assign the attribute of technical knowledge, programming skills, and defense evasion capabilities to each type of threat actor.
* Nation-state: **High sophistication level**
* Script Kiddie: **Low sophistication level**
* Hacktivist: **Low-to-medium sophistication level**
* Insider Threat: **Low-to-high sophistication level**
* Organized Crime: **Medium-to-high sophistication level**
* Shadow IT: **Low-to-medium sophistication level**

### Versión en Español
El lector debe asignar el atributo de nivel de conocimientos técnicos, habilidades de programación y evasión de defensas a cada tipo de actor de amenazas.
* Estado-nación: **Alto nivel de sofisticación**
* Atacante inexperto (Script Kiddie): **Bajo nivel de sofisticación**
* Hacktivista: **Nivel de sofisticación bajo a medio**
* Amenaza interna (Insider Threat): **Nivel de sofisticación de bajo a alto**
* Delincuencia organizada: **Nivel de sofisticación medio a alto**
* Tecnología de la sombra (Shadow IT): **Nivel de sofisticación bajo a medio**

### 1. Explicación General
El nivel de sofisticación técnica evalúa la capacidad de un actor para desarrollar herramientas personalizadas, descubrir fallos de día cero (Zero-days) y eludir sistemas de detección avanzados (como EDR o SIEM).

### 2. ¿Por qué es la correcta y no el resto?
* **Hacktivist y Shadow IT (Bajo a medio):** Los hacktivistas se enfocan en ataques ruidosos de denegación de servicio (DDoS) o modificaciones estéticas web (defacement) usando software público. Los usuarios de Shadow IT son empleados que despliegan servicios comerciales (SaaS) legítimos por comodidad laboral; no desarrollan malware ni vulneran defensas.
* **Insider Threat (Bajo a alto):** El rango abarca desde el extremo más bajo (un empleado que conecta un USB infectado por accidente) hasta el más alto (un ingeniero principal de infraestructura que conoce las debilidades exactas del sistema).
* **Organized Crime (Medio a alto):** Contratan a desarrolladores profesionales del mercado negro para empaquetar y modificar malware existente con el fin de evadir soluciones antivirus tradicionales.

### 3. Clave para el Examen SY0-701
En las preguntas desplegables, la descripción de sofisticación que cubre todo el espectro de Bajo a Alto (Low-to-high) le pertenece de forma única a la Amenaza interna (Insider Threat), debido a la diversidad de roles que pueden existir dentro de una plantilla laboral.

---

## Pregunta 4: Matriz de Motivaciones Típicas / Threat Actor Motivations (Matching)

### English Version
The reader must select the set of motivations and incentives driving the illicit or risky actions of each type of threat agent.
* Nation-state: **Espionage, political/philosophical beliefs, disruption/chaos, warfare**
* Script Kiddie: **Disruption/chaos, financial gain, revenge**
* Hacktivist: **Ethical beliefs, philosophical/political beliefs, disruption/chaos**
* Insider Threat: **Revenge, financial gain, service disruption**
* Organized Crime: **Financial gain, data breach, extortion**
* Shadow IT: **Convenience, lack of awareness of security risks, fulfilling specific needs**

### Versión en Español
El lector debe seleccionar el conjunto de motivaciones e incentivos que impulsan las acciones ilícitas o riesgosas de cada tipo de agente de amenaza.
* Estado-nación: **Espionaje, creencias políticas/filosóficas, perturbación/caos, guerra**
* Atacante inexperto (Script Kiddie): **Disrupción/caos, beneficio económico, venganza**
* Hacktivista: **Creencias éticas, creencias filosóficas/políticas, disrupción/caos**
* Amenaza interna (Insider Threat): **Venganza, beneficio económico, interrupción del servicio**
* Delincuencia organizada: **Beneficio económico, filtración de datos, extorsión**
* Tecnología de la sombra (Shadow IT): **Conveniencia, falta de conocimiento de los riesgos de seguridad, satisfacción de necesidades específicas**

### 1. Explicación General
La motivación identifica el "por qué" del ataque, lo que permite a los defensores anticipar cuáles activos de información serán el blanco principal del adversario.

### 2. ¿Por qué es la correcta y no el resto?
* **Shadow IT (Conveniencia):** Se diferencia drásticamente de los demás porque el usuario no tiene intenciones maliciosas contra la empresa; actúa motivado por la comodidad operativa y la agilidad para cumplir sus labores específicas.
* **Delincuencia organizada (Extorsión):** Su único motor es el financiero y el robo de datos corporativos para la posterior demanda de un rescate económico (Ransomware).
* **Insider Threat (Venganza/Saboteo):** Se asocia con empleados descontentos que buscan dañar la reputación o la continuidad del servicio de la organización como represalia.

### 3. Clave para el Examen SY0-701
Para resolver correctamente el cruce de opciones en los menús desplegables, se deben memorizar estas asociaciones directas de palabras clave: Conveniencia = Shadow IT; Extorsión = Delincuencia organizada; Venganza = Amenaza interna; Espionaje/Guerra = Estado-nación.

---

## Pregunta 5: Campañas de Ataques Prolongados / Advanced Persistent Threats

### English Version
Which of the following terms is used to describe sophisticated, prolonged cyberattacks typically conducted by highly funded and structured groups, such as nation-states?
* [ ] MitM
* [✅] **APT**
* [ ] XSRF
* [ ] DDoS

### Versión en Español
¿Cuál de los siguientes términos se utiliza para describir los ciberataques sofisticados y prolongados, a menudo llevados a cabo por grupos bien financiados y organizados, como los estados nación?
* [ ] MitM
* [✅] **APT**
* [ ] XSRF
* [ ] DDoS

### 1. Explicación General
Las Amenazas Avanzadas Persistentes (APT) son operaciones cibernéticas dirigidas y continuas. A diferencia de los ataques oportunistas, una APT busca infiltrarse silenciosamente en una red y mantener el acceso a largo plazo para recolectar información e inteligencia estratégica de forma sostenida.

### 2. ¿Por qué es la correcta y no el resto?
* **Opción Correcta:** `[APT]` debido a que cumple de manera exacta con las tres características del enunciado: Sofisticación técnica (Avanzada), permanencia en el tiempo (Persistente) y patrocinio de organizaciones de alto presupuesto como estados-nación.
* **Análisis de los distractores:**
    * *MitM (Man-in-the-Middle):* Es una técnica específica de interceptación de comunicaciones en tránsito, no un tipo de campaña militar o estatal.
    * *XSRF (Cross-Site Request Forgery):* Corresponde a una vulnerabilidad de seguridad en aplicaciones web.
    * *DDoS (Distributed Denial of Service):* Es un ataque de saturación masiva de tráfico que busca la interrupción inmediata y visible de un servicio, lo opuesto al sigilo y persistencia de una APT.

### 3. Clave para el Examen SY0-701
Cuando un escenario del examen resalte las palabras "Prolongado" (Prolonged), "Sigiloso" (Stealthy) o mencione el robo continuo de propiedad intelectual por parte de un Estado-nación, el término técnico que se debe seleccionar siempre es APT.

---

## Pregunta 6: Concepto Fundamental de TI en la Sombra / Shadow IT Definition

### English Version
In computer security, the term "Shadow IT" is used to describe the practice of using systems, software, or services within an organization without the explicit approval or oversight of the organization's IT department.
* [✅] **True**
* [ ] False

### Versión en Español
En seguridad informática, el término "TI en la sombra" se utiliza para describir la práctica de usar sistemas, software o servicios informáticos dentro de una organización sin la aprobación o supervisión explícita del departamento de TI de la organización.
* [✅] **Verdadero**
* [ ] Falso

### 1. Explicación General
Shadow IT abarca cualquier solución tecnológica (aplicaciones en la nube, dispositivos de almacenamiento, hardware) introducida en el entorno corporativo por empleados o departamentos sin el conocimiento del equipo de seguridad informática. Esta práctica genera serios problemas de cumplimiento y pérdida de control de datos.

### 2. ¿Por qué es la correcta y no el resto?
* **Opción Correcta:** `[True / Verdadero]` dado que define textualmente el principio de falta de visibilidad y control gubernamental que caracteriza al Shadow IT dentro del marco de seguridad de CompTIA.
* **Análisis del distractor:** Se descarta debido a que contradice la terminología oficial y los estándares de gestión de activos de la industria.

### 3. Clave para el Examen SY0-701
Si el escenario describe a un grupo de usuarios que decide utilizar herramientas de comunicación externas o nubes de almacenamiento personales para facilitar el intercambio de archivos de trabajo porque consideran que los sistemas oficiales de la empresa son lentos o restrictivos, se está ejemplificando un caso de Shadow IT.

---

[[ExamCompass - Cuestionarios por Temas|⬅️ Volver a Cuestionarios por Temas]]