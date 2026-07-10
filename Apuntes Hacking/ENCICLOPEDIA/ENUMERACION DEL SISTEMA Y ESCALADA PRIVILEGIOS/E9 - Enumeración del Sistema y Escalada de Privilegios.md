---
tags:
  - estructura/subseccion
  - formato/lista
---
Índice maestro de técnicas ofensivas para la elevación de privilegios en sistemas comprometidos.

## 🗂️ Nodos de Conocimiento (Conceptos)
- [[PrivEsc - Abuso de Permisos Sudoers]]
	- *Descripción:* Explotación de comandos asignados sin contraseña (`sudo -l`).
- [[PrivEsc - Explotación de Binarios SUID]]
	- *Descripción:* Búsqueda de ejecutables con privilegios heredados del propietario (root).
- [[PrivEsc - Tareas Cron y Scripts Desprotegidos]]
	- *Descripción:* Secuestro de tareas automatizadas del sistema con permisos de escritura.
- [[PrivEsc - Path Hijacking (Manipulación de Variables)]]
	- *Descripción:* Alteración de rutas de ejecución para interceptar comandos legítimos.
- [[PrivEsc - Detección y Abuso de Capabilities]]
	- *Descripción:* Elevación mediante privilegios granulares asignados a herramientas comunes.
- [[PrivEsc - Explotaciones de Kernel y Servicios Locales]]
	- *Descripción:* Compilación de exploits locales e interceptación de puertos internos del sistema.
- [[PrivEsc - Secuestro de Bibliotecas (.so / .dll)]]
	- *Descripción:* Abuso de cargas dinámicas mal implementadas en el arranque de aplicaciones.
- [[PrivEsc - Docker Breakout (Escape de Contenedores)]]
	- *Descripción:* Rompimiento de aislamiento desde entornos Docker hacia el Host anfitrión.
- [[Recurso - GTFOBins como Guía de Escalada SUID/Sudoers]]
	- *Descripción:* Catálogo estricto para forzar shells interactivas de root usando binarios legítimos.

---
[[📖 ENCICLOPEDIA|⬅️ Volver a 📖 ENCICLOPEDIA]]