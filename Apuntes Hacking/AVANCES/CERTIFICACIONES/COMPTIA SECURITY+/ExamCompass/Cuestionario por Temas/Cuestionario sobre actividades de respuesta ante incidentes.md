---
tags:
  - "formato/apunte"
  - "operaciones/incident-response"
  - "forense/legal"
  - "examen/test-especifico"
---
Este apunte contiene la cuarta sección del análisis de los cuestionarios temáticos de ExamCompass para la certificación CompTIA Security+ (SY0-701). Se enfoca exhaustivamente en el Ciclo de Vida de Respuesta a Incidentes (NIST SP 800-61 r2), metodologías de entrenamiento operativo (Tabletop/Simulación) y la preservación legal de evidencia digital, contrastando mis respuestas con las oficiales del simulador.

---

## Pregunta 1: Fase de Preparación (Preparation)

### English Version
Which part of the Incident Response process involves establishing and maintaining an incident response capability as well as creating an incident response team?
- [x] **Preparation**
- [ ] Detection and Analysis
- [ ] Containment, Eradication, and Recovery
- [ ] Post-Incident Activity

### Versión en Español
¿Qué parte del proceso de respuesta a incidentes implica establecer y mantener la capacidad de respuesta a incidentes, así como crear un equipo de respuesta a incidentes?
- [x] **Preparación**
- [ ] Detección y análisis
- [ ] Contención, erradicación y recuperación
- [ ] Actividad posterior al incidente

### 1. Explicación General
La fase de Preparación es la base de todo programa de respuesta ante incidentes. Antes de que ocurra una brecha de seguridad, la organización debe desarrollar políticas, directrices, flujos de comunicación y conformar equipos especializados que puedan reaccionar de manera organizada y veloz ante eventos de seguridad.

### 2. ¿Por qué es la correcta y no el resto?
- **Preparation:** Incluye la planeación técnica y administrativa proactiva (fase cero), como la creación del *Incident Response Team (IRT)* y la adquisición de herramientas de monitoreo.
- **Detección y Análisis:** Se enfoca en identificar y validar incidentes que ya están ocurriendo en tiempo real.
- **Contención, Erradicación y Recuperación:** Ocurre después de detectar y confirmar una amenaza activa.
- **Actividad Posterior al Incidente:** Se realiza una vez que el peligro ha sido neutralizado y los sistemas están estables.

### 3. Clave para el Examen SY0-701
Las 4 fases principales del NIST que CompTIA evalúa rigurosamente son: *Preparation ➡️ Detection & Analysis ➡️ Containment, Eradication & Recovery ➡️ Post-Incident Activities*. Memorizar el orden cronológico y sus hitos de ingeniería es fundamental.

---

## Pregunta 2: Fase de Detección y Análisis (Detection and Analysis)

### English Version
In the Incident Response process, the step that involves identifying and understanding potential incidents to determine their scope, impact, and root cause is part of:
- [ ] Preparation Phase
- [x] **Detection and Analysis Phase**
- [ ] Containment, Eradication, and Recovery Phase
- [ ] Post-Incident Activity Phase

### Versión en Español
En el proceso de respuesta a incidentes, el paso que implica identificar y comprender los incidentes potenciales para determinar su alcance, impacto y causa raíz forma parte de:
- [ ] Etapa de preparación
- [x] **Etapa de detección y análisis**
- [ ] Etapa de contención, erradicación y recuperación
- [ ] Etapa de actividad posterior al incidente

### 1. Explicación General
Durante esta etapa, los analistas del SOC y del equipo de respuesta a incidentes analizan alertas de seguridad, comportamientos anómalos, registros de auditoría y eventos correlacionados para clasificar si se está produciendo una brecha real o un falso positivo, determinando su gravedad inicial.

### 2. ¿Por qué es la correcta y no el resto?
- **Detection and Analysis:** Es la única fase dedicada específicamente a correlacionar alertas, analizar evidencia inicial, validar indicadores de compromiso (IoCs) y definir el impacto y alcance del ataque.
- Las demás opciones representan fases que ocurren antes del ataque (Preparación) o como respuesta operativa y de aprendizaje posterior al análisis del vector de entrada.

### 3. Clave para el Examen SY0-701
Si el escenario del examen menciona el análisis de *Logs*, validación de alertas del SIEM, inspección de *IoCs*, o la determinación del alcance del daño en caliente, la respuesta es invariablemente **Detection and Analysis**.

---

## Pregunta 3: Contención, Erradicación y Recuperación

