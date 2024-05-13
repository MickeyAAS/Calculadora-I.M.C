# Calculadora de índice de masa corporal
# Alumno: Miguel Angel Sauza Anastacio
#U Campers Python
# Módulo 1

nombre = imput("Introduzca su nombre: ")
apellido = imput("Introduzca su apellido paterno: ")
apellido = imput("Introduczca su apellido materno: ")
edad = int(imput("Introduzca su edad: "))
peso = float(imput("Introduzca su peso en kilogramos"))
estatura = float(imput("Introduzca su estatura en metros"))

IMC = peso / estatura **2
print(IMC: " + str(IMC))

si IMC >= 18,50 e IMC <= 24,99:
      print ("Todavía tienes chance de una torta má")
si IMC >= 25,00 e IMC <=29,99:
      print ("Hay que bajarle al pan")
si IMC >= 30,00 e IMC <=34,99:
      print ("Bueno, ¿Tú no entiendes verdad?")
      
# Rúbricas de IMC para referencias serías
# 18.50 a 24.99 Normal
# 25.00 a 29.99 sobrepeso
# 30.00 a 34.99 obesidad leve
