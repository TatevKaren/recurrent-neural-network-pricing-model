import torch
from torch import autograd

# Define two tensors
x = torch.tensor(1.0, requires_grad=True)
print(x)
y = torch.tensor(2.0, requires_grad=True)
print(y)

# Define a simple operation
a = x + y

# Define another operation
b = a * 3

# Now create a computation graph for the gradient
graph = autograd.grad(outputs=b, inputs=(x, y), grad_outputs=torch.ones_like(b), create_graph=True)

# The computation graph is created on the fly
# Now print the gradients
print(f'Gradient wrt x: {graph[0]}')
print(f'Gradient wrt y: {graph[1]}')