### English Version
Which of the following refer to the Containment, Eradication, and Recovery stage of the Incident Response process? (Select all that apply)
- [x] **Restoring normal operations**
- [x] **Eliminating the threat**
- [ ] Monitoring and detecting possible incidents
- [ ] Establishing and maintaining an incident response policy
- [x] **Mitigating the impact of the incident**

### Versión en Español
¿Cuál o cuáles de las siguientes respuestas se refieren a la etapa de contención, erradicación y recuperación del proceso de respuesta ante incidentes? (Seleccione todas las que correspondan)
- [x] **Restablecimiento de las operaciones normales**
- [x] **Eliminar la amenaza**
- [ ] Monitoreo y detección de posibles incidentes
- [ ] Establecer y mantener una política de respuesta ante incidentes
- [x] **Mitigar el impacto del incidente**

### 1. Explicación General
Una vez que un incidente ha sido verificado, el equipo de seguridad debe ejecutar acciones de control activo. Esta fase representa la intervención técnica directa sobre los activos de la organización para detener los daños, limpiar los entornos e implementar la resiliencia del negocio.

### 2. ¿Por qué es la correcta y no el resto?
- **Mitigar el impacto, Eliminar la amenaza y Restablecer operaciones:** Representan de forma exacta la tríada operativa de esta fase:
    - *Contain (Contener):* Aislar sistemas para mitigar el impacto.
    - *Eradicate (Erradicar):* Eliminar el malware o credenciales del atacante.
    - *Recover (Recuperar):* Devolver los sistemas a producción de forma segura.
- Las opciones excluidas corresponden a labores de *Detection & Analysis* (Monitoreo) y *Preparation* (Establecer políticas).

### 3. Clave para el Examen SY0-701
Alineación conceptual de acciones directas:
- `Contain` ➡️ Detener la propagación (aislamiento de red).
- `Eradicate` ➡️ Remover el peligro (limpieza y parchado).
- `Recover` ➡️ Volver a la normalidad (restauración de respaldos).

---

## Pregunta 4: Actividad Posterior al Incidente (Post-Incident Activity)

### English Version
Which phase of the Incident Response process involves updating incident response plans, policies, and procedures?
- [ ] Preparation
- [ ] Detection and Analysis
- [ ] Containment, Eradication, and Recovery
- [x] **Post-Incident Activity**

### Versión en Español
¿Qué etapa del proceso de respuesta a incidentes implica la actualización de los planes, políticas y procedimientos de respuesta a incidentes?
- [ ] Preparación
- [ ] Detección y análisis
- [ ] Contención, erradicación y recuperación
- [x] **Actividad posterior al incidente**

### 1. Explicación General
Tras neutralizar con éxito un incidente y estabilizar el entorno de producción, la organización debe realizar un ejercicio introspectivo. Analizar minuciosamente la cronología de los eventos permite robustecer las defensas corporativas y optimizar el plan de respuesta para eventos futuros.

### 2. ¿Por qué es la correcta y no el resto?
- **Post-Incident Activity:** Alberga el hito conocido como **Lecciones Aprendidas (Lessons Learned)**, que exige documentar el reporte del incidente y actualizar los controles administrativos o técnicos basados en las fallas detectadas durante la crisis.
- Las fases previas están orientadas a la planificación inicial o al manejo activo de la emergencia en curso.

### 3. Clave para el Examen SY0-701
Asociación directa para el examen: `Lessons Learned / Documentar mejoras del proceso / Actualizar manuales de IR ➡️ Post-Incident Activity`.

---

## Pregunta 5: Entrenamiento Teórico (Tabletop Exercise)

### English Version
Which of the following refers to a discussion-based activity in which team members analyze different scenarios to evaluate the incident response plan without activating any systems?
- [x] **Tabletop Exercise**
- [ ] Simulation
- [ ] Threat Hunting
- [ ] Root Cause Analysis

### Versión en Español
¿Cuál de las respuestas que se enumeran a continuación se refiere a una actividad basada en el debate en la que los miembros del equipo analizan diferentes escenarios para evaluar el plan de respuesta ante incidentes sin activar ningún sistema?
- [x] **Ejercicio de mesa (Tabletop Exercise)**
- [ ] Simulación
- [ ] Caza de amenazas
- [ ] Análisis de la causa raíz

### 1. Explicación General
Un *Tabletop Exercise* es un ejercicio de entrenamiento de baja fidelidad y puramente teórico. Reúne a los actores clave (directores, seguridad, legal, relaciones públicas) en una sala para revisar un escenario hipotético de ataque y evaluar si las políticas y líneas de comunicación escritas son claras.

