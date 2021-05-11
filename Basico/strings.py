myStr = "Hello wordl"

#print(dir(myStr)) #para obtener lo que se puede hacer con un string

print(myStr.upper()) #Este metodo convierte todo a mayuscula
print(myStr.lower())#para que todo sea a minuscula
print(myStr.swapcase())#Alterna de mayuscula a minuscula, las letras de la palabra
print(myStr.capitalize())#Convierte la primera letra de cada String a mayusculas
print(myStr.replace('Hello','bye'))#remplaza una palabra del texto por otra que querramos
print(myStr.replace('Hello','Bye').upper())#Se pueden convinar los metodos-Metodo encadenado
print(myStr.count('l'))#Este metodo es para contar cuandas veces aparece una letra
print(myStr.startswith('hola'))#Indica falso o verdadero, si la palabra que ingresamos inicia el string
print(myStr.startswith('Hello'))
print(myStr.endswith("wordl"))#Indica falso a verdadero, si la palabra que ingresamos, es con la que termina el string
print(myStr.split())#Separa un String por palabras, lo divide por defecto donde hay un caracter en blanco, pero se le puede indicar donde separar
print(myStr.split('o'))
print(myStr.find('o'))#devuelve la posicion de un caracter
print(len(myStr))#Nos indica la longitud de la cadena 
print(myStr.index('e'))#Nos indica el indice o la posicion
print(myStr.isnumeric())#Para ver si es numerico
print(myStr.isalpha())#Inverso de isnumeric

name = "daniel"
print("Mi nombre es: "+name)
print(f"Mi nombre es {name}")#La f indica que se debe de tomar en cuenta la variable anterior 
print("Mi nombre es {0}".format(name))