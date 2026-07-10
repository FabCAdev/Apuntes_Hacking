# 1- TITULOS

# Este es un título principal (Grande), se usa con "#"
## Este es un subtítulo (Mediano), se usa con "##"

### Este es un título de sección (Chico), se usa con "###"

#### Tamaño cuarto, se usa con "####"

##### Tamaño quinto, se usa con "#####"

###### Tamaño sexto, se usa con "#######"

Tamaño normal

# **2- NEGRITAS** 

Quiero que esta palabra esté en **negrita** para que resalte, se usa "** palabra **"

# 3- LISTAS y VIÑETAS

- Primer punto "-"
* Segundo punto "*"
- Tercer punto

# 4- BLOQUES DE CÓDIGO```
```bash
sudo less /etc/profile
*Se verá así en Obsidian (limpio y con colores de terminal):*
```bash
sudo less /etc/profile
```

se pone "```(al inicio y final)```"

# 5- ENLACES

Se usa "[[Ejemplo nota markdown]]"

# 6- LISTA DE TAREAS

- [ ] Lista de tarea "- [ ]"

# 6- BLOQUES DE NOTAS

> ⚠️ **¡Cuidado!** Recuerda encender la VPN (`sudo openvpn`) antes de intentar hacer ping a la IP de TryHackMe, o no va a conectar.  

Se usa ">" al inicio de cada linea

# 6- TABLAS MANUALES 

| Herramienta | Fase de Hacking       | ¿Para qué sirve?                       |
| :---------- | :-------------------- | :------------------------------------- |
| Nmap        | Escaneo / Enumeración | Descubrir puertos abiertos y servicios |
| Burp Suite  | Explotación Web       | Intercepta y modifica peticiones HTTP  |
| OpenVPN     | Conectividad          | Conectarse a los laboratorios de THM   |
Se usa barras verticales, separando con "-"
| sd | asdas | asdasd |
| :--- | :--- | :--- |
| asd | asd | asd |

# 7- TEXTO OCULTO DESPLEGABLE

<details>
<summary>🔑 Ver la bandera (Flag) de la máquina Neighbour</summary>

`THM{idor_vulnerability_mastered}`
</details>

(usa las flechas para ver adentro)

# 8-Formatos de texto Extra

~~texto~~ Tachado "~~ abriendo y cerrando"
==texto== Marcatextos "== abriendo y cerrando"
*texto* Cursica "* abriendo y cerrando"

[[Ejemplo nota markdown]]

[[📖 ENCICLOPEDIA|⬅️ Volver a 📖 ENCICLOPEDIA]]