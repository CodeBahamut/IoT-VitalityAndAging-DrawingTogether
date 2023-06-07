# PyTorch

## Introduction to Tensors
In machine learning, when representing the data, we need to do that numerically. A tensor is simply a container that can hold data in multiple dimensions. In mathematical terms, however, a tensor is a fundamental unit of data that can be used as the foundation for advanced mathematical operations. It can be a number, vector, matrix, or multi-dimensional array like Numpy arrays. Tensors can also be handled by the CPU or GPU to make operations faster. There are various types of tensors like Float Tensor, Double Tensor, Half Tensor, Int Tensor, and Long Tensor, but PyTorch uses the 32-bit Float Tensor as the default type.

## How to apply PyTorch

At its core, PyTorch provides two main features:

1. An n-dimensional Tensor, similar to numpy but can run on GPUs
2. Automatic differentiation for building and training neural networks

We will initially create the network in numpy before moving on to PyTorch.

Numpy includes an n-dimensional array object as well as several functions for manipulating these arrays. Numpy is a general-purpose scientific computing framework; it is unaware of computation graphs, deep learning, or gradients. However, by manually constructing the forward and backward traverses over the network using numpy operations, we can easily fit a third order polynomial to a sine function:


Numpy is a fantastic framework, however it cannot use GPUs to speed up numerical operations. GPUs frequently give speedups of 50x or larger for contemporary deep neural networks, hence numpy will not suffice for modern deep learning.

```python
# -*- coding: utf-8 -*-
import numpy as np
import math

# Create random input and output data
x = np.linspace(-math.pi, math.pi, 2000)
y = np.sin(x)

# Randomly initialize weights
a = np.random.randn()
b = np.random.randn()
c = np.random.randn()
d = np.random.randn()

learning_rate = 1e-6
for t in range(2000):
    # Forward pass: compute predicted y
    # y = a + b x + c x^2 + d x^3
    y_pred = a + b * x + c * x ** 2 + d * x ** 3

    # Compute and print loss
    loss = np.square(y_pred - y).sum()
    if t % 100 == 99:
        print(t, loss)

    # Backprop to compute gradients of a, b, c, d with respect to loss
    grad_y_pred = 2.0 * (y_pred - y)
    grad_a = grad_y_pred.sum()
    grad_b = (grad_y_pred * x).sum()
    grad_c = (grad_y_pred * x ** 2).sum()
    grad_d = (grad_y_pred * x ** 3).sum()

    # Update weights
    a -= learning_rate * grad_a
    b -= learning_rate * grad_b
    c -= learning_rate * grad_c
    d -= learning_rate * grad_d

print(f'Result: y = {a} + {b} x + {c} x^2 + {d} x^3')

```

The Tensor is the most fundamental PyTorch notion, and it is introduced here. A PyTorch Tensor is essentially equivalent to a numpy array: a Tensor is an n-dimensional array, and PyTorch includes several methods for working with Tensors. Tensors can maintain track of a computational graph and gradients behind the scenes, but they're also valuable as a general tool for scientific computing.

In addition, unlike numpy, PyTorch Tensors may use GPUs to speed numeric operations. To execute a PyTorch Tensor on GPU, simply supply the appropriate

```python
import torch
import math

dtype = torch.float
device = torch.device("cpu")
device = torch.device("cuda:0") # Uncomment this to run on GPU

Create random input and output data
x = torch.linspace(-math.pi, math.pi, 2000, device=device, dtype=dtype)
y = torch.sin(x)

Randomly initialize weights
a = torch.randn((), device=device, dtype=dtype)
b = torch.randn((), device=device, dtype=dtype)
c = torch.randn((), device=device, dtype=dtype)
d = torch.randn((), device=device, dtype=dtype)

learning_rate = 1e-6
for t in range(2000):

Forward pass: compute predicted y
y_pred = a + b * x + c * x ** 2 + d * x ** 3

    # Compute and print loss
    loss = (y_pred - y).pow(2).sum().item()
    if t % 100 == 99:
        print(t, loss)

    # Backprop to compute gradients of a, b, c, d with respect to loss
    grad_y_pred = 2.0 * (y_pred - y)
    grad_a = grad_y_pred.sum()
    grad_b = (grad_y_pred * x).sum()
    grad_c = (grad_y_pred * x ** 2).sum()
    grad_d = (grad_y_pred * x ** 3).sum()

    # Update weights using gradient descent
    a -= learning_rate * grad_a
    b -= learning_rate * grad_b
    c -= learning_rate * grad_c
    d -= learning_rate * grad_d


print(f'Result: y = {a.item()} + {b.item()} x + {c.item()} x^2 + {d.item()} x^3')
```

### PyTorch: nn
Computational graphs and autograd are a highly effective paradigm for creating complicated operators and automatically calculating derivatives; yet, raw autograd might be too low-level for big neural networks.

When designing neural networks, we typically consider layering the computation, with certain levels having learnable parameters that will be tuned during learning.

Packages like Keras, TensorFlow-Slim, and TFLearn in TensorFlow give higher-level abstractions over raw computational graphs that may be used to create neural networks.

The nn package in PyTorch provides the same function. The Modules defined by the nn package are generally comparable to neural network layers. A Module accepts input Tensors and computes output Tensors, but it may also store internal state, such as Tensors with learnable parameters. Below is an example of how the Pytorch nn works:

```python
# -*- coding: utf-8 -*-
import torch
import math


# Create Tensors to hold input and outputs.
x = torch.linspace(-math.pi, math.pi, 2000)
y = torch.sin(x)

# For this example, the output y is a linear function of (x, x^2, x^3), so
# we can consider it as a linear layer neural network. Let's prepare the
# tensor (x, x^2, x^3).
p = torch.tensor([1, 2, 3])
xx = x.unsqueeze(-1).pow(p)

# In the above code, x.unsqueeze(-1) has shape (2000, 1), and p has shape
# (3,), for this case, broadcasting semantics will apply to obtain a tensor
# of shape (2000, 3) 

# Use the nn package to define our model as a sequence of layers. nn.Sequential
# is a Module which contains other Modules, and applies them in sequence to
# produce its output. The Linear Module computes output from input using a
# linear function, and holds internal Tensors for its weight and bias.
# The Flatten layer flatens the output of the linear layer to a 1D tensor,
# to match the shape of `y`.
model = torch.nn.Sequential(
    torch.nn.Linear(3, 1),
    torch.nn.Flatten(0, 1)
)

# The nn package also contains definitions of popular loss functions; in this
# case we will use Mean Squared Error (MSE) as our loss function.
loss_fn = torch.nn.MSELoss(reduction='sum')

learning_rate = 1e-6
for t in range(2000):

    # Forward pass: compute predicted y by passing x to the model. Module objects
    # override the __call__ operator so you can call them like functions. When
    # doing so you pass a Tensor of input data to the Module and it produces
    # a Tensor of output data.
    y_pred = model(xx)

    # Compute and print loss. We pass Tensors containing the predicted and true
    # values of y, and the loss function returns a Tensor containing the
    # loss.
    loss = loss_fn(y_pred, y)
    if t % 100 == 99:
        print(t, loss.item())

    # Zero the gradients before running the backward pass.
    model.zero_grad()

    # Backward pass: compute gradient of the loss with respect to all the learnable
    # parameters of the model. Internally, the parameters of each Module are stored
    # in Tensors with requires_grad=True, so this call will compute gradients for
    # all learnable parameters in the model.
    loss.backward()

    # Update the weights using gradient descent. Each parameter is a Tensor, so
    # we can access its gradients like we did before.
    with torch.no_grad():
        for param in model.parameters():
            param -= learning_rate * param.grad

# You can access the first layer of `model` like accessing the first item of a list
linear_layer = model[0]

# For linear layer, its parameters are stored as `weight` and `bias`.
print(f'Result: y = {linear_layer.bias.item()} + {linear_layer.weight[:, 0].item()} x + {linear_layer.weight[:, 1].item()} x^2 + {linear_layer.weight[:, 2].item()} x^3')
```

## Conclusion
**NOTE** This research is not fully complete (since the author has solved the power issue in another ticket!).
has been applied on a stand-alone machine (not on the Jetbot), actually the merits of Tensorflow overweigh the ones of Pytorch.
There is no need to choose the Pytorch technique over Tensorflow, since our problem with Tensorflow is only having the power issue, which undoubtedly Pytorch has (because it also uses all the GPU cores for recognizing the objects). This problem could be solved by finding a way to limit the amount of used cores by the machine.      

