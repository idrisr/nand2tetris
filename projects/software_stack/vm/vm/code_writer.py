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
        self.SP_update()

    def SP_update(self):
        self.SP = 256 + len(self.stack)

    def process_command(self, command):
        """ call proper methods of this class based on the command type """
        self.command = command
        self.command.parse_command()
        ctypes = {
            'C_ARITHMETIC' : self.write_arithmetic,
            'C_PUSH'       : self.write_push,
            'C_POP'        : self.write_pop,
            'C_LABEL'      : lambda x: x,
            'C_GOTO'       : lambda x: x,
            'C_IF'         : lambda x: x,
            'C_FUNCTION'   : lambda x: x,
            'C_RETURN'     : lambda x: x,
            'C_CALL'       : lambda x: x
        }

        ctypes[self.command.ctype]()
        self.write_command()


    def write_command(self):
        print self.assm


    def open_stream(self, file_name):
        # TODO: try blocks etc. doing this boilerplate an awful lot...
        self.f = open(file_name, 'w')
        pass

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
        self.SP_update()

        result = operand[self.command.arg1]((a, b))

        asm = []
        asm.extend(['@%s' % (self.SP + len(self.stack))])
        asm.extend(['M=M+D'])
        asm.extend(['@SP', 'M=M-1'])
        self.stack.extend([result])
        self.assm = '\n'.join(asm)

    def write_pop(self):
        print 'write pop'

    def write_push(self):
        assert self.command.ctype == 'C_PUSH'
        self.stack.extend(self.command.arg2)

        asm = []
        asm.extend(['@%s' % ( self.command.arg2, )] )
        asm.extend(["D=A"])
        asm.extend(['@%s'  % (self.SP, )])
        asm.extend(['M=D'])
        self.SP_update()
        asm.extend(['@SP', 'M=M+1'])
        self.assm = '\n'.join(asm)

    def close(self):
        """ Closes the output file """
        pass

    def __repr__(self):
        attributes = ['stack', 'SP', 'command']
        return ''.join(['%s:\t%r\n' % (_, getattr(self, _, ''),) for _ in attributes])
