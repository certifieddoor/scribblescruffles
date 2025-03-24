NUM_DRAWINGS = 42
from idConstants import idConstants
import numpy as np

########ACTIVATION FUNCTION########

def relu(x):
  return np.maximum(0, x)

def leaky_relu(x):
  return np.maximum(0.01*x, x)

def softmax():
  pass


########DERIVATIVES########
def d_leaky_relu(a):
    #returns derivative of leaky relu
    #derivative is 1 is x > 1, 0.01 if x < 0
    return np.maximum(a>1,0.01)

def dZ(W,dZ,d_func,Z):
    #returns derivative of Z
    #dZ and W parameters are of the layer to the right
    #Z parameter is the Z you're finding the derivative of
    return np.dot(W.T, dZ) * d_func(Z)


def dW(dZ,A,m):
    #returns derivative of W
    #dZ is derivative of current layer's Z, A is previous layer activations
    #m is number of training examples
    return np.dot(dZ, A.T)/m

def db(dZ,m):
    #returns derivative of b
    #dZ is derivative of current layer Z, m is number of training examples
    return np.sum(dZ,axis = 1,keepdims = True)/m

def identifyDoodle():
  return []
