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

        # dont really need to keep track of SP. Can calc it by 256 + len(self.stack)
        # of course this requires constantly measuing the lenght of the list
        # but does it really matter?
        self.SP = 256

    def process_command(self, command):
        """ call proper methods of this class based on the command type """
        self.command = command
        ctypes = {
            'C_ARITHMETIC' : self.add(),
            'C_PUSH'       : self.push(),
            'C_POP'        : self.push(),
            'C_LABEL'      : lambda x: x,
            'C_GOTO'       : lambda x: x,
            'C_IF'         : lambda x: x,
            'C_FUNCTION'   : lambda x: x,
            'C_RETURN'     : lambda x: x,
            'C_CALL'       : lambda x: x
        }

        ctypes[command.ctype]()


    def open_stream(self, file_name):
        # TODO: try blocks etc. doing this boilerplate an awful lot...
        self.f = open(file_name, 'w')
        pass

    # def pop(self):                       
        # """ returns popped element off stack """
        # # decrement stack pointer
        # self.SP = self.SP - 1     
        # return self.stack.pop()    

    # def push(self, i):          
        # """ push element onto stack """
        # # increment stack pointer     
        # self.SP = self.SP + 1        
        # return self.stack.extend(i)

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
        # pop top two items off of the stack
        # do the proper arithmetic operand

        # theres some more clever way of doing this using the +, -, * etc symbols
        operand = {'add': lambda x: x[0]+x[1],
                   'sub': lambda x: x[0]-x[1]
                   }

        assert self.command.ctype == 'C_ARITHMETIC'

        a = int(self.stack.pop())
        b = int(self.stack.pop())

        result = operand[self.command.arg1]((a, b))
        self.stack.extend([result])

        asm = []
        asm.extend(['@%s' % (self.SP + len(self.stack))])
        asm.extend(['M=M+D'])
        self.assm = '\n'.join(asm)

    def write_push(self):
        assert self.command.ctype == 'C_PUSH'
        self.stack.extend(self.command.arg2)

        asm = []
        asm.extend(['@%s' % ( self.command.arg2, )] )
        asm.extend(["D=A"])
        asm.extend(['@%s'  % (self.SP, )])
        asm.extend(['M=D'])
        self.SP = self.SP + 1

        self.assm = '\n'.join(asm)

    def close(self):
        """ Closes the output file """
        pass

    def __repr__(self):
        attributes = ['stack', 'SP', 'command']
        return ''.join(['%s:\t%r\n' % (_, getattr(self, _, ''),) for _ in attributes])
