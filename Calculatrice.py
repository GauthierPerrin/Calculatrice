import time
Addition = 0
Division =0
Soustraction = 0
Multiplication =0
a=0
b=0
c=0
c1 = 0
d=-1
d= int(d)
while (d != 0) :
    print ("Choisir l'operation :")
    print ("\t0 - pour quitter")
    print ("\t1 - Addition ")
    print ("\t2 - Division  ")
    print ("\t3 - Soustraction  ")
    print ("\t4 - Multiplication  ")
    print ("\t5 - Racine caree  ")
    d=-1
    while (d != 0 and d != 1 and d != 2 and d != 3 and d != 4 and d !=5) :
        d = input ("Operation choisie : ")
        d= int (d)
    if (d != 0):
        a = input ("Entrer la premiere valeur :")  
        a = int (a)
        b= input ("Entrer la deuxieme valeur :")
        b = int (b)
        if (d==1):
            c= a+b    
        elif (d==2):
            c= a/b
        elif (d==3):
            c= a-b
        elif (d==4):
            c= a*b
        elif (d==5):
            c= a * a
            c1 = b*b
        print ("Le resultat est :",c ,"\n")
        print ("Le resultat est :",c1 ,"\n")
        print ("Fin")
        time ( 200) 

