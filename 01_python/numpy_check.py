import numpy as np
grades = np.array([
    [4, 1, 4, 2],
    [3, 3, 1, 2],
    [5, 5, 5, 4],
    [2, 4, 3, 5]
])

print("Prosjek svakog studenta: ", np.mean(grades, axis = 1))
print("Indeks studenta s najvecim prosjekom: ", np.argmax((np.average(grades, axis = 1))))

print("Studenti s barem jednom jedinicom: ", grades[(np.any(grades == 1, axis=1))])

print("Udio ocjena koje su >= 4 je", (np.sum(grades >=4)) / grades.size)
print("Udio ocjena koje su >= 4 je", np.mean(grades  >= 4))

scores = np.array([[78, 92, 85], [65, 74, 80]])

row_means = scores.mean(axis=1, keepdims=True)
print("row_means shape:", row_means.shape)

row_means_alt = scores.mean(axis=1)[:, None]
print("row_means_alt shape:", row_means_alt.shape)

print(scores - row_means)