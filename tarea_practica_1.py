
# coding: utf-8

# In[25]:


import validaciones


# # Ejercicios Python

# ## Zen of Python
# 
# Lee una vez mas el Zen of Python antes de iniciar con la tarea

# In[26]:


import this


# ## 1 - XOR
# 
# En la siguiente celda crea una funcion para la compuerta logica XOR 
# 
# <img src="assets/xor.png" width="400">
# 

# In[34]:


def xor(a,b):
    """
    Esta funcion recibe dos valores booleanos, ejemplo xor(1, 0) o True y False
    y retorna 0 o 1 como resultado de la operacion logica XOR
    """
    # tu codigo aqui
    return not(a == b)
#    x = 1 if a+b == 1 else 0
#    return x


# In[35]:


xor(0 , 1)


# In[36]:


xor(0 , 0)


# In[37]:


xor(True , False)


# ### Pruebas  Automaticas
# 
# Todas las pruebas deben funcionar para obetener los puntos del ejercicio.

# In[38]:


validaciones.xor_function(xor)

print(validaciones.xor_function(xor))


# ## 2 - Sumando N series
# 
# Tenemos una secuencia cuyo $n^{th}$ es:
# \begin{equation*}
# \ T_n = n^2 - (n-1)^2
# \end{equation*}
# 
# Hay que evaluar las series:
# \begin{equation*}
# \ S_n = T_1 + T_2 + ... + T_n
# \end{equation*}
# 
# 
# **Instrucciones**
# En la siguiente celda en la funcion summingSeries debemos **retornar** en valor de $S_n$, tenemos como entrada n
# 
# **Ejemplo 1:**
# 
# Si la entrada es 2
# 
# Salida:
# 4
# 
# Explicacion:
# 
# $T_1 = 1$
# 
# $T_2 = 3$
# 
# $S_2 = T_1 + T_2$
# 
# $S_2 = 4 $
# 
# 
# 
# **Tip :**
# Antes te implementar $S_n$ la solución, analicemos algebraicamente el problema para encontrar una solución equivalente optima.
# 

# In[9]:


def sumatoriaSerie(n):
    """
    La funcion recibe como parametro n y retorna el valor de la serie
    """
    # tu codigo aqui
    return n*n
#Solucion1
#T = 0
#S = 0
#for i in range(1,n+1,1):
#    S+= pow(i,2)-pow(i-1,2)

#Solucion2 
#S = 0
#   for i in range(1,n+1,1):
#      S+= 2*i-1

#Solucion3
#return sum(range(1,2*n,2))

#Solucion4
#return  n*n


# #### 2.1 - Ciclos
# 
# Crea un ciclo for que imprima el resultado de la funcion **summingSeries** desde 1 hasta 10

# In[10]:


for i in range(1,11,1): print(sumatoriaSerie(i))


# ### Pruebas  Automaticas
# 
# Todas las pruebas deben funcionar para obetener los puntos del ejercicio.
# 
# ##### Importante :
# En este ejercicio se evalua que la funcion sea optima, el tiempo de ejecucion tiene que ser el menor posible, se va a evaluar el resultado correcto y el tiempo de ejecucion, si en alguna de las pruebas obtienes **[FALLO: TIMEOUT]** la funcion no es optima debes cambiarla hasta que todas las pruebas pasen

# In[11]:


validaciones.summingSeries_function(sumatoriaSerie)


# ## 3 - Factores Primos
# 
# Para cada $n$ queremos obtener el conteo maximo de numeros primos unicos en en rango inclusivo $[1, n]$,
# y retornar el valor del conteo en una nueva linea
# 
# **Nota:** Recuerda que un numero primo solo es divisible por el mismo y que 1 no es un numero primo
# 
# ##### Ejemplos:
# 
# ###### Ejemplo 1
# Entrada: 1
# 
# Salida esperada: 1
# 
# Explicacion: El numero maximo de factores primos unicos en el rango inclusivo $[1,1]$ es $0$, porque $1$ no es un numero primo.
# 
# ###### Ejemplo 2
# Entrada: 3
# 
# Salida esperada: 1
# 
# Explicacion: El numero maximo de factores primos unicos en el rango inclusivo $[1,3]$ es $1$, porque el numero $3$ tiene 1 factor primo unico (el mismo) 
# 
# ###### Ejemplo 3
# Entrada: 500
# 
# Salida esperada: 4
# 
# Explicacion: El numero maximo de factores primos unicos en el rango inclusivo $[1,500]$ es $4$, porque el producto de los primeros cuatro numeros primos unicos es $2 \times 3 \times 5 \times 7 = 210$ y no hay ningun numero primo unico que multiplicado por el resultado sea $	\leqslant 500$
# 
# 
# 
# #### Tip: 
# Utiliza la funcion `range()` de python
# 

# In[12]:


#Range
a = range(1,10,2)
print(a)


# In[13]:


def conteoPrimos(n):
    """
    Esta funcion recibe como parametro n y 
    retorna el conteo maximo de numeros primos unicos
    """
    # tu codigo aqui
    primos = []
    factores = 0
    mult = 1
    for i in range(1,n+1,1):
        for a in range(1,i,1):
            if i%a == 0 and a>1:
                break
            elif a == i-1:
                primos.append(i)
                mult = primos[-1]*mult
            else:
                continue
        if mult > n:
            factores = len(primos)-1
            break                
    return factores
conteoPrimos(500)


# ### Pruebas

# In[14]:


conteoPrimos(1)


# In[15]:


conteoPrimos(1000)


# ### Pruebas  Automaticas
# 
# Todas las pruebas deben funcionar para obetener los puntos del ejercicio.
# 
# ##### Importante :
# En este ejercicio se evalua que la funcion sea optima, el tiempo de ejecucion tiene que ser el menor posible, se va a evaluar el resultado correcto y el tiempo de ejecucion, si en alguna de las pruebas obtienes **[FALLO: TIMEOUT]** la funcion no es optima debes cambiarla hasta que todas las pruebas pasen

# In[16]:


validaciones.primeCount_function(conteoPrimos)


# ## 4 - Metodo de Euler
# 
# El metodo de Euler se utiliza para aproximar la solucion particular de una ecuacion diferencial dado un valor inicial. Con esta informacion se sabe que la grafica de esa solucion pasa a traves del punto $(x_0,y_0)$ y tiene una pendiente $F(x_0,y_0)$ en ese punto, esto da un punto de partida para aproximar la solucion.
# 
# A partir del punto inicial, se sigue en la direccion indicada por la pendiente. Mediante un pequeño paso $h$, se mueve a lo largo de la recta tangente hasta llegar al punto $(x_1,y_1)$ donde:
# \begin{equation*}
# \ x_1 = x_0 + h       \\
# \ y_1 = y_0 + hF(x_0,y_0)\\
# \end{equation*}
# 
# 
# <img src="assets/Euler.png" width="350">
# 
# Como se muestra en la figura se considera $(x_1,y_1)$ como un nuevo punto inicial.
# 
# Los valores de $x$ son:
# \begin{equation*}
# \ x_1 = x_0 + h       \\
# \ x_2 = x_1 + h       \\
# \    .                \\
# \    .                \\
# \    .                \\
# \ x_n = x_{n-1} + h   \\
# \end{equation*}
# 
# 
# Los valores de $y$ son:
# \begin{equation*}
# \ y_1 = y_0 + hF(x_0,y_0)\\
# \ y_1 = y_1 + hF(x_1,y_1)\\
# \       . \\
# \       . \\
# \       . \\
# \ y_n = y_{n-1} + hF(x_{n-1},y_{n-1})\\
# \end{equation*}
# 
# 
# #### Problema 4
# El ejecicio consiste en implementar la funcion *euler_metod* esta funcion recibe como parametro el 
# * punto inicial $x_0$
# * punto inicial $y_0$
# * Paso $h$ 
# * numero de iteraciones $n$ 
# * La equacion diferencial que queremos aproximar, esta funcion tambien recibe los parametros $x$ y $y$
# * La funcion de la solucion exacta que tambien tambien recibe los parametros $x$ y $y$
# 
# La funcion debe retornar el valor de $y_n$ y el error
# $error=|y - y_n|$ 

# In[18]:


import math 


# In[19]:


def euler_method(x,y,h,n, diff_eq, func):
    """
    Parametros x, y punto inicial, logitud del paso h , n numero de iteraciones,
    diff_eq la equacion diferencial y func la funcion de la solucion exacta
    Retorna y y el error
    """
    # tu codigo aqui
    for a in range(0, n, 1):
        x = x + h
        y = y + h*(diff_eq(x,y))
        
    return y, (diff_eq(x,y) - y)


# ### Ejemplo
# 
# Queremos aproximar la solucion particular de la ecuacion diferencial
# \begin{equation*}
# \ \frac{\partial y}{\partial x} = -2y \\
# \end{equation*}
# Donde $y(0) = 4$ vamos a unsa un de $h=0.1$
# 
# Tambien vamos a calcular el error en este caso podemos verificar el error  con la solucion exacta:
# \begin{equation*}
# \ y = 4e^{-2x} \\
# \end{equation*}

# In[16]:


### Implementando las funciones del ejemplo
def y_prime(x, y):
    return -2*y

def y(x):
    return 4 * math.exp(-2*x)


# In[17]:


"""
Llamamos a la funcion de euler
euler_method(0,4,0.1,10, y_prime,y)
Parametros :
x = 0
y = 4
d = 0.1
n = 10
diff_eq = y_prime
func = y
"""

euler_method(0,4,0.1,10, y_prime,y)


# ### Solucion:
# 
# Utiliza esta tabla como guia para validar que tu funcion este correcta,
# y reemplaza los valores que faltan con la salida de tu funcion.
# 
# | x     | 0 | 0.1         | 0.2    | 0.4    | 0.6    | 0.8    | 1            |
# |-------|---|-------------|--------|--------|--------|--------|--------------|
# | y     | 4 | 3.2749      | 2.6813 | 1.7973 | 1.2048 | 0.8076 | 0.5413       |
# | $y_n$ | 4 | $y_1$       | 2.56   | 1.6384 | 1.0486 | 0.6711 | $y_10$       |
# | error | 0 | y - $y_1$   | 0.1213 | 0.1589 | 0.1562 | 0.1365 | y-$y_{10}$ |

# ### 4.1 Probando la implementacion con una aplicación real de data science
# 
# Podemos utilizar ecuaciones diferenciales  como modelos matemáticos de fenónemos reales, por ejemplo si llegas a trabajar como data scientist para una farmaceutica  puede que interese analizar la desintegración radioactiva de cierta sustancia y como esto cambia en el tiempo
# #### Desintegracion Radiactiva
# 
# $A$ es la cantidad de sustancia en el tiempo $t$, la derivada $\frac{\partial A}{\partial t}$ es rapidez a la que se desintegran los nucleos de una sustancia.
# 
# Queremos aproximar la solucion particular de la ecuacion diferencial
# \begin{equation*}
# \ \frac{\partial A}{\partial t} =  -0.56A \\
# \end{equation*}
# Donde $A(0) = 1$ vamos a un tamaño de $h=0.1$
# 
# Tambien vamos a calcular el error en este caso podemos verificar el error  con la solucion exacta:
# \begin{equation*}
# \ A(t) = e^{-0.56t} \\
# \end{equation*}
# 
# **Nota** En este caso sencillo, poseemos la solución exacta a la ED por lo cual no se necesita una solución aproximada , pero en aplicaciones y proyectos reales muchas veces la solución exacta no se posee, o es muy difícil de calcular y recurrimos a soluciones aproximadas por computadora , para este ejercicio el saber la solución exacta nos sirve para medir la exactitud de nuestra solución aproximada.

# In[49]:


def A_prime(x, y):
    return -0.56*y

def A(x):
    return math.exp(-0.56*x)


# In[50]:


euler_method(0,1,0.1,10, A_prime,A)


# ## 5 - Rotacion de listas hacia la izquierda
# 
# Una rotacion a la izquierda en una lista mueve cada elemento de la lista una vez hacia la izquierda. Por ejemplo, si hacemos $1$ rotacion en en el arreglo $[1,2,3,4,5]$, el arreglo resultante seria $[2,3,4,5,1]$
# 
# #### Descipcion de la funcion
# Dado un arreglo $a$ de $n$ integers y un numero $d$ de rotaciones, realizar $d$ rotaciones hacia la izquierda. La funcion debe retorner el arreglo re-ordenado.
# 
# **rotIzquierda** tiene los siguientes parametros:
# 
# * $a$ Un arreglo de numeros entreros.
# * $d$ numero de rotaciones.

# In[19]:


def rotIzquierda(a, d):
    # tu codigo aqui
    return a[d:] + a[:d]

#Solucion#1
#    sliceob2 = slice(0,d)
#    sliceob1 = slice(d,len(a))
#    rotado = a[sliceob1] + a[sliceob2]
#    return rotado

#Solucion#2
#rotado = a[slice(d,len(a))] + a[slice(0,d)]
#    return rotado

#Solucion#3 - No pude hacerlo mas directo que esto...
#    return a[d:] + a[:d]


# In[20]:


rotIzquierda([1, 2, 3, 4, 5], 3)
# Resultado: [5, 1, 2, 3, 4]


# ### Pruebas  Automaticas
# 
# Todas las pruebas deben funcionar para obetener los puntos del ejercicio.
# 
# ##### Importante :
# En este ejercicio se evalua que la funcion sea optima, el tiempo de ejecucion tiene que ser el menor posible, se va a evaluar el resultado correcto y el tiempo de ejecucion, si en alguna de las pruebas obtienes **[FALLO: TIMEOUT]** la funcion no es optima debes cambiarla hasta que todas las pruebas pasen
# 
# #### TIP:
# Utiliza **slice** en el array para optimizar la funcion

# In[21]:


validaciones.rotIzquierda_function(rotIzquierda)

