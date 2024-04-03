import RPi.GPIO as GPIO
import time
import datetime
import serial
import threading
from libreria import teclado
from libreria import datosBD
from libreria import menu
from libreria import LCD_LIB_16x2 as LCD
from libreria import habilitacionAnimal


class DatosAnimal:
    def __init__(self, number: str,dayStart: str,dayDiet: str,load: str,horary: str,eat: str,dispensed: str):
        self.number = number
        self.dayStart = dayStart
        self.dayDiet = dayDiet
        self.load = load
        self.horary = horary
        self.eat= eat
        self.dispensed = dispensed
        
antena = serial.Serial('/dev/ttyUSB0', 9600)

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.IN)
GPIO.setup(29, GPIO.IN)
GPIO.setup(31, GPIO.IN)
GPIO.setup(33, GPIO.IN)
GPIO.setup(37, GPIO.IN)
GPIO.setup(32, GPIO.OUT)

GPIO.output(32,True)


LCD.lcd_init()

caravana=""
cadena=""
countKey=0
fin=1
keyPress=""
main=0
showCaravana=0
addAnimal=False
dosis=1
reader=""
animales={}
foodOK=[False,0]
retardoON=False
listAuxMain=[]
habilitado=True
datoAnimal=[]
i=0
alarmaDesconicido=False
mensajeDesconocido=False


fecha=datetime.datetime.now()
fechAux=fecha.strftime('%d/%m/%Y-%H:%M')

LCD.lcd_string(fechAux,LCD.LINE_1)
LCD.lcd_string("esperando animal",LCD.LINE_2)

def Retardo():
    GPIO.output(32,True)
    global foodOK
    foodOK[0]=False
    global retardoON
    retardoON=False
    global mensajeDesconocido
    mensajeDesconocido=False
    global showCaravana
    showCaravana=0


datoAnimal=datosBD.LeerDatoAnimal()

while(True):
    
    #fin=fin+1
    if(main==0):

        if(mensajeDesconocido):
            LCD.lcd_string(" ID desconocido ",LCD.LINE_1)
        else:
            fecha=datetime.datetime.now()    
            fechAux=fecha.strftime('%d/%m/%Y-%H:%M')
            LCD.lcd_string(fechAux,LCD.LINE_1)
        
        if (showCaravana == 0):
            LCD.lcd_string("esperando animal",LCD.LINE_2)
        else:

            LCD.lcd_string(caravana,LCD.LINE_2)
    
        #keyPress=teclado.Teclado(keyPress,countKey)
    
        transmition=antena.inWaiting()
        if transmition:
            caravanaAux = antena.read()
            caravanaAux1=caravanaAux.decode()
            if(caravanaAux1 == '$'):
                reader=""
                cadena=""
            else:
                cadena=cadena + caravanaAux.decode()
            if(caravanaAux1 == '#'):
                reader=cadena[8:23:]
                caravana=reader
        reader=input()
        
        if reader!="":
            for i in range(len(datoAnimal)):
                if(datoAnimal[i].number!=reader):
                    alarmaDesconicido=True
                    mensajeDesconocido=True
                    foodOK[0]=True
                    foodOK[1]=0
                else:
                    alarmaDesconicido=False
                    break
        if((reader!="") and (not alarmaDesconicido)):        
            foodOK,datoAnimal=habilitacionAnimal.HabilitacionAnimal(reader,datoAnimal)
        #if reader in animales:
        #    subtr = datetime.datetime.now() - animales[reader]
        #    subtrSec = (subtr.days*24*3600)+(subtr.seconds)
        #    if subtrSec > 120 :
        #        foodOK=True
        #        animales[reader]= datetime.datetime.now()
        #    else:
        #        caravana="animal inhabil."
        #        showCaravana=1
        #        t=threading.Timer(10,Retardo)
        #        t.start()
        #    reader=""
        #else:
        #    if reader!="":
        #        animales[reader]= datetime.datetime.now()
        #        foodOK=True
        #        reader=""
        print(foodOK)
        if foodOK[0] and (not retardoON):
            GPIO.output(32,False)
            retardoON=True
            showCaravana=1
            if(foodOK[1]==0):
                if(not mensajeDesconocido):
                    caravana="animal inhabil."
                    t=threading.Timer(15*dosis,Retardo)
                else:
                    caravana=reader
                    t=threading.Timer(15*dosis,Retardo)
            else:
                t=threading.Timer(foodOK[1]*dosis,Retardo)
            t.start()
#            foodOK[0]=False
#            escribirFile.GuardarDatoReal(caravana,dosis)
        
            #print(animales)
            #GPIO.output(32,False)
            #time.sleep(10)
            #GPIO.output(32,True)
            #foodOK=False
        
        
    if(keyPress==""):     
        keyPress=teclado.Teclado(keyPress,countKey)
        print(keyPress)
        if(keyPress==""):
            habilitado=True
    
    if(main==0 and keyPress!="Right"):
        keyPress=""
        
    
    if(main==0 and keyPress=="Right"):
        keyPress=""
        main=1
       
    if(habilitado):
        listAuxMain=menu.Menu(main,keyPress,habilitado,dosis)
    keyPress=listAuxMain[0]
    main=listAuxMain[1]
    habilitado=listAuxMain[2]
    dosis=listAuxMain[3]
        #menu(teclado)

  #  if fin>2000:
   #     fin=0
        

GPIO.cleanup()
 