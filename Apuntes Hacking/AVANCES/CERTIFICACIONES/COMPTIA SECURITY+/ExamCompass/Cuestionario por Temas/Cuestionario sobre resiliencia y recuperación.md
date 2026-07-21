---
tags:
  - "formato/apunte"
  - "hacking/fundamental"
  - "examen/test-especifico"
  - "gestion/estado/terminado"
---
Este apunte contiene el análisis detallado del cuestionario temático sobre resiliencia, alta disponibilidad, tolerancia a fallos, redundancia física y planes de recuperación ante desastres de la plataforma ExamCompass para la certificación CompTIA Security+ (SY0-701), alineado con las respuestas oficiales del simulador.

---

## Pregunta 1: Hardware RAID 0

### English Version
Hardware RAID level 0: (Select all that apply)
* [✅] Requires a minimum of 2 drives for implementation
* [✅] Is also known as disk striping
* [✅] Decreases reliability (failure of any drive in the array results in data loss of the entire array)
* [ ] Is also known as disk mirroring
* [ ] Offers lower volume capacity compared to RAID 1
* [ ] Requires at least 3 drives for implementation
* [✅] Is suitable for systems where performance has a higher priority than fault tolerance
* [ ] Offers improved reliability by creating identical data sets on each drive

### Versión en Español
Nivel RAID de hardware 0: (Seleccione todas las opciones que correspondan)
* [✅] Requiere un mínimo de 2 unidades para su implementación
* [✅] También se conoce como franjas de disco
* [✅] Disminuye la fiabilidad (el fallo de cualquier disco en la matriz provoca la pérdida de todos los datos de la matriz)
* [ ] También se conoce como duplicación de disco
* [ ] Ofrece menor capacidad de volumen en comparación con RAID 1
* [ ] Requiere al menos 3 unidades para su implementación
* [✅] Es adecuado para sistemas donde el rendimiento tiene mayor prioridad que la tolerancia a fallos
* [ ] Ofrece una mayor fiabilidad al crear conjuntos de datos idénticos en cada unidad

### 1. Explicación General
RAID 0 distribuye los datos equitativamente entre dos o más discos (un proceso llamado striping o franjeado) sin guardar ninguna información de paridad ni redundancia. Al leer y escribir en múltiples unidades al mismo tiempo, maximiza el rendimiento del almacenamiento.

### 2. ¿Por qué es la correcta y no el resto?
* **Correctas:** Necesita un mínimo de 2 discos, se le llama franjeado (striping), compromete la fiabilidad (si un disco muere, todo el volumen se destruye) y prioriza el rendimiento puro.
* **Incorrectas:** No es duplicación (eso es RAID 1), no ofrece menor capacidad (aprovecha el 100% del espacio de los discos, a diferencia de RAID 1 que solo aprovecha el 50%), y no requiere 3 discos (eso es RAID 5).

### 3. Clave para el Examen SY0-701
Grábate esto: RAID 0 = Cero tolerancia a fallos. Si la pregunta del examen menciona que se requiere proteger la disponibilidad de los datos ante fallos de hardware, RAID 0 debe ser descartado de inmediato.

---

## Pregunta 2: Hardware RAID 1

### English Version
Hardware RAID level 1: (Select 3 answers)
* [✅] Requires at least 2 drives for implementation
* [ ] Is also known as disk striping
* [ ] Offers improved performance compared to RAID 0
* [ ] Requires at least 3 drives for implementation
* [✅] Offers improved reliability by creating identical data sets on each drive (failure of one drive does not destroy the array, as each drive contains an identical copy of the data)
* [✅] Is also known as disk mirroring

### Versión en Español
RAID de hardware de nivel 1: (Seleccione 3 respuestas)
* [✅] Requiere al menos 2 unidades para su implementación
* [ ] También se conoce como franjas de disco
* [ ] Ofrece un rendimiento mejorado en comparación con RAID 0
* [ ] Requiere al menos 3 unidades para su implementación
* [✅] Ofrece una fiabilidad mejorada al crear conjuntos de datos idénticos en cada unidad (el fallo de una unidad no destruye la matriz, ya que cada unidad contiene una copia idéntica de los datos)
* [✅] También se conoce como duplicación de disco

### 1. Explicación General
RAID 1 duplica la información escribiendo exactamente los mismos datos en dos o más discos en tiempo real (mirroring o espejo). Si una unidad falla de manera física, el sistema sigue operando con la unidad restante de forma transparente.

### 2. ¿Por qué es la correcta y no el resto?
* **Correctas:** Requiere mínimo 2 discos, ofrece alta fiabilidad gracias a la redundancia exacta de datos y se conoce comúnmente como espejo o duplicación.
* **Incorrectas:** No es franjeado (eso es RAID 0), no rinde mejor que RAID 0 (escribir el doble de datos consume tiempo y reduce el rendimiento de escritura) y no requiere 3 discos.

### 3. Clave para el Examen SY0-701
RAID 1 es la solución de tolerancia a fallos más barata y sencilla para servidores pequeños o estaciones de trabajo críticamente locales que no pueden permitirse paradas operativas si un disco duro mecánico o SSD falla.

---

## Pregunta 3: Hardware RAID 5

### English Version
Hardware RAID level 5: (Select 3 answers)
* [ ] Requires at least 2 drives for implementation
* [ ] Continues to function in case of failure of more than one drive
* [ ] Is also known as disk striping with double parity
* [✅] Requires at least 3 drives for implementation
* [✅] Offers increased performance and fault tolerance (failure of a single drive does not destroy the array and lost data can be recreated by the remaining drives)
* [ ] Requires at least 4 drives for implementation
* [✅] Is also known as disk striping with parity

### Versión en Español
RAID de hardware de nivel 5: (Seleccione 3 respuestas)
* [ ] Requiere al menos 2 unidades para su implementación
* [ ] Continúa funcionando en caso de fallo de más de una unidad
* [ ] También se conoce como segmentación de disco con doble paridad
* [✅] Requiere al menos 3 unidades para su implementación
* [✅] Ofrece mayor rendimiento y tolerancia a fallos (el fallo de una sola unidad no destruye la matriz y los datos perdidos pueden ser recreados por las unidades restantes)
* [ ] Requiere al menos 4 unidades para su implementación
* [✅] También se conoce como segmentación de disco con paridad

