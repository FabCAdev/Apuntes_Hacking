---
tags:
  - "formato/apunte"
  - "hacking/fundamental"
  - "examen/test-especifico"
  - "gestion/estado/progreso"
---

Este apunte contiene la segunda sección del análisis de los cuestionarios temáticos de ExamCompass para la certificación CompTIA Security+ (SY0-701). Se enfoca exhaustivamente en los modelos de control de acceso (MAC, DAC, RBAC, ABAC) y políticas de seguridad operativas, contrastando mis respuestas con las oficiales del simulador.

---

## Pregunta 1: Control de Acceso Obligatorio (MAC)

### English Version
Which of the following refer to the Mandatory Access Control (MAC) model? (Select all that apply)
- [x] **Users are not allowed to change access policies at their own discretion**
- [x] **Labels and clearance levels can only be assigned and modified by an administrator**
- [ ] Each object has an owner who determines what permissions other users may have
- [ ] Access to resources is based on user identity
- [x] **Each resource has a sensitivity label that matches a clearance level assigned to a user**

### Versión en Español
¿Cuál o cuáles de las siguientes respuestas se refieren al modelo de Control de Acceso Obligatorio (MAC)? (Seleccione todas las que correspondan)
- [x] **Los usuarios no tienen permitido cambiar las políticas de acceso a su propia discreción**
- [x] **Las etiquetas y los niveles de autorización solo pueden ser aplicados y modificados por un administrador**
- [ ] Cada objeto tiene un propietario que, a su propia discreción, determina qué tipo de permisos pueden tener otros usuarios sobre ese objeto
- [ ] Acceso a recursos basado en la identidad del usuario
- [x] **Cada recurso tiene una etiqueta de sensibilidad que coincide con un nivel de autorización asignado a un usuario**

### 1. Explicación General
El Control de Acceso Obligatorio (**MAC**) es la arquitectura de autorización más rígida y jerárquica de la seguridad informática. Su implementación está destinada a entornos militares, agencias gubernamentales de inteligencia o corporaciones con un manejo crítico de secretos industriales. Las decisiones operativas no recaen en el creador o dueño del archivo, sino en un motor criptográfico centralizado gobernado exclusivamente por la administración del sistema.

### 2. ¿Por qué es la correcta y no el resto?
- **Respuestas Seleccionadas:** Son las propiedades clave de MAC. La infraestructura se basa en **etiquetas de sensibilidad** (*sensitivity labels*) asignadas a los recursos (ej. *Confidencial*, *Secreto*, *Top Secret*) que se contrastan directamente contra los **niveles de autorización** (*clearance levels*) del sujeto. Ningún usuario común puede alterar estas políticas.
- **Each object has an owner... / Based on user identity:** Estas dos sentencias describen conceptualmente el modelo discrecional (DAC), donde el propietario del archivo retiene la autonomía para otorgar privilegios a otros individuos basados en sus identidades.

### 3. Clave para el Examen SY0-701
Asociación rápida en el examen: `MAC = Etiquetas de sensibilidad + Niveles de autorización centralizados`.
Si un archivo requiere nivel de autorización *"Top Secret"* y el sujeto tiene nivel *"Secret"*, el sistema denegará el acceso automáticamente, sin importar su rol o jerarquía corporativa.

---

## Pregunta 2: Control de Acceso Discrecional (DAC)

### English Version
Discretionary Access Control (DAC) is an access control model based on user identity. In DAC, each object has an owner who determines what permissions other users may have for that object.
- [x] **True**
- [ ] False

### Versión en Español
El Control de Acceso Discrecional (DAC) es un modelo de control de acceso basado en la identidad del usuario. En DAC, cada objeto tiene un propietario que, a su discreción, determina qué tipo de permisos pueden tener otros usuarios para ese objeto.
- [x] **Verdadero**
- [ ] Falso

### 1. Explicación General
El modelo **DAC** es el estándar nativo en la gran mayoría de los sistemas operativos comerciales e infraestructuras de compartición de archivos del mercado (como sistemas de archivos NTFS en Windows o permisos POSIX en Linux). Su núcleo funcional radica en la *discrecionalidad*: el usuario que crea un objeto se convierte automáticamente en su propietario (*owner*) y tiene plena autoridad para alterar los permisos de lectura, escritura o ejecución a terceros.

