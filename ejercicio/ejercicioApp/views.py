from django.shortcuts import render

# Create your views here.
def renderHome(request):
    return render(request,'/TemplateApp/home.html')

def renderCatalogo(request,Categoria,Producto1,Producto2,Producto3):
    datos={"Categoria":Categoria,
           "Producto1":Producto1,
           "Producto2":Producto2,
           "Producto3":Producto3}
    return render(request,'/TemplateApp/catalogo.html',datos)




def renderCatalogos(request):
    datos={"Categoria":"Jueguetes",
           "Producto1":"Max Steel",
           "Imagen1":"max.jpg",
           "Descripcion1":"Jueguete de accion",
           "Precio1":"15.000",

           "Producto2":"Terreneitor",
           "Imagen2":"terreneitor.jpg",
           "Descripcion2":"Jueguete de carreras",
           "Precio2":"45.000",

           "Producto3":"Barbie",
           "Imagen1":"barbie.jpg",
           "Descripcion1":"Jueguete ",
           "Precio1":"12.000"}
    
    return render(request,'/TemplateApp/catalogo.html',datos)




    