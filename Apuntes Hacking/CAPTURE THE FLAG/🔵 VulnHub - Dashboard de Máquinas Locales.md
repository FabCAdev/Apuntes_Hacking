---
tags:
  - formato/tabla
  - laboratorio/plataforma/vulnhub
  - estructura/seccion-principal
---
## 📖 Descripción de la Plataforma
VulnHub provee un catálogo abierto de imágenes de discos virtuales (VMs) vulnerables por diseño. A diferencia de las plataformas Cloud, requiere que configures y gestiones el entorno de red de forma local, simulando una auditoría física en una red interna.

### ⚡ Características Clave:
* **Auditoría Local Disconectada:** Despliegue completo dentro de hipervisores locales (VirtualBox o VMware) sin depender de conexiones a internet o VPNs.
* **Configuración de Red Real:** Exige dominar el descubrimiento inicial de hosts mediante técnicas de ARP scanning y Netdiscover.
* **Cajas Clásicas y Creativas:** Incluye retos de la vieja escuela y enfoques basados en acertijos lógicos complejos (*CTF Pure*).

## 👤 Mi Perfil de Auditor
> [!info] Registro Local de Operaciones
> *Nota: Al ser una plataforma descentralizada, las soluciones y progreso se gestionan de forma local en este baúl de Obsidian.*
> 🔗 **Repositorio Personal:** [[🔵 VulnHub - Dashboard de Máquinas Locales]] (Progreso General)

---

## 🗂️ Panel de Control de Máquinas Locales

| Máquina Local                  | IP            | S.O / Entorno | Dificultad                    | Técnicas de Intrusión (User)                    | Técnicas de Escalada (Root)                  | Estatus                         |
| :----------------------------- | :------------ | :------------ | :---------------------------- | :---------------------------------------------- | :------------------------------------------- | :------------------------------ |
| [[VulnHub - Kioptrix Level 1]] | `192.168.1.X` | Linux         | #laboratorio/dificultad/facil | Explotación de vulnerabilidad en Apache mod_ssl | Explotación local del Kernel (OpenFuck)      | #laboratorio/estado/root-flag   |
| [[VulnHub - Kioptrix Level 2]] | `192.168.1.Y` | Linux         | #laboratorio/dificultad/facil | SQL Injection manual para evasión de Login web  | Explotación del Kernel (Linux sock_sendpage) | #laboratorio/estado/sin-empezar |

---
[[CAPTURE THE FLAG|⬅️ Volver a CAPTURE THE FLAG]]