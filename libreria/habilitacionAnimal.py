class DatosAnimal:
    def __init__(self, number: str,dayStart: str,dayDiet: str,load: str,horary: str,eat: str,dispensed: str):
        self.number = number
        self.dayStart = dayStart
        self.dayDiet = dayDiet
        self.load = load
        self.horary = horary
        self.eat = eat
        self.dispensed = dispensed

import RPi.GPIO as GPIO
import time
import datetime
import os
from libreria import datosBD

animal=[]


#animal=datosBD.LeerDatoAnimal()

def HabilitacionAnimal(animalLeido,animal):
    nutricion=[]
    nutricionAUX=[]
    diaDietaActual=0
    food=[]
    nro=""
    diaInicio=""
    diaDieta=""
    peso=""
    hora=""
    comido=""
    dispensado=""
    horaReal=""
    i=0
    horaGuardar=""
    retorno=[9999,False]
    animalInhabilitado=[]
#for para crear un nuevo array con todos los elementos que
#contengan el numero de caravana leido    
    for i in range(len(animal)):
        
        if (animal[i].number==animalLeido):
            nro=animal[i].number
            diaInicio=animal[i].dayStart
            diaDieta=animal[i].dayDiet
            peso=animal[i].load
            hora=animal[i].horary
            comido=animal[i].eat
            dispensado=animal[i].dispensed

            nutricion.append(DatosAnimal(nro,diaInicio,diaDieta,peso,hora,comido,dispensado))
    
#if para identificar si el animal tiene dieta o es desconocido

#segun el dia de inicio de dieta se calcula que dia que va de ciclo
    diaDietaActual=(int(time.time()*1000)-(int(nutricion[0].dayStart)))//86400000


#for para crear un nuevo array donde se agregan los elementos
#que el dia de dieta son menor que el dia dieta actual
    for i in range(len(nutricion)):
        if(diaDietaActual>=int(nutricion[i].dayDiet)):
            nutricionAUX.append(DatosAnimal(nutricion[i].number,nutricion[i].dayStart,nutricion[i].dayDiet,nutricion[i].load,nutricion[i].horary,nutricion[i].eat,nutricion[i].dispensed))
        else:
            break

#asigno el valor de diadieta del ultimo elemento del vector
#que este va a contener la dieta mas proxima por lo tanto la que corresponde dar               
    diaDietaAnimal=nutricionAUX[-1].dayDiet
    i=0
#for para crear el arreglo que contiene la dieta a dispensar
    for i in range(len(nutricionAUX)):
        if(nutricionAUX[i].dayDiet==diaDietaAnimal):
            food.append(DatosAnimal(nutricionAUX[i].number,nutricionAUX[i].dayStart,nutricionAUX[i].dayDiet,nutricionAUX[i].load,nutricionAUX[i].horary,nutricionAUX[i].eat,nutricionAUX[i].dispensed))
    
#se le asigna el valor de la hora que es a la variable horaReal para poder comparar
    horaReal=datetime.datetime.now()
    horaReal=horaReal.strftime('%H')

#compara la dieta del dia con la hora para saber si da la comida
    for i in range(len(food)):
        if (int(food[i].horary)<=int(horaReal):
            
        #if ((int(food[i].horary)<=int(horaReal)) and (food[i].eat=="0")):
        #    retorno[1]=int(food[i].load)
        #    retorno[0]=True
        #    food[i].eat="1"

                #########
            for j in range(len(animal)):
                if((animal[j].number==food[i].number) and (animal[j].dayStart==food[i].dayStart) and (animal[j].dayDiet==food[i].dayDiet) and (animal[j].load==food[i].load) and (animal[j].horary==food[i].horary)):
                    animal[j].eat="1"
                    horaGuardar=int(time.time()*1000)
                    animal[j].dispensed=str(horaGuardar)
                    break
                #########
            print(retorno)
            animal=datosBD.GuardarDatoReal(animal)
            break
        else:
            horaGuardar=int(time.time()*1000)
            animal.append(DatosAnimal(animalLeido,"0000000000000",str(diaDietaActual).zfill(3),"0000","00","0",str(horaGuardar)))
            animal=datosBD.GuardarDatoReal(animal)
            retorno[1]=0
            retorno[0]=True

    food.clear()
    nutricion.clear()
    nutricionAUX.clear()    
    #si el animal es desconocido se le administra una dieta predeterminada

    return retorno,animal