---
tags:
  - estructura/nodo-principal
  - formato/lista
---
# 📚 ENCICLOPEDIA: Base de Conocimiento Técnico

Repositorio modular de metodologías ofensivas, administración de sistemas, explotación de vulnerabilidades y herramientas de auditoria.

---

## 🗂️ Módulos de Conocimiento Estructurado

### 💻 Fase 1: Fundamentos e Infraestructura
* **[[E1 - Conceptos Base (Sistemas y Fundamentos de Redes)]]**
	- *Contenido:* Arquitectura OS, protocolos de red y comandos esenciales de diagnóstico (Ej: Identificación de OS mediante **TTL / Ping**).
* **[[E2 - Tecnologías Clave y Plataformas]]**
	- *Contenido:* Ecosistema del auditor (GitHub, LinkedIn, Obsidian, Google Dorking, HackerOne, HackTheBox, TryHackMe, Exploit-DB, Docker).
	- *Recurso Global:* Integración de **Hacktricks** como enciclopedia de consulta externa prioritaria.
* **[[E4 - VMs y Docker]]**
	- *Contenido:* Despliegue de laboratorios aislados, gestión de contenedores, imágenes y entornos de práctica controlados.
* **[[E5 - GitHub]]**
	- *Contenido:* Control de versiones, gestión de repositorios personales, automatizaciones y búsqueda de fugas de información (Leaks).

### 🔍 Fase 2: Reconocimiento y Enumeración (Infraestructura y Web)
* **[[E3 - Reconocimiento Pasivo y Activo]]**
	- *Contenido:* Nmap, Wireshark, Wappalyzer, WhatWeb, BuiltWith, Subdominios, Fuzzing con wFuzz, Hunter.io, Intelligence X, Phonebook.cz, Clearbit Connect, PimEyes y DeHashed.
	- *Recurso:* Uso de la suite web **Pentest-Tools** para recolección pasiva automatizada.
* **[[E6 - Enumeración de Servicios y CMS]]**
	- *Contenido:* Auditoría de protocolos comunes (FTP, SSH, HTTP/S, SMB) y vectores de ataque en gestores de contenido (WordPress, Joomla, Drupal, Magento).

### 🚀 Fase 3: Explotación e Intrusión
* **[[E7 - Conceptos Básicos de Explotación]]**
	- *Contenido:* Tipos de Shells (Bind, Reverse y Forward), tipos de Payloads (Staged y Non-staged) y metodologías operativas (Explotaciones Automáticas vs. Manuales).
* **[[E8 - Vulnerabilidades y OWASP Top 10]]**
	- *Contenido:* Explotación profunda de fallas lógicas: SQLI, XSS, XXE, LFI, RFI, Log Poisoning y vectores web críticos.
* **[[E10 - Buffer Overflow]]**
	- *Contenido:* Corrupción de memoria, control de registros (EIP/RIP), inyección de Shellcodes y evasión básica de protecciones en arquitecturas x86/x64.

### 🛡️ Fase 4: Post-Explotación, Escalada y Movimiento Lateral
* **[[E9 - Enumeración del Sistema y Escalada de Privilegios]]**
	- *Contenido:* Abuso de Sudoers, permisos SUID, tareas Cron, Path Hijacking, permisos incorrectos, Capabilities, exploits de Kernel, usuarios especiales, servicios internos, secuestro de bibliotecas (.so/.dll) y Docker Breakout.
	- *Recurso Crítico:* Consulta estricta a **GTFOBins** para el abuso de binarios legítimos y elevación a Root.
* **[[E11 - Pivoting y Enrutamiento]]**
	- *Contenido:* Salto entre redes internas, técnicas de port-forwarding, túneles SSH, Chisel, Socat y compromiso de subredes aisladas.
* **[[E13 - Active Directory y Hacking Corporativo]]** - *Contenido:* Arquitectura de dominios Windows, Kerberos, enumeración con BloodHound/NetExec, ataques de extracción de tickets (Kerberoasting, ASREPRoasting) y movimiento lateral. 

### ☁️ Fase 5: Infraestructura Moderna y Cloud
* **[[E14 - Seguridad y Hacking en la Nube (Cloud & Kubernetes)]]**
	- *Contenido:* Enumeración de servicios AWS/Azure, fugas de información en Buckets S3, explotación de IAM y auditoría de clústeres Kubernetes.
### 🤖 Fase 6: Automatización y Desarrollo
* **[[E12 - Programación y Scripting]]**

[[Uso de markdown]]

<div style="text-align: left; margin-bottom: 20px;">
    <a href="🛡️ HACKING" class="internal-link" style="background-color: var(--interactive-accent); color: var(--text-on-accent); padding: 6px 12px; border-radius: 4px; text-decoration: none; font-weight: bold; display: inline-flex; align-items: center; gap: 5px;">
        ⬅️ Volver atras
    </a>
</div>