### 1. Explicación General
RAID 5 combina el franjeado de datos (striping) con un sistema de paridad distribuida. Los datos y los cálculos de paridad se reparten equitativamente entre todos los discos de la matriz, lo que permite reconstruir la información si un solo disco falla.

### 2. ¿Por qué es la correcta y no el resto?
* **Correctas:** Necesita un mínimo de 3 unidades, ofrece buen rendimiento y tolerancia a fallos (puede perder 1 disco sin detenerse) y se conoce como franjeado con paridad.
* **Incorrectas:** No funciona si fallan 2 discos (eso destruiría la matriz), no es doble paridad (eso es RAID 6), y no requiere un mínimo de 4 discos (se puede montar con 3).

### 3. Clave para el Examen SY0-701
RAID 5 es un estándar clásico en centros de datos corporativos porque balancea perfectamente el costo por gigabyte aprovechable, la tolerancia a fallos de hardware y la velocidad de lectura del almacenamiento.

---

## Pregunta 4: Hardware RAID 6

### English Version
Hardware RAID level 6: (Select 3 answers)
* [ ] Is also known as disk striping with parity
* [✅] Requires at least 4 drives for implementation
* [✅] Offers increased performance and fault tolerance (failure of up to 2 drives does not destroy the array and lost data can be recreated by the remaining drives)
* [ ] Requires at least 3 drives for implementation
* [✅] Is also known as disk striping with double parity
* [ ] Continues to function in case of failure of more than 2 drives
* [ ] At least 5 drives are required for implementation

### Versión en Español
RAID de hardware de nivel 6: (Seleccione 3 respuestas)
* [ ] También se conoce como segmentación de disco con paridad
* [✅] Requiere al menos 4 unidades para su implementación
* [✅] Ofrece mayor rendimiento y tolerancia a fallos (el fallo de hasta 2 unidades no destruye la matriz y los datos perdidos pueden ser recreados por las unidades restantes)
* [ ] Requiere al menos 3 unidades para su implementación
* [✅] También se conoce como división de disco con doble paridad
* [ ] Continúa funcionando en caso de fallo de más de 2 unidades
* [ ] Se requieren al menos 5 unidades para su implementación

### 1. Explicación General
RAID 6 es muy similar a RAID 5, pero escribe dos bloques de paridad independientes distribuidos en los discos. Esto significa que la matriz puede tolerar la pérdida física y simultánea de hasta dos unidades de disco sin que se pierdan datos.

### 2. ¿Por qué es la correcta y no el resto?
* **Correctas:** Requiere un mínimo de 4 unidades físicas, sobrevive a la pérdida de hasta 2 discos, y es denominado doble paridad.
* **Incorrectas:** No sobrevive a la pérdida de más de 2 unidades (3 fallos destruyen el volumen), no es paridad simple y no requiere un mínimo de 5 unidades para crearse.

### 3. Clave para el Examen SY0-701
Cuando los sistemas críticos manejan discos de altísima capacidad (donde los tiempos de reconstrucción de un disco caído pueden durar días), se prefiere RAID 6 sobre RAID 5 para evitar que un segundo fallo de disco durante la reconstrucción corrompa la base de datos.

---

## Pregunta 5: Hardware RAID 10 (RAID 1+0)

### English Version
Hardware RAID level 10 (also known as RAID 1+0): (Select 3 answers)
* [✅] Requires a minimum of 4 drives for implementation
* [✅] Is referred to as a stripe of mirrors, i.e., a combination of RAID 1 (disk mirroring) and RAID 0 (disk striping)
* [ ] Requires a minimum of 5 drives for implementation
* [✅] Offers increased performance and fault tolerance (failure of one drive in each mirrored drive pair does not destroy the array)
* [ ] Requires a minimum of 3 drives for implementation
* [ ] Continues to function in case of failure of more than 2 drives
* [ ] Is referred to as a mirror of stripes, i.e., a combination of RAID 1 (disk striping) and RAID 0 (disk mirroring)

### Versión en Español
RAID de hardware de nivel 10 (también conocido como RAID 1+0): (Seleccione 3 respuestas)
* [✅] Requiere un mínimo de 4 unidades para su implementación
* [✅] Se denomina franja de espejos, es decir, una combinación de RAID 1 (duplicación de disco) y RAID 0 (franjeado de disco)
* [ ] Requiere un mínimo de 5 unidades para su implementación
* [✅] Ofrece mayor rendimiento y tolerancia a fallos (el fallo de una unidad en cada par de unidades de disco en espejo no destruye la matriz)
* [ ] Requiere un mínimo de 3 unidades para su implementación
* [ ] Continúa funcionando en caso de fallo de más de 2 unidades
* [ ] Se denomina configuración de franjas de espejos, es decir, una combinación de RAID 1 (distribución de datos en franjas) y RAID 0 (duplicación de datos en espejos)

### 1. Explicación General
RAID 10 es un nivel RAID anidado o híbrido. Crea conjuntos de discos duplicados en espejo (RAID 1) y luego distribuye la información en franjas a través de esos espejos (RAID 0), ofreciendo las ventajas de velocidad de lectura de RAID 0 y la seguridad de tolerancia a fallos de RAID 1.

### 2. ¿Por qué es la correcta y no el resto?
* **Correctas:** Exige un mínimo de 4 unidades, es una franja de espejos (RAID 1+0) y permite la pérdida de un disco por cada pareja en espejo sin que se caiga la matriz de almacenamiento.
* **Incorrectas:** No es un "espejo de franjas" (eso sería RAID 01 o 0+1, que es menos eficiente ante reconstrucciones), y no sobrevive al fallo garantizado de más de 2 unidades si estas pertenecen a la misma pareja en espejo.

### 3. Clave para el Examen SY0-701
RAID 10 es la opción preferida de alta gama para bases de datos transaccionales masivas que requieren velocidad de entrada/salida (I/O) extrema sin tener la penalización de rendimiento en escritura que introduce el cálculo de paridad de RAID 5/6.

---

## Pregunta 6: Niveles RAID sin Tolerancia a Fallos

### English Version
Which of the following RAID levels does not offer fault tolerance?
* [ ] RAID 6
* [ ] RAID 10
* [ ] RAID 5
* [✅] RAID 0
* [ ] RAID 1

### Versión en Español
¿Cuál de los siguientes niveles RAID no ofrece tolerancia a fallos?
* [ ] RAID 6
* [ ] RAID 10
* [ ] RAID 5
* [✅] RAID 0
* [ ] RAID 1

