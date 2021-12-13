# Írj programot, mely beolvas három egész számot, és kiírja a képernyőre a legkisebbet!

szam1= int(input('Adja meg az egyik számot! '))
szam2= int(input('Adja meg a masik szamot! '))
szam3= int(input('Adja meg a harmadik számot! '))

if szam1 < szam2 < szam3: 
  print('Az első szám a legkisebb' )

elif szam3 < szam2 < szam1 :
  print('A második a legkisebb')

else:
  print('A harmadik a legkisebb')