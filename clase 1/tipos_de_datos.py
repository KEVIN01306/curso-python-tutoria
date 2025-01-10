

# int = enteros 

# float = 140.00

# str = cadenas de texto 

# boolean = True / false

# list = [1,2,3,4,5]

# tuples = (1,2,)

# diccionarios = { "a": 12 }

# funcion type()


#------ Variables ---------------

"""a = 12  

b = a 

a = a+1



print(b)
print(a)"""

# int 

entero = 12

#float 

decimal = 12.00

#str 

string = "hola Andrea"

#booleas 

bolean = True

# tuples 

tupla = (1,)


#diccionario 

diccionario = { "a": 
                    {'b': 
                        {"c": 
                            { "d":
                                2
                            }
                        }
                    },
                "b": 
                    {'b': 
                        {"c": 
                            { "d":
                                22
                            }
                        }
                    },
                "c": 
                    {'b': 
                        {"c": 
                            { "d":
                                222
                            }
                        }
                    }
                }

#diciconario2 = diccionario["a"]["b"]["c"]["d"]

#print(diciconario2)

"""for i in diccionario: 
    for ii in diccionario[i] :
        for iii in diccionario[i][ii]:
            for iiii in diccionario[i][ii][iii]:
                print(diccionario[i][ii][iii][iiii])"""

"""
print(f
        soy un entero: {entero}
        
        soy un decimal: {decimal}
        
        soy un string: {string}
        
        soy un bolean: {bolean}
        
        soy un tupla: {tupla}
        
        
    )
"""

# dicciconario ejrcicio 

diccionario3 = {
    "a": {
        "b": 1
    },
    "b": {
        "b": {
            "c":
                120
        }
    },
    "c": 100
}

valor1=diccionario3["a"]["b"]
valor2=diccionario3["b"]["b"]["c"]
valor3=diccionario3["c"]

print("suma:", valor1+valor2+valor3)

#sumar todos los numeros de los diccionarios 