### 2. ¿Por qué es la correcta y no el resto?
El enunciado es completamente **Verdadero**. El control discrecional vincula la gestión de la seguridad directamente a la identidad de los usuarios del sistema operativo, permitiéndoles delegar o revocar accesos dentro de sus recursos asignados sin intervención del administrador de red.

### 3. Clave para el Examen SY0-701
Regla básica CompTIA: `DAC = El Propietario (Owner) controla los permisos`.
Cada vez que un escenario describa a un usuario modificando los permisos de una carpeta local mediante listas de control de acceso (ACL) para compartirlas con un compañero de equipo, se está ejecutando el modelo DAC.

---

## Pregunta 3: Control de Acceso Basado en Roles (RBAC)

### English Version
Which type of access control model associates user permissions with specific job responsibilities?
- [ ] DAC
- [x] **RBAC**
- [ ] RuBAC
- [ ] ABAC

### Versión en Español
¿Qué tipo de modelo de control de acceso vincula los permisos de usuario con sus responsabilidades específicas?
- [ ] DAC
- [x] **RBAC**
- [ ] RuBAC
- [ ] ABAC

### 1. Explicación General
En entornos corporativos de mediana y gran escala, gestionar los accesos de forma individualizada (usuario por usuario) se vuelve inmanejable. **RBAC** (Role-Based Access Control) soluciona esto abstrayendo los privilegios y vinculándolos de forma estricta a funciones laborales o cargos dentro de la empresa (*job functions*).

### 2. ¿Por qué es la correcta y no el resto?
- **RBAC:** Es el único modelo diseñado específicamente para estructurar permisos en base a perfiles laborales (por ejemplo: *Contador*, *Ingeniero de Soporte*, *Auditor*). Los usuarios no reciben privilegios de forma directa, sino que los heredan automáticamente al ser asignados a un rol.
- **DAC:** Se basa en decisiones discrecionales del dueño de cada archivo.
- **ABAC:** Evalúa atributos lógicos dinámicos, no solo el perfil operativo.
- **RuBAC:** Rule-Based Access Control se basa en reglas aplicadas globalmente a objetos o routers (como reglas de firewall), no en funciones laborales específicas del personal.

### 3. Clave para el Examen SY0-701
Palabras clave en el examen CompTIA para identificar **RBAC**: *Puesto de trabajo, cargo, departamento, responsabilidades laborales u operaciones organizacionales*.

---

## Pregunta 4: Control de Acceso Basado en Atributos (ABAC)

### English Version
Which access control model allows detailed rules that consider user roles, time restrictions, and network access limitations?
- [ ] DAC
- [ ] RBAC
- [ ] RuBAC
- [x] **ABAC**

### Versión en Español
¿Qué modelo de control de acceso permite definir reglas detalladas que tengan en cuenta los roles de usuario, las restricciones de tiempo y las limitaciones de acceso a la red?
- [ ] DAC
- [ ] RBAC
- [ ] RuBAC
- [x] **ABAC**

### 1. Explicación General
El Control de Acceso Basado en Atributos (**ABAC**) representa la evolución de los modelos lógicos de autorización. A diferencia de RBAC, que solo mira el rol del sujeto, ABAC puede analizar múltiples variables simultáneamente (atributos del sujeto, del recurso que se quiere abrir, de la acción que se va a ejecutar y del entorno) antes de otorgar o denegar un acceso.

### 2. ¿Por qué es la correcta y no el resto?
- **ABAC:** Su motor lógico permite la creación de políticas dinámicas cruzando información granular. Puede orquestar una regla como: *"Permitir al rol de Recursos Humanos (Sujeto) modificar expedientes médicos (Recurso) solo si está en horario de oficina (Entorno: Restricción de tiempo) y conectado desde la VPN corporativa (Entorno: Red)"*.
- **RBAC y DAC:** Carecen de la inteligencia contextual para interpretar de manera nativa restricciones ambientales simultáneas como direcciones IP o el tiempo de forma flexible.

### 3. Clave para el Examen SY0-701
Si CompTIA te plantea un escenario corporativo moderno donde el acceso requiere cumplir múltiples condicionales cruzados (ubicación + hora + tipo de dispositivo), la respuesta siempre será **ABAC**.

---

## Pregunta 5: Pilares Fundamentales de ABAC

### English Version
Examples of properties used to define access policies in Attribute-Based Access Control (ABAC) include:
- [ ] Subject
- [ ] Type of action
- [ ] Type of resource
- [ ] Environment
- [x] **All of the above**

