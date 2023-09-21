print("Mario Villanueva")
w=1
while w ==1:
 print("desea ingresar a la calculadora, 1:si o 2:no")
 z=input()
 z=int(z)
 if z == 2:
  break
 print("ingrese un numero del 1 al 10")
 i = input()
 i=int(i)
 x=1
 x=int(x)
 if i> 10:
    print("el numero no puede ser mayor a 10")
 elif i<1:
    print("la variable no puede ser menor a 1")
 else:
    for x in range(1, 11):
     print(str(i)+"x"+str(x)+"="+str(i*x))
