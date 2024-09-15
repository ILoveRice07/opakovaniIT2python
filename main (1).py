import random
# 1. úkol proměnná
jmeno = "Tomáš"

# 2. úkol proměnná
prijmeni = "Nguyen"

# 3. úkol vypíše proměnnou #1 a #2
print(jmeno,prijmeni)

# 4. úkol zadání věku
while True:
 vek = input("Zadej svůj věk v číslech:")

# 9. úkol ověření věku
 if vek.isdigit():
   vek = int(vek)
   print("Děkuji.")
   break
 else:
   print("Zadej jen celočíselnou hodnotu!!")
   continue

# 5. úkol vypsání dělky #1 a #2
print("Délka jména je",len(jmeno),"písmen.")
print("Délka příjmení je",len(prijmeni),"písmen.")

# 6. úkol proměnná
x=6

# 7. úkol cyklus sčítání 3, 5 krát
for i in range(5):
 x=x+3

# 8. úkol vypsání výsledku cyklu
print("Výsledek cyklu je",x,".")

# 10. úkol náhodná hondota od 1-10
nhodnota=random.randint(1,10)
print("Vylosoval/a jste",nhodnota,".")
