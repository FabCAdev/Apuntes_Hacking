---
tags:
  - formato/tabla
  - estructura/seccion-principal
  - laboratorio/plataforma/htb
---
---
tags:
  - estructura/subseccion
  - formato/tabla
  - laboratorio/plataforma/htb
---
## 📖 Descripción de la Plataforma
HackTheBox es un entorno altamente competitivo y de nivel profesional enfocado en la simulación de redes e infraestructuras corporativas reales. A diferencia de otras plataformas, exige un entendimiento sólido de reconocimiento y explotación manual, simulando escenarios de cajas negras (*Black Box*).

### ⚡ Características Clave:
* **Enfoque Corporativo:** Máquinas basadas en vectores de ataque actuales del mundo real, configuraciones de red complejas y entornos empresariales.
* **Active Directory:** Laboratorios avanzados (Pro Labs / Endgames) especializados en la explotación de infraestructuras Windows Server a gran escala.
* **Sistemas Operativos:** Balance estricto entre servidores Linux avanzados y despliegues Windows complejos.

## 👤 Mi Perfil de Auditor
> [!info] Certificación y Progreso en HTB
> Puedes monitorear mi rango, puntos y máquinas retiradas directamente en mi perfil oficial:
> 🔗 **Enlace a mi Perfil:** [Tu Nombre de Usuario en HackTheBox](https://hackthebox.eu/home/users/profile/TU_ID_AQUÍ)

---

## 🗂️ Panel de Control de Intrusiones

| Máquina                   | IP            | S.O / Entorno | Dificultad                    | Técnicas de Intrusión (User)                        | Técnicas de Escalada (Root)                 | Estatus                            |
| :------------------------ | :------------ | :------------ | :---------------------------- | :-------------------------------------------------- | :------------------------------------------ | :--------------------------------- |
| [[HTB - Máquina Lame]]    | `10.10.10.3`  | Linux         | #laboratorio/dificultad/facil | Explotación de Samba (Siri) / Vsftpd backdoor       | Abuso de privilegios SUID (nmap)            | #laboratorio/estado/root-flag      |
| [[HTB - Máquina Legacy]]  | `10.10.10.4`  | Windows       | #laboratorio/dificultad/facil | Explotación de SMBv1 (EternalBlue - MS17-010)       | Privilegios heredados (NT AUTHORITY\SYSTEM) | #laboratorio/estado/root-flag      |
| [[HTB - Máquina Nibbles]] | `10.10.10.75` | Linux         | #laboratorio/dificultad/facil | Explotación de plugin vulnerable en Apache          | Abuso de permisos en archivo Sudoers        | #laboratorio/estado/user-flag      |
| [[HTB - Máquina Blue]]    | `10.10.10.40` | Windows       | #laboratorio/dificultad/facil | Pentesting de SMB / Escaneo e inyección de MS17-010 | Ejecución directa de payload en memoria     | #laboratorio/estado/reconocimiento |

---
[[CAPTURE THE FLAG|⬅️ Volver a CAPTURE THE FLAG]]