import openpyxl

libro = openpyxl.load_workbook('prueba.xlsx')
hoja = libro.active
hoja['E1'] = 'Suma total'
hoja['E2'] = '=SUM(B2:B14)'

libro.save('prueba.xlsx')