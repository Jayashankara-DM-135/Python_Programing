"""
when __all__ is used. It is a list of strings defining what symbols in a
module will be exported when from <module> import * is used on the module.

For example: if this module is imported by some module called demo.py using below syntax.
syntax:
from Module_importing__all__ import *

In this case demo.py as only access to symbols declared under __all__.  but not for other symbols like
TEXT in below example code.

But demo.py module still can import TEXT symbol using below syntax
Syntax:
from Module_importing__all__ import TEXT

Note:
1> If __all__ is not present, then defalut behaviour of import * is to import all the sysmbols that
   do not begin with underscore.
2> __all__ affects the from <module> import * behavior only. Members that are not mentioned in __all__ are
    still accessible from outside the module and can be imported with from <module> import <member>.
"""

__all__ = (
    'DIGITS',
    'LETTERS',
    'CHARS',
    'sigmoid',
    'softmax',
)

import numpy


DIGITS = "0123456789"
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
CHARS = LETTERS + DIGITS
TEXT = "HELLO TEXT"
def softmax(a):
    exps = numpy.exp(a.astype(numpy.float64))
    return exps / numpy.sum(exps, axis=-1)[:, numpy.newaxis]

def sigmoid(a):
  return 1. / (1. + numpy.exp(-a))
