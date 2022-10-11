from django.shortcuts import render
from .models import Datos 
import pandas as pd
# Create your views here.



def  muestra_datos(request):
    consulta = Datos.objects.all()
    contexto= {'datos':consulta }
    data = pd.read_csv('prueba1/prueba.csv')
    for i in range(len(data)):
         info = Datos(
             x1= data['D1'][i],
             c1=data['Caracter1'][i],
             x2 = data['D2'][i],
             x3 = data['D3'][i],
         )
         info.save()
    return render (request,'prueba1/index.html', contexto)