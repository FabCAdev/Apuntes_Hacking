---
tags:
  - "#formato/lista"
  - gestion/relevancia/alta
  - gestion/estado/terminado
  - gestion/dificultad/normal
  - "#gestion/academia/hack4u"
  - "#hacking/otros"
  - entorno/os/linux
  - "#tecnologia/redes"
  - "#tecnologia/servicio/ssh"
  - "#desarrollo/scripting"
  - "#desarrollo/lenguaje/bash"
  - "#gestion/duracion/medio"
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

### 🐧 1. Introducción
- [x] 01. Bienvenido/a al curso
- [x] 02. Sistemas operativos para pentesting
- [x] 03. Creando una nueva máquina virtual
- [x] 04. Instalación del sistema operativo

### 🛠️ 2. Temario
- [x] 05. Comandos básicos de Linux (1-2)
- [x] 06. Comandos básicos de Linux (2-2)
- [x] 07. Control del flujo stderr-stdout, operadores y procesos en segundo plano
- [x] 08. Descriptores de archivo
- [x] 09. Cuestionario de control de flujo y operadores
- [x] 10. Lectura e interpretación de permisos (1-2)
- [x] 11. Lectura e interpretación de permisos (2-2)
- [x] 12. Asignación de permisos (1-2)
- [x] 13. Asignación de permisos (2-2)
- [x] 14. Notación octal de permisos
- [x] 15. Permisos especiales - Sticky Bit
- [x] 16. Control de atributos de ficheros en Linux - Chattr y Lsattr
- [x] 17. Permisos especiales - SUID y SGID
- [x] 18. Cuestionario de permisos
- [x] 19. Privilegios especiales - Capabilities
- [x] 20. Estructura de directorios del sistema
- [x] 21. Uso de bashrc y zshrc
- [x] 22. Actualización y Upgradeo del sistema
- [x] 23. Uso y manejo con Tmux
- [x] 24. Búsquedas a nivel de sistema
- [x] 25. Creación de scripts en Bash
- [x] 26. Uso y configuración de la Kitty
- [x] 27. Uso del editor Vim

### 🦉3. OverTheWire
- [x] 28. Conexiones SSH
- [x] 29. Lectura de archivos especiales (1-2)
- [x] 30. Lectura de archivos especiales (2-2)
- [x] 31. Directorios y archivos ocultos
- [x] 32. Detección del tipo y formato de archivos
- [x] 33. Búsquedas precisas de archivos (1-2)
- [x] 34. Búsquedas precisas de archivos (2-2)
- [x] 35. Métodos de filtrado de datos (1-2)
- [x] 36. Método de filtrado de datos (2-2)
- [x] 37. Interpretación de archivos binarios
- [x] 38. Codificación y decodificación en base64
- [x] 39. Cifrado césar y uso de tr para la traducción de caracteres
- [x] 40. Creamos un descompresor recursivo automático de archivos en Bash
- [x] 41. Manejo de pares de claves y conexiones SSH
- [x] 42. Uso de netcat para realizar conexiones
- [x] 43. Uso de conexiones encriptadas
- [x] 44. Creando nuestros propios escáneres en Bash
- [x] 45. Detección de diferencias entre archivos
- [x] 46. Ejecución de comandos por SSH
- [x] 47. Abusando de privilegio SUID para migrar de usuario
- [x] 48. Jugando con conexiones
- [x] 49. Abusando de tareas Cron (1-3)
- [x] 50. Abusando de tareas Cron (2-3)
- [x] 51. Abusando de tareas Cron (3-3)
- [x] 52. Comprendiendo las expresiones de las tareas Cron
- [x] 53. Cuestionario de tareas Cron
- [x] 54. Fuerza bruta aplicada a conexiones
- [x] 55. Escapando del contexto de un comando
- [x] 56. Operando con proyectos de Github (1-5)
- [x] 57. Operando con proyectos de Github (2-5)
- [x] 58. Operando con proyectos de Github (3-5)
- [x] 59. Operando con proyectos de Github (4-5)
- [x] 60. Operando con proyectos de Github (5-5)
- [x] 61. Argumentos posicionales en Bash
- [x] 62. Cuestionario de conceptos y comandos en Linux

### 💻 4. Scripting en Bash - Principiante a Avanzado (Primer Proyecto)
- [x] 63. PRIMER PROYECTO – Creando un buscador
- [x] 64. Scripting en Bash (1-15)
- [x] 65. Scripting en Bash (2-15)
- [x] 66. Scripting en Bash (3-15)
- [x] 67. Scripting en Bash (4-15)
- [x] 68. Scripting en Bash (5-15)
- [x] 69. Scripting en Bash (6-15)

### 💻 5. Scripting en Bash - Principiante a Avanzado (Segundo Proyecto)
- [x] 70. SEGUNDO PROYECTO – Desafiando la ruleta de un casino
- [x] 71. Scripting en Bash (1-15) 
- [x] 72. Scripting en Bash (2-15) 
- [x] 73. Scripting en Bash (3-15) 
- [x] 74. Scripting en Bash (4-15) 
- [x] 75. Scripting en Bash (5-15) 
- [x] 76. Scripting en Bash (6-15) 
- [x] 77. Scripting en Bash (7-15)
- [x] 78. Scripting en Bash (8-15)
- [x] 79. Scripting en Bash (9-15)
- [x] 80. Scripting en Bash (10-15)
- [x] 81. Scripting en Bash (11-15)
- [x] 82. Scripting en Bash (12-15)
- [x] 83. Scripting en Bash (13-15)
- [x] 84. Scripting en Bash (14-15)
- [x] 85. Scripting en Bash (15-15)

### 📝 6. Examen Final
- [x] 86. Examen final de tensión máxima

### 🎓 7. Despedida
- [x] 87. Clase final y certificado

<div style="text-align: left; margin-bottom: 20px;">
    <a href="💻 CURSOS HACK4U" class="internal-link" style="background-color: var(--interactive-accent); color: var(--text-on-accent); padding: 6px 12px; border-radius: 4px; text-decoration: none; font-weight: bold; display: inline-flex; align-items: center; gap: 5px;">
        ⬅️ Volver atras
    </a>
</div>