### Versión en Español
Algunos ejemplos de propiedades utilizadas para definir políticas de acceso en el modelo de control de acceso basado en atributos (ABAC) son:
- [ ] Sujeto (usuario o proceso que solicita acceso)
- [ ] Tipo de acción (leer, escribir, ejecutar)
- [ ] Tipo de recurso (expediente médico, cuenta bancaria, etc.)
- [ ] Entorno (hora del día, geolocalización, etc.)
- [x] **Todo lo anterior**

### 1. Explicación General
Para estructurar una política en el modelo ABAC, el motor debe catalogar la información en cuatro categorías de variables muy bien definidas. El cruce completo de estas propiedades conforma el estado lógico final del acceso.

### 2. ¿Por qué es la correcta y no el resto?
**Todo lo anterior** es la opción válida porque las cuatro opciones presentadas constituyen el núcleo fundamental de las propiedades evaluables de ABAC:
1. **Subject (Sujeto):** Atributos del usuario (edad, departamento, nivel de entrenamiento).
2. **Resource / Object (Recurso):** Propiedades del archivo o dato (clasificación, fecha de creación).
3. **Action (Acción):** Lo que se intenta hacer con el recurso (lectura, borrado, modificación).
4. **Environment (Entorno):** El contexto operativo externo (hora local, geolocalización IP, nivel de amenaza actual).

### 3. Clave para el Examen SY0-701
Es indispensable recordar los 4 pilares estructurales de ABAC. En Security+, suelen presentarse en preguntas teóricas para validar si el alumno sabe diferenciar qué datos caen dentro del dominio del *entorno* frente al del *sujeto*.

---

## Pregunta 6: Políticas en Lenguaje Natural (ABAC)

### English Version
Which access control model defines access control rules using statements that closely resemble natural language?
- [ ] DAC
- [x] **ABAC**
- [ ] MAC
- [ ] RBAC

### Versión en Español
¿Qué modelo de control de acceso define las reglas de control de acceso mediante el uso de enunciados que se asemejan mucho al lenguaje natural?
- [ ] DAC
- [x] **ABAC**
- [ ] MAC
- [ ] RBAC

### 1. Explicación General
Debido a la naturaleza flexible y gramatical de las reglas en **ABAC**, las políticas del sistema suelen estructurarse mediante lógica booleana condicional simple (IF/THEN) basada en enunciados legibles que simulan la sintaxis gramatical humana común.

### 2. ¿Por qué es la correcta y no el resto?
- **ABAC:** Su sintaxis se define bajo oraciones de control simples: *"Permitir acceso si el Sujeto es Médico, el Objeto es Historial Clínico, la Acción es Modificar y el Entorno es la red interna de la clínica"*.
- **MAC / DAC / RBAC:** Se configuran a través de asignación binaria de etiquetas estrictas, identidades directas o agrupaciones estáticas en matrices de control de acceso (ACM), las cuales no guardan similitud formal con estructuras de lenguaje natural descriptivo.

### 3. Clave para el Examen SY0-701
Cuando en el examen Security+ se usen las palabras clave **"expresiones lógicas avanzadas"**, **"contexto del sistema"** o **"enunciados similares a lenguaje natural"**, asócialo de forma directa al modelo **ABAC**.

---

## Pregunta 7: Comparativa de Rigidez en Modelos de Acceso

### English Version
Which access control model enforces the most restrictive set of access rules?
- [x] **MAC**
- [ ] RBAC
- [ ] DAC
- [ ] ABAC

### Versión en Español
¿Cuál de los modelos de control de acceso que se enumeran a continuación aplica el conjunto de reglas de acceso más estricto?
- [x] **MAC**
- [ ] RBAC
- [ ] DAC
- [ ] ABAC

### 1. Explicación General
En el diseño de políticas de ciberseguridad corporativa e industrial, existe un balance técnico continuo entre flexibilidad organizativa y rigidez restrictiva de datos. Los modelos se ubican en extremos opuestos de este espectro.

### 2. ¿Por qué es la correcta y no el resto?
- **MAC:** Es intrínsecamente el modelo **más estricto y prohibitivo**. Un error o deseo de un usuario no puede poner en peligro los datos debido a que la seguridad está incrustada directamente en las etiquetas a nivel de Kernel o sistema de archivos. Se rige por denegación implícita absoluta.
- **DAC:** Se posiciona en el extremo opuesto; es el modelo más flexible y con mayor margen de error operativo.
- **ABAC / RBAC:** Proveen un balance dinámico, siendo granulares y complejos pero no tan herméticos a nivel operativo como MAC.