### 2. ¿Por qué es la correcta y no el resto?
- **Tabletop Exercise:** Se define estrictamente por ser **basado en discusión** y por no interactuar de ninguna manera con la infraestructura viva de la empresa.
- **Simulation:** Involucra un despliegue operativo e interactivo.
- **Threat Hunting** e **RCA:** Son procesos operativos de seguridad real, no dinámicas de entrenamiento teórico.

### 3. Clave para el Examen SY0-701
Palabras clave en el examen: `Discussion-based / No technical systems activated / Review roles on a conference room ➡️ Tabletop Exercise`.

---

## Pregunta 6: Ejercicio Técnico Operativo (Simulation)

### English Version
Which of the following refers to a more comprehensive exercise that may include activating systems and performing real incident response actions?
- [ ] Penetration Testing
- [ ] Threat Hunting
- [x] **Simulation**
- [ ] Vulnerability Scanning

### Versión en Español
¿Cuál de las siguientes respuestas se refiere a un ejercicio más exhaustivo, que puede incluir la activación de sistemas y la realización de acciones reales para responder al incidente?
- [ ] Pruebas de penetración
- [ ] Caza de amenazas
- [x] **Simulación**
- [ ] Escaneo de vulnerabilidades

### 1. Explicación General
A diferencia de los ejercicios de mesa, las Simulaciones son entrenamientos prácticos de alta fidelidad. Los equipos técnicos (Blue Team) deben interactuar con plataformas reales, responder a alertas sintéticas, aislar máquinas en entornos de pruebas y desplegar sus Playbooks de forma física.

### 2. ¿Por qué es la correcta y no el resto?
- **Simulation:** Es la metodología diseñada específicamente para validar la efectividad de las defensas técnicas, herramientas informáticas y la destreza práctica de los analistas en tiempo real ante un entorno de contingencia controlado.
- El resto de las opciones son herramientas y disciplinas de auditoría ofensiva o defensiva permanente, pero no constituyen una metodología integral de simulación del plan de incidentes.

### 3. Clave para el Examen SY0-701
Contraste técnico indispensable para CompTIA:
- `Tabletop` = Hablar, debatir, revisar documentación (Teórico).
- `Simulation` = Ejecutar comandos, aislar sistemas, validar herramientas (Práctico).

---

## Pregunta 7: Análisis de Causa Raíz (Root Cause Analysis - RCA)

### English Version
During the Post-Incident phase, this step involves analyzing logs, forensic data, and other evidence to prevent the incident from recurring.
- [ ] Reporting
- [ ] E-Discovery
- [x] **Root Cause Analysis**
- [ ] Threat Hunting

### Versión en Español
Durante la fase de actuación posterior al incidente, este paso implica el análisis de registros, datos forenses y otras pruebas para evitar que el incidente se repita.
- [ ] Informes
- [ ] Descubrimiento electrónico
- [x] **Análisis de la causa raíz**
- [ ] Caza de amenazas

### 1. Explicación General
El Análisis de Causa Raíz (RCA) busca determinar el fallo fundamental o la vulnerabilidad base que permitió al atacante comprometer el sistema. Su objetivo es ir más allá de reparar los síntomas inmediatos para neutralizar permanentemente el vector de entrada original.

### 2. ¿Por qué es la correcta y no el resto?
- **Root Cause Analysis:** Es la metodología de ingeniería inversa procedimental y técnica cuyo propósito explícito es responder a la pregunta *"¿Por qué ocurrió el incidente en su origen?"* para blindar la red contra ataques idénticos.
- Las demás actividades como *Reporting* (comunicación formal) o *E-Discovery* (recolección legal) no tienen como meta principal aislar la causa raíz de la falla informática.

### 3. Clave para el Examen SY0-701
Fórmula de resolución: `Analizar forense/logs + Prevenir recurrencia idéntica = Root Cause Analysis`.

---

## Pregunta 8: Naturaleza del Threat Hunting

### English Version
Threat hunting refers to proactively searching for Indicators of Compromise (IoCs) to identify and address potential threats before they become major incidents.
- [x] **True**
- [ ] False

### Versión en Español
El término "caza de amenazas" se refiere a una búsqueda proactiva de indicadores de compromiso (IoC) para identificar y abordar posibles amenazas y vulnerabilidades antes de que puedan convertirse en incidentes de gran magnitud.
- [x] **Verdadero**
- [ ] Falso

