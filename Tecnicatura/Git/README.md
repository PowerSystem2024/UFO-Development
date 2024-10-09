# Comandos Git


## 1_ Comandos basicos Crear-Mover-Ver Carpetas

* *para ver la ruta de la carpeta/directorio donde estoy posicionado*
  ```
  pwd
  ```
* *para ver las carpetas*
  ```
  ls
  ```
* *para dirigirnos a una carpeta especifica ejemplo $cd /d/repositorio*
  ```
  cd (nombre de la carpeta)
  ```
* *para dirigirnos a la carpeta origen comunmente disco local C*
  ```
  cd 
  ```
* *para ir a la carpeta/directorio anterior*
  ````
  cd ..
  ````
* *clear #Limpia la consola o ctrl + l¨*
  ````
  clear
  ````
## 2_Trabajando con carpetas


* *para crear una carpeta nueva*
  ```
  mkdir (nombre de la carpeta)
  ```
* *para borrar una carpeta vacia*
  ```
  rmdir (nombre de la carpeta)
  ```
* *borra una carpeta con archivos*
  ```
  rm -rf (nombre de la carpeta)
  ```
* *quitar una carpeta con sus archivos del area de preparacion*
  ```
  git rm --cached -r (nombre_carpeta)
  ```


 ## 3_Configuración Repositorio

 
* *Configura tu nombre de usuario para todos tus repositorios*
  ``` 
  git config --global user.name "Tu Nombre"
  ```
* *Configura tu correo electrónico*
  ```
  git config --global user.email tuemail@example.com
  ``` 
* *Configura tu editor de texto preferido*
  ```
  git config --global core.editor "tu_editor"
  ```
* *Ver los cambios generados/aplicados*
  ```
  Git config --list
  ```

## 4_Creación y Clonación de Repositorios


* *Inicializa un nuevo repositorio git en el directorio/carpeta actual*
  ```
  git init	
  ```
* *Clona un repositorio remoto a tu máquina local*
  ```
  git clone URL
  ```
* *direccion o hash de commit que quiero cargar*
  ```
  Git checkout hash
  ```

  
## 5_Remotos (Remotes)


* *Agrega un repositorio remoto*  
  ```
  git remote add (carpeta_local) (URL)
  ```
* *Muestra los repositorios remotos configurados*
  ```
  git remote -v
  ```
 * *#Descarga cambios desde el repositorio remoto sin fusionarlos*
  ```
  git fetch
  ```
* *#Descarga y fusiona cambios desde el repositorio remoto*
  ```
  git pull
  ```
* *#Envía tus commits a la rama especificada en el repositorio remoto*
  ```
  git push origin (nombre_rama)
  ```
* *se utiliza para eliminar una referencia a un repositorio remoto en tu repositorio local*
  ```
  git remote remove (nombre_carpeta)
  ```

## 6_Trabajando con archivos


* *Muestra el estado actual del repositorio (archivos modificados, agregados etc)*
  ```
  git status
  ```
  * *Para agregar archivos al area de preparacion*
  ```
  git add .
  ```
* *Para crear archivos especificos (hay que agregar el formato .txt, .md, .html*
  ```
  touch (nombre_archivo.formato)
  ```
  * *Elimina el archivo*
  ```
  rm (archivo)
  ```
* *Guarduar los cambios o commits de los archivos puestos en el area de preparacion*
  ```
  git commit -m "Mensaje del commit"
  ```
* *hacer commit sin necesidad de git add . #Sólo con archivos modificado(No se puede utilizar con archivos nuevos)*
  ```
  git commit –am “escribimos el comentario de nuestro commit”
  ```
* * Eliminar un archivo del área de preparación y del repositorio (es decir, dejar de rastrearlo), pero mantenerlo en tu directorio de trabajo.*
  ```
  git rm --cached (nombre_carpeta)
  ```
* *Deshacer los cambios en el área de preparación (staging area) y restaurar el archivo a su estado en el último commit.*
  ```
   git restore --stage (nombre-del-archivo)
  ```
* **
  ```
  ls
  ```
* **
  ```
  ls
  ```
* **
  ```
  ls
  ```
* **
  ```
  ls
  ```
* **
  ```
   ls
  ```
* **
  ```
  ls
  ```
* **
  ```
  ls
  ```
* **
  ```
  ls
  ```
