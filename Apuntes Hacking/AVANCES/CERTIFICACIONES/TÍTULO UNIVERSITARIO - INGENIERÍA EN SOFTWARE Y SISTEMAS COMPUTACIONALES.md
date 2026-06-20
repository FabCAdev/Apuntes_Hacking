---
tags:
  - formato/documentacion
  - gestion/duracion/muy-largo
---
# 🏛️ Control de Hito Académico: Universidad De La Salle Bajío

* **Carrera:** Ingeniería en Software y Sistemas Computacionales
* **Plan de Estudios:** 4 Años / 8 Semestres
* **Estatus Global:** #gestion/estado/en-curso
* **Dificultad Percibida:** #gestion/dificultad/muy-dificil

---

## 📅 1. Mapa de Progreso y Semestres

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

- [x] Semestre 01
- [x] Semestre 02
- [x] Semestre 03
- [x] Semestre 04
- [ ] Semestre 05
- [ ] Semestre 06
- [ ] Semestre 07
- [ ] Semestre 08

---

## 📚 2. Asignaturas Clave & Conexiones Técnicas

* **FUNDAMENTOS DE PROGRAMACION / POO:** -> Vinculado a #entorno/os 
* **INFRAESTRUCTURA Y SEGURIDAD EN LA NUBE:** -> Vinculado a ciberseguridad
* **INFRAESTRUCTURA DE REDES Y SERVIDORES:** -> Vinculado a `#tecnologia/redes`
* **SISTEMAS OPERATIVOS:** -> Vinculado a `#entorno/os/linux` y `#entorno/os/windows`
* **BASE DE DATOS:** -> Vinculado a `#vulnerabilidades/web/sqli`
* **BASES DE DATOS NO RELACIONALES**

---

<div style="text-align: left; margin-bottom: 20px;">
    <a href="🏅 CERTIFICACIONES" class="internal-link" style="background-color: var(--interactive-accent); color: var(--text-on-accent); padding: 6px 12px; border-radius: 4px; text-decoration: none; font-weight: bold; display: inline-flex; align-items: center; gap: 5px;">
        ⬅️ Volver atras
    </a>
</div>