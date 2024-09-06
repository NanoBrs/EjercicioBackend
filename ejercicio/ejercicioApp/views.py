from django.shortcuts import render

# Create your views here.
def renderHome(request):
    return render(request,'ejercicioApp/home.html')


def renderCatalogo(request,Categoria,Producto1,Producto2,Producto3):
    datos={"Categoria":Categoria,
           "Producto1":Producto1,
           ""
           "Producto2":Producto2,
           "Producto3":Producto3}
    return render(request,'/TemplateApp/catalogo.html',datos)




def renderJuguetes(request):
    datos={"Categoria":"Juguetes",
           "Producto1":"Max Steel",
           "Descripcion1":"Jueguete de accion",
           "img1":"max.jpg",
           "Precio1":"15.000",

           "Producto2":"Terreneitor",
           "img2":"terreneitor.png",
           "Descripcion2":"Jueguete de carreras",
           "Precio2":"45.000",

           "Producto3":"Barbie",
           "img3":"barbie.png",
           "Descripcion3":"Jueguete ",
           "Precio3":"12.000"}
    
    return render(request,'ejercicioApp/catalogo.html',datos)




def renderElectronica(request):
    datos={"Categoria":"Electronica",
           "Producto1":"Monitor",
           "Descripcion1":"Jueguete de accion",
           "img1":"monitor.png",
           "Precio1":"150.000",

           "Producto2":"Parlante",
           "img2":"parlante.jpg",
           "Descripcion2":"Jueguete de carreras",
           "Precio2":"45.000",

           "Producto3":"Audifonos",
           "img3":"audifonos.jpg",
           "Descripcion3":"Audifonos blutuh ",
           "Precio3":"37.000"}
    
    return render(request,'ejercicioApp/catalogo.html',datos)



def renderRopa(request):
    datos={"Categoria":"Ropa",
           "Producto1":"Polera gucci",
           "Descripcion1":"polera gucci",
           "img1":"polera.jpg",
           "Precio1":"65.000",

           "Producto2":"Zapatillas Campus",
           "img2":"campus.png",
           "Descripcion2":"zapatillas original",
           "Precio2":"109.990",

           "Producto3":"Gorro",
           "img3":"gorro.png",
           "Descripcion3":"Gorrito de lana ",
           "Precio3":"12.000"}
    
    return render(request,'ejercicioApp/catalogo.html',datos)

    