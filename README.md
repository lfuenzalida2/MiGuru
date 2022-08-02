# Documentación

Para esta tarea se utilizaron los paquetes **selenium** y **pandas**, antes de correr el archivo principal (**scrapper.py**), es necesario instalar estos paquetes, para ello se puede usar el comando:

> pip install -r requirements.txt

Luego es necesario tener la versión correcta de Google Chrome (en mi caso usé la versión 103.0.5060.134) para poder utilizar el driver correcto de este, en caso de no funcionar con el driver que está en el repositorio puedes descargar el driver que necesites <a href= https://chromedriver.chromium.org/downloads>aquí</a> (para ver cual es tu versión de Google Chrome puedes ir a la configuración del navegador o el mismo programa te dice cual es al momento de correrlo).

Finalmente para correr el programa solamente es necesario hacer:

> py \.scapper.py

en el path raíz del repositorio.

### Consideraciones
Corri varias veces el algortimo y en todas me dió casos en los que habían **terms** que no tienen **titles**, pero que iban cambiando después de correrlo un par de veces, creo yo que esto es porque se me bloqueó temporalmente la IP por parte de **opcionempleo.cl**, el servidor de estos se les saturó o simplemente el algortimo pasó muy rapido en esos casos (creo que es el segundo caso porque esto pasa en casos secuenciales y luego se pueden seguir obteniendo datos de la página). Por esto para hacer un poco mas ameno el tiempo de espera, no se parchó el problema (mi solución era hacer esperar al algoritmo hasta que responda el servidor).