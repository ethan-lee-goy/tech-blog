import numpy as np

def true_value_function(s):
    return np.sin(s)

np.random.seed(42)
sampled_states = np.random.uniform(-np.pi, np.pi, 50)
sampled_targets = true_value_function(sampled_states) + np.random.normal(0, 0.1, 50)

class LinearValueApproximator:
    def __init__(self, degree=3, lr=0.01):
        self.degree = degree
        self.lr = lr
        self.w = np.zeros(degree + 1)
        
    def extract_features(self, s):
        return np.array([s**i for i in range(self.degree + 1)])
        
    def predict(self, s):
        features = self.extract_features(s)
        return np.dot(self.w, features)
        
    def update(self, s, target):
        features = self.extract_features(s)
        prediction = self.predict(s)
        error = target - prediction
        self.w += self.lr * error * features

linear_approx = LinearValueApproximator(degree=5, lr=0.00001)
epochs = 10000
for _ in range(epochs):
    for s, target in zip(sampled_states, sampled_targets):
        linear_approx.update(s, target)

print(linear_approx.w)
