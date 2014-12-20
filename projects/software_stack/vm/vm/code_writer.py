#!/usr/bin/env python

class CodeWriter(object):
    """
        I feel this object should simply take a command and return its assm equivalent
        Most likely the VMParser objet will have a CodeWriter
        currently CodeWriter holds the state of the stack and other memory segments
        I might break this out into another class
    """

    def __init__(self):
        """ opens the output file/stream and gets ready to write into it """
        self.stack = []
        self.SP = 256

    def open_stream(self, file_name):
        # TODO: try blocks etc. doing this boilerplate an awful lot...
        self.f = open(file_name, 'w')
        pass

    def pop(self):
        """ returns popped element off stack """
        # decrement stack pointer
        self.SP = self.SP - 1
        return self.stack.pop()

    def push(self, i):
        """ push element off stack """
        # increment stack pointer
        self.SP = self.SP + 1
        return self.stack.extend(i)

    def set_file_name(self):
        """
        informs the code writer that the translation of a new VM file is
        started
        """
        pass

    def write_arithmetic(self):
        """
        Writes the assembly code that is the translation of the given
        arithmetic command
        """
        pass

    def write_push_pop(self):
        """
        Write the assembly code that is the translation of the given
        command where command is either C_PUSH or C_POP
        """
        pass

    def write_push(self, command):
        assert command.ctype == 'C_PUSH'
        asm = []
        asm.extend(['@%s' % ( command.arg2, )] )
        asm.extend(["D=A"])
        asm.extend(['@%s'  % (self.SP, )])
        asm.extend(['M=D'])
        self.SP = self.SP + 1
        print asm

        return '\n'.join(asm)

    def close(self):
        """ Closes the output file """
        pass
