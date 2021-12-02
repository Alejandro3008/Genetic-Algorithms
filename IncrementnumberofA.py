
import random
import numpy as np
import matplotlib.pyplot as plt

# * Crea el array de 200 posiciones con su indice de 3 digitos.
def createArray():
    alphabet = 'abcdefghijklmnñopqrstuvwxyz';
    wordArray =[]
    for i in range(200):
        word='';
        word=''.join(random.choices(alphabet, k=8))
        aCounter= str(word.count('a'))
        wordArray.append(aCounter+word)
        cpArray = [x.upper() for x in wordArray]
        cpArray.sort(reverse=True)
    # * Agrega el indice
    array = addIndex(cpArray)
    return array


# * Agrega index a cada posicion del array
def addIndex(array):
    for i in range(200):
        x= str(i+1).zfill(3)
        array[i] = x+array[i]
    return array


# * Selecciona los primeros 100
def selec100(wordArray):
    best100 = []
    for item in range(100):
        best100.append(wordArray[item])
    return best100

# * Crea un arreglo de 100 y compara 2 posiciones al azar, selecciona la mejor y la agrega.
# * Con una funcion recursiva
def select100_2(array,newarray,z=1):
    if(z == 101): # * Si la funcion se esta ejecutan por vez numero 101 retorna el nuevo arreglo.
        return newarray
    numRandom = random.randint(0,199-z-1) # * Se generan 2 numeros randon entre 0 y 199 que cada vez que se haga recursion se reducira el rango en -1
    numRandom2 = random.randint(0,199-z-1) # * z-1 por que z  inicia en 1 y la primera vez no deberia restar nada al rango ya que excluiria la ultima posicion
    if(array[numRandom][3] > array[numRandom2][3]):
        listValue = array.pop(numRandom)
        newarray.append(listValue)
    else:
        listValue = array.pop(numRandom2) # * En caso de que el primer elemento NO sea mayor que el segundo quiere decir que el segundo es mayor o igual.
        newarray.append(listValue)
    return select100_2(array,newarray,z+1)

# * Quita el index a cada posicion del array
def resetArray(array):
    for item in range(len(array)):
        array[item] = array[item][3:12]
    return array

def sortIndex(array,array2):
    newArray200 = array + array2 # * Junto el array de padres con el de hijos en un array nuevo
    sortArray = sorted(newArray200,reverse=True) # * Lo ordeno de mayor a menor
    sortArray = addIndex(sortArray) # * Llamo a la funcion para agregar un indice al principio
    return sortArray # * Retorno el array ordenado y con sus index agregados

# * Operador cruzado 'Single Point'
def singlePoint(array):
    arrayHijos = []
    arrayLoop = array.copy()
    arrayIndex = array.copy()
    for item in range(50):
        padre1,padre2 = random.sample(arrayLoop,2)
        palabra1 = padre1[1:6] + padre2[6:9]
        palabra2 = padre2[1:6] + padre1[6:9]
        contador1= str(palabra1.count('A'))
        contador2= str(palabra2.count('A'))
        arrayHijos.append(contador1+palabra1)
        arrayHijos.append(contador2+palabra2)
        arrayLoop.remove(padre1)
        arrayLoop.remove(padre2)
    
    newArray = sortIndex(arrayHijos,arrayIndex)
    return newArray

# * Operador cruzado 'Multiple Point'
def multiplePoint(array):
    arrayHijos = []
    arrayLoop = array.copy()
    arrayIndex = array.copy()
    for item in range(50):
        # padre1 = random.randint(0,99)
        # padre2 = random.randint(0,99)
        padre1,padre2 = random.sample(arrayLoop,2)
        palabra1 = padre1[1:3] + padre2[3:6] + padre1[6:9]
        palabra2 = padre2[1:3] + padre1[3:6] + padre2[6:9]
        contador1= str(palabra1.count('A'))
        contador2= str(palabra2.count('A'))
        arrayHijos.append(contador1+palabra1)
        arrayHijos.append(contador2+palabra2)
        arrayLoop.remove(padre1)
        arrayLoop.remove(padre2)
    
    newArray = sortIndex(arrayHijos,arrayIndex)
    return newArray

# * Operador Cruzado 'Uniform'
def uniform(array):
    arrayHijos = []
    arrayLoop = array.copy()
    arrayIndex = array.copy()
    for item in range(50):
        # padre1 = random.randint(0,99)
        # padre2 = random.randint(0,99)
        padre1,padre2 = random.sample(arrayLoop,2)
        palabra1 = padre1[1:2] + padre2[2:3] + padre1[3:4] + padre2[4:5] + padre1[5:6] + padre2[6:7] + padre1[7:8] + padre2[8:9]
        palabra2 = padre2[1:2] + padre1[2:3] + padre2[3:4] + padre1[4:5] + padre2[5:6] + padre1[6:7] + padre2[7:8] + padre1[8:9]
        contador1= str(palabra1.count('A'))
        contador2= str(palabra2.count('A'))
        arrayHijos.append(contador1+palabra1)
        arrayHijos.append(contador2+palabra2)
        arrayLoop.remove(padre1)
        arrayLoop.remove(padre2)

    newArray = sortIndex(arrayHijos,arrayIndex)
    return newArray

# * Suma de todas las fitness function del array
def fitnessFunctionTotal(array):
    total = 0
    for item in range(len(array)):
        total = total + int(array[item][3]) 
    resp = total
    return resp

def main():
    # * Creacion del arreglo principal
    arregloPrincipal = createArray() # * Creo el array principal de 200 posiciones.
    arregloPrincipalCopia = arregloPrincipal # * Creo una copia de ese array por que voy a usar 2 metodos de seleccion y en cada metodo se modifica el array principal
    # * Creacion de los arreglos por los 2 metodos.
    arregloTop100 = selec100(arregloPrincipal) # * Arreglo de 100 posiciones con seleccion de los primeros 100
    arregloTorneo = select100_2(arregloPrincipalCopia,newarray=[]) # * Arreglo de 100 posiciones con seleccion por torneo
    # * Quitamos los index para la creacion de los hijos
    arregloTop100NoIndex = resetArray(arregloTop100)
    arregloTorneoNoIndex = resetArray(arregloTorneo)
    # * Creacion de hijos por los distintos metodos
    arregloSinglePoint = singlePoint(arregloTop100NoIndex)
    arregloMultiplePoint = multiplePoint(arregloTop100NoIndex)
    arregloUniform = uniform(arregloTop100NoIndex)
    arregloSinglePoint2 = singlePoint(arregloTorneoNoIndex)
    arregloMultiplePoint2 = multiplePoint(arregloTorneoNoIndex)
    arregloUniform2 = uniform(arregloTorneoNoIndex)
    # * Calculo del fitness function total de cada arreglo
    totalAT100SP = fitnessFunctionTotal(arregloSinglePoint)
    totalATornSP2 = fitnessFunctionTotal(arregloSinglePoint2)
    totalAT100MP = fitnessFunctionTotal(arregloMultiplePoint)
    totalATornMP2 = fitnessFunctionTotal(arregloMultiplePoint2)
    totalAT100U = fitnessFunctionTotal(arregloUniform)
    totalATornU2 = fitnessFunctionTotal(arregloUniform2)


    print('--------- Arreglo con eleccion de top 100 por single point ----------')
    print(arregloSinglePoint)
    print(totalAT100SP)
    print('--------- Arreglo con eleccion de torneo por single point ----------')
    print(arregloSinglePoint2)
    print(totalATornSP2)
    print('--------- Arreglo con eleccion de top 100 por multiple point ----------')
    print(arregloMultiplePoint)
    print(totalAT100MP)
    print('--------- Arreglo con eleccion de torneo por multiple point ----------')
    print(arregloMultiplePoint2)
    print(totalATornMP2)
    print('--------- Arreglo con eleccion de top 100 por uniform ----------')
    print(arregloUniform)
    print(totalAT100U)
    print('--------- Arreglo con eleccion de torneo por uniform ----------')
    print(arregloUniform2)
    print(totalATornU2)

def loop100SinglePoint():
    arrayFunction = createArray()
    arrayFF = []
    for i in range(100):
        if(i==0):
            loopArray = arrayFunction
        else:
            loopArray = newArray

        newArray = selec100(loopArray)
        newArray = resetArray(newArray)
        newArray = singlePoint(newArray)
        numFF = fitnessFunctionTotal(newArray)
        arrayFF.append(numFF)
        # print('------------- arreglo numero:',i,'--------------------------------------')
        # print(newArray)
        # print(numFF)
    
    return arrayFF

def loop100MultiplePoint():
    arrayFunction = createArray()
    arrayFF = []
    for i in range(100):
        if(i==0):
            loopArray = arrayFunction
        else:
            loopArray = newArray

        newArray = selec100(loopArray)
        newArray = resetArray(newArray)
        newArray = multiplePoint(newArray)
        numFF = fitnessFunctionTotal(newArray)
        arrayFF.append(numFF)
        # print('------------- arreglo numero:',i,'--------------------------------------')
        # print(newArray)
        # print(numFF)
    
    return arrayFF

def loop100Uniform():
    arrayFunction = createArray()
    arrayFF = []
    for i in range(100):
        if(i==0):
            loopArray = arrayFunction
        else:
            loopArray = newArray

        newArray = selec100(loopArray)
        newArray = resetArray(newArray)
        newArray = uniform(newArray)
        numFF = fitnessFunctionTotal(newArray)
        arrayFF.append(numFF)
        # print('------------- arreglo numero:',i,'--------------------------------------')
        # print(newArray)
        # print(numFF)
    
    return arrayFF

def loop100SinglePointTournamet():
    arrayFunction = createArray()
    arrayFF = []
    for i in range(100):
        if(i==0):
            loopArray = arrayFunction
        else:
            loopArray = newArray
        loopArray2 = loopArray.copy()
        newArray = select100_2(loopArray2,newarray=[])
        newArray = resetArray(newArray)
        newArray = singlePoint(newArray)
        numFF = fitnessFunctionTotal(newArray)
        arrayFF.append(numFF)
        # print('------------- arreglo numero:',i,'--------------------------------------')
        # print(newArray)
        # print(numFF)
    
    return arrayFF

def loop100MultiplePointTournamet():
    arrayFunction = createArray()
    arrayFF = []
    for i in range(100):
        if(i==0):
            loopArray = arrayFunction
        else:
            loopArray = newArray

        loopArray2 = loopArray.copy()
        newArray = select100_2(loopArray2,newarray=[])
        newArray = resetArray(newArray)
        newArray = multiplePoint(newArray)
        numFF = fitnessFunctionTotal(newArray)
        arrayFF.append(numFF)
        # print('------------- arreglo numero:',i,'--------------------------------------')
        # print(newArray)
        # print(numFF)
    
    return arrayFF

def loop100UniformTournamet():
    arrayFunction = createArray()
    arrayFF = []
    for i in range(100):
        if(i==0):
            loopArray = arrayFunction
        else:
            loopArray = newArray

        loopArray2 = loopArray.copy()
        newArray = select100_2(loopArray2,newarray=[])
        newArray = resetArray(newArray)
        newArray = uniform(newArray)
        numFF = fitnessFunctionTotal(newArray)
        arrayFF.append(numFF)
        # print('------------- arreglo numero:',i,'--------------------------------------')
        # print(newArray)
        # print(numFF)
    
    return arrayFF


def graficartop100():
    singlepointArray = loop100SinglePoint()
    multiplepointArray = loop100MultiplePoint()
    uniformArray = loop100Uniform()
    x=np.arange(1,101)
    plt.plot(x,singlepointArray,'bo',label='Single Point')
    plt.plot(x,multiplepointArray,'ro',label='Multiple Point')
    plt.plot(x,uniformArray,'go',label='Uniform')
    plt.title('Operadores Cruzados de top 100')
    plt.legend(loc = 'lower right')
    plt.show()

def graficarTournamet():
    singlepointArray = loop100SinglePointTournamet()
    multiplepointArray = loop100MultiplePointTournamet()
    uniformArray = loop100UniformTournamet()
    x=np.arange(1,101)
    plt.plot(x,singlepointArray,'bo', label ='Single Point')
    plt.plot(x,multiplepointArray,'ro', label = 'Multiple Point')
    plt.plot(x,uniformArray,'go', label='Uniform')
    plt.title('Operadores Cruzados de seleccion por torneo')
    plt.legend(loc = 'lower right')
    plt.show()

#graficartop100()
#graficarTournamet()