### 1. Explicación General
El propósito principal de la tolerancia a fallos es mantener operativo un sistema informático incluso si uno de sus componentes de hardware falla. El nivel de almacenamiento RAID 0 (striping puro) carece por completo de datos duplicados o algoritmos de paridad que asistan en la recuperación de bloques de información.

### 2. ¿Por qué falló tu respuesta?
Elegiste *RAID 10*. RAID 10 es altamente redundante ya que es una franja de espejos de RAID 1, tolerando caídas de múltiples discos. La respuesta correcta es **RAID 0** porque la pérdida de un solo disco implica la pérdida total e irreversible de los datos de la matriz.

### 3. Clave para el Examen SY0-701
Recuerda siempre: "RAID 0 tiene CERO tolerancia a fallos". Es una regla nemotécnica fundamental para no fallar esta pregunta clásica de almacenamiento seguro en CompTIA.

---

## Pregunta 7: Función Principal del Equilibrio de Carga (Load Balancing)

### English Version
Which of the answers listed below refers to the primary function of load balancing?
* [ ] Maintains identical copies of data on multiple servers to improve data availability and reliability
* [✅] Distributes workload across multiple servers to improve performance
* [ ] Groups servers to provide high availability and fault tolerance
* [ ] Distributes content geographically across multiple servers to improve performance, reduce latency, and manage high volumes of traffic

### Versión en Español
¿Cuál de las respuestas que se enumeran a continuación se refiere a la función principal del equilibrio de carga?
* [ ] Mantiene copias idénticas de los datos en varios servidores para mejorar la disponibilidad y la fiabilidad de los datos.
* [✅] Distribuye la carga de trabajo entre varios servidores para mejorar el rendimiento
* [ ] Agrupa servidores para proporcionar alta disponibilidad y tolerancia a fallos.
* [ ] Distribuye el contenido geográficamente entre varios servidores para mejorar el rendimiento, reducir la latencia y gestionar grandes volúmenes de tráfico.

### 1. Explicación General
El Equilibrio de Carga (Load Balancing) utiliza un dispositivo físico o un software que intercepta las peticiones de red entrantes de los clientes y las distribuye inteligentemente entre un grupo (pool) de servidores web o de aplicaciones para asegurar que ningún servidor individual sea sobrecargado.

### 2. ¿Por qué es la correcta y no el resto?
* **Distribuye la carga de trabajo entre varios servidores** es la función primaria del balanceador para asegurar que el rendimiento sea óptimo y escalable.
* **Mantiene copias idénticas:** Se refiere a la sincronización o replicación de bases de datos y archivos.
* **Agrupa servidores para tolerancia a fallos:** Es la definición del clúster de alta disponibilidad.
* **Distribuye el contenido geográficamente:** Es la descripción de una CDN (Content Delivery Network / Red de Distribución de Contenido).

### 3. Clave para el Examen SY0-701
En arquitecturas de red seguras, los balanceadores de carga también mitigan ataques de Denegación de Servicio (DoS/DDoS) distribuyendo el tráfico anómalo y pueden realizar la descarga de descifrado SSL/TLS (SSL Offloading) para aliviar a los servidores de backend.

---

## Pregunta 8: Función Principal de la Agrupación (Clustering)

### English Version
Which of the following is the primary function of clustering?
* [ ] Distributes content geographically across multiple servers to improve performance, reduce latency, and manage high traffic volumes
* [✅] Groups servers to provide high availability and fault tolerance
* [ ] Maintains identical copies of data on multiple servers to improve data availability and reliability
* [ ] Distributes workload across multiple servers to improve performance

### Versión en Español
¿Cuál de las siguientes es la función principal de la agrupación?
* [ ] Distribuye el contenido geográficamente entre varios servidores para mejorar el rendimiento, reducir la latencia y gestionar grandes volúmenes de tráfico.
* [✅] Agrupa servidores para proporcionar alta disponibilidad y tolerancia a fallos
* [ ] Mantiene copias idénticas de los datos en varios servidores para mejorar la disponibilidad y la fiabilidad de los datos.
* [ ] Distribuye la carga de trabajo entre varios servidores para mejorar el rendimiento.

### 1. Explicación General
La Agrupación o Clúster (Clustering) consiste en conectar e integrar varios servidores (nodos) de manera que trabajen y se comporten como un único sistema lógico de cara al usuario. Su objetivo primordial no es solo el rendimiento, sino garantizar que si un nodo físico experimenta un fallo crítico de hardware, otro servidor de la agrupación tome su lugar inmediatamente (failover) manteniendo la disponibilidad del servicio.

### 2. ¿Por qué es la correcta y no el resto?
* **Agrupa servidores para alta disponibilidad y tolerancia a fallos** es la definición del propósito de un clúster activo-pasivo o activo-activo.
* **Distribución geográfica de contenido:** Describe a las CDNs.
* **Distribución de carga:** Describe a los balanceadores de carga.
* **Copias idénticas de datos:** Describe replicación de datos en almacenamiento.

### 3. Clave para el Examen SY0-701
CompTIA evalúa la alta disponibilidad mediante el concepto de Clúster Activo-Activo (todos los servidores procesan solicitudes a la vez y comparten la carga) y Clúster Activo-Pasivo (un servidor principal atiende y el secundario está en espera, activándose automáticamente solo si el principal se cae).

---

## Pregunta 9: Centros de Datos Redundantes en Vivo (Hot Site)

### English Version
Which of the terms listed below refers to a replica of the original site, with fully operational computer systems and near-complete backups of user data?
* [✅] Hot site
* [ ] Warm site
* [ ] Cold site
* [ ] Mobile site

### Versión en Español
¿Cuál de los términos que se enumeran a continuación se refiere a una réplica del sitio original, con sistemas informáticos totalmente operativos y copias de seguridad casi completas de los datos de los usuarios?
* [✅] Sitio popular (Hot Site)
* [ ] Sitio cálido
* [ ] Sitio frío
* [ ] Sitio web móvil

### 1. Explicación General
En la planificación de recuperación ante desastres (DRP), un Hot Site (traducido literalmente en la pregunta como "Sitio popular") es un centro de datos alternativo totalmente equipado y redundante. Tiene energía eléctrica activa, servidores encendidos con sistemas idénticos al de producción, telecomunicaciones configuradas y los datos de la empresa sincronizados continuamente o con desfase mínimo.

### 2. ¿Por qué falló tu respuesta?
Elegiste *Sitio cálido*. El sitio cálido (Warm site) no está completamente operativo y requiere configuraciones manuales de red además de restauración manual de backups para comenzar a operar. El único que está listo para reanudar operaciones de forma inmediata con copias de seguridad de datos casi al instante es el **Hot Site (Sitio popular)**.

### 3. Clave para el Examen SY0-701
Si el caso de estudio de CompTIA describe una organización financiera que no tolera perder más de unos minutos de operación tras un desastre y requiere un tiempo de recuperación mínimo (RTO muy bajo), la solución indispensable es la implementación de un Hot Site.

---

## Pregunta 10: Sitios de Recuperación Semi-Equipados (Warm Site)

### English Version
Which of the following terms refers to an alternative site that provides pre-installed hardware and software and might have partial data backups, but is not fully operational and requires additional configuration before use?
* [ ] Cold site
* [ ] Hot site
* [ ] Mirror site
* [✅] **Warm site**

### Versión en Español
¿Cuál de los siguientes términos se refiere a un sitio alternativo que proporciona hardware y software preinstalados y que podría tener copias de seguridad parciales de los datos, pero que no está completamente operativo y requiere configuración adicional antes de su uso?
* [ ] Sitio frío
* [ ] Sitio popular
* [ ] Sitio espejo
* [✅] **Sitio cálido**

### 1. Explicación General
El Sitio Cálido (Warm Site) es la opción intermedia en costos y tiempos de recuperación de la continuidad del negocio. El espacio físico cuenta con racks, servidores ya cableados y sistemas operativos instalados, pero no está procesando tráfico activamente y sus bases de datos no están completamente al día con producción, requiriendo restauraciones manuales previas al arranque.

### 2. ¿Por qué es la correcta y no el resto?
* **Sitio cálido** describe perfectamente el estado híbrido de tener la infraestructura física instalada pero requiriendo ajustes de configuración y recuperación de datos antes de entrar en servicio.
* **Sitio popular (Hot Site):** Ya está completamente operativo y listo para uso inmediato sin necesidad de restauración manual de emergencia de respaldos.
* **Sitio frío (Cold Site):** Carece por completo de hardware o software preinstalado.

### 3. Clave para el Examen SY0-701
El Warm Site representa el equilibrio costo-beneficio más popular para empresas de tamaño mediano que no pueden pagar la millonaria infraestructura de duplicación en vivo de un Hot Site, pero que tampoco pueden permitirse las semanas de retraso que implica levantar un Cold Site desde cero.

---

## Pregunta 11: Infraestructura Alternativa Vacía (Cold Site)

### English Version
A disaster recovery facility that provides only the physical space for recovery operations is known as a:
* [ ] Hot site
* [ ] Warm site
* [✅] **Cold site**
* [ ] Mirror site

### Versión en Español
Una instalación de recuperación ante desastres que proporciona únicamente el espacio físico para las operaciones de recuperación se conoce como:
* [ ] Sitio popular
* [ ] Sitio cálido
* [✅] **Sitio frío**
* [ ] Sitio espejo

### 1. Explicación General
El Sitio Frío (Cold Site) es simplemente un espacio físico vacío contratado con anticipación que cuenta con servicios básicos (como energía eléctrica, control de humedad/aire acondicionado, conexiones de red externas e infraestructura de cableado básico), pero sin ningún tipo de computadora, servidor o almacenamiento dentro de él.

### 2. ¿Por qué es la correcta y no el resto?
* **Sitio frío** es, por definición, el sitio alternativo vacío que solo provee espacio físico.
* **Sitio cálido y popular:** Vienen equipados con hardware de computación y sistemas de almacenamiento preexistentes de fábrica.

### 3. Clave para el Examen SY0-701
El Cold Site requiere el RTO (Recovery Time Objective) más largo (semanas o meses), ya que la organización debe comprar, transportar, instalar y configurar todo el equipamiento de hardware y restaurar la totalidad de los datos antes de poder iniciar operaciones desde allí.

---

## Pregunta 12: Costo de Implementación de Sitios Alternativos

### English Version
Which alternative site is the least expensive to implement?
* [✅] **Cold site**
* [ ] Mirror site
* [ ] Warm site
* [ ] Hot site

### Versión en Español
¿Qué sitio alternativo es el menos costoso de implementar?
* [✅] **Sitio frío**
* [ ] Sitio espejo
* [ ] Sitio cálido
* [ ] Sitio popular

### 1. Explicación General
Los costos de mantenimiento de un sitio de recuperación alternativa son proporcionales a su nivel de equipamiento tecnológico y de operación activa. Al ser una infraestructura desprovista de servidores, computadoras o licencias de software activas que requieran actualizaciones o administración constante de TI, un sitio frío tiene los costos más bajos del mercado.

### 2. ¿Por qué es la correcta y no el resto?
* **Sitio frío** tiene el menor costo de implementación y mantenimiento porque solo se paga la renta de un espacio físico vacío y la disponibilidad de infraestructura básica de energía y red.
* **Sitio cálido y popular:** Requieren inversiones millonarias constantes en mantenimiento de hardware duplicado, licencias activas y mano de obra técnica para mantener el sitio actualizado y sincronizado.

### 3. Clave para el Examen SY0-701
En la gestión de riesgos para Security+, siempre existe un compromiso (trade-off) directo: el sitio más barato (Cold Site) es también el que tiene el tiempo de recuperación de negocio más lento, mientras que el sitio más costoso (Hot Site) ofrece la recuperación más veloz.

---

## Pregunta 13: Velocidad de Recuperación de Sitios Alternativos

### English Version
Which alternative location allows the fastest disaster recovery?
* [ ] Cold site
* [✅] **Hot site**
* [ ] Mobile site
* [ ] Warm site

### Versión en Español
¿Qué ubicación alternativa permite la recuperación ante desastres más rápida?
* [ ] Sitio frío
* [✅] **Sitio popular (Hot Site)**
* [ ] Sitio web móvil
* [ ] Sitio cálido

### 1. Explicación General
La velocidad de recuperación se mide mediante el RTO (Recovery Time Objective). Un Hot Site (Sitio popular) tiene todo listo de manera idéntica al centro de datos principal; por lo tanto, la conmutación de tráfico se puede automatizar para desviar los usuarios en minutos o segundos cuando el sitio principal se declare inoperable.

