---
tags:
  - formato/tabla
  - laboratorio/plataforma/portswigger
  - estructura/seccion-principal
---
## 📖 Descripción de la Plataforma
Creada por los desarrolladores de **Burp Suite**, esta academia es el estándar de la industria para auditorías de aplicaciones web. Se enfoca exclusivamente en la capa de aplicación (Capa 7 del modelo OSI), prescindiendo de infraestructuras de red o sistemas operativos para centrarse puramente en código, APIs y lógica de negocio.

### ⚡ Características Clave:
* **Especialización OWASP Top 10:** Laboratorios profundos de inyecciones SQL, XSS, CSRF, fallas lógicas, deseserialización insegura y vulnerabilidades de APIs.
* **Integración con Burp Suite:** Diseñado para exprimir al máximo el proxy, repetidor, intrusor y extensiones de Burp.
* **Niveles de Seguridad:** Laboratorios categorizados desde nivel aprendiz (*Practitioner*) hasta experto experto (*Expert*).

## 👤 Mi Perfil de Auditor
> [!info] Progreso Académico PortSwigger
> Control de laboratorios web resueltos bajo la suite de Burp Suite:
> 🔗 **Enlace a mi Perfil:** [Mi Cuenta en PortSwigger Academy](https://portswigger.net/web-security/my-account)

---

## 🗂️ Panel de Control de Vulnerabilidades Web

| Módulo Web                             | Vector / URL         | Entorno      | Dificultad                    | Técnicas de Intrusión (Web)                      | Escalada de Privilegios Web                        | Estatus                         |
| :------------------------------------- | :------------------- | :----------- | :---------------------------- | :----------------------------------------------- | :------------------------------------------------- | :------------------------------ |
| [[PortSwigger - SQL Injection]]        | Parámetro `category` | Web Server   | #laboratorio/dificultad/facil | SQLi basada en errores / UNION-based manual      | Inyección para extraer hashes de administrador     | #laboratorio/estado/root-flag   |
| [[PortSwigger - Cross-Site Scripting]] | Parámetro `search`   | Web Browser  | #laboratorio/dificultad/facil | Reflected XSS / Stored XSS en comentarios        | Robo de cookies de sesión para secuestro de cuenta | #laboratorio/estado/user-flag   |
| [[PortSwigger - File Inclusion]]       | Parámetro `filename` | Linux Server | #laboratorio/dificultad/media | Path Traversal (`../../etc/passwd`) / LFI manual | Log Poisoning mediante cabecera User-Agent         | #laboratorio/estado/sin-empezar |

---
<div style="text-align: left; margin-top: 20px;">
    <a href="CAPTURE THE FLAG" class="internal-link" style="background-color: var(--interactive-accent); color: var(--text-on-accent); padding: 6px 12px; border-radius: 4px; text-decoration: none; font-weight: bold; display: inline-flex; align-items: center; gap: 5px;">
        ⬅️ Volver a Capture The Flag
    </a>
</div>