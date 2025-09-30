#Creando variables y ciclos en python

menuOpciones=0
  #Pasos para crear una lista
  #1. Se crea la variable y se iguala a corchetes 
listaProductos=[]

while menuOpciones!=5:
    print("Bienvenido a la bodegas JuanFE")
    print("******************************")
    print("1. Digita 1 para agregar un producto a la bodega:")
    print("2. Digita 2 para ver todos  los  productos de la bodega:")
    print("3. Digita 3 para calcular el costo total de productos de la bodega:")
    menuOpciones=int(input("\nDigita una opcion: "))

    if menuOpciones==1:
        print("comenzaremos a registrar los productos: \n")
        #un producto es un diccionario(objeto)
        #Pasos para crear diccionario
        #1. creamos la variable ultilizando llaves 
        diccionarioProducto={}
         #2.agregamos valores y llaves al diccionario
        diccionarioProducto["id"]=int(input("Digita el id del producto: "))
        diccionarioProducto["nombre"]=input("Digita el nombre del producto: ")
        diccionarioProducto["descripcion"]=input("Digita la descripcion del producto: ")
        diccionarioProducto["precioUnitario"]=int(input("Digita el precio unitario  del producto: "))
        diccionarioProducto["cantidadBodega"]=int(input("Digita la cantidad del producto en bodega : "))
        #fotografia
        diccionarioProducto["fotografia"]=input("Digita la  URL de la fotografia del producto: ")
        #marca
        diccionarioProducto["marca"]=input("Digita la marca del producto: ")
        #3.agregamos el diccionario al lista
        listaProductos.append(diccionarioProducto)
        print("\n Exito agregando el producto 😁\n ")


    elif menuOpciones==2:
        print("📃revisaremos nuestro inventario:\n")
    elif menuOpciones==3:
        print("📊 estamos calculando :\n")
    else:
     print("😢Aun no contamos con esa opcion.....\n")