### 2. ¿Por qué falló tu respuesta?
Elegiste *Sitio cálido*. El sitio cálido no es la opción más rápida, ya que requiere configuraciones manuales y restauración de datos antes de su entrada en producción. El **Hot Site** es el más rápido porque no requiere aprovisionar hardware, instalar sistemas ni realizar restauraciones masivas de datos históricos desde unidades externas de cinta o red.

### 3. Clave para el Examen SY0-701
Para el examen, asocia siempre el término "Near-zero RTO" (Objetivo de tiempo de recuperación cercano a cero) con la adquisición técnica de un Hot Site (Sitio caliente o popular).

---

## Pregunta 14: Marco Gubernamental de Continuidad (COOP)

### English Version
What is the name of a US government initiative that provides a set of procedures and plans that an organization can implement to ensure the continued performance of its essential functions during unexpected events?
* [ ] SLA
* [✅] **COOP**
* [ ] RPO
* [ ] BIA

### Versión en Español
¿Cuál es el nombre de una iniciativa del gobierno estadounidense que proporciona un conjunto de procedimientos y planes que una organización puede implementar para garantizar el desempeño continuo de sus funciones esenciales durante eventos inesperados?
* [ ] SLA
* [✅] **COOPERATIVA (COOP - Continuity of Operations)**
* [ ] RPO
* [ ] BIA

### 1. Explicación General
COOP (Continuity of Operations / Continuidad de Operaciones) es una directiva e iniciativa federal de los Estados Unidos diseñada originalmente para agencias gubernamentales, pero ampliamente adoptada por el sector privado. Establece metodologías estandarizadas para asegurar que las funciones esenciales del estado y del negocio continúen ejecutándose ante desastres naturales, ataques terroristas o emergencias de seguridad nacional.

### 2. ¿Por qué es la correcta y no el resto?
* **COOP** es la iniciativa y sigla exacta que define las directrices y planes federales de continuidad operativa del gobierno estadounidense.
* **SLA (Service Level Agreement):** Acuerdo de nivel de servicio que define métricas de soporte técnico entre un proveedor y un cliente.
* **RPO (Recovery Point Objective):** Métrica que define la cantidad máxima de pérdida de datos tolerable medida en tiempo.
* **BIA (Business Impact Analysis):** Es la fase de análisis del negocio diseñada para identificar y priorizar qué sistemas y procesos de la organización son los más críticos.

### 3. Clave para el Examen SY0-701
En Security+, un plan de continuidad de operaciones (COOP) exitoso debe definir claramente la Cadena de mando (Succession Planning): quién toma las decisiones críticas de la organización si el CEO o el equipo ejecutivo queda incomunicado durante un desastre.

---

## Pregunta 15: Pruebas de Continuidad Teóricas (Tabletop Exercise)

### English Version
Which of the answers listed below refers to a simulated scenario conducted in an informal, discussion-based environment, typically involving debates and planning around hypothetical security incidents?
* [✅] **Tabletop exercise**
* [ ] Sandboxing
* [ ] Threat hunting
* [ ] Security awareness training

### Versión en Español
¿Cuál de las respuestas que se enumeran a continuación se refiere a un escenario simulado llevado a cabo en un entorno controlado, que normalmente implica debates y planificación en torno a incidentes de seguridad hipotéticos?
* [✅] **Ejercicio de mesa (Tabletop Exercise)**
* [ ] Sandboxing
* [ ] Caza de amenazas
* [ ] Capacitación en concientización sobre seguridad

### 1. Explicación General
Un Tabletop Exercise (ejercicio de mesa) es un simulacro teórico basado en discusiones guiadas. Un facilitador presenta un escenario de incidente hipotético (como un brote de ransomware en la red interna) y los miembros del equipo de respuesta a incidentes sentados en la mesa analizan paso a paso el protocolo formal que seguirían para resolver el caso, detectando brechas en la documentación del plan de incidentes.

### 2. ¿Por qué falló tu respuesta?
Elegiste *Sandboxing*. El Sandboxing es un control meramente técnico (no un ejercicio de personal) que aísla de manera automatizada archivos sospechosos en una máquina virtual cerrada para observar su comportamiento real de malware. El ejercicio enfocado en debatir incidentes simulados de forma teórica es el **Ejercicio de mesa (Tabletop)**.

### 3. Clave para el Examen SY0-701
Los ejercicios de mesa (tabletop) son vitales porque permiten a la organización evaluar la preparación de su personal de manera económica y sin causar interrupciones operativas ni riesgos a la red de producción de la empresa.

---

## Pregunta 16: Conmutación de Servicios en Alta Disponibilidad (Failover)

### English Version
The process of switching to a redundant or standby system upon detecting a failure in the primary system is called:
* [✅] **Failover**
* [ ] Multipath I/O
* [ ] Load balancing
* [ ] Parallel processing

### Versión en Español
El proceso de conmutación a un sistema redundante o de reserva al detectar una interrupción en el sistema principal se denomina:
* [✅] **Conmutación por error (Failover)**
* [ ] E/S de rutas múltiples
* [ ] Balanceo de carga
* [ ] Procesamiento paralelo

### 1. Explicación General
La Conmutación por error (Failover) es una función automática en sistemas de alta disponibilidad. Consiste en que al detectar de forma automática que el sistema o servidor primario ha fallado (normalmente mediante la pérdida de una señal de latido o "heartbeat"), el sistema secundario o de respaldo (standby) toma el control de inmediato y asume las operaciones para evitar interrupciones en el servicio.

### 2. ¿Por qué es la correcta y no el resto?
* **Conmutación por error (Failover)** es el término técnico que describe el acto y redireccionamiento automatizado ante la caída de un servicio.
* **E/S de rutas múltiples (Multipath I/O):** Técnica para crear múltiples rutas físicas entre un servidor y su almacenamiento para tolerancia a fallos en el cableado de red (SAN).
* **Balanceo de carga:** Distribución del tráfico activo entre varios sistemas operacionales sanos, no el cambio por detección de fallos de un sistema completo.

### 3. Clave para el Examen SY0-701
Para Security+, el failover exitoso debe ser lo más transparente posible para el usuario final. Se asocia con configuraciones de firewalls redundantes de alta disponibilidad (Active/Passive) y balanceadores que envían peticiones solo a nodos saludables.

---

## Pregunta 17: Escenarios Activos de Respuesta (Simulación)

