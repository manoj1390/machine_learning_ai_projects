import numpy as np
from random import shuffle
from past.builtins import xrange

def softmax_loss_naive(W, X, y, reg):
  """
  Softmax loss function, naive implementation (with loops)

  Inputs have dimension D, there are C classes, and we operate on minibatches
  of N examples.

  Inputs:
  - W: A numpy array of shape (D, C) containing weights.
  - X: A numpy array of shape (N, D) containing a minibatch of data.
  - y: A numpy array of shape (N,) containing training labels; y[i] = c means
    that X[i] has label c, where 0 <= c < C.
  - reg: (float) regularization strength

  Returns a tuple of:
  - loss as single float
  - gradient with respect to weights W; an array of same shape as W
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using explicit loops.     #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  # compute the loss and the gradient
  num_classes = W.shape[1]
  num_train = X.shape[0]
  loss = 0.0
  

  for i in xrange(num_train):
    f = X[i].dot(W)
    max_val = np.max(f)
    f -= max_val
    exp_val = np.exp(f)
    sum_f =0.0
    for j in f:
      sum_f+=np.exp(j)
    loss -= np.log(exp_val[y[i]]/sum_f)
    dW[:,y[i]] -= X[i]
    for j in xrange(num_classes):
        dW[:,j] += X[i]*exp_val[j]/sum_f
    #for j in range(num_classes):
    #  prob = np.exp(f[j])/sum_f
    #  dW[:,j] += (prob-(j == y[i])) * X[i]

  # Right now the loss is a sum over all training examples, but we want it
  # to be an average instead so we divide by num_train.
  loss /= num_train
  dW   /= num_train

  # Add regularization to the loss.
  loss += reg * np.sum(W * W)
  
  # Add regularization factor to gradient
  dW += 2*reg*W
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
  """
  Softmax loss function, vectorized version.

  Inputs and outputs are the same as softmax_loss_naive.
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  num_classes = W.shape[1]
  num_train = X.shape[0]
  # compute the loss and the gradient
  f = X.dot(W)
  max_val = np.max(f)
  f -= max_val
  exp_val = np.exp(f)
  correct_Nr = exp_val[range(num_train),y]
  Dr = np.sum(exp_val,axis=1, keepdims=True)
  loss = -np.mean(np.log(correct_Nr/Dr))
  # Add regularization to the loss.
  Nr = exp_val
  loss += reg * np.sum(W * W)
  probs = Nr/Dr
  probs[range(num_train),y]-=1
  probs   /= num_train
  dW = np.dot(X.T, probs)
  dW += 2*reg*W
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW

