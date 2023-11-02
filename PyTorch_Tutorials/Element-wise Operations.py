import torch

# Create two tensors
tensor1 = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
tensor2 = torch.tensor([[5, 6], [7, 8]], dtype=torch.float32)

# Element-wise Addition
add_result = tensor1 + tensor2
print(f'Addition Result:\n{add_result}\n')

# Element-wise Subtraction
sub_result = tensor1 - tensor2
print(f'Subtraction Result:\n{sub_result}\n')

# Element-wise Multiplication
mul_result = tensor1 * tensor2
print(f'Multiplication Result:\n{mul_result}\n')

# Element-wise Division
div_result = tensor1 / tensor2
print(f'Division Result:\n{div_result}\n')

# Broadcasting: operating with tensors of different shapes
# Create a tensor of shape (2, 2)
tensor3 = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)

# Create a tensor of shape (2,)
tensor4 = torch.tensor([1, 2], dtype=torch.float32)

# Broadcast tensor4 to the shape of tensor3 and perform element-wise addition
broadcast_result = tensor3 + tensor4
print(f'Broadcasting Result:\n{broadcast_result}\n')