### English Version
Which of the following answers refers to a more realistic scenario that tests cybersecurity incident response by mimicking real-world attacks?
* [ ] Fingerprinting
* [✅] **Simulation**
* [ ] Threat hunting
* [ ] Tabletop exercise

### Versión en Español
¿Cuál de las siguientes respuestas se refiere a un escenario más realista que pone a prueba la respuesta ante incidentes de ciberseguridad mediante la imitación de ataques reales?
* [ ] Toma de huellas dactilares
* [✅] **Simulación (Simulation)**
* [ ] Caza de amenazas
* [ ] Ejercicio de mesa

### 1. Explicación General
Una Simulación (*Simulation*) consiste en un ejercicio de seguridad activo y práctico donde se replican técnicas, tácticas y procedimientos (TTP) de atacantes reales en un entorno controlado. Sirve para medir con precisión milimétrica el tiempo de detección de las herramientas automáticas de seguridad y la efectividad de la respuesta del equipo humano de defensa.

### 2. ¿Por qué es la correcta y no el resto?
* **Simulación** implica acción técnica real (como realizar un ataque controlado de phishing a los empleados o emular un malware en la red) para observar la respuesta del sistema.
* **Ejercicio de mesa (Tabletop exercise):** Es un simulacro exclusivamente teórico, basado en conversaciones y debates verbales de un comité en una sala de juntas, sin interactuar con infraestructura tecnológica real.
* **Toma de huellas dactilares (Fingerprinting):** Es un método puramente técnico de escaneo de red para identificar el sistema operativo y servicios que corren en un host.
* **Caza de amenazas (Threat hunting):** Consiste en buscar proactivamente atacantes que ya han evadido los controles de seguridad y están activos dentro de la red, no es un escenario de entrenamiento simulado.

### 3. Clave para el Examen SY0-701
En el examen, las simulaciones de ataque de alta madurez se representan frecuentemente como ejercicios de *Red Team* (atacantes simulados) vs. *Blue Team* (defensores del SOC). Son herramientas indispensables para evaluar la preparación práctica real ante incidentes sin limitarse a la teoría de los manuales de políticas.

---

## Pregunta 18: Rendimiento y Redundancia Computacional (Procesamiento Paralelo)

### English Version
Which of the solutions listed below provides redundancy and fault tolerance by dividing tasks into smaller subtasks and distributing them among multiple systems to be executed simultaneously?
* [ ] Load balancing
* [ ] Multitasking
* [ ] Clustering
* [✅] **Parallel processing**

### Versión en Español
¿Cuál de las soluciones que se enumeran a continuación proporciona redundancia y tolerancia a fallos al dividir las tareas en subtareas más pequeñas y distribuirlas entre varios sistemas para que se ejecuten simultáneamente?
* [ ] Balanceo de carga
* [ ] Multitarea
* [ ] Agrupación
* [✅] **Procesamiento paralelo (Parallel processing)**

### 1. Explicación General
El Procesamiento Paralelo (*Parallel Processing*) es una arquitectura y método computacional que rompe un problema de cálculo masivo en múltiples porciones o subprocesos más pequeños para que puedan ser ejecutados de forma simultánea por diversos núcleos de procesamiento, hilos de ejecución o servidores independientes. Si un procesador o nodo físico falla a mitad del cálculo, el sistema reasigna el hilo de datos interrumpido a otra CPU activa, garantizando la continuidad del procesamiento.

### 2. ¿Por qué es la correcta y no el resto?
* **Procesamiento paralelo** describe exactamente la fragmentación de una sola tarea lógica grande en piezas simultáneas para redundancia matemática y de hardware.
* **Balanceo de carga:** Trabaja a nivel de red o de aplicaciones distribuyendo flujos de conexiones completas de múltiples usuarios (como tráfico web), no dividiendo un cálculo de datos individual de bajo nivel.
* **Multitarea (Multitasking):** Es la capacidad de un único sistema operativo de aparentar que ejecuta varias aplicaciones a la vez alternando rápidamente el uso del tiempo de CPU, no implica necesariamente múltiples procesadores ni distribución entre sistemas paralelos.
* **Agrupación (Clustering):** Es la infraestructura de red física que aloja e interconecta los servidores para trabajar juntos, pero no es la técnica matemática de ejecución del procesamiento de instrucciones propiamente dicha.

### 3. Clave para el Examen SY0-701
Para el examen de CompTIA, asocia el procesamiento paralelo con la tolerancia a fallos dentro de la computación de alto rendimiento (HPC), clusters de bases de datos masivas y arquitecturas donde el cómputo de cifrado o la minería de datos pesada no puede verse interrumpida si falla un nodo de cómputo individual.

---

## Pregunta 19: Representación del Estado de Máquinas Virtuales (Instantánea)

### English Version
A file-based representation of the state of a virtual machine at a given point in time is called a:
* [ ] Restore point
* [ ] Snapshot copy
* [✅] **Snapshot**
* [ ] System image

### Versión en Español
Una representación basada en archivos del estado de una máquina virtual en un momento dado se denomina:
* [ ] Punto de restauración
* [ ] Copia de instantánea
* [✅] **Instantánea (Snapshot)**
* [ ] Imagen del sistema

### 1. Explicación General
Una Instantánea (*Snapshot*) es una captura lógica rápida de la configuración, estado de almacenamiento de disco, y opcionalmente el contenido de la memoria RAM de una máquina virtual en un segundo preciso en el tiempo. Permite a los administradores de sistemas realizar cambios de alto riesgo (como instalar parches o actualizaciones) y revertir la máquina virtual entera a su estado idéntico anterior en cuestión de segundos si el sistema se vuelve inestable.

### 2. ¿Por qué es la correcta y no el resto?
* **Instantánea (Snapshot)** es el término técnico formal que utilizan los hipervisores (como VMware vSphere, Microsoft Hyper-V, KVM) para la representación directa de archivos que congelan el estado de una VM.
* **Punto de restauración:** Es una característica de software a nivel de sistema operativo cliente (como Windows System Restore) para archivos de configuración locales, no un archivo administrador de la máquina virtual completa en el hipervisor.
* **Imagen del sistema (System image):** Es una copia exacta bit a bit del contenido de un disco duro físico completo, utilizada principalmente para la clonación inicial o aprovisionamiento físico masivo.
* **Copia de instantánea (Snapshot copy):** No es el término estándar definido para este archivo de congelamiento del hipervisor.

