# sentencias de control 


# if = si 

# elif = sino si 

# else = sino 

"""a = 10 

b = 10

if a<b : # validaciones
    print('a es menor que b')

elif a>b : 
    print('b es menor que a')

else : 
    print('b es igual que a')
"""


a = 12 

b = 12 

c = 12

if a>b and a>c:
    print("a es mayor que b y c")

elif a<b and a<c:
    print("a es menor que b y c")

elif a>b and a<c:
    print("a es mayor que b y menor que c")

elif a<b and a>c:
    print("a es menor que b y mayor que c")

elif b>a and b>c:
    print("b es mayor que a y c")

elif b<a and b<c:
    print("b es menor que a y c")

elif b>a and b<c:
    print("b es mayor que a y menor que c")

elif b<a and b>c:
    print("b es menor que a y mayor que c")

elif c>a and c>b:
    print("c es mayor que a y b")

elif c<a and c<b:
    print("c es menor que a y que b")

elif c>a and c<b:
    print("c es mayor que a y menor que b")

elif c<a and c>b:
    print("c es menor que a y  mayor que b")

else:
    print("a, b y c son iguales")

    
