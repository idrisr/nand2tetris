#!/usr/bin/env python

class Stack(object):
    """ TODO: make as singleton object """
    def __init__(self):
        self.stack = []
        self._update_pointer()

    def push(self, val):
        self.stack.extend([val])
        self._update_pointer()

    def pop(self):
        popped = int(self.stack.pop())
        self._update_pointer()
        return popped

    def _update_pointer(self):
        self.location = self.base_address + len(self.stack)

    def __repr__(self):
        attributes = ['stack', 'location']
        return '\n'.join(['%s:%s' % (attr, getattr(self, attr, ''),) for attr in attributes])

class SP(Stack):
    def __init__(self):
        self.base_address = 256
        super(SP, self).__init__()

class LCL(Stack):
    def __init__(self):
        self.base_address = 52
        super(SP, self).__init__()

class ARG(Stack):
    def __init__(self):
        self.base_address = 0 
        super(SP, self).__init__()

class THIS(Stack):
    def __init__(self):
        self.base_address = 0 
        super(SP, self).__init__()

class THAT(Stack):
    def __init__(self):
        self.base_address = 0 
        super(SP, self).__init__()