### 3. Clave para el Examen SY0-701
Es una de las preguntas de advertencia de CompTIA más importantes: las instantáneas de máquinas virtuales son una magnífica herramienta de contingencia a corto plazo, pero **nunca** deben considerarse o utilizarse como un reemplazo de las copias de seguridad tradicionales (backups), ya que dependen físicamente del disco virtual base original para operar y pueden degradar severamente el rendimiento si se acumulan por mucho tiempo.

---

## Pregunta 20: Respaldos en Infraestructuras Virtuales (Snapshot Backups)

### English Version
Which type of backups are commonly used with virtual machines?
* [ ] Incremental backups
* [✅] **Snapshot backups**
* [ ] Tape backups
* [ ] Differential backups

### Versión en Español
¿Qué tipo de copias de seguridad se utilizan habitualmente con las máquinas virtuales?
* [ ] Copias de seguridad incrementales
* [✅] **Copias de seguridad instantáneas (Snapshot backups)**
* [ ] Copias de seguridad en cinta
* [ ] Copias de seguridad diferenciales

### 1. Explicación General
En los entornos modernos virtualizados, las Copias de seguridad instantáneas (*Snapshot backups*) son la solución preferida debido a que aprovechan la API del hipervisor para capturar la estructura completa del disco virtual (.vmdk o .vhdx). Esto permite realizar copias de seguridad consistentes sin requerir instalar agentes individuales dentro de cada máquina virtual ni apagar o pausar el sistema durante el proceso de respaldo.

### 2. ¿Por qué falló tu respuesta?
Elegiste *Copias de seguridad incrementales*. Aunque el software de respaldo moderno utiliza internamente lógicas incrementales o diferenciales para copiar únicamente los bloques de datos que cambiaron y así ahorrar almacenamiento, esta es la técnica de transferencia lógica de datos. El método nativo a nivel de infraestructura para copiar y respaldar de raíz las máquinas virtuales completas a través del hipervisor se denomina **Copia de seguridad instantánea (Snapshot backup)**.

### 3. Clave para el Examen SY0-701
En escenarios donde se requiera un RTO (Objetivo de tiempo de recuperación) muy bajo para servidores de producción virtuales, las copias de seguridad basadas en snapshots permiten restaurar la máquina virtual de manera íntegra, con su sistema operativo, aplicaciones y bases de datos intactos en un hardware físico totalmente distinto de forma inmediata.

---

## Pregunta 21: Copia de Datos en Tiempo Real (Replicación)

### English Version
Which of the following terms refers to a backup strategy that relies on creating and maintaining real-time or near-real-time copies of data on a separate system?
* [ ] Mirroring
* [ ] Virtualization
* [ ] Journaling
* [✅] **Replication**

### Versión en Español
¿Cuál del los siguientes de refiere a una estrategia de respaldo que se basa en la creación y el mantenimiento de copias de datos en tiempo real o casi en tiempo real en un sistema separado?
* [ ] Reflejo
* [ ] Virtualización
* [ ] Diario personal (Traducción errónea de Journaling)
* [✅] **Replicación (Replication)**

### 1. Explicación General
La Replicación (*Replication*) es el proceso de transferir continuamente y de forma automatizada las transacciones o bloques de datos recién escritos en un servidor de almacenamiento principal hacia un servidor o centro de datos de destino secundario, usualmente ubicado a gran distancia geográfica. Puede ser síncrona (exactamente en tiempo real) o asíncrona (casi en tiempo real, con pequeños segundos o minutos de retraso).

### 2. ¿Por qué es la correcta y no el resto?
* **Replicación** es la técnica diseñada específicamente para duplicar continuamente bases de datos u objetos enteros de archivos entre múltiples servidores distribuidos con fines de alta disponibilidad geográfica.
* **Reflejo (Mirroring):** Es una tecnología local e interna enfocada en duplicar datos entre discos duros que comparten el mismo controlador o servidor físico (como en un arreglo RAID 1), no como estrategia global distribuida entre sistemas remotos separados.
* **Journaling (Diario):** Es un mecanismo interno local de los sistemas de archivos para evitar daños por apagones repentinos en el propio disco duro, sin transmisión de red.

### 3. Clave para el Examen SY0-701
La replicación de almacenamiento es el motor que permite mantener actualizado un sitio alternativo activo o *Hot Site*. Si tu base de datos de producción replica cada cambio en tiempo real al sitio alternativo, la conmutación de tráfico en caso de desastre físico en el edificio principal se puede realizar casi sin pérdida de datos (RPO cercano a cero).

---

## Pregunta 22: Integridad y Recuperación de Transacciones (Journaling)

### English Version
A technique that allows retrieving changes that occurred since the last backup in the event of a system failure is known as:
* [ ] Replication
* [✅] **Journaling**
* [ ] Virtualization
* [ ] Mirroring

### Versión en Español
Una técnica que permite recuperar los cambios ocurridos desde la última copia de seguridad en caso de fallo del sistema se conoce como:
* [ ] Replicación
* [✅] **Escribir un diario (Journaling)**
* [ ] Virtualización
* [ ] Reflejo

### 1. Explicación General
El *Journaling* es una funcionalidad de robustez integrada en sistemas de archivos (como NTFS en Windows o ext4 en Linux) y motores de bases de datos. Consiste en escribir de forma secuencial cada operación o cambio pendiente en un registro histórico circular dedicado (el "diario" o log de transacciones) antes de realizar la escritura real en los bloques de almacenamiento del disco principal. Si el sistema se apaga repentinamente a mitad de una transacción, al iniciar lee este diario para reconstruir y validar las escrituras incompletas.

### 2. ¿Por qué falló tu respuesta?
Elegiste *Replicación*. La replicación duplica la base de datos confirmada hacia un sistema remoto externo de forma continua, pero no es la técnica interna encargada de procesar las transacciones individuales incompletas del sistema de archivos local cuando este experimenta un corte abrupto de energía y necesita arrancar sin errores en su siguiente inicio. Esa labor de consistencia local es el **Journaling**.

### 3. Clave para el Examen SY0-701
El journaling es vital para la disponibilidad (*Availability* en la tríada CIA), ya que reduce drásticamente el tiempo de inactividad de un servidor después de un apagón imprevisto, evitando la necesidad de ejecutar análisis exhaustivos de consistencia de disco (chkdsk o fsck) que tardan horas en discos duros masivos de producción.

---