### 3. Clave para el Examen SY0-701
Esta tabla resume el comportamiento de los modelos frente a los extremos del diseño de seguridad:

| Característica clave | Modelo Ganador |
| :--- | :--- |
| **El modelo más estricto / restrictivo** | `MAC` |
| **El modelo más flexible / dinámico** | `ABAC` |
| **El modelo más propenso a errores del usuario** | `DAC` |

---

## Pregunta 8: Ventanas de Mantenimiento y Restricciones de Tiempo

### English Version
Which access control method would be most appropriate for scheduling system maintenance tasks during periods of low user activity?
- [ ] Resource Provisioning
- [x] **Time-based Restrictions**
- [ ] Principle of Least Privilege
- [ ] Just-in-Time Permissions

### Versión en Español
¿Cuál de los siguientes métodos de control de acceso sería el más adecuado para programar las tareas de mantenimiento del sistema durante períodos de baja actividad de los usuarios?
- [ ] Aprovisionamiento de recursos
- [x] **Restricciones horarias**
- [ ] Principio del mínimo privilegio
- [ ] Permisos Just-in-Time

### 1. Explicación General
Las políticas operativas de control de acceso no solo regulan *qué* puede hacer un usuario, sino también *cuándo* le está permitido hacerlo. Limitar los accesos automatizados o de administración a ventanas horarias de baja actividad mitiga vectores de ataque significativos y reduce el impacto de incidentes críticos sobre la producción corporativa.

### 2. ¿Por qué es la correcta y no el resto?
- **Restricciones horarias (Time-based Restrictions):** Habilitan el acceso al sistema o la ejecución de procesos únicamente dentro de franjas horarias parametrizadas (ej. de 02:00 AM a 05:00 AM), bloqueando intentos fuera de ese rango.
- **Principle of Least Privilege:** Garantiza que el operador tenga los permisos mínimos necesarios, pero no gestiona la programación cronológica de las ventanas de mantenimiento.
- **Just-in-Time Permissions (JIT):** Otorga privilegios elevados a demanda del administrador solo por un periodo limitado, pero el detonante es la solicitud explícita del operador humano, no una regla de programación fija del sistema en horas de baja actividad.

### 3. Clave para el Examen SY0-701
Cada vez que el examen mencione **"ventanas de mantenimiento"**, **"fuera de horario laboral"** o **"control del reloj del sistema"**, la implementación de control de acceso objetivo es **Time-Based**.

---

## Pregunta 9: Principio del Mínimo Privilegio (PoLP)

### English Version
The Principle of Least Privilege is a security rule that prevents users from accessing resources and information outside the scope of their responsibilities.
- [x] **True**
- [ ] False

### Versión en Español
El principio del mínimo privilegio es una regla de seguridad que impide a los usuarios acceder a información y recursos que se encuentran fuera del ámbito de sus responsabilidades.
- [x] **Verdadero**
- [ ] Falso

### 1. Explicación General
El Principio del Mínimo Privilegio (**PoLP**, *Principle of Least Privilege*) es una de las reglas de oro de la seguridad informática y de la arquitectura de confianza cero (*Zero Trust*). Dictamina que cualquier entidad (usuarios, aplicaciones, servicios de fondo) debe disponer única y exclusivamente de los accesos indispensables para realizar su actividad operativa cotidiana, ni un solo permiso más.

### 2. ¿Por qué es la correcta y no el resto?
El enunciado es completamente **Verdadero**. Al confinar de forma estricta los privilegios de un usuario a su área operativa, se reduce drásticamente la "superficie de ataque" global de la infraestructura. Si un atacante compromete las credenciales de un empleado de atención al cliente, el PoLP garantiza que dicho atacante no podrá saltar a las bases de datos de finanzas o servidores críticos, puesto que el usuario original jamás dispuso de tales accesos.

### 3. Clave para el Examen SY0-701
El principio del mínimo privilegio está intrínsecamente conectado a conceptos modernos evaluados en CompTIA como: **PAM (Privileged Access Management)**, **Políticas Just-in-Time (JIT)** y el diseño de la **Arquitectura Zero Trust**.

---

[[ExamCompass - Cuestionarios por Temas|⬅️ Volver a Cuestionarios por Temas]]