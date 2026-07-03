---
tags:
  - "#estructura/subseccion-principal"
  - "#formato/apunte"
  - "#gestion/duracion/muy-corto"
  - "#gestion/relevancia/muy-alta"
  - "#gestion/estado/en-curso"
  - "#gestion/dificultad/facil"
  - "#hacking/red-team"
  - "#auditoria/reconocimiento"
  - "#auditoria/enumeracion"
  - "#tecnologia/servicio/http-s"
  - "#herramientas/burp-suite"
---
## 📌 ¿Qué es Burp Suite y para qué sirve?

Burp Suite es un entorno integrado diseñado específicamente para realizar pruebas de seguridad en aplicaciones web. Su función técnica principal es actuar como un **Proxy Interceptador Local (Man-in-the-Middle)**. Se posiciona directamente en medio del flujo de comunicación entre tu navegador web de auditoría y el servidor de la aplicación objetivo.

Al capturar este tráfico, te otorga visibilidad absoluta sobre la "anatomía real" de la web: peticiones HTTP ocultas, cabeceras personalizadas, cookies de sesión, parámetros y tokens de seguridad. Su propósito fundamental en una auditoria es darte el control total del tráfico para manipular los datos antes de que viajen hacia el servidor, permitiéndote evaluar de forma manual o automatizada si la lógica del backend puede ser vulnerada.

Es una herramienta de prueba de penetración donde fácilmente puedes manipular los datos o encontrar diversas vulnerabilidades de seguridad que se presentan en aplicaciones web. Es de los mas populares e importantes para la industria de la Ciberseguridad ofensiva pero también en el lado defensivo. Estaremos analizando cada una

BurpSuite cuenta con 2 versiones, 1 vendría siendo la versión gratuita y la otra de suscripción de pago con coste de 499 dolares estadounidenses anualmente.

---

## 🗺️ Mapa de Ruta del Vault: Notas por Pestañas

Tomando como base la barra de herramientas de la suite, dividiremos la documentación técnica en notas individuales separadas dentro de Obsidian para analizar cada módulo a fondo:

### 🧩 Módulo 1: Gestión y Reconocimiento Primario
* [[01. Dashboard]]: Monitoreo del rendimiento, estado del proxy, logs del sistema y visualización de tareas activas/pasivas (vulnerabilidades detectadas automáticamente).
* [[02. Target]]: Definición del objetivo. Configuración estricta del **Scope** (alcance) para evitar auditar webs ajenas, y análisis detallado del **Site Map** (árbol de directorios de la app).
* [[03. Proxy]]: Interceptación pura de tráfico. Modificación en caliente de `Requests` (Peticiones) y `Responses` (Respuestas), reglas de filtrado y configuración de listeners.

### 🧪 Módulo 2: Ataque, Análisis y Manipulación Avanzada
* [[04. Intruder]]: Motor de automatización y Fuzzing. Configuración de tipos de ataque (*Sniper, Battering Ram, Pitchfork, Cluster Bomb*) para inyección de payloads o fuerza bruta.
* [[05. Repeater]]: Manipulación manual dirigida. Modificación y reenvío repetitivo de peticiones individuales para estudiar las respuestas del servidor sin alterar la navegación.
* [[06. Collaborator]]: Identificación de vulnerabilidades fuera de banda (OOB - Out of Band). Captura de interacciones DNS, HTTP o SMTP generadas a ciegas por el servidor web.

### 📊 Módulo 3: Procesamiento de Datos y Logs
* [[07. Sequencer]]: Análisis estadístico de la aleatoriedad de los tokens de sesión (`Session IDs`), cookies o CSRF tokens para determinar si son predecibles.
* [[08. Decoder]]: Herramienta de conversión rápida. Codificación y decodificación manual o en cadena (URL, Base64, Hex, HTML, hashes) para evadir sanitizaciones.
* [[09. Comparer]]: Utilidad visual de análisis de diferencias (*diff*). Comparación byte a byte o por palabras entre dos respuestas para detectar sutiles cambios lógicos.
* [[10. Logger]]: Historial cronológico completo de todo el tráfico procesado por Burp Suite (incluyendo lo modificado por otros módulos).

### ⚙️ Módulo 4: Organización y Entorno
* [[11. Organizer]]: Repositorio interno para almacenar, clasificar y añadir notas sobre peticiones interesantes que sirvan de evidencia para el reporte final.
* [[12. Extensions]]: Gestión del ecosistema (antiguo Extender) y acceso a la **BApp Store** para instalar complementos que añaden utilidades especializadas de la comunidad.
* [[13. Learn]]: Centro de documentación nativo de PortSwigger con guías rápidas de configuración y recursos educativos integrados.

## 🎯 Caso de Prueba Final (Laboratorio Práctico)

* [[14. Caso Practica - Auditoria Web de practica de SQLI]]: Una documentación paso a paso donde unificaremos las funciones mas importantes de Burp Suite, mediante un contenedor de docker creado para practicar la vulnerabilidad SQLI. 
  
  **Flujo operativo:** Mapearemos el objetivo (`Target`) -> interceptaremos credenciales (`Proxy`) -> modificaremos el flujo (`Repeater`) -> automatizaremos un bypass con fuzzing (`Intruder`) -> decodificaremos respuestas encoded (`Decoder`) -> validaremos diferencias (`Comparer`) para cerrar la auditoria de forma exitosa.

## Características de la versión de pago

- [[15. Características de la versión de pago ]]: Analizaremos las características de la versión de pago de Burp Suite

---

[[E3 - Reconocimiento Pasivo y Activo|⬅️ Volver a Reconocimiento Pasivo y Activo]]