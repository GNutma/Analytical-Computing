import numpy as np

np.random.seed(12324)

n_states = 5
n_steps = 50
tolerance = 1e-5

# Random transition matrix and state vector
transitionMatrix = np.array([[0.8, 0.1, 0.1],[0.4, 0.5, 0.1],[0.6, 0.2, 0.2]])
stateVector = np.array([0.1, 0.7, 0.2])
print(transitionMatrix.T)
# Normalize rows in P
transitionMatrix /= transitionMatrix.sum(axis=1)[:, np.newaxis]
print(transitionMatrix)

# Normalize p
stateVector /= stateVector.sum()

# Take steps
for k in range(n_steps):
    Test1 = transitionMatrix.dot(stateVector)

p_50 = Test1
print(p_50)

# Compute stationary state
w, v = np.linalg.eig(transitionMatrix.T)

p_stationary = v[:, np.argmin(abs(w - 1.0))].real
p_stationary /= p_stationary.sum()
print(p_stationary)

# Compare
if all(abs(p_50 - p_stationary) < tolerance):
    print("Tolerance satisfied in infty-norm")

if np.linalg.norm(p_50 - p_stationary) < tolerance:
    print("Tolerance satisfied in 2-norm")
