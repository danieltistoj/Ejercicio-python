#Recibe como parametro una representacion de un diccionario y si es factible, devuelve un diccionario de datos
dic = dict(nombre="nestor",apellido="Plasencia",edad=22)
#print(dic)

#zip()
zip1 = zip('abcd',[1,2,3,4])

#print(zip1)

dic = dict(zip('abcd',[1,2,3,4]))
#print(dic)

#fromkeys()
dic = dict.fromkeys(['a','b','c','d'],1)
#print(dic)

#setdefault()
dic = {"a":1,"b":2,"c":3,"d":4}
valor = dic.setdefault("a")
print(valor)
valor = dic.setdefault("e",5) #si el valor e no existe se le asigna el valor de 5 y se crea la clave e
#print(dic)
#update()
dic1 = {'a' : 1, 'b' : 2, 'c' : 3 , 'd' : 4}
dic2 = {'c' : 6, 'b' : 5, 'e' : 9 , 'f' : 10}
dic1.update(dic2)
print(dic1)