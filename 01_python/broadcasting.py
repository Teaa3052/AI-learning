import numpy as np

scores = np.array([[78, 92, 85],
                   [65, 74, 80]])

print(scores.shape)
print(scores.mean(axis=0), scores.mean(axis=0).shape)
print(scores.mean(axis=1), scores.mean(axis=1).shape)

print(scores - scores.mean(axis=0))
print(scores - scores.mean(axis=1))
