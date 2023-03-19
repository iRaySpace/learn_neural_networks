# Receive inputs and weight inputs
data = [
    {"input": 12, "weight": 0.5},
    {"input": 4, "weight": -1},
]

# Weighted inputs
weighted_data = [x.get("input") * x.get("weight") for x in data]

# Sum all the weighted inputs
result = sum(weighted_data)

# Activation function
def activate(x):
    return 1 if x > 0 else -1

output = activate(result)

print(output)
