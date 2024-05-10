def servicios():
    print("************************************")
    print("Ingrese la opcion del servicio que desea")
    print("1. Internet de fibra optica")
    print("2.Planes pospago")
    print("3.Planes prepago")

    print("**********************************")

def pedir_opcion():
    opc= 0
    try:
        opc = int(input("Ingrese su opcion"))
        print("******************************")
        return opc
    except Exception:
        print("valor invsalido")
        print("****************************")
        return-1