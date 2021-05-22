from openpyxl import Workbook
from openpyxl.chart import ScatterChart,Reference,Series

libro = Workbook()
hoja = libro.active

for i in range(1,15):
    hoja[f'A{i}'] = i

for i in range(1,15):
    hoja[f'B{i}'] = i*10

c1 = ScatterChart()
c1.title = "Grafica de dispersion"
c1.style = 13

c1.y_axis.title = 'eje Y'
c1.x_axis.title = 'eje X'

xvalues = Reference(hoja,min_col=1,min_row=1,max_col=1,max_row=14)
yvalues = Reference(hoja,min_col=2,min_row=1,max_col=2,max_row=14)

ser = Series(yvalues, xvalues,title='recta')
c1.series.append(ser)
hoja.add_chart(c1,'D3')
libro.save('Grafica.xlsx')