## Pregunta 23: Distribución Eléctrica de Alta Capacidad (PDU)

### English Version
Which of the answers listed below refers to a device designed to supply (and control the quality of) electrical power to multiple power outlets?
* [ ] Power supply
* [ ] MDF
* [✅] **PDU**
* [ ] IDF

### Versión en Español
¿Cuál de las respuestas que aparecen a continuación se refiere a un dispositivo diseñado para suministrar (y controlar la calidad de) energía eléctrica a múltiples tomas de corriente?
* [ ] Fuente de alimentación
* [ ] MDF
* [✅] **PDU (Power Distribution Unit)**
* [ ] IDF

### 1. Explicación General
Una PDU (*Power Distribution Unit* / Unidad de Distribución de Energía) es un dispositivo industrial equipado con múltiples tomas de corriente diseñado para ser montado en los gabinetes o racks de servidores de un centro de datos. Distribuye energía regulada de manera segura hacia los componentes de hardware e, incluso, en modelos avanzados (Managed PDUs), permite monitorear a distancia el consumo eléctrico de cada servidor y encenderlos o apagarlos remotamente.

### 2. ¿Por qué es la correcta y no el resto?
* **PDU** es el equipo diseñado específicamente para la distribución, control y dosificación inteligente de tomas eléctricas dentro de un rack de TI.
* **Fuente de alimentación (Power supply):** Es el transformador de voltaje físico interno e individual de cada servidor para convertir corriente alterna en continua, no distribuye energía hacia múltiples equipos externos.
* **MDF (Main Distribution Frame) / IDF (Intermediate Distribution Frame):** Son términos que definen la infraestructura física de cableado estructurado de redes de datos (racks de telecomunicaciones principales e intermedios), no componentes de energía eléctrica.

### 3. Clave para el Examen SY0-701
Para implementar la alta disponibilidad eléctrica, cada rack se equipa con dos PDUs redundantes conectadas a fuentes y subestaciones eléctricas distintas. Los servidores de alta gama cuentan con fuentes de alimentación duales (Dual Power Supplies), conectando cada una de ellas a una PDU independiente para que, si falla una línea eléctrica completa, el servidor siga operando sin detenerse.

---

## Pregunta 24: Resiliencia de Energía a Corto Plazo (UPS)

### English Version
What is the name of a device that can provide short-term emergency power during an unexpected power outage of the main power supply?
* [✅] **UPS**
* [ ] PoE
* [ ] SVC
* [ ] Power supply

### Versión en Español
¿Cómo se llama un dispositivo que puede proporcionar energía de emergencia a corto plazo durante un corte inesperado del suministro eléctrico principal?
* [✅] **UPS (Uninterruptible Power Supply)**
* [ ] PoE
* [ ] SVC
* [ ] Fuente de alimentación

### 1. Explicación General
Un UPS (*Uninterruptible Power Supply* / Sistema de Alimentación Ininterrumpida - SAI) es un equipo que contiene un banco de baterías químicas internas de recarga constante y electrónica de control rápido. En el momento en que se interrumpe la electricidad de la red comercial, el UPS reacciona en milisegundos para suministrar energía de emergencia limpia a los sistemas críticos conectados, protegiéndolos contra picos y caídas de tensión dañinas.

### 2. ¿Por qué falló tu respuesta?
Elegiste *Fuente de alimentación*. La fuente de alimentación convierte la electricidad, pero carece de un banco de baterías internas para retener carga; por lo tanto, en cuanto se corta la energía de la pared, la computadora se apaga de inmediato de forma forzada. El único dispositivo de red diseñado para almacenar y suministrar de inmediato energía de respaldo ante apagones es el **UPS**.

### 3. Clave para el Examen SY0-701
El propósito estratégico de un UPS en la continuidad empresarial **no** es mantener toda la oficina trabajando de corrido por horas, sino proporcionar una ventana de tiempo crítica y suficiente (comúnmente de 15 a 30 minutos) para que los servidores ejecuten un script de apagado ordenado y seguro sin corromper bases de datos, o para que entre en acción el generador de combustión de respaldo.

---

## Pregunta 25: Resiliencia de Energía a Largo Plazo (Generador de Respaldo)

### English Version
Which of the following power redundancy solutions would be the most suitable for providing long-term emergency power during an unexpected outage of the main power supply?
* [ ] Dual power supply
* [ ] Standby UPS
* [✅] **Backup generator**
* [ ] Managed PDU

### Versión en Español
¿Cuál de las siguientes soluciones de redundancia de energía sería la más adecuada para proporcionar energía de emergencia a largo plazo durante un corte inesperado de la fuente de alimentación principal?
* [ ] Fuente de alimentación dual
* [ ] UPS de reserva
* [✅] **Generador de respaldo (Backup generator)**
* [ ] PDU gestionada

### 1. Explicación General
Para responder ante incidentes graves que causen interrupciones eléctricas extendidas de largo plazo (como desastres naturales o colapso de la red de energía nacional por días enteros), las baterías químicas de los UPS del centro de datos se agotan en pocos minutos. La solución indispensable es instalar un Generador de respaldo (*Backup generator*) impulsado por un motor de combustión interna (normalmente a base de diésel, gas natural o gas propano), capaz de proveer energía de manera ininterrumpida mientras sea abastecido con combustible de forma continua.

### 2. ¿Por qué falló tu respuesta?
Elegiste *UPS de reserva*. Los sistemas UPS, incluso aquellos de grado industrial masivo, son estrictamente soluciones de corto plazo dependientes de la capacidad física máxima de sus celdas de baterías. Para garantizar la redundancia de energía a largo plazo (horas, días o semanas), el único dispositivo viable que escala con combustible externo sin requerir apagar los sistemas es el **Generador de respaldo**.

### 3. Clave para el Examen SY0-701
El plan de resiliencia ideal de un datacenter para el examen combina ambos elementos:
1. El corte eléctrico es recibido instantáneamente por el **UPS** (evitando que los servidores se apaguen o se dañen por caídas de tensión).
2. Un interruptor de transferencia automática (ATS) detecta el corte y arranca el **Generador de respaldo**.
3. El generador estabiliza sus revoluciones, y la carga eléctrica pasa del UPS al generador en cuestión de un par de minutos, manteniendo al datacenter operando indefinidamente.

---

[[ExamCompass - Cuestionarios por Temas|⬅️ Volver a Cuestionarios por Temas]]