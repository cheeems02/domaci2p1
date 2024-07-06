import math as m

###unos
lista = []
def unos(list1): 
    trougao = input().split() #Unos kao string od 6 brojeva
    for i in range(6):
        if trougao != []:#Ne konvertuj prazan trougao
            trougao[i] = float(trougao[i])
    if trougao != []:
        list1.append(trougao)
    while trougao != []: #kada je prazan unos isti se prekida
        trougao = input().split()
        for i in range(6):
            if trougao != []:
                trougao[i] = float(trougao[i])
        if trougao != []:
            list1.append(trougao)
    return list1
lista = unos(lista)
def ispis(list1): 
    for skup in list1:
        print("{:.2f}".format(skup[0]),"{:.2f}".format(skup[1]),"{:.2f}".format(skup[2]),"{:.2f}".format(skup[3]),"{:.2f}".format(skup[4]),"{:.2f}".format(skup[5]))
ispis(lista)

###stranice
a = []
b = []
c = []
def stranice(list1,list2,list3,list4):
    for i in range(len(list1)):#Primena Pitagorine teoreme na Dekartov koordinatni sistem
        list2.append(m.sqrt((list1[i][0]-list1[i][2])**2+(list1[i][1]-list1[i][3])**2))
        list3.append(m.sqrt((list1[i][2]-list1[i][4])**2+(list1[i][3]-list1[i][5])**2))
        list4.append(m.sqrt((list1[i][0]-list1[i][4])**2+(list1[i][1]-list1[i][5])**2))
    return list2, list3, list4
a, b, c = stranice(lista, a, b, c)

###validnost
def validnost(list1, list2, list3, list4):
    j = 0
    while j < len(lista):#kad naiđe na trougao i izbaci ga, svim trouglovima se indeks pomeri za 1 unazad pa zato ne raste brojač svaki put
        if list2[j] + list3[j] <= list4[j] or list2[j] + list4[j] <= list3[j] or list3[j] + list4[j] <= list2[j]:#Nejednakost trougla -> pravilo a+b>c 
            list2.pop(j)
            list3.pop(j)
            list4.pop(j)
            list1.pop(j)
        else:
            j += 1 #Ako je trougao validan, pređi na sledeći, pošto isti nije izbačen broj članova i indeks istih se ne menja
    return list1, list2, list3, list4    
lista, a, b, c = validnost(lista, a, b, c)
ispis(lista)

###Površina 
def površina(list1, list2, list3, list4):
    if len(list1)>0:###da ne računa površinu ako je lista prazna
        p = []
        for f in range(len(list1)):
            p.append(m.sqrt((list2[f]+list3[f]+list4[f])*(list2[f]+list3[f]-list4[f])*(list2[f]-list3[f]+list4[f])*(list3[f]+list4[f]-list2[f])/16))#Heronov obrazac
        maksimum = max(p)
        minimum = min(p)
        maksimum_indeks = p.index(maksimum)
        minimum_indeks = p.index(minimum)
        #Ispis kao na početku
        print("{:.2f}".format(list1[maksimum_indeks][0]),"{:.2f}".format(list1[maksimum_indeks][1]),"{:.2f}".format(list1[maksimum_indeks][2]),"{:.2f}".format(list1[maksimum_indeks][3]),"{:.2f}".format(list1[maksimum_indeks][4]),"{:.2f}".format(list1[maksimum_indeks][5]))
        print("{:.2f}".format(list1[minimum_indeks][0]),"{:.2f}".format(list1[minimum_indeks][1]),"{:.2f}".format(list1[minimum_indeks][2]),"{:.2f}".format(list1[minimum_indeks][3]),"{:.2f}".format(list1[minimum_indeks][4]),"{:.2f}".format(list1[minimum_indeks][5]))
površina(lista, a, b, c)
###kraj