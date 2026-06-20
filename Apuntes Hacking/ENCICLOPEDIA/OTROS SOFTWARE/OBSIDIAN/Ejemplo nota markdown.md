
# 📓 Guía Maestra de Markdown para Obsidian

Esta nota contiene todos los formatos esenciales para documentar apuntes de ciberseguridad, programación e ingeniería.

---

## 🏗️ 1. Títulos y Jerarquía (Encabezados)
Los títulos se crean usando almohadillas `#`. Entre más uses, más pequeño es el subtítulo:

# Título Principal (H1)
## Subtítulo de Sección (H2)
### Subsección Temática (H3)
#### Detalle Técnico (H4)

---

## ✍️ 2. Formatos de Texto y Énfasis
Herramientas para hacer resaltar palabras clave en tus reportes:

* Esto es texto en **Negrita** para datos cruciales.
* Esto es texto en *Cursiva* para conceptos teóricos.
* Esto es texto ~~Tachado~~ para comandos que ya no se usan.
* Esto es texto ==Resaltado con Fluorescente== para alertas críticas.

---

## 🗂️ 3. Listas y Control de Tareas

### Lista de Viñetas (Puntos):
* Fase 1: Reconocimiento pasivo.
* Fase 2: Escaneo activo con Nmap.
* Fase 3: Explotación del sistema.

### Listas de Tareas Interactivas (Checklists):
- [x] Configurar la VPN de TryHackMe (`openvpn`)
- [x] Encontrar la vulnerabilidad web (IDOR)
- [ ] Escalar privilegios a usuario root

---

## 💻 4. Bloques de Código (Terminal y Scripts)
Para aislar comandos y código de programación. Si pones el nombre del lenguaje (como `bash`, `python`, `cpp`, `json`), Obsidian le dará colores automáticos:

```bash
# Comando para auditar procesos en segundo plano
ps -eo command | grep root
```

<div style="text-align: left; margin-bottom: 20px;">
    <a href="Uso de markdown" class="internal-link" style="background-color: var(--interactive-accent); color: var(--text-on-accent); padding: 6px 12px; border-radius: 4px; text-decoration: none; font-weight: bold; display: inline-flex; align-items: center; gap: 5px;">
        ⬅️ Volver atras
    </a>
</div>