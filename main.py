#Creando variables y ciclos en python

menuOpciones=0
while menuOpciones!=5:
    print("Bienvenido a la bodegas JuanFE")
    print("******************************")
    print("1. Digita 1 para agregar un producto a la bodega:")
    print("2. Digita 2 para ver todos  los  productos de la bodega:")
    print("3. Digita 3 para calcular el costo total de productos de la bodega:")
    menuOpciones=int(input("\nDigita una opcion: "))

    if menuOpciones==1:
        print("😎comenzaremos a registrar los productos: \n")
    elif menuOpciones==2:
        print("📃revisaremos nuestro inventario:\n")
    elif menuOpciones==3:
        print("📊 estamos calculando :\n")
    else:
     print("😢Aun no contamos con esa opcion.....\n")