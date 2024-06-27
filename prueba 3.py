def registrar_libro():
    generos = ["accion", "ficcion", "no ficcion", "misterio"]
    while True:
        try:
            print("*********************************")
            titulo=input("Ingrese Titulo: ")
            autor=input("ingrese autor: ")
            genero= input("ingrese genero: ").lower()
            precio=int(input("ingrese precio: "))
            stock=int(input("ingrese stock: "))
            print("*********************************") 
            if genero in generos: 
                break
        except:
            print("Ingrese bien los datos")
    Libro = {titulo : [autor, genero, precio, stock]}
    return Libro

def registrar_venta(LibroStock):
    LibroX = input("que libro desea veder?")
    for i in LibroStock:
        if LibroX in i:
            
def imp_rep_ventas():
    print()
def gen_txt():
    print()
##vars
LibroStock= [{"Titutlo" : ["autor", "genero", "precio", "stock"]}]
##main
while True:
    try:
        print("_________________________________")
        print("(1) Registrar Libro")
        print("(2) Listar todos los libros")
        print("(3) Registrar Ventas")
        print("(4) Imprimir reporte de ventas")
        print("(5) Generar txt")
        print("(6) Sair del programa")
        print("_________________________________")
        OP=int(input("Ingrese una opcion: "))
        if OP==1:
            LibroStock.append(registrar_libro())
        elif OP==2:
            for i in LibroStock:
                print(i)
        elif OP==3:
            registrar_venta(LibroStock)
        elif OP==4:
            print("wip")
        elif OP==5:
            print("wip")
        elif OP==6:
            print("Buen turno")
            break
        else:
            print("Error ~ opcion no valida")   
    except:
        print("Ingrese una opcion valida")