from math import *
import time
Addition = 0
Division =0
Soustraction = 0
Multiplication =0
val1=0
val2=0
res1=0
res2 = 0
d= -1
d= int(d)
p = False
while (d != 0) :
    print ("Choisir l'operation :")
    print ("\t0 - pour quitter")
    print ("\t1 - Addition ")
    print ("\t2 - Division  ")
    print ("\t3 - Soustraction  ")
    print ("\t4 - Multiplication  ")
    print ("\t5 - Racine caree  ")
    d = input ("Operation choisie : ")
    d= int (d)
    while  (d == 1 or d == 2 or d == 3 or d == 4 or d == 5 ) :
        if (p == False) :
            val1 = input ("Entrer la premiere valeur :")  
            val1 = int (val1)
            val2= input ("Entrer la deuxieme valeur :")
            val2 = int (val2)
            p = True
            if (d==1):
                res1= val1+val2
            elif (d==2):
                res1= val1/val2    
            elif (d==3):
                res1= val1-val2    
            elif (d==4):
                res1= val1*val2    
            elif (d==5):
                res1= sqrt(val1+val2)
        else :
            val2= input ("Entrer la deuxieme valeur :")
            val2= int (val2)
            if (d==1):
                res1= res1+val2
            elif (d==2):
                res1= res1/val2    
            elif (d==3):
                res1= res1-val2    
            elif (d==4):
                res1= res1*val2    
            elif (d==5):
                res1= sqrt(res1+val2)
            
        print ("Le resultat est :",res1,"\n\n")
        print ("Choisir l'operation :")
        print ("\t0 - pour quitter")
        print ("\t1 - Addition ")
        print ("\t2 - Division  ")
        print ("\t3 - Soustraction  ")
        print ("\t4 - Multiplication  ")
        print ("\t5 - Racine caree  ")
        d = input ("Operation choisie : ")
        d = int (d)
        
          


