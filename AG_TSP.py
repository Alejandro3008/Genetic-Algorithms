import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt


file = pd.ExcelFile('DistanciasCiudades.xlsx') 
dataFrame = file.parse('Hoja1') 
dataFrame.drop(['Cities'], axis=1,inplace=True)
arrayCities = dataFrame.keys() 
arrayCities = np.array(arrayCities) 
arrayCities = np.delete(arrayCities,0) 
arrayNumbers = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]


def createPoblation():
    newArray = []
    for i in range(1000):
        finalnum = ''
        arrayNumbersCopy = arrayNumbers.copy()
        for j in range(18):
            num = random.sample(arrayNumbersCopy,1)
            if(j == 17):
                finalnum += str(num[0])
                
            else:
                finalnum += str(num[0]) + ','
            arrayNumbersCopy.remove(num[0])
        newArray.append(finalnum)
    return newArray

def addFF(array):
    newArray =[]
    for i in range(len(array)):
        fitnessFunction = 0
        arrayCitiesDistance = array[i].split(',')
        for j in range(17):
            if(j == 17):
                break
            fitnessFunction += dataFrame.iloc[int(arrayCitiesDistance[j]),int(arrayCitiesDistance[j+1])]
        fitnessFunction += dataFrame.iloc[int(arrayCitiesDistance[17]),int(arrayCitiesDistance[0])]
        fitnessFunction = round(fitnessFunction,2)
        newCityDistance = str(fitnessFunction) + ',' + array[i]
        newArray.append(newCityDistance)
    return newArray

def sortPoblation(array):
    array.sort()
    return array

def selectBest100(array):
    newArray=[]
    for i in range(100):
        newArray.append(array[i])
    return newArray

def deleteFF(array):
    newArray = []
    for i in range(len(array)):
        newValue = array[i].split(',')
        newValue.pop(0)
        cityDistance = ''
        for  j in range(len(newValue)):
            if(j == 17):
                cityDistance += newValue[j]
            else:
                cityDistance += newValue[j] + ',' 
        newArray.append(cityDistance)

    return newArray

#def operatorPMX(array):
    arrayLoop = array.copy()
    arrayIndex = array.copy()
    newArray = []
    for item in range(50):
        sampleP1,sampleP2 = random.sample(arrayLoop,2)
        p1 = sampleP1.split(',')
        p2 = sampleP2.split(',')
        padre1P2 = p1[6:12]
        padre2P2 = p2[6:12]
        padre1P1_2 = p1[0:6] + p1[12:18] 
        padre2P1_2 =p2[0:6] + p2[12:18] 
        h1Repeat =[]
        h2Repeat =[]
        
        for i in range(len(padre1P1_2)):
            if(padre1P1_2[i] in padre2P2):
                value = i
                h1Repeat.append(value)
                #print(h1Repeat)      
            if(padre2P1_2[i] in padre1P2):
                value = i
                h2Repeat.append(value)
                #print(h2Repeat)

        for i in range(len(h1Repeat)):
            value1 = padre1P1_2[h1Repeat[i]]
            value2 = padre2P1_2[h2Repeat[i]]
            padre1P1_2[h1Repeat[i]] = value2
            padre2P1_2[h2Repeat[i]] = value1

        final1 = padre1P1_2[0:6] + padre2P2 + padre1P1_2[6:12]
        final2 = padre2P1_2[0:6] + padre1P2 + padre2P1_2[6:12]
        
        cityDistance1 =''
        cityDistance2 =''
        for  j in range(len(final1)):
            if(j == 17):
                cityDistance1 += final1[j]
                cityDistance2 += final2[j]
            else:
                cityDistance1 += final1[j] + ',' 
                cityDistance2 += final2[j] + ',' 
        
        # print('padre1',sampleP1)
        # print('padre2',sampleP2)
        # print('Hijo 1',cityDistance1)
        # print('Hijo 2',cityDistance2)
        newArray.append(cityDistance1)
        newArray.append(cityDistance2)
        # print(newArray)
        arrayLoop.remove(sampleP1)
        arrayLoop.remove(sampleP2)
        
    #print('-------------------------------------------------------------------------')
    #print(newArray)
    newChilds = invertedExMutation(newArray)
    newPoblation = arrayIndex + newChilds
    #print('-------------------------------------------------------------------------')
    #print(newPoblation)
    newPoblationFF = addFF(newPoblation)
    newPoblationSort = sortPoblation(newPoblationFF)
    return newPoblationSort

def operatorPMX2(array):
    arrayCopy = array.copy()
    arrayParents = array.copy()
    arrayChilds = []
    for item in range(50):
        sampleParent1,sampleParent2 = random.sample(arrayCopy,2)
        arrayParent1 = sampleParent1.split(',')
        arrayParent2 = sampleParent2.split(',')
        middleParent1 = arrayParent1[6:12]
        middleParent2 = arrayParent2[6:12]
        restParent1 = arrayParent1 [0:6] + arrayParent1[12:18] 
        restParent2 = arrayParent2 [0:6] + arrayParent2[12:18]
        newRestParent1 = []
        newRestParent2 = []
        for i in range(len(restParent1)):
            if(restParent1[i] not in middleParent2):
                newRestParent1.append(restParent1[i])
            elif(restParent1[i] in middleParent2):
                position = middleParent2.index(restParent1[i])
                while(middleParent1[position] in middleParent2):
                    position = middleParent2.index(middleParent1[position])
                newRestParent1.append(middleParent1[position])
                    
        for i in range(len(restParent2)):
            if(restParent2[i] not in middleParent1):
                newRestParent2.append(restParent2[i])
            elif(restParent2[i] in middleParent1):
                position = middleParent1.index(restParent2[i])
                while(middleParent2[position] in middleParent1):
                    position = middleParent1.index(middleParent2[position])
                newRestParent2.append(middleParent2[position])

        newChild1 = newRestParent1[0:6] + middleParent2 + newRestParent1[6:12]
        newChild2 = newRestParent2[0:6] + middleParent1 + newRestParent2[6:12]
        cityDistance1 =''
        cityDistance2 =''
        for  j in range(len(newChild1)):
            if(j == 17):
                cityDistance1 += newChild1[j]
                cityDistance2 += newChild2[j]
            else:
                cityDistance1 += newChild1[j] + ',' 
                cityDistance2 += newChild2[j] + ',' 
        
        arrayChilds.append(cityDistance1)
        arrayChilds.append(cityDistance2)
        arrayCopy.remove(sampleParent1)
        arrayCopy.remove(sampleParent2)

    newArraychilds = invertedExMutation(arrayChilds)
    newPoblation = arrayParents + newArraychilds
    newPoblationFF = addFF(newPoblation)
    newPoblationSort = sortPoblation(newPoblationFF)
    return newPoblationSort

def invertedExMutation(array):
    arrayCopy = array.copy()
    reps = (5*len(array)/100)
    reps = int(reps)
    for i in range(reps):
        x = len(arrayCopy)
        position = random.randint(0,x-1)
        subStringP = random.randint(6,17)
        sampleChild = arrayCopy[position]
        arraySampleChild = sampleChild.split(',')
        newSubString = arraySampleChild[subStringP:subStringP-6:-1]
        arraySampleChild[subStringP-5:subStringP+1] = newSubString
        cityDistance1 = ''
        for  j in range(len(arraySampleChild)):
            if(j == 17):
                cityDistance1 += arraySampleChild[j]
            else:
                cityDistance1 += arraySampleChild[j] + ',' 
        array[position] = cityDistance1
        
    return array

def graficar(array):
    y = array.copy()
    x = np.arange(1,101)
    plt.plot(x,y)
    plt.title('100 generaciones')
    plt.show()

def loop100Generations():
    arrayFunction = createPoblation()
    arrayFF = []
    for i in range(100):
        if(i==0):
            loopArray = arrayFunction
        else:
            loopArray = newArray5
            loopArray = deleteFF(loopArray)
        
        newArray = addFF(loopArray)
        newArray2 = sortPoblation(newArray)
        newArray3 = selectBest100(newArray2)
        newArray4 = deleteFF(newArray3)
        newArray5 = operatorPMX2(newArray4)
        bestDistance = newArray5[0].split(',')
        bestDistanceValue = float(bestDistance[0])
        arrayFF.append(bestDistanceValue)        
        
        print('-----------------------------Generacion numero : ',i+1,' ---------------------------------------------------------')
        print(newArray5)
    graficar(arrayFF)

loop100Generations()