### 1. Explicación General
El *Threat Hunting* parte de la premisa de que las defensas perimetrales convencionales y las herramientas de monitoreo automatizado (SIEM/EDR) ya han sido evadidas por un atacante sigiloso que reside de forma latente dentro de la red corporativa.

### 2. ¿Por qué es la correcta y no el resto?
La premisa es **Verdadera** porque define exactamente la naturaleza **proactiva** de la disciplina. No espera el disparo de una alerta del sistema; los analistas de Threat Hunting formulan hipótesis y buscan de forma manual e inteligente patrones anómalos o artefactos ocultos (*IoCs*) en la memoria y discos.

### 3. Clave para el Examen SY0-701
Asociación conceptual clave: `Threat Hunting = Proactivo / Asumir que la brecha ya ocurrió / Buscar IoCs de forma manual`.

---

## Pregunta 9: Integridad de Evidencias (Chain of Custody)

### English Version
The process of maintaining a documented record of the handling and movement of evidence to ensure its integrity and admissibility in court is called:
- [x] **Chain of Custody**
- [ ] Chain of Evidence
- [ ] Chain of Responsibility
- [ ] Chain of Accountability

### Versión en Español
El proceso de mantener un registro documentado del manejo y movimiento de las pruebas para garantizar su integridad y admisibilidad en los tribunales se denomina:
- [x] **Cadena de custodia**
- [ ] Cadena de evidencias
- [ ] Chain of Responsibility
- [ ] Chain of Accountability

### 1. Explicación General
En el ámbito legal y de informática forense, cualquier evidencia física o digital extraída de la escena de un crimen digital debe protegerse contra alteraciones, manipulación indebida o sustituciones accidentales para mantener su valor probatorio ante la ley.

### 2. ¿Por qué es la correcta y no el resto?
- **Chain of Custody:** Es el término estándar legal internacional para la bitácora cronológica ininterrumpida que registra: quién recolectó la prueba, etiquetas de hash, fechas de transferencia, lugares de almacenamiento y firmas de cada custodio.
- Las opciones restantes son términos descriptivos no reconocidos formalmente en marcos de informática forense judicial.

### 3. Clave para el Examen SY0-701
Garantía legal en el examen: Si el enunciado menciona *Admisibilidad en la corte (Admissibility in court)*, *Integridad de la prueba*, o la documentación de la transferencia de discos/memorias capturadas, la respuesta correcta es obligatoriamente **Chain of Custody**.

---

## Pregunta 10: Preservación Legal de Datos (E-Discovery)

### English Version
The process of identifying, collecting, and producing electronically stored information with the intent of using it in a legal proceeding or investigation is known as:
- [ ] Litigation Hold
- [ ] Evidence Management
- [ ] Digital Forensics
- [x] **E-Discovery**

### Versión en Español
El proceso de identificar, recopilar y producir información almacenada electrónicamente con la intención de utilizarla en un procedimiento legal o una investigación se denomina:
- [ ] Retención de litigios (Litigation Hold)
- [ ] Gestión de la evidencia
- [ ] Análisis forense digital
- [x] **Descubrimiento electrónico (E-Discovery)**

### 1. Explicación General
El Descubrimiento Electrónico (*E-Discovery*) es un proceso normativo, corporativo y legal mediante el cual los datos digitales legibles por humanos (correos electrónicos, documentos contractuales, chats corporativos) se buscan, filtran y empaquetan para responder a demandas, litigios judiciales o auditorías gubernamentales.

### 2. ¿Por qué es la correcta y no el resto?
- **E-Discovery:** Corresponde propiamente a la fase completa de identificación, clasificación y entrega masiva de información digital estructurada solicitada formalmente por un marco legal.
- **Digital Forensics:** Se enfoca en la ciencia de bajo nivel (análisis de metadatos, recuperación de archivos eliminados en crudo, análisis de registros volátiles).
- **Litigation Hold:** Es el mandato administrativo previo que ordena *congelar y no borrar* ninguna información relevante para un caso, pero no define el proceso de producción de datos en sí.

### 3. Clave para el Examen SY0-701
Diferencia crítica de examen:
- `Digital Forensics` ➡️ Investigación de bajo nivel técnico y análisis científico de artefactos informáticos.
- `E-Discovery` ➡️ Recopilación corporativa y estructurada de documentos/comunicaciones para su presentación ante la corte.

---

[[ExamCompass - Cuestionarios por Temas|⬅️ Volver a Cuestionarios por Temas]]