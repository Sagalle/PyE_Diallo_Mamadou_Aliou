from csv import *
from datetime import date
import re
from sqlite3 import Date
def nomValid(Nom):
    if row ["Nom"][0].isalpha() and len(Nom)>=2:
        return True

def prenomValid(Prenomom):
    if row["PrÃ©nom"][0].isalpha() and len(Prenomom)>=3:
        return True

def numValid(Numero):
    if row["Numero"].isalnum() and row["Numero"].isupper and len(Numero)>= 7:
        return True
Date = "10_02@20"
def formatdate(Date):
    datevalid = re.split("[ -./:;_$@]",Date)
    m = ( re.split("[ -./:;_$@]",Date))
    # print(m)
    # if m[1].isalpha():
    #         if m in "janvier":
    #             m = 1
    #         elif m in ["fevrier","février","fev","fév"]:
    #             m = 2
    #         elif m in "mars":
    #             m = 3
    #         elif m in "avril":
    #             m = 4
    #         elif m in "mai":
    #             m = 5
    #         elif m in "juin":
    #             m = 6
    #         elif m in "juillet":
    #             m = 7
    #         elif m in ["Aout", "Aoùt","aout","aoùt"]:
    #             m = 8
    #         elif m in "septembre":
    #             m = 9
    #         elif m in "octobre":
    #             m = 10
    #         elif m in "Novembre":
    #             m = 11
    #         elif m in ["decembre","décembre"]:
    #             m = 12

    return datevalid

def verifDate(j,m,a):
    try:
        naiss = date(a,m,j)
        return True
    except ValueError:
        
        return False

d="10_02@20"
x=formatdate(d)
print(formatdate(d))
j = int(x[0])
m = int(x[1])
a = int(x[2])

# print(verifDate(j,m,a))
valide = [] 
nonvalide = []   
incomplet = []   
file0 = open("fic.csv","r")
myReader = DictReader(file0)
for row in myReader:
    if row["Nom"] == ""  or  row["PrÃ©nom"] == "" or  row["Numero"] == "":
        incomplet.append(row)
    elif nomValid(row["Nom"]) == True and prenomValid(row["PrÃ©nom"]) == True and numValid(row["Numero"]) == True: 
        x=formatdate(row["Date de naissance"])
        # print(x)
        # if verifDate(x[0],x[1],x[2]) == True:
        valide.append(row)
    else:
        nonvalide.append(row)
print("\nfichier valide")
print(valide)
print("\nfichier non valide")
print(nonvalide)
print("\nfichier avec colonne(s) vide(s)")
print(incomplet)