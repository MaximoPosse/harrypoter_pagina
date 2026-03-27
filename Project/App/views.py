from django.shortcuts import render, redirect
from .models import *
from datetime import datetime
# Create your views here.
def Home(request):
    data = {
        "products": Producto.objects.all().order_by("-fechaIngreso")[:3]
    }
    return render(request,'Home.html', data)

def Productos(request):
    # ---> Guardamos todos los Productos en una variable
    Productos=Producto.objects.all()
    data={
        # ---> Enviamos todos los productos a la palabra reservada
        'products':Productos
    }
    # --------------->Enviamos mediante la Palabra Data
    return render(request,'Productos.html',data)

def AnadirProducto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        cantidad = request.POST.get('cantidad')
        precio = request.POST.get('precio')
        rareza = request.POST.get('rareza')
        fechaIngreso = request.POST.get('fechaIngreso')
        Imagen = request.FILES.get('Imagen')
        
        # Crear el producto
        producto = Producto(
            Nombre=nombre,
            Cantidad=cantidad,
            Precio=precio,
            Rareza=rareza,
            fechaIngreso=fechaIngreso,
            Imagen=Imagen
        )
        producto.save()
        return redirect('Productos')
    
    return render(request, "AnadirProducto.html")