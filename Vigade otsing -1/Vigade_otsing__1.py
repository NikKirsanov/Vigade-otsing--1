from math import * #pole seda väärt õige *

print("Ruudu karakteristikud")
a=float(input("Sisesta ruudu külje pikkus => ")) #esimene viga, mille ma leidsin, on 4. real 2. punkt lisa ujuk
S=a**2
print("Ruudu pindala", (S,1))
P=4*a
print("Ruudu ümbermõõt", (P,1))
di=a*sqrt(2) #seada"
print("Ruudu diagonaal", round(di,2))
print()
print("Ristküliku karakteristikud") #sulg pole õige
b=float(input("Sisesta ristküliku 1. külje pikkus => "))
c=float(input("Sisesta ristküliku 2. külje pikkus => "))
S=b*c
print("Ristküliku pindala" , round(S,1))
P=2*(b+c)
print("Ristküliku ümbermõõt", (P,1))
di=sqrt(b*2+c*2) #seada"
print("Ristküliku diagonaal", round(di,1))
print()
print("Ringi karakteristikud")
r=float(input("Sisesta ringi raadiusi pikkus => "))  #pane see korda"
d="2r" #pane "
print("Ringi läbimõõt" , round(S,2)) #kolis"
S=pi*r**2
print("Ringi pindala", round(S,2))
C=2*pi*r #pane"
print("Ringjoone pikkus", round (C,2))
