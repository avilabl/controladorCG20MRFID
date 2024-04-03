import RPi.GPIO as GPIO
import time
import datetime
from libreria import teclado
from libreria import LCD_LIB_16x2 as LCD
from libreria import cambiarHora
from libreria import dienteAzul
from libreria import ingresarMAC
from libreria import transferDatos
from libreria import agregarAnimal
from libreria import apagarCtrl




def Menu(menu,tecla,habil,timeDosis):
    if(menu==1):
        LCD.lcd_string("    Calibrar    ",LCD.LINE_1)
        LCD.lcd_string("  Fecha y Hora  ",LCD.LINE_2)
        #fecha=datetime.datetime.now()    
        #fechAux=fecha.strftime('%d/%m/%Y-%H:%M')
        #LCD.lcd_string(fechAux,LCD.LINE_2)
        if(tecla == "Right"):
            menu=2
            habil=False
        elif(tecla == "Left"):
            menu=7
            habil=False
        elif(tecla == "Enter"):
            cambiarHora.CambiarHora()
            LCD.lcd_string("Cal.fecha/hora",LCD.LINE_1)
            fecha=datetime.datetime.now()    
            fechAux=fecha.strftime('%d/%m/%Y-%H:%M')
            LCD.lcd_string(fechAux,LCD.LINE_2)
            habil=False
        tecla=""
#    elif (menu==2):
#        LCD.lcd_string(" Config. Disp. ",LCD.LINE_1)
#        LCD.lcd_string("   BLUETOOTH   ",LCD.LINE_2)
#        if(tecla == "Right"):
#            menu=3
#            habil=False
#        elif(tecla == "Left"):
#            menu=1
#            habil=False
#        elif(tecla == "Enter"):
#            dienteAzul.DienteAzul()
#            habil=False
#        tecla=""
    elif (menu==2):
        LCD.lcd_string("Transferir Datos",LCD.LINE_1)
        LCD.lcd_string("Del Dispositivo",LCD.LINE_2)
        if(tecla == "Right"):
            menu=3
            habil=False
        elif(tecla == "Left"):
            menu=1
            habil=False
        elif(tecla == "Enter"):
            dirMAC=ingresarMAC.IngresarMAC()
            transferDatos.TransferirDatos(dirMAC)
            habil=False
        tecla=""
    elif (menu==3):
        LCD.lcd_string(" Agregar Animal ",LCD.LINE_1)
        LCD.lcd_string("     Nuevo      ",LCD.LINE_2)
        if(tecla == "Right"):
            menu=4
            habil=False
        elif(tecla == "Left"):
            menu=2
            habil=False
        elif(tecla == "Enter"):
            agregarAnimal.AgregarAnimal()
            habil=False
        tecla=""
    elif (menu==4):
        LCD.lcd_string("Calibrar Dosis",LCD.LINE_1)
        msjDosis=str(timeDosis)
        msjDosis=msjDosis + " segundos  100g"
        LCD.lcd_string(msjDosis,LCD.LINE_2)
        if(tecla == "Right"):
            menu=5
            habil=False
        elif(tecla == "Left"):
            menu=3
            habil=False
        elif(tecla == "Up"):
            timeDosis=timeDosis+1
            if timeDosis>15:
                timeDosis=15
            habil=False
        elif(tecla == "Down"):
            timeDosis=timeDosis-1
            if timeDosis<1:
                timeDosis=1
            habil=False
        elif(tecla == "Enter"):
            GPIO.output(32,False)
            time.sleep(timeDosis)
            GPIO.output(32,True)
            habil=False
        tecla=""
    elif (menu==5):
        LCD.lcd_string("     Apagar     ",LCD.LINE_1)
        LCD.lcd_string("   Controlador  ",LCD.LINE_2)
        if(tecla == "Right"):
            menu=4
            habil=False
        elif(tecla == "Left"):
            menu=6
            habil=False
        elif(tecla == "Enter"):
            apagarCtrl.ApagarCtrl()
            habil=False
        tecla=""
        
    elif (menu==6):
        LCD.lcd_string("   Salir del    ",LCD.LINE_1)
        LCD.lcd_string("      Menu      ",LCD.LINE_2)
        if(tecla == "Right"):
            menu=1
            habil=False
        elif(tecla == "Left"):
            menu=5
            habil=False
        elif(tecla == "Enter"):
            menu=0
            habil=False
        tecla=""
    else:
       menu=0
       
    listAux=[tecla,menu,habil,timeDosis]
    
    return listAux
    
