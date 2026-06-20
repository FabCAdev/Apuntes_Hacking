### 1. Arquitectura del Baúl (`#estructura/` y `#formato/`)
#estructura/nodo-principal              -> Centro que conecta todo
#estructura/seccion-principal           -> Principales categorías (Ej: AVANCES)
#estructura/subseccion-principal        -> Subcategorías mayores (Ej: CURSOS HACK4U)
#estructura/subseccion                  -> Módulos formativos derivados (Ej: INTRO LINUX)

#gestion/duracion/muy-corto             -> Duración muy corta (Ej: Horas / Conceptos rápidos)
#gestion/duracion/corto                  -> Duración corta (Ej: Dias / Módulos simples)
#gestion/duracion/medio                  -> Duración media (Ej: Semanas / Máquinas intermedias)
#gestion/duracion/largo                  -> Duración larga (Ej: Meses (hasta medio año) / Cursos completos)
#gestion/duracion/muy-largo              -> Duración muy larga (Ej: Mas de Medio Año / Proyectos de desarrollo o Universidad)

#formato/lista                          -> Contenido basado en listas
#formato/tabla                          -> Contenido basado en tablas
#formato/apunte                         -> Contenido basado en conceptos/apuntes teóricos
#formato/cheatsheet                     -> Listas rápidas de puros comandos
#formato/documentacion                  -> Informes técnicos o reportes de auditoría

### 2. Gestión y Progreso (`#gestion/`)
#gestion/relevancia/muy-alta            -> Relevancia Muy Alta
#gestion/relevancia/alta                -> Relevancia Alta
#gestion/relevancia/media               -> Relevancia Media
#gestion/relevancia/baja                -> Relevancia Baja
#gestion/relevancia/nula                -> Relevancia Nula

#gestion/estado/sin-empezar             -> No iniciado
#gestion/estado/en-curso                -> En ejecución actualmente
#gestion/estado/pausado                 -> Detenido temporalmente
#gestion/estado/terminado               -> Finalizado con éxito

#gestion/dificultad/muy-facil           -> Nula o poca dificultad
#gestion/dificultad/facil               -> Poca dificultad
#gestion/dificultad/normal              -> Dificultad media
#gestion/dificultad/dificil             -> Alta dificultad
#gestion/dificultad/muy-dificil         -> Dificultad extrema

#gestion/academia/hack4u                -> Contenido perteneciente a la academia Hack4U

### 3. Categorización de la Seguridad (`#hacking/`)
#hacking/fundamental                    -> Nota esencial de Ciberseguridad / Hacking
#hacking/otros                          -> Aporta valor pero no es 100% hacking
#hacking/red-team                       -> Orientado a la seguridad ofensiva 🔴
#hacking/blue-team                      -> Orientado a la seguridad defensiva 🔵
#hacking/purple-team                    -> Orientado a la seguridad mixta / táctica 🟣

### 4. Entornos y Sistemas Operativos (`#entorno/`)
#entorno/os/windows                     -> Entorno operativo Windows
#entorno/os/linux                       -> Entorno operativo Linux
#entorno/os/mac                         -> Entorno operativo macOS
#entorno/os/android                     -> Entorno operativo Android
#entorno/os/ios                         -> Entorno operativo iOS (Corregido !Phone)

#entorno/infra/virtual-machine          -> Uso de Hipervisores / Máquinas Virtuales
#entorno/infra/docker                   -> Despliegue o explotación de contenedores
#entorno/infra/servidor-local           -> Pruebas en el mismo equipo (localhost)
#entorno/infra/servidor-remoto          -> Pruebas dirigidas a hosts externos

### 5. Fases de Auditoría y Desarrollo (`#auditoria/`)
#auditoria/reconocimiento                -> Recolección pasiva/activa de información
#auditoria/reconocimiento/subdominios    -> Descubrimiento de estructuras de dominios
#auditoria/reconocimiento/google-dorks   -> Uso de operadores de búsqueda avanzada

#auditoria/enumeracion                   -> Identificación activa de vectores de ataque
#auditoria/enumeracion/servicios         -> Identificación de software expuesto
#auditoria/enumeracion/cms               -> Análisis de gestores de contenido

#auditoria/fuzzing                       -> Pruebas automatizadas de fuerza bruta web

#auditoria/explotacion/manual            -> Intrusión manual sin scripts automáticos
#auditoria/explotacion/automatizada      -> Intrusión apoyada por herramientas de terceros

#auditoria/maquinas                      -> Conexión y compromiso de un Host/Target

#auditoria/pivoting                      -> Movimiento lateral y salto entre redes

### 6. Protocolos, Servicios y CMS (`#tecnologia/`)
#tecnologia/redes                       -> Conceptos teóricos de Redes y Telecomunicaciones

#tecnologia/protocolo/tcp-ip            -> Arquitectura de la suite TCP/IP
#tecnologia/protocolo/modelo-osi         -> Capas del Modelo OSI

#tecnologia/servicio/ftp                -> Auditoría al puerto 21 (File Transfer Protocol)
#tecnologia/servicio/ssh                -> Auditoría al puerto 22 (Secure Shell)
#tecnologia/servicio/http-s             -> Auditoría a los puertos 80/443 (Web)
#tecnologia/servicio/smb                -> Auditoría a los puertos 139/445 (Server Message Block)

#tecnologia/cms/wordpress               -> Explotación específica en WordPress
#tecnologia/cms/joomla                  -> Explotación específica en Joomla
#tecnologia/cms/drupal                  -> Explotación específica en Drupal
#tecnologia/cms/magento                 -> Explotación específica en Magento

#tecnologia/infra/active-directory      -> Entornos de dominio corporativo de Windows / AD
#tecnologia/cloud 

### 7. Lenguajes y Desarrollo (`#desarrollo/`)
#desarrollo/programacion                -> Contenido conceptual de programación
#desarrollo/scripting                   -> Automatización mediante Scripts

#desarrollo/lenguaje/bash               -> Desarrollo o uso intensivo de scripts en Bash
#desarrollo/lenguaje/python             -> Desarrollo o uso intensivo de scripts en Python
#desarrollo/lenguaje/lua                -> Configuración o scripting en Lua

### 8. Herramientas y Plataformas (`#herramientas/`)
#herramientas/obsidian                  -> Uso u optimización de este editor de notas
#herramientas/nmap                      -> Escaneo y detección con Nmap
#herramientas/firewall                  -> Evasión o análisis de Firewalls / WAFs
#herramientas/burp-suite                -> Uso de BurpSuite para interceptar tráfico
#herramientas/metasploit                -> Uso de la suite Metasploit Framework
#herramientas/sqlmap                    -> Automatización de inyecciones con SQLMap
#herramientas/immunity-debugger         -> Ingeniería inversa con Immunity Debugger
#herramientas/plataforma/github         -> Repositorios y control de versiones con Git
#herramientas/plataforma/hackerone       -> Plataforma de Bug Bounty HackerOne
#herramientas/multimedia/imagenes       -> Manipulación o análisis de imágenes (Esteganografía)

### 9. Técnicas y Vectores de Acceso (`#vectores/`)
#vectores/phishing                      -> Ingeniería social para clonación o credenciales
#vectores/shells/reverse                -> Establecimiento de conexiones inversas
#vectores/shells/bind                   -> Establecimiento de conexiones atadas a puerto
#vectores/shells/forward                -> Simulación de shell interactiva mediante archivos
#vectores/payloads/staged               -> Ejecución de cargas útiles por etapas
#vectores/payloads/non-staged           -> Ejecución de cargas útiles completas monolíticas

### 10. Vulnerabilidades Web (`#vulnerabilidades/web/`)
#vulnerabilidades/web/sqli              -> SQL Injection
#vulnerabilidades/web/nosqli            -> NoSQL Injection
#vulnerabilidades/web/xss               -> Cross-Site Scripting
#vulnerabilidades/web/xxe               -> XML External Entity Injection
#vulnerabilidades/web/lfi               -> Local File Inclusion
#vulnerabilidades/web/rfi               -> Remote File Inclusion
#vulnerabilidades/web/log-poisoning     -> Inyección de código en logs del sistema
#vulnerabilidades/web/csrf              -> Cross-Site Request Forgery
#vulnerabilidades/web/ssrf              -> Server-Side Request Forgery
#vulnerabilidades/web/ssti              -> Server-Side Template Injection
#vulnerabilidades/web/csti              -> Client-Side Template Injection
#vulnerabilidades/web/padding-oracle    -> Descifrado de información mediante Padding Oracle
#vulnerabilidades/web/type-juggling    -> Evasión de validaciones mediante Type Juggling
#vulnerabilidades/web/ldapi             -> LDAP Injection
#vulnerabilidades/web/deserialization   -> Insegura Deserialización de Objetos general
#vulnerabilidades/web/deserialization/yaml   -> Deserialización insegura en YAML (Python/Java)
#vulnerabilidades/web/deserialization/pickle -> Deserialización insegura en Pickle (Python)
#vulnerabilidades/web/latexi            -> LaTeX Injection
#vulnerabilidades/web/api-abuse         -> Abuso de lógica o endpoints en APIs
#vulnerabilidades/web/file-upload       -> Vulnerabilidades de subida de archivos insegura
#vulnerabilidades/web/prototype-pollution -> Abuso de la propiedad prototipo en JavaScript
#vulnerabilidades/web/axfr-attack       -> Transferencia de zona DNS no autorizada
#vulnerabilidades/web/mass-assignment   -> Modificación masiva de parámetros de objetos
#vulnerabilidades/web/open-redirect     -> Redirección abierta hacia sitios maliciosos
#vulnerabilidades/web/webdav            -> Explotación del protocolo WebDAV mal configurado
#vulnerabilidades/web/squid-proxy       -> Abuso y saltos mediante Proxies SQUID
#vulnerabilidades/web/shellshock        -> Explotación de vulnerabilidad de entorno en Bash
#vulnerabilidades/web/xpathi            -> XPath Injection
#vulnerabilidades/web/idors             -> Insecure Direct Object References
#vulnerabilidades/web/cors              -> Cross-Origin Resource Sharing Attack
#vulnerabilidades/web/sql-truncation    -> Truncamiento de datos en bases de datos SQL
#vulnerabilidades/web/session-fixation  -> Session Puzzling / Fixation / Overloading
#vulnerabilidades/web/jwt-attack        -> Ataques y bypasses a Json Web Tokens
#vulnerabilidades/web/race-condition    -> Condición de carrera en peticiones concurrentes
#vulnerabilidades/web/cssi              -> CSS Injection
#vulnerabilidades/web/graphql-introspection -> Exposición de esquemas por introspección GraphQL
#vulnerabilidades/infraestructura 

### 11. Laboratorios Hacking (`#laboratorio/`)

#laboratorio/plataforma/htb -> Para todas tus máquinas de HackTheBox.
#laboratorio/plataforma/thm -> Para tus salas y retos de TryHackMe.
#laboratorio/plataforma/vulnhub -> Para las máquinas virtuales locales de VulnHub.
#laboratorio/plataforma/portswigger -> Para los retos específicos de la academia web.

#laboratorio/dificultad/easy -> Dificultad del laboratorio fácil
#laboratorio/dificultad/medium -> Dificultad del laboratorio media
#laboratorio/dificultad/hard -> Dificultad del laboratorio dificil
#laboratorio/dificultad/insane -> Dificultad del laboratorio muy dificil

#laboratorio/estado/sin-empezar -> Máquina en cola (en lista de pendientes).
#laboratorio/estado/reconocimiento -> Ya se escaneo los puertos con Nmap y estás buscando el vector.
#laboratorio/estado/user-flag -> Se consiguio intrusión inicial y se obtuvo la flag de usuario de bajo privilegio.
#laboratorio/estado/root-flag -> Se escalo privilegios con éxito, convirtiendo root / system y la máquina está 100% comprometida.