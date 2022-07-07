from tkinter import *
import pandas as pd
import sympy as sp
import matplotlib.pyplot as plt

HayFrameMostrado=0

def Funcion_Grafica(funcion_graficar,varlo_a_reemplazar):
    x= sp.Symbol("x")
    funcion_conversion= sp.diff(funcion_graficar,x,0) #Aqui convertimos el str a spint
    resultado = funcion_conversion.subs(x,varlo_a_reemplazar) #Reemplazamos valor
    return resultado

def funcion_derivada(ecuacion,xi):
    x = sp.Symbol('x')
    derivada= sp.diff(ecuacion,x)
    resultado = derivada.subs(x,xi)
    return resultado






def Menu():
    # ||||||||||||||||||||| Aproximacion |||||||||||||||||||||||
    def InterfazAproximacion():
        global HayFrameMostrado
        #Destruir 
        #if(HayFrameMostrado==2):
            #destroy()
        #if(HayFrameMostrado==3):
            #Destroy



        def Calcular_Aproximación():
            #Obetener Datos
            xi= Dato_xi.get()
            convergencia= Dato_convergencia.get()
            funcion= Dato_funcion.get()
            
            #Variable para la tablas
            tabla_n=[]
            tabla_xi=[]
            tabla_xn=[]
            tabla_dx=[]
            tabla_signo=[]
            xi= float(xi)
            convergencia= float(convergencia)
            
            #Proceso
            n= 0
            nummax = 100 #Limiter de contador para la busqueda de raices
            dx = 1.0
            xn=0
            #Grafica
            rango = range(-100,100)
            plt.plot(rango,[Funcion_Grafica(funcion,i) for i in rango])

            #Busquedad De La Raiz
            while n<= nummax :
                xn=(Funcion_Grafica(funcion,xi)* Funcion_Grafica(funcion,xi+dx)) 
                if xn==0:
                    plt.plot(xi,0,"bo")
                    signo= "raiz"                  
                elif xn <0:
                    dx= dx/10.00
                    signo= "negativo"
                else:
                    signo= "positivo"
                    n=n+1
                if abs(xi - (xi+dx)) < convergencia:
                    signo= "raiz"
                    plt.plot(xi,0,"bo")
    
                #Ingresamo dato en la tabla
                tabla_xi.append(xi)
                tabla_dx.append(dx)
                conversion= float(xn)
                tabla_xn.append(conversion)
                tabla_signo.append(signo)
                xi= xi+dx
                if(signo=="raiz"):
                    break



            #Configuracion de Grafica
            plt.hlines(y=0, xmin=-100, xmax=100,color="k")
            plt.vlines(x=0, ymin=-100, ymax=100,color="k")

            #Lo valores predeterminado
            plt.ylim(-20,20)
            plt.xlim(-20,20)

            datos = {"Xi":tabla_xi,"Dx":tabla_dx,"Xn":tabla_xn,"Raices":tabla_signo}
            pd.options.display.max_columns= None
            pd.options.display.max_rows= None
            df = pd.DataFrame(datos)
            MostrarDatos.insert(1.0,df)
            plt.show()





        InterfazAproxi= Frame(ventenaPrincipal)
        InterfazAproxi.config(bg="lavender",width=1010,height=600)
        InterfazAproxi.place(x= 270, y=0)
        #Variable dinamica
        Dato_funcion= StringVar()
        Dato_xi= StringVar()
        Dato_convergencia= StringVar()

        
        Titulo_Del_Metodo= Label(InterfazAproxi, text="Aproximación",font=('Times New Roman',20),bg="lavender").place(x=400,y=25)
        #Datos A pedir
        Label(InterfazAproxi,text="Función:",font=('Times New Roman',18),bg="lavender").place(x=10,y=100)
        Entrada_funcion=Entry(InterfazAproxi,textvariable=Dato_funcion,font=('Times New Roman',17),width=75,border=4).place(x=105,y=100)
        Label(InterfazAproxi,text="Xi:",font=('Times New Roman',18),bg="lavender").place(x=10,y=150)
        Entrada_Xi=Entry(InterfazAproxi,textvariable=Dato_xi,font=('Times New Roman',17),width=7,border=4).place(x=50,y=150)
        Label(InterfazAproxi,text="Eps:",font=('Times New Roman',18),bg="lavender").place(x=150,y=150)
        Entrada_Convergencia=Entry(InterfazAproxi,textvariable=Dato_convergencia,font=('Times New Roman',17),width=7,border=4).place(x=200,y=150)
        Calcular_Buton= Button(InterfazAproxi, text="Calcular",font=('Times New Roman',12),border=5,command=lambda: Calcular_Aproximación()).place(x=300,y=150)
        #Ventana Tabla
        MostrarDatos= Text(InterfazAproxi,font=('Consolas',10),width=60,height=20,relief="groove",border=4)
        MostrarDatos.place(x=10,y=275)
        scrollvertical= Scrollbar(InterfazAproxi, command=MostrarDatos.yview)
        scrollvertical.place(x=435,y=400)
        
        

        #Ventana Grafica


    # ||||||||||||||||||||| Netwon Rapshon |||||||||||||||||||||||
    def InterfazNetwonRapshon():
        global HayFrameMostrado
        #Destruir 
        #if(HayFrameMostrado==2):
            #destroy()
        #if(HayFrameMostrado==3):
            #Destroy
        #Obetener Datos
        


        def Calcular_NetwonRapshon():
            
            def funcion_aproximacion(funcion,xi):
                funcion_n= Funcion_Grafica(funcion,xi)
                funcion_d= funcion_derivada(funcion,xi)
                aproximacion = ((xi - ((funcion_n/funcion_d))))
                print(aproximacion)
                return aproximacion
            
            
            
            xi= Dato_xi.get()
            convergencia= Dato_convergencia.get()
            funcion= Dato_funcion.get()
            
            #Variable para la tablas
            tabla_xi=[]
            tabla_fx=[]
            tabla_derivadax=[]
            tabla_raiz=[]
            xi= float(xi)
            convergencia= float(convergencia)
            xi-=1.00
            #Proceso
            n= 0
            nummax = 100 #Limiter de contador para la busqueda de raices
            xn=0
            #Grafica
            rango = range(-100,100)
            plt.plot(rango,[Funcion_Grafica(funcion,i) for i in rango])
            detectorSigno=0
            valor_temporal1=0
            valor_temporal2=0
            xi_temporal=0 # xi = x0 → 0
            
            while(n<=100 and detectorSigno==0):
                if(n==0):

                    valor_temporal1= Funcion_Grafica(funcion,xi)
                    valor_temporal2=valor_temporal1
                    xi +=1.00
                else:
                    valor_temporal1= valor_temporal2
                    valor_temporal2= Funcion_Grafica(funcion,xi)
                    xi +=1.00
                    if((valor_temporal1<0) != (valor_temporal2<0)):
                        xi -=2.00
                        detectorSigno=1
                        break
                n+=1
            print(n)
            almacenadoaproxi=0
            bandera=True
            while(detectorSigno==1):
                if(bandera):            
                    aproximacion2 =funcion_aproximacion(funcion,xi)
                    almacenadoaproxi= aproximacion2
                    tabla_xi.append(xi)
                    tabla_fx.append(Funcion_Grafica(funcion,xi))
                    tabla_derivadax.append(funcion_derivada(funcion,xi))
                    tabla_raiz.append("-----")
                    bandera=False
                else:
                    if(abs(aproximacion2-almacenadoaproxi) < 0.00001):
                        xi=aproximacion2
                        tabla_xi.append(xi)
                        tabla_fx.append(Funcion_Grafica(funcion,xi))
                        tabla_derivadax.append(funcion_derivada(funcion,xi))
                        tabla_raiz.append("raíz")
                        plt.plot(aproximacion2,0,"bo")
                        print(xi)          
                        break
                    else:
                        almacenadoaproxi=aproximacion2
                        xi= aproximacion2
                        tabla_xi.append(xi)
                        tabla_fx.append(Funcion_Grafica(funcion,xi))
                        tabla_derivadax.append(funcion_derivada(funcion,xi))
                        tabla_raiz.append("-----")

            
            plt.hlines(y=0, xmin=-100, xmax=100,color="k")
            plt.vlines(x=0, ymin=-100, ymax=100,color="k")
            #Rango de la linea x
            plt.xlim(-10, 10)
            #Rango de la linea y
            plt.ylim(-10, 10)


            datos = {"Xi":tabla_xi,"F(x)":tabla_fx,"D(x)":tabla_derivadax,"Encontrado":tabla_raiz}
            pd.options.display.max_columns= None
            pd.options.display.max_rows= None
            df = pd.DataFrame(datos)
            MostrarDatos.insert(1.0,df)




            #Mostrar Graficar
            plt.show()



        InterfazNetwon= Frame(ventenaPrincipal)
        InterfazNetwon.config(bg="lavender",width=1010,height=600)
        InterfazNetwon.place(x= 270, y=0)
        #Variable dinamica
        Dato_funcion= StringVar()
        Dato_xi= StringVar()
        Dato_convergencia= StringVar()


        Titulo_Del_Metodo= Label(InterfazNetwon, text="Netwon Rapshon",font=('Times New Roman',20),bg="lavender").place(x=400,y=25)
        #Datos A pedir
        Label(InterfazNetwon,text="Función:",font=('Times New Roman',18),bg="lavender").place(x=10,y=100)
        Entrada_funcion=Entry(InterfazNetwon,textvariable=Dato_funcion,font=('Times New Roman',17),width=75,border=4).place(x=105,y=100)
        Label(InterfazNetwon,text="Xi:",font=('Times New Roman',18),bg="lavender").place(x=10,y=150)
        Entrada_Xi=Entry(InterfazNetwon,textvariable=Dato_xi,font=('Times New Roman',17),width=7,border=4).place(x=50,y=150)
        Label(InterfazNetwon,text="Eps:",font=('Times New Roman',18),bg="lavender").place(x=150,y=150)
        Entrada_Convergencia=Entry(InterfazNetwon,textvariable=Dato_convergencia,font=('Times New Roman',17),width=7,border=4).place(x=200,y=150)
        Calcular_Buton= Button(InterfazNetwon, text="Calcular",font=('Times New Roman',12),border=5,command=lambda: Calcular_NetwonRapshon()).place(x=300,y=150)
        #Ventana Tabla
        MostrarDatos= Text(InterfazNetwon,font=('Consolas',10),width=80,height=20,relief="groove",border=4)
        MostrarDatos.place(x=10,y=275)
        scrollvertical= Scrollbar(InterfazNetwon, command=MostrarDatos.yview)
        scrollvertical.place(x=580,y=400)



    # |||||||||||||||||||| Biscecion |||||||||||||||||||||||||||||||||||||||
    def InterfazBisecion():
        global HayFrameMostrado
        
        def Calcular_Bisecion():
           
            tabla_xi=[]
            tabla_xr=[]
            tabla_xu=[]
            tabla_fxi=[]
            tabla_fxu=[]
            tabla_fxr=[]
            tabla_xu_xr=[]




           #Variable dinamica
            funcion= Dato_funcion.get()
            xi= Dato_xi.get()
            xu= Dato_xu.get()
            convergencia= Dato_convergencia.get()
            #Conversion
            xi= float(xi)
            xu= float(xu)
            convergencia= float(convergencia)


            #Ragno de tabla
            rango = range(-100,100)
            plt.plot(rango,[Funcion_Grafica(funcion,i) for i in rango])

            xr=0
            fxi=0
            fxu=0
            fxr=0
            fx=0


            n=0
            nummax= 100
            while n< nummax:
                xr= (xi-xu)/2.0
                fxi= Funcion_Grafica(funcion,xi)
                fxu= Funcion_Grafica(funcion,xu)
                fxr= Funcion_Grafica(funcion,xr)
                fx= fxi*fxu
                tabla_xi.append(xi)
                tabla_xu.append(xu)
                tabla_xr.append(xr)
                tabla_fxi.append(fxi)
                tabla_fxu.append(fxu)
                tabla_fxr.append(fxr)
                oososo= xi -xu
                tabla_xu_xr.append(oososo)


                if(fxr==0.00):     
                    signo= "Raiz"
                    plt.plot(xi,0,"bo")
                    break
                elif (fxu*fxr<0):
                    xi= xr
                    fxi= fxr
                    signo="Negativo"
                else:
                    xu=xr
                    fxu=fxr
                    signo="Positivo"

                if(abs(xi-xu)< convergencia):
                    plt.plot(xi,0,"bo")
                    break
                n=n+1
                

            plt.hlines(y=0, xmin=-100, xmax=100,color="k")
            plt.vlines(x=0, ymin=-100, ymax=100,color="k")
            #Rango de la linea x
            plt.xlim(-10, 10)
            #Rango de la linea y
            plt.ylim(-10, 10)

            datos = {"Xi":tabla_xi,"Xu":tabla_xu,"Xr":tabla_xr,"Fxi":tabla_fxi,"Fxu":tabla_fxu,"Fxr":tabla_fxr,"Xi - Xu":tabla_xu_xr}
            pd.options.display.max_columns= None
            pd.options.display.max_rows= None
            df = pd.DataFrame(datos)
            MostrarDatos.insert(1.0,df)



            plt.show()






        InterfazBise= Frame(ventenaPrincipal)
        InterfazBise.config(bg="lavender",width=1010,height=600)
        InterfazBise.place(x= 270, y=0)
        #Variable dinamica
        Dato_funcion= StringVar()
        Dato_xi= StringVar()
        Dato_convergencia= StringVar()
        Dato_xu= StringVar()

        Titulo_Del_Metodo= Label(InterfazBise, text="Bisección",font=('Times New Roman',20),bg="lavender").place(x=400,y=25)
        #Datos A pedir
        Label(InterfazBise,text="Función:",font=('Times New Roman',18),bg="lavender").place(x=10,y=100)
        Entrada_funcion=Entry(InterfazBise,textvariable=Dato_funcion,font=('Times New Roman',17),width=75,border=4).place(x=105,y=100)
        Label(InterfazBise,text="Xi:",font=('Times New Roman',18),bg="lavender").place(x=10,y=150)
        Entrada_Xi=Entry(InterfazBise,textvariable=Dato_xi,font=('Times New Roman',17),width=7,border=4).place(x=50,y=150)
        Label(InterfazBise,text="Xu:",font=('Times New Roman',18),bg="lavender").place(x=150,y=150)
        Entrada_Xu=Entry(InterfazBise,textvariable=Dato_xu,font=('Times New Roman',17),width=7,border=4).place(x=190,y=150)
        
        
        Label(InterfazBise,text="Eps:",font=('Times New Roman',18),bg="lavender").place(x=330,y=150)
        Entrada_Convergencia=Entry(InterfazBise,textvariable=Dato_convergencia,font=('Times New Roman',17),width=7,border=4).place(x=380,y=150)
        Calcular_Buton= Button(InterfazBise, text="Calcular",font=('Times New Roman',12),border=5,command=lambda: Calcular_Bisecion()).place(x=550,y=150)
        #Ventana Tabla
        MostrarDatos= Text(InterfazBise,font=('Consolas',10),width=80,height=20,relief="groove",border=4)
        MostrarDatos.place(x=10,y=275)
        scrollvertical= Scrollbar(InterfazBise, command=MostrarDatos.yview)
        scrollvertical.place(x=580,y=400)













    # |||||||||||||||||Menu| |||||||||||||||||||||||||||
    global HayFrameMostrado
    #Ventana Principal
    master=Tk()
    x_ventana = master.winfo_screenwidth() // 2 - 1280 // 2
    y_ventana = master.winfo_screenheight() // 2 - 720 // 2
    posicion = str(1280) + "x" + str(600) + "+" + str(x_ventana) + "+" + str(y_ventana)
    master.geometry(posicion)
    master.resizable(1,1)
    master.title("Método Numéricos")
    ventenaPrincipal= Frame(master)
    ventenaPrincipal.pack()
    ventenaPrincipal.config(bg="lavender",width=1280,height=720)


    Label(ventenaPrincipal,text="Métodos",font=('Times New Roman',24),bg="lavender").place(x=65,y=50)
    Label(ventenaPrincipal,bg="LightBlue4",width=2,height=100).place(x=250,y=0)


    Boton_Aproximación= Button(ventenaPrincipal,text="Aproximación",font=('Times New Roman',18),width=15 ,border=6,command= lambda: InterfazAproximacion()).place(x=20,y=150)
    Boton_NetwonRapshon= Button(ventenaPrincipal,text="Netwon Rapshon",font=('Times New Roman',18),width=15 , border=6,command= lambda: InterfazNetwonRapshon()).place(x=20,y=250)
    Boton_Aproximación= Button(ventenaPrincipal,text="Bisección",font=('Times New Roman',18),width=15 , border=6,command= lambda:InterfazBisecion()).place(x=20,y=350)

    mainloop()
    
    
    Menu()
    
    
    
    
    
