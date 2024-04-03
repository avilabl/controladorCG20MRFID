class DatosAnimal:
    def __init__(self, number: str,dayStart: str,dayDiet: str,load: str,horary: str,eat: str,dispensed: str):
        self.number = number
        self.dayStart = dayStart
        self.dayDiet = dayDiet
        self.load = load
        self.horary = horary
        self.eat = eat
        self.dispensed = dispensed

import os

def GuardarDatoReal(Caravana):
    
    texto=open("archivos/datoAnimal.txt", "w")

    for i in range(len(Caravana)):
        print(Caravana[i].number)
        print(Caravana[i].dayStart)
        print(Caravana[i].dayDiet)
        print(Caravana[i].load)
        print(Caravana[i].horary)
        print(Caravana[i].eat)
        print(Caravana[i].dispensed)
        texto.write(str(Caravana[i].number)+str(Caravana[i].dayStart)+str(Caravana[i].dayDiet)+str(Caravana[i].load)+str(Caravana[i].horary)+str(Caravana[i].eat)+str(Caravana[i].dispensed+"\n"))
    
    texto.close()

    texto=open("./archivos/datoAnimal.txt", "r")

    nutricion=[]

    for line in texto.readlines():
    
        caravana=line[0:15]
        diaInicio=line[15:28]
        diaDieta=line[28:31]
        peso=line[31:35]
        hora=line[35:37]
        comido=line[37:38]
        dispensado=line[38:51]
        if((dispensado=="\n") or (dispensado=="")):
            dispensado='0000000000000'
    
        nutricion.append(DatosAnimal(caravana,diaInicio,diaDieta,peso,hora,comido,dispensado))
    
    texto.close()

    return nutricion

def LeerDatoAnimal():

    nutricion=[]
    texto=open("archivos/datoAnimal.txt", "r")

    for line in texto.readlines():
    
        caravana=line[0:15]
        diaInicio=line[15:28]
        diaDieta=line[28:31]
        peso=line[31:35]
        hora=line[35:37]
        comido=line[37:38]
        dispensado=line[38:51]
        if((dispensado=="\n") or (dispensado=="")):
            dispensado='0000000000000'
    
        nutricion.append(DatosAnimal(caravana,diaInicio,diaDieta,peso,hora,comido,dispensado))
    
    texto.close()

    return nutricion