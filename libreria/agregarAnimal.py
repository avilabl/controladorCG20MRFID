import RPi.GPIO as GPIO
import time
import datetime
import os
from libreria import teclado
from libreria import LCD_LIB_16x2 as LCD
from libreria import agregarAnimal

def AgregarAnimal():
    
    flagDisp=0
    key=""
    count=0
    ok=True
    dig=0
    digCaravana=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    nroCaravana=0
    guardarSalir=False
    guardar=True
    
    while(ok):
        
        LCD.lcd_string("Nro de Caravana",LCD.LINE_1)
        if(flagDisp > 20):
            flagDisp=0
        else:
            flagDisp=flagDisp+1
        if(key==""):     
            key=teclado.Teclado(key,count)
            print(key)
        if(key=="Up"):
            digCaravana[dig]=digCaravana[dig]+1
            if(digCaravana[dig]>9):
                digCaravana[dig]=0
            elif(digCaravana[dig]<0):
                digCaravana[dig]=0
            key=""
        elif(key=="Down"):
            digCaravana[dig]=digCaravana[dig]-1
            if(digCaravana[dig]<0):
                digCaravana[dig]=9
            elif(digCaravana[dig]>9):
                digCaravana[dig]=0
            key=""
        elif(key=="Left"):
            dig=dig+1
            if(dig>14):
                dig=0
            elif(dig<0):
                dig=0
            key=""
        elif(key=="Right"):
            dig=dig-1
            if(dig<0):
                dig=14
            elif(dig>14):
                dig=0
            key=""
        elif(key=="Enter"):
            for i in range(14, -1, -1):
                nroCaravana=nroCaravana+(digCaravana[i]*(10**(14-i)))
            ok=False
            guardarSalir=True
            key=""
        else:
            key=""
        
        if(flagDisp<10):
            LCD.lcd_string(str(digCaravana[0])+str(digCaravana[1])+str(digCaravana[2])+
                           str(digCaravana[3])+str(digCaravana[4])+str(digCaravana[5])+
                           str(digCaravana[6])+str(digCaravana[7])+str(digCaravana[8])+
                           str(digCaravana[9])+str(digCaravana[10])+str(digCaravana[11])+
                           str(digCaravana[12])+str(digCaravana[13])+str(digCaravana[14]),LCD.LINE_2)
        else:
            if(dig==0):
                LCD.lcd_string(" "+str(digCaravana[1])+str(digCaravana[2])+
                           str(digCaravana[3])+str(digCaravana[4])+str(digCaravana[5])+
                           str(digCaravana[6])+str(digCaravana[7])+str(digCaravana[8])+
                           str(digCaravana[9])+str(digCaravana[10])+str(digCaravana[11])+
                           str(digCaravana[12])+str(digCaravana[13])+str(digCaravana[14]),LCD.LINE_2)
            elif(dig==1):
                LCD.lcd_string(str(digCaravana[0])+ " " +str(digCaravana[2])+
                           str(digCaravana[3])+str(digCaravana[4])+str(digCaravana[5])+
                           str(digCaravana[6])+str(digCaravana[7])+str(digCaravana[8])+
                           str(digCaravana[9])+str(digCaravana[10])+str(digCaravana[11])+
                           str(digCaravana[12])+str(digCaravana[13])+str(digCaravana[14]),LCD.LINE_2)
            elif(dig==2):
                LCD.lcd_string(str(digCaravana[0])+str(digCaravana[1])+ " " +
                           str(digCaravana[3])+str(digCaravana[4])+str(digCaravana[5])+
                           str(digCaravana[6])+str(digCaravana[7])+str(digCaravana[8])+
                           str(digCaravana[9])+str(digCaravana[10])+str(digCaravana[11])+
                           str(digCaravana[12])+str(digCaravana[13])+str(digCaravana[14]),LCD.LINE_2)
            elif(dig==3):
                LCD.lcd_string(str(digCaravana[0])+str(digCaravana[1])+str(digCaravana[2])+
                           " " +str(digCaravana[4])+str(digCaravana[5])+
                           str(digCaravana[6])+str(digCaravana[7])+str(digCaravana[8])+
                           str(digCaravana[9])+str(digCaravana[10])+str(digCaravana[11])+
                           str(digCaravana[12])+str(digCaravana[13])+str(digCaravana[14]),LCD.LINE_2)
            elif(dig==4):
                LCD.lcd_string(str(digCaravana[0])+str(digCaravana[1])+str(digCaravana[2])+
                           str(digCaravana[3])+ " " +str(digCaravana[5])+
                           str(digCaravana[6])+str(digCaravana[7])+str(digCaravana[8])+
                           str(digCaravana[9])+str(digCaravana[10])+str(digCaravana[11])+
                           str(digCaravana[12])+str(digCaravana[13])+str(digCaravana[14]),LCD.LINE_2)
            elif(dig==5):
                LCD.lcd_string(str(digCaravana[0])+str(digCaravana[1])+str(digCaravana[2])+
                           str(digCaravana[3])+str(digCaravana[4])+ " " +
                           str(digCaravana[6])+str(digCaravana[7])+str(digCaravana[8])+
                           str(digCaravana[9])+str(digCaravana[10])+str(digCaravana[11])+
                           str(digCaravana[12])+str(digCaravana[13])+str(digCaravana[14]),LCD.LINE_2)
            elif(dig==6):
                LCD.lcd_string(str(digCaravana[0])+str(digCaravana[1])+str(digCaravana[2])+
                           str(digCaravana[3])+str(digCaravana[4])+str(digCaravana[5])+
                           " " +str(digCaravana[7])+str(digCaravana[8])+
                           str(digCaravana[9])+str(digCaravana[10])+str(digCaravana[11])+
                           str(digCaravana[12])+str(digCaravana[13])+str(digCaravana[14]),LCD.LINE_2)
            elif(dig==7):
                LCD.lcd_string(str(digCaravana[0])+str(digCaravana[1])+str(digCaravana[2])+
                           str(digCaravana[3])+str(digCaravana[4])+str(digCaravana[5])+
                           str(digCaravana[6])+ " " +str(digCaravana[8])+
                           str(digCaravana[9])+str(digCaravana[10])+str(digCaravana[11])+
                           str(digCaravana[12])+str(digCaravana[13])+str(digCaravana[14]),LCD.LINE_2)
            elif(dig==8):
                LCD.lcd_string(str(digCaravana[0])+str(digCaravana[1])+str(digCaravana[2])+
                           str(digCaravana[3])+str(digCaravana[4])+str(digCaravana[5])+
                           str(digCaravana[6])+str(digCaravana[7])+ " " +
                           str(digCaravana[9])+str(digCaravana[10])+str(digCaravana[11])+
                           str(digCaravana[12])+str(digCaravana[13])+str(digCaravana[14]),LCD.LINE_2)
            elif(dig==9):
                LCD.lcd_string(str(digCaravana[0])+str(digCaravana[1])+str(digCaravana[2])+
                           str(digCaravana[3])+str(digCaravana[4])+str(digCaravana[5])+
                           str(digCaravana[6])+str(digCaravana[7])+str(digCaravana[8])+
                           " " +str(digCaravana[10])+str(digCaravana[11])+
                           str(digCaravana[12])+str(digCaravana[13])+str(digCaravana[14]),LCD.LINE_2)
            elif(dig==10):
                LCD.lcd_string(str(digCaravana[0])+str(digCaravana[1])+str(digCaravana[2])+
                           str(digCaravana[3])+str(digCaravana[4])+str(digCaravana[5])+
                           str(digCaravana[6])+str(digCaravana[7])+str(digCaravana[8])+
                           str(digCaravana[9])+ " " +str(digCaravana[11])+
                           str(digCaravana[12])+str(digCaravana[13])+str(digCaravana[14]),LCD.LINE_2)
            elif(dig==11):
                LCD.lcd_string(str(digCaravana[0])+str(digCaravana[1])+str(digCaravana[2])+
                           str(digCaravana[3])+str(digCaravana[4])+str(digCaravana[5])+
                           str(digCaravana[6])+str(digCaravana[7])+str(digCaravana[8])+
                           str(digCaravana[9])+str(digCaravana[10])+ " " +
                           str(digCaravana[12])+str(digCaravana[13])+str(digCaravana[14]),LCD.LINE_2)
            elif(dig==12):
                LCD.lcd_string(str(digCaravana[0])+str(digCaravana[1])+str(digCaravana[2])+
                           str(digCaravana[3])+str(digCaravana[4])+str(digCaravana[5])+
                           str(digCaravana[6])+str(digCaravana[7])+str(digCaravana[8])+
                           str(digCaravana[9])+str(digCaravana[10])+str(digCaravana[11])+
                           " " +str(digCaravana[13])+str(digCaravana[14]),LCD.LINE_2)
            elif(dig==13):
                LCD.lcd_string(str(digCaravana[0])+str(digCaravana[1])+str(digCaravana[2])+
                           str(digCaravana[3])+str(digCaravana[4])+str(digCaravana[5])+
                           str(digCaravana[6])+str(digCaravana[7])+str(digCaravana[8])+
                           str(digCaravana[9])+str(digCaravana[10])+str(digCaravana[11])+
                           str(digCaravana[12])+ " " +str(digCaravana[14]),LCD.LINE_2)
            elif(dig==14):
                LCD.lcd_string(str(digCaravana[0])+str(digCaravana[1])+str(digCaravana[2])+
                           str(digCaravana[3])+str(digCaravana[4])+str(digCaravana[5])+
                           str(digCaravana[6])+str(digCaravana[7])+str(digCaravana[8])+
                           str(digCaravana[9])+str(digCaravana[10])+str(digCaravana[11])+
                           str(digCaravana[12])+str(digCaravana[13])+ " " ,LCD.LINE_2)
            
    while(guardarSalir):
 
        LCD.lcd_string(str(nroCaravana).zfill(15),LCD.LINE_1)
        
        if(flagDisp > 20):
            flagDisp=0
        else:
            flagDisp=flagDisp+1
        if(key==""):     
            key=teclado.Teclado(key,count)
            print(key)
            
        if(key=="Enter"):
            guardarSalir=False
            key=""
        elif(key=="Right" or key=="Left"):
            if(guardar):
                guardar=False
            else:
                guardar=True
            key=""    
        elif(key=="Down" or key=="Up"):
            key=""
        
        if(flagDisp<10):
            LCD.lcd_string("Guardar    Salir",LCD.LINE_2)
        else:
            if(guardar):
                LCD.lcd_string("           Salir",LCD.LINE_2)
            else:
                LCD.lcd_string("Guardar         ",LCD.LINE_2)
        
    if(guardar):
        LCD.lcd_string("***guardando***",LCD.LINE_2)
        time.sleep(2)
    else:
        LCD.lcd_string("***no guardado***",LCD.LINE_2)
        time.sleep(2)
        
    return