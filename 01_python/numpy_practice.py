import numpy as np


# =========================
# 1. Basic arrays
# =========================

numbers = np.array([1, 2, 3, 4, 5])

print(numbers)
print(numbers * 10)


# =========================
# 2. Shape and dimensions
# =========================

grades = np.array([
    [5, 4, 5],
    [3, 5, 4],
    [4, 4, 5]
])

print(grades)
print(grades.shape)
print(grades.dtype)
print(grades.ndim)
print(grades.shape[0])
print(grades.shape[1])


# =========================
# 3. Aggregations
# =========================

print(np.min(grades, axis=1))
print(np.average(grades, axis=0))


# =========================
# 4. Boolean masking
# =========================

print(grades[grades < 4])
print(grades[(grades == 3) | (grades == 5)])


scores = np.array([
    [78, 92, 85],
    [65, 74, 80],
    [90, 88, 95],
    [55, 67, 61],
    [82, 79, 91]
])

print("Dimenzije matrice:", scores.shape)


# =========================
# 5. Agregation and data analysis
# =========================

print("\nOSNOVNA ANALIZA")

print("Ukupan broj elemenata ", np.size(scores))
print("Ukupan zbroj svih razultata ", np.sum(scores))
print("Najveci rezultat je ", np.max(scores))
print("Najmanje rezultat je ", np.min(scores))
print("Prosjek svih rezultat ", np.average(scores))

print("\nANALIZA PO STUDENTIMA")
print("Prosjek ", np.average(scores, axis=1))
print("Najbolji rezultat ", np.max(scores, axis=1))
print("Najlosiji rezultat ", np.min(scores, axis=1))
print("Zbroj bodova ", np.sum(scores, axis=1))

print("\nANALIZA PO PREDMETIMA")
print("Prosjek ", np.average(scores, axis=0))
print("Najbolji rezultat ", np.max(scores, axis=0))
print("Najlosiji rezultat ", np.min(scores, axis=0))
print("Zbroj bodova ", np.sum(scores, axis=0))

print("\nFILTRIRANJE")
print("Svi rezultati veci od 80 ", scores[scores > 80])
print("Svi rezultati manji od 60 ", scores[scores < 60])
print("Svi rezultati izmedu 70 i 90 ", scores[(scores > 70) & (scores < 90)])
print("Svi rezultati koji su točno 95 ", scores[scores == 95])
print("Najveci prosjek ", np.max(np.average(scores, axis=1)))

# Izračunaj prosjek svakog studenta i pomoću boolean 
# maskiranja pronađi samo studente čiji je prosjek ≥ 80.

print("Maskiranje\n", scores[np.average(scores, axis=1)>=80])
print(np.average(scores, axis=1) >= 80)

# std 
print(np.std(scores))
print(np.std(scores, axis=1))

# Pronadi studente koji imaju barem jednu ocjenu veću od 95 
print(scores[(np.any(scores >= 95, axis=1))])

# Pronadi ocjene koje su vece ili jednake 80 bez obzira kojem studentu/predmetu pripadaju 
print(scores[scores >= 80])

# Ispisi retke studenata kojima je standardna devijacija ocjena manja od 10 
print(scores[(np.std(scores, axis=1) < 10)])

# Pronadi indeks studenta koji ima najveci prosjek 
print(np.argmax((np.average(scores, axis=1))))
print(np.argmin((np.average(scores, axis=1))))

print("Prvi redak\n", scores[0:1])
print("Zadnji redak\n", scores[-1])
print("Prva ocjena svakog studenta (prvi stupac)\n", scores[:, 0])
print("Zadnja dva retka\n", scores[3:])
print("Prva dva stupca\n", scores[:, 0:2])

print("Ocjene prvog i treceg studenta\n", scores[[0, 2]]) # "Fancy indexing"
print("Prve dvije ocjene drugog studenta\n", scores[1:2, 0:2])

print("Sve osim prvog retka i prvog stupca\n", scores[1:, 1:] )


a = np.array([
    [4, 1, 4, 2],
    [3, 3, 1, 2],
    [5, 5, 5, 4]
])

print("Prosjek ocjena svakog stupca:\n", a.mean(axis=0))
print("Ukupan broj ocjena većih od prosjeka:\n", np.sum((a > a.mean())))
print("Ukupan broj ocjena većih od prosjeka:\n", (a > a.mean()).sum())

# print(a > a.mean())