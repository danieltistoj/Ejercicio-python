import openpyxl
libro = openpyxl.load_workbook('prueba.xlsx')

hoja = libro.active

a1 = hoja['A1']
a2 = hoja['A2']

print(a1.value)
print(a2.value)

print(type(a1.value))

hoja2 = libro['hoja2']
print(hoja2['A1'].value)

#modificar valores

hoja2['A1'] = 'Hola mundo 2'
libro.save('prueba.xlsx')