# Modo de apertura de Ficheros

### Utilizamnos la función ***open()*** para abrir un archivo, si el archivo no se puede abrir, se genera un error *OSError*. 

```
    open(file, mode)
```

- ***file*** es una cadena que proporciona el nombre de ruta del archivo que se abrirá.

- ***mode*** es una cadena opcional que especifica el modo en el que se abre el archivo. Su valor predeterminado es *'r'*, que significa abierto para lectura en modo texto. Otros valores comunes son:
&nbsp;
&nbsp;
  
| Modo | Descripción |
| ----------- | ----------- |
| *'r'*  | 	Este es el modo predeterminado. Abre archivo para leer. |
| *'w'*  | 	Este modo Abre el archivo para escribir. Si el archivo no existe, crea un nuevo archivo. Si el archivo existe, trunca el archivo. |
| *'x'*  | 	Crea un nuevo archivo. Si el archivo ya existe, la operación falla. |
| *'a'*  | 	Abre el archivo en modo agregar. Si el archivo no existe, crea un nuevo archivo. |
| *'t'*  | 	Este es el modo predeterminado. Se abre en modo texto. |
| *'b'*  | 	Esto se abre en modo binario. |
| *'+'*  | 	Esto abrirá un archivo para leer y escribir (actualizar) |
