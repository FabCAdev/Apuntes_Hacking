---
tags:
  - "#formato/lista"
  - "#gestion/relevancia/media"
  - "#gestion/estado/terminado"
  - "#gestion/dificultad/facil"
  - "#gestion/academia/hack4u"
  - "#hacking/otros"
  - "#entorno/os/linux"
  - "#desarrollo/scripting"
  - "#desarrollo/lenguaje/bash"
  - "#gestion/duracion/muy-corto"
---

### 📊 Progreso del Módulo
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

### ⚙️ 1. Introducción
- [x] 01. Bienvenido/a al curso
- [x] 02. Instalación del sistema operativo

### 🎨 2. Configurando el entorno
- [x] 03. Instalación y configuración de Bspwm y Sxhkd
- [x] 04. Instalación de la Polybar, Picom y Rofi
- [x] 05. Configurando las fuentes, la Kitty e Instalación de Feh
- [x] 06. Despliegue de la Polybar
- [x] 07. Configurando los bordeados, las sombras y los difuminados con Picom
- [x] 08. Configurando la ZSH e instalando Powerlevel10k
- [x] 09. Instalación de Batcat y Lsd
- [x] 10. Configurando y creando nuevos módulos en la Polybar
- [x] 11. Configuración e integración de NVChad en Neovim
- [x] 12. Repaso final por todos los atajos definidos

### 🎓 3. Despedida
- [x] 13. Clase final y certificado

<div style="text-align: left; margin-bottom: 20px;">
    <a href="💻 CURSOS HACK4U" class="internal-link" style="background-color: var(--interactive-accent); color: var(--text-on-accent); padding: 6px 12px; border-radius: 4px; text-decoration: none; font-weight: bold; display: inline-flex; align-items: center; gap: 5px;">
        ⬅️ Volver atras
    </a>
</div>