# Creacion de Scripts

Etiquetas: #linux #bash #scripts #shell-scripting #automatizacion

Creacion de Scripts en linux

`#!/bin/bash`

Le das a entender que es un script de bash, fundamental que vaya al principio

funcion [nombre funcion] (){

}

Declaracion de una funcion en un script

function ctrl_c(){

echo -e "\n\n [!] Saliendo...\n"

exit 1

}

Declara la funcion ctrl_c donde realiza las siguientes instrucciones que seria un echo y un exit

echo -e [mensaje]

Echo para imprimir un mensaje, pero con el atributo -e permitimos los caracteres especiales como los saltos de linea con \n

exit 0

exit 1

exit 2

exit 126

exit 127

exit 128

exit 128+n

exit 255

Sucess

General Error

Misuse of shell built-ins

Command cannot execute

Command not found

Invalid exit argument

Fatal error signal “n”

Exit status out of range

El comando se ejecutó correctamente sin errores.

Error genérico (división por cero, errores de sintaxis en scripts, etc.).

Uso incorrecto de comandos internos del shell (ej. error de sintaxis).

Se encontró el comando, pero no tiene permisos de ejecución.

El comando no existe en el $PATH o está mal escrito.

Se pasó un argumento inválido a la función exit.

El proceso terminó por una señal (ej. 130 es Ctrl+C).

El código devuelto está fuera del rango 0-255.

trap [teclado] INT

Registra el evento de presionar una tecla en especifico

trap ctrl_c INT

Registra el evento de presionar ctrl + c

`#Colours`

greenColour="\e[0;32m\033[1m"

endColour="\033[0m\e[0m"

redColour="\e[0;31m\033[1m"

blueColour="\e[0;34m\033[1m"

yellowColour="\e[0;33m\033[1m"

purpleColour="\e[0;35m\033[1m"

turquoiseColour="\e[0;36m\033[1m"

grayColour="\e[0;37m\033[1m"

Variables para colores

while getopts "m:h" arg in; do

case $arg in

m)

h) helpPanel;;

esac

done

while getopts "m:h" arg in; do

done

Condional while, con getops indicado pabuscar letras predecidas por un guion, poniendo m podemos hacer que el script espere un parametro en especifico, y la h funcionaria como un interruptor como tal. El arg in; do

case $arg in

esac

Condicional case

declare -i parameter_counter=0

Es un indicador, usando declare para variables, parametro -i para que solo sea una variable integer y con parameter_counter=0 sirve para inicializar la variable con el nombre y un valor inicial de 0
