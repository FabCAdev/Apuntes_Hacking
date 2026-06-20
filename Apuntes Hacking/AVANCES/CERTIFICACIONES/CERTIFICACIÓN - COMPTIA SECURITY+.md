---
tags:
  - formato/documentacion
  - gestion/duracion/largo
---
# 🌐 Plan de Certificación: CompTIA Security+ (SY0-701)

* **Entidad Emisora:** CompTIA
* **Tipo de Examen:** Teórico (90 preguntas máximo, opción múltiple y PBQs)
* **Puntuación de Aprobación:** 750 / 900
* **Estatus de Preparación:** #gestion/estado/sin-empezar
* **Dificultad Estimada:** #gestion/dificultad/normal
* **Tiempo Duracion:** #gestion/duracion/largo 

---

## 📚 1. Control del Temario Oficial (Dominios de CompTIA)

```dataviewjs
const markdown = await dv.io.load(dv.current().file.path);

if (markdown) {
  const allTasks = markdown.match(/^[ \t]*-[ \t]*\[[ xX]\][ \t]*(.*)$/gm) || [];
  const completedTasks = markdown.match(/^[ \t]*-[ \t]*\[[xX]\][ \t]*(.*)$/gm) || [];

  const total = allTasks.length;
  const completed = completedTasks.length;
  const percent = total > 0 ? Math.round((completed / total) * 100) : 0;

  // Creamos el texto del porcentaje de forma nativa
  dv.el("div", `${percent}% completado (${completed}/${total})`, {
    attr: { style: "font-weight: bold; margin-bottom: 5px;" }
  });

  // Creamos la barra de progreso de forma nativa para que Obsidian la dibuje sí o sí
  dv.el("progress", "", {
    attr: { 
      value: percent, 
      max: "100", 
      style: "width: 100%; height: 18px; accent-color: #f38ba8;" 
    }
  });
} else {
  dv.el("div", "No se pudo leer el archivo.");
}
```

- [ ] **Dominio 1.0: Conceptos de Seguridad (12%)**
	- *Temas:* Confidencialidad, Integridad y Disponibilidad (CIA Triad), Tipos de Controles de Seguridad.
- [ ] **Dominio 2.0: Amenazas, Vulnerabilidades y Mitigaciones (22%)**
	- *Temas:* Malware (WannaCry), Ingeniería Social (Phishing), Vectores de Ataque.
- [ ] **Dominio 3.0: Arquitectura y Diseño (18%)**
	- *Temas:* Arquitectura de Red Segura, Conceptos de Nube, Resiliencia y Seguridad Física.
- [ ] **Dominio 4.0: Operaciones de Seguridad (28%)**
	- *Temas:* Gestión de Incidentes, Herramientas de Auditoría, Criptografía (Llaves públicas/privadas).
- [ ] **Dominio 5.0: Gestión, Riesgo y Cumplimiento de Seguridad (20%)**
	- *Temas:* Gobernanza, Políticas corporativas, Evaluación de riesgos, Privacidad de datos.

---

## 🛠️ 2. Simulacros de Examen y Recursos de Estudio
*Bitácora de puntajes obtenidos en exámenes de prueba antes de presentarte al real.*

* **Recursos Principales:** Profesor Messer (YouTube/Notas), Cursos de Jason Dion (Udemy).
* **Historial de Simulacros (Target: > 85%):**
	1. `[DD/MM/AAAA]` - Simulador Dion 01: `0%` ❌
	2. `[DD/MM/AAAA]` - Simulador Dion 02: `0%` ❌

---

## 🎟️ 3. Información del Váucher y Cita del Examen
* **Fecha Programada:** `Pendiente`
* **Centro de Evaluación:** Pearson VUE (Presencial u Online)
* **Código del Váucher:** `[Ingresar código una vez comprado]`

<div style="text-align: left; margin-bottom: 20px;">
    <a href="🏅 CERTIFICACIONES" class="internal-link" style="background-color: var(--interactive-accent); color: var(--text-on-accent); padding: 6px 12px; border-radius: 4px; text-decoration: none; font-weight: bold; display: inline-flex; align-items: center; gap: 5px;">
        ⬅️ Volver atras
    </a>
</div>