# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 09:58:47 2024

@author: userlocal
"""
import csv
import webbrowser
import matplotlib.pyplot as plt #pour tracer les graphes 
import numpy as np #pour faire des calculs numeriques 



#ouvrir le fichier "fichieratraiter.txt"
fichier=open("fichier a traiter.txt", "r")

#creation des listes = Creer des listes pour remplir chacune d'elles avec les donnees appropriees dans la capture de paquets tcpdump.
ipsr=[]
ipde=[]
longueur=[]
flag=[]
seq=[]
heure=[]

      # creer des compteurs
#un paquet contient des données à envoyer
flagcounterP=0
# le début d'une connexion.
flagcounterS=0
#compteur du nombre de flag [.] Les paquets de confirmation de connexion.
flagcounter=0
#compteur des trames echanges 
framecounter=0
#compteur request = counter for the number of requests
requestcounter=0
#compteur reply = counter for number of replies
replycounter=0
#compteur sequence = sequences counter
seqcounter=0
#compteur acknowledgement = acknowledgments counter
ackcounter=0
#compteur window = windows counter
wincounter=0

for ligne in fichier:
    #faire une separation avec un espace comme delimiteur
    split=ligne.split(" ")
    #delete the hexadecimal blocks and keep only the lines which contain the information
    #supprimez les blocs hexadecimaux et conservez uniquement les lignes contenant les informations.
    if "IP" in ligne :
    #filling the flag list
    #remplissage de la liste drapeau   
        framecounter+=1
        if "[P.]" in ligne :
            flag.append("[P.]")
            flagcounterP+=1
        if "[.]" in ligne :
            flag.append("[.]")
            flagcounter+=1
        if "[S]" in ligne :
            flag.append("[S]")
            flagcounterS+=1
        #filling the seq list
        #remplir la liste seq
        if "seq" in ligne :
            seqcounter+=1
            seq.append(split[8])
        #counting windows
        ##comptage des fenêtres
        if "win" in ligne :
            wincounter+=1
        #counting acks
        #comptage d'accuse de reception
        if "ack" in ligne:
            ackcounter+=1
           
        #filling the IP source(ipsr) list
        #Remplissage de la liste des sources IP (ipsr)
        ipsr.append(split[2]) 
        #filling the IP destination(ipde) list
        #Remplissage de la liste des destinations IP (ipsr)
        ipde.append(split[4])
        #filling the hour (heure) list
        #remplissage de la liste des heures
        heure.append(split[0])
        #filling the lenght (longueur) list
        #remplir la liste de longueur
        if "length" in ligne:
            split = ligne.split(" ")
            if "HTTP" in ligne :
                longueur.append(split[-2])
            else:
                longueur.append(split[-1])
        #to detect request and reply via ICMP protocol
        #detecter les requêtes et les reponses via le protocole ICMP. request icmp
        if "ICMP" in ligne:
            if "request" in ligne:
                requestcounter+=1
            if "reply" in ligne:
                replycounter+=1
'''ipsource2 = []
ipdesti2 = []  
ipdestifinale=[]            
               
for i in ipsr:
    if not "." in i:
        ipsource2.append(i)
    elif "ssh" in i or len(i) > 15 or "B" in i:
        ports = i.split(".")
        del ports[-1]
        delim = "."
        delim = delim.join(ports)
        ipsource2.append(delim)
    else:
        ipsource2.append(i)
for j in ipde:
    if not "." in j:
        ipdesti2.append(j)
    elif "ssh" in j or len(j) > 15 or "B" in j:
        ports = j.split(".")
        del ports[-1]
        delim = "."
        delim = delim.join(ports)
        ipdesti2.append(delim)
    else:
        ipdesti2.append(j)

for l in ipdesti2:
    if not ":" in l:
        ipdestifinale.append(l)
    else:
        deuxp = l.split(":")
        ipdestifinale.append(deuxp[0])   '''

            
globalflagcounter=flagcounter+flagcounterP+flagcounterS

P=flagcounterP/globalflagcounter
S=flagcounterS/globalflagcounter
A=flagcounter/globalflagcounter

globalreqrepcounter=replycounter+requestcounter
req=requestcounter/globalreqrepcounter
rep=replycounter/globalreqrepcounter
         
#transform all counters into lists to view them on the csv file
#transformer tous les compteurs en listes pour les afficher dans le fichier csv
flagcounter=[flagcounter]
flagcounterP=[flagcounterP]
flagcounterS=[flagcounterS]
framecounter=[framecounter]
requestcounter=[requestcounter]
replycounter=[replycounter]
seqcounter=[seqcounter]
ackcounter=[ackcounter]
wincounter=[wincounter]



# create python graphic with matplotlib library
#creer un graphe avec la bibliothèque matplotlib
  #circular graphic for flags
  #graphe circulaire pour les flags
name = ['Flag [.]', 'Flag [P]', 'Flag [S]']
data = [A,P,S]

explode=(0, 0, 0) #Ecartement
plt.pie(data, explode=explode, labels=name, autopct='%1.1f%%', startangle=90, shadow=True)
plt.axis('equal') #garantit que le graphique est parfaitement circulaire.
plt.savefig("graphe1.png")
plt.show() #affiche le graphique.
  #circular graphic for request and reply
  #graphe circulaire pour les requêtes et reponses
name2 = ['Request' , 'Reply']
data2 = [req,rep] 
explode=(0,0)
plt.pie(data2,explode=explode,labels=name2, autopct='%1.1f%%',startangle=90, shadow=True)
plt.savefig("graphe2.png")
plt.show()

#contenu de la page web = web page content
htmlcontenu='''
# Traitement des données

## Khadidiatou Ba A1

### Projet SAE 15

Sur cette page web je vais vous présenter les informations et données pertinentes que j'ai trouvées dans le fichier à traiter.

### Nombre total des trames échangées
%s

### Drapeaux (Flags)
- Nombre de flags [P] (PUSH) = %s
- Nombre de flags [S] (SYN) = %s 
- Nombre de flag [.] (ACK) = %s

![Graphique 1](graphe1.png)

### Nombre des requêtes et réponses
- Requêtes = %s
- Réponses = %s

![Graphique 2](graphe2.png)

### Statistiques entre seq, win et ack
- Nombre de seq = %s
- Nombre de win = %s
- Nombre de ack = %s

'''%(framecounter,flagcounterP,flagcounterS,flagcounter,requestcounter,replycounter,seqcounter,wincounter,ackcounter)

#ouverture d'un fichier csv = open a csv file for data extracted from txt file untreated
with open('Khadi.csv', 'w', newline='') as fichiercsv:
    writer = csv.writer(fichiercsv)
    writer.writerow(['Heure','IP source','IP destination','Flag','Seq','Length'])
    writer.writerows(zip(heure,ipsr,ipde,flag,seq,longueur))
    fichiercsv.close()
   
#ouverture d'un fichier csv    = open a csv file for different stats
with open('khadija.csv', 'w', newline='') as fichier2:
    writer = csv.writer(fichier2)
    writer.writerow(['Flag[P] (PUSH)','Flag[S] (SYN)','Flag[.] (ACK)','Nombre total de trames',"nombre de request","nombre de reply","nombre de sequence","nombre de acknowledg","nombre de window"])
    writer.writerows(zip(flagcounterP,flagcounterS,flagcounter,framecounter,requestcounter,replycounter,seqcounter,ackcounter,wincounter))
    fichier2.close()
   
#partie page  web = open a web page with important information and statistics
with open("Khadidiatou.html","w") as html:
    html.write(htmlcontenu)
    print("page web creee avec succès")

      
fichier.close()

