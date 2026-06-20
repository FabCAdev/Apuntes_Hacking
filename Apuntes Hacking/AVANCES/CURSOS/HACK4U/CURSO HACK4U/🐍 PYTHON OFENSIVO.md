---
tags:
  - "#formato/lista"
  - "#gestion/relevancia/muy-alta"
  - "#gestion/estado/en-curso"
  - "#gestion/academia/hack4u"
  - "#hacking/fundamental"
  - "#entorno/os/linux"
  - "#tecnologia/redes"
  - "#desarrollo/scripting"
  - desarrollo/lenguaje/python
  - gestion/dificultad/normal
  - "#gestion/duracion/largo"
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

### ⚙️ 1. Introducción al curso
- [x] 01. Bienvenido/a al curso

### 🐍 2. Introducción a Python
- [x] 02. Historia y filosofía de Python
- [x] 03. Características y ventajas de Python
- [x] 04. Diferencias entre Python2, Python3, PIP2 y PIP3

### 💻 3. Conceptos básicos de Python
- [x] 05. El intérprete de Python
- [x] 06. Shebang y convenios en Python
- [ ] 07. Variables y tipos de datos
- [ ] 08. Operadores básicos en Python
- [ ] 09. String Formatting
- [ ] 10. Control de flujo (Condicionales y Bucles)
- [ ] 11. Funciones y ámbito de las variables
- [ ] 12. Funciones lambda anónimas
- [ ] 13. Manejo de errores y excepciones
- [ ] 14. Cuestionario de conceptos básicos

### 📊 4. Colecciones y estructuras de datos en Python
- [ ] 15. Listas
- [ ] 16. Tuplas
- [ ] 17. Conjuntos
- [ ] 18. Diccionarios
- [ ] 19. Proyecto de videojuegos
- [ ] 20. Cuestionario de estructura de datos

### 🤖 5. Programación Orientada a Objetos en Python (POO)
- [ ] 21. Clases y objetos (1/2)
- [ ] 22. Clases y objetos (2/2)
- [ ] 23. Métodos estáticos y métodos de clase
- [ ] 24. Comprendiendo mejor el uso de self
- [ ] 25. Herencia y polimorfismo
- [ ] 26. Encapsulamiento y métodos especiales
- [ ] 27. Decoradores y propiedades
- [ ] 28. Cuestionario de POO

### 📦 6. Módulos y paquetes en Python
- [ ] 29. Organización del código en módulos
- [ ] 30. Importación y uso de módulos
- [ ] 31. Creación y distribución de paquetes
- [ ] 32. Cuestionario sobre módulos y paquetes en Python

### 💾 7. Entrada y salida de datos
- [ ] 33. Entrada por teclado y salida por pantalla
- [ ] 34. Lectura y escritura de archivos
- [ ] 35. Formateo de cadenas y manipulación de texto
- [ ] 36. Cuestionario de entrada y salida de datos

### 🎯 8. Proyectos de POO para reforzar lo aprendido
- [ ] 37. Proyecto de gestión de biblioteca de libros (1/2)
- [ ] 38. Proyecto de gestión de biblioteca de libros (2/2)
- [ ] 39. Proyecto de gestión de animales en tienda
- [ ] 40. Proyecto de administración de flota de vehículos
- [ ] 41. Proyecto de gestión de notas (1/2)
- [ ] 42. Proyecto de gestión de notas (2/2)

### 📚 9. Biblioteca estándar y herramientas adicionales
- [ ] 43. Manejo de fechas y horas
- [ ] 44. Expresiones regulares
- [ ] 45. Manejo de archivos y directorios
- [ ] 46. Conexiones de red y protocolos (1/4)
- [ ] 47. Conexiones de red y protocolos (2/4)
- [ ] 48. Conexiones de red y protocolos (3/4)
- [ ] 49. Conexiones de red y protocolos (4/4)
- [ ] 50. Cuestionario de biblioteca estándar y herramientas adicionales

### 🔍 10. Manejo de librerías comunes
- [ ] 51. Librería os y sys
- [ ] 52. Librería requests (1/2)
- [ ] 53. Librería requests (2/2)
- [ ] 54. Librería Urllib3
- [ ] 55. Librería threading y multiprocessing
- [ ] 56. Cuestionario de manejo de librerías comunes

### 🖥️ 11. Desarrollo de aplicaciones de escritorio con Python
- [ ] 57. Introducción a las interfaces gráficas de usuario (GUI)
- [ ] 58. Desarrollo de aplicaciones GUI con Tkinter (1/8)
- [ ] 59. Desarrollo de aplicaciones GUI con Tkinter (2/8)
- [ ] 60. Desarrollo de aplicaciones GUI con Tkinter (3/8)
- [ ] 61. Desarrollo de aplicaciones GUI con Tkinter (4/8)
- [ ] 62. Desarrollo de aplicaciones GUI con Tkinter (5/8)
- [ ] 63. Desarrollo de aplicaciones GUI con Tkinter (6/8)
- [ ] 64. Desarrollo de aplicaciones GUI con Tkinter (7/8)
- [ ] 65. Desarrollo de aplicaciones GUI con Tkinter (8/8)
- [ ] 66. Desarrollo de aplicaciones GUI avanzado con CustomTkinter
- [ ] 67. Chat Multiusuario con GUI y Cifrado E2E (1/5)
- [ ] 68. Chat Multiusuario con GUI y Cifrado E2E (2/5)
- [ ] 69. Chat Multiusuario con GUI y Cifrado E2E (3/5)
- [ ] 70. Chat Multiusuario con GUI y Cifrado E2E (4/5)
- [ ] 71. Chat Multiusuario con GUI y Cifrado E2E (5/5)
- [ ] 72. Cuestionario de interfaces gráficas

### 🦅 12. Introducción a Python Ofensivo
- [ ] 73. Previo a la explotación
- [ ] 74. Creando un escáner de puertos (1/4)
- [ ] 75. Creando un escáner de puertos (2/4)
- [ ] 76. Creando un escáner de puertos (3/4)
- [ ] 77. Creando un escáner de puertos (4/4)
- [ ] 78. Creando un programa que nos cambie la dirección MAC (macchanger)
- [ ] 79. Creando un escáner de red (ICMP)
- [ ] 80. Creando un escáner de red (ARP) con Scapy
- [ ] 81. Creando un envenenador ARP (ARP Spoofer) con Scapy
- [ ] 82. Creando un interceptor de consultas DNS (DNS Spoofer) con Scapy
- [ ] 83. Creando un interceptor de consultas HTTP (HTTP Sniffer) con Scapy
- [ ] 84. Creando un interceptor de consultas HTTPS (HTTPS Sniffer) con Mitmproxy
- [ ] 85. Creando un rastreador de imágenes con enlaces de tipo IPlogger (generador de...
- [ ] 86. Creando un DNS Spoofer con Scapy y NetfilterQueue
- [ ] 87. Creando un interceptor y modificador de archivos al vuelo (Malicious...)
- [ ] 88. Creando una Reverse Shell
- [ ] 89. Creando un Keylogger (1/2)
- [ ] 90. Creando un Keylogger (2/2)
- [ ] 91. Creación de Malware (1/2)
- [ ] 92. Creación de Malware (2/2)
- [ ] 93. Creación de Command and Control (C2) (Ejemplo) (1/2)
- [ ] 94. Creación de Backdoors y Command and Control (C2) (Ejemplo) (2/2)
- [ ] 95. Creación de Forward Shell (1/4)
- [ ] 96. Creación de Forward Shell (2/4)
- [ ] 97. Creación de Forward Shell (3/4)
- [ ] 98. Creación de Forward Shell (4/4)

### 📝 13. Examen final y certificado
- [ ] 99. Examen final de tensión máxima
- [ ] 100. Despedida

<div style="text-align: left; margin-bottom: 20px;">
    <a href="💻 CURSOS HACK4U" class="internal-link" style="background-color: var(--interactive-accent); color: var(--text-on-accent); padding: 6px 12px; border-radius: 4px; text-decoration: none; font-weight: bold; display: inline-flex; align-items: center; gap: 5px;">
        ⬅️ Volver atras
    </a>
</div>