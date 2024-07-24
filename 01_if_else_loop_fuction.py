# "if" es una declaración de Python bastante implementada, busca ejecutarr bloques de código de acuerdo con condiciones
#Indiquemos si una persona es mayor de edad conforme a su edad
x= int(input("Indica tu edad: "))
if x < 0:
    x = 0
    print("Opps.. Parece que has escrito mal tu edad, !inténtalo de nuevo!")
elif x == 18:
    print("Eres un jóven adulto")
elif x > 18:
    print(" Ya eres un adulto con largas y años de historias de vida, felicitaciones")
else:
    print("Intentalo de nuevo")

# for es una declaración en Python que tambien tiene un uso constante y se utiliza en listas y cadenas 
# Indicar cuantas letras tiene un nombre 
nombres = ['Linda','Villamil','Julian','Cano']
for n in nombres:
        print(n, len(n))

#También podemos crear listas desde una simple hacia una nueva
#Por ejemplo

#crear una lista de usuarios
usuarios = {'Linda': 'active', 'Nana': 'inactive', 'Gato': 'active'}

# Iterar sobr euna copia
for usuario, status in usuarios.copy().items():
    if status == 'inactive' :
        del usuarios[usuario]

#Ahora crear la nueva colección
Usuarios_activos = {}
for usuario, status in usuarios.items():
    if status == 'active':
        Usuarios_activos [usuario] = status
        print(Usuarios_activos)

#Ahora, veremos la función /range/, el cual es una progresión aritmetica que permite obtener un conjunto de números, es importante tener presente que esta función nos da la cantidad de valores asignados desde su inicio pero nunca su final
    #Saca un listado de numeros de 0 al 100
for n in range(8):
    print(n)
    #si requerimos un listado en puntual e simportante especificarlo, incluso se puede con números negativos.
list((range(5,10)))

#iteraciones combinadas
Grupo1 = ['Linda', 'Marcela', 'Karen', 'Thiago']
for i in range(len(Grupo1)):
    print(i,Grupo1[i])
# Usaremos la función
sum(range(4))  # 0 + 1 + 2 + 3
print(sum)
