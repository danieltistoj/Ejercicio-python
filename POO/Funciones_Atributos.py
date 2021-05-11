class Persona:
    edad = 27
    nombre = 'Victor'
    pais = 'brazil'

doctor = Persona()
#print('La edad es de: ',doctor.edad)
#print('la edad es: ',getattr(doctor,'edad'))#nos permite mostrar el valor de un atributo es un get
print('¿el doctor tiene edad?',hasattr(doctor,'edad'))#esta funcion nos permite ver si un atributo existe, nos devuelve un valor boleano
print('¿el doctor tiene apellido? ',hasattr(doctor,'apellido'))

print('Antes: ',doctor.nombre)
setattr(doctor,'nombre','hector')#Esta funcion permite modificar un abributo. Es un set
print('Ahora: ',doctor.nombre)

print('Antes: ',hasattr(doctor,'pais'))
delattr(Persona,'pais')#Elimina un atributo de una clase
print('Ahora: ',hasattr(doctor,'pais'))
