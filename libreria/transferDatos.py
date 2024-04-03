import RPi.GPIO as GPIO
import time
import datetime
import os
from libreria import teclado
from libreria import LCD_LIB_16x2 as LCD
from libreria import transferDatos



def TransferirDatos(dirMac):
    
    flagDisp=0
    key=""
    count=0
    envRec=False
    envRecAUX=False
    
    
    
    while(not envRecAUX):
        
        if (flagDisp>20):
            flagDisp=1
        else:
            flagDisp=flagDisp+1
        if(key==""):     
            key=teclado.Teclado(key,count)
            print(key)
        
        if((key=="Up")or(key=="Down")):
            if(envRec):
                envRec=False
            else:
                envRec=True
            key=""
        elif((key=="Right")or(key=="Left")):
            key=""
        elif(key=="Enter"):
            envRecAUX=True
            key=""
        else:
            key=""
        
        if(flagDisp<10):
            LCD.lcd_string("     ENVIAR     ",LCD.LINE_1)
            LCD.lcd_string("    RECIBIR    ",LCD.LINE_2)
        else:
            if(envRec):
                LCD.lcd_string(" ",LCD.LINE_1)
                LCD.lcd_string("    RECIBIR    ",LCD.LINE_2)
            else:
                LCD.lcd_string("     ENVIAR     ",LCD.LINE_1)
                LCD.lcd_string(" ",LCD.LINE_2)
        
    while(envRecAUX):
        if(envRec):
            print("holis")
        else:
            print("chauchis")
            
        
    return