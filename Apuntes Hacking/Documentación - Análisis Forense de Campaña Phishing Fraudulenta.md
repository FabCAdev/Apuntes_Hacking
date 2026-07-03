---
tags:
  - "#estructura/proyecto"
  - "#gestion/duracion/medio"
  - "#gestion/relevancia/alta"
  - "#gestion/estado/en-curso"
  - "#gestion/dificultad/normal"
  - "#hacking/defensivo"
  - "#analisis/phishing"
  - "#herramientas/burp-suite"
  - "#entorno/vmware"
---

# 🕵️‍♂️ Proyecto de Análisis: Triaje y Descomposición de Sitios Sospechosos de Phishing

## 📌 1. Contexto del Entorno e Infraestructura

Para la ejecución segura de este proyecto, se ha diseñado un laboratorio de análisis aislado que previene la ejecución de código malicioso o fugas de información hacia el sistema operativo anfitrión. La arquitectura del entorno se compone de los siguientes elementos:

* **Hipervisor:** Uso de VMware para el despliegue y control de los sistemas virtuales.
* **Sistema de Análisis:** Instancia virtualizada bajo el sistema operativo **Windows Server 22H2**, encargada de interactuar directamente con los recursos bajo sospecha.
* **Aislamiento de Red:** El adaptador de red de la máquina virtual se encuentra configurado en modo **NAT** (*Network Address Translation*), garantizando salida a internet controlada a través del segmento virtualizado del host.
* **Privacidad y Cifrado:** Uso de **OpenVPN** integrado para anonimizar los llamados salientes y mitigar el rastreo o bloqueo geográfico por parte de la infraestructura del atacante.
* **Interceptación de Tráfico:** El análisis estructural se realiza desde la **máquina nativa** (Host) utilizando **Burp Suite**, estableciendo una comunicación remota dirigida desde la máquina virtual hacia el listener de la interfaz del host.

---

## 🎯 2. Concepto y Mecánica del Vector (Phishing)

El **phishing** se define como una técnica de ataque basada en ingeniería social, cuyo propósito es suplantar la identidad visual y operativa de una plataforma legítima (entidades bancarias, servicios cloud, redes sociales). El flujo táctico del vector consta de las siguientes fases:

1. **Clonación de Interfaz:** Estructuración de un sitio web idéntico al original, empleando hojas de estilo (CSS) y recursos multimedia idénticos para engañar la percepción del usuario.
2. **Ingeniería Social:** Distribución de enlaces a través de canales dirigidos (correo electrónico, SMS, campañas maliciosas) utilizando pretextos de alta urgencia, bloqueos de seguridad o actualizaciones obligatorias.
3. **Exfiltración de Datos:** Disposición de formularios controlados por el atacante diseñados para recolectar de forma directa credenciales de acceso, datos personales, números de tarjetas de crédito o tokens de doble factor de autenticación (2FA), redirigiéndolos hacia servidores de comando o canales de mensajería privados.

---

## 🛡️ 3. Preparación de Protección para Revisión de Auditoría

Con el fin de auditar la aplicación web de manera segura, privada y bajo un estricto principio de anonimato, se implementó una serie de protocolos de hardening y tunelización en la máquina de análisis:

### A. Entorno de Navegación y Flexibilidad
Se optó por la instalación de **Firefox** como el navegador principal debido a su alto nivel de personalización de configuraciones internas, aislamiento de cookies y flexibilidad en el manejo de extensiones de red.

### B. Despliegue del Túnel VPN y Validación de Identidad
Para enmascarar la procedencia de las solicitudes e impedir el bloqueo por parte de los mecanismos anti-análisis de la página sospechosa, se configuró una red privada virtual externa:

1. Obtención de perfiles criptográficos en la plataforma `https://www.vpnbook.com/` (sección OpenVPN), seleccionando un perfil de conexión con extensión `.ovpn`.
2. Inicialización del cliente nativo de **OpenVPN** integrado en el entorno de pruebas para levantar la interfaz virtual tunelizada.
3. Verificación de salida y asignación geográfica mediante la consulta directa de la IP pública a través del adaptador virtual:

```bash
❯ curl --interface tun0 ifconfig.me 2>/dev/null || curl --interface tun1 ifconfig.me

147.135.15.16
```

## Informacion del sitio
El sitio a investigar vendria siento el siguiente:

`https://email.kjbm.colegioagp.com/c/eJxskc-O2yAYxJ8GX6qN-G84cGiVRuq5D2B9Np8TdmOggLdNn75y4pWqVU6I-Q0jNAM5DxEWdG_wCmN4qS0VnEuKrb7kkvw6tZBi551RghrRoWN9b2UvLZMdLhCug8dreMdyG4J3kllJuZC9oDsN3nGmeqOVYWzXFqwVzji0W0b3kMaSwE9Q224pWNNaJnz6vuKvFeMDfkjreE_7vt2-fQp7Ri7OSutBsHGemNIUPGUwg5iZQdDApeyC45RrqjhnRigmD7MdvTC9MT2fZiM0kfTtdVwOU7riOSQ458OUlu7qLq3lSsRXwk-EnyCHw-8LtAr5biD8VDH6DYpTvqSIRBwVZ0ppxi3TwhKuG_5p23HLG727hrguIxbC9bYajBVjI-JIu48-t1Qsg08LhOiefa24BW4BCoS_MEMjkp63Wh4Mp5ADxnbvXFNqmbZadzW0fQZpKDdUq665n6Hhlx9HwsV_8rvj_wIAAP__8ALCuA`