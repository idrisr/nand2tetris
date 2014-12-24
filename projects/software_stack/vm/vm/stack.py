#!/usr/bin/env python

class Stack(object):
    """ singleton object """
    def __init__(self):
        self.stack = []

    def push(self):
        pass

    def pop(self):
        pass

class SP(Stack):
    base_address = 256

class LCL(Stack):
    base_address = 256

class ARG(Stack):
    base_address = 256

class THIS(Stack):
    base_address = 256

class THAT(Stack):
    base_address = 256
