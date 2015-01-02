#!/usr/bin/env python

from stack import SP, LCL, ARG, THIS, THAT
import pdb

class CodeWriter(object):
    """
        I feel this object should simply take a command and return its assm
        equivalent Most likely the VMParser objet will have a CodeWriter
        currently CodeWriter holds the state of the stack and other memory
        segments I might break this out into another class
    """

    def __init__(self):
        """ opens the output file/stream and gets ready to write into it """
        self.sp = SP()
        self.lcl = LCL()
        self.arg = ARG()
        self.THIS = THIS()
        self.THAT = THAT()
        self.label = 0
        self.seg_map = {
            'argument' : 'ARG',
            'local'    : 'LCL',
            'pointer'  : '',
            'static'   : '',
            'temp'     : 'TEMP',
            'that'     : 'THAT',
            'this'     : 'THIS'
        }

    def process_command(self, command):
        """ call proper methods of this class based on the command type """
        self.command = command
        self.command.parse_command()
        ctypes = {
            'C_ARITHMETIC' : self.write_arithmetic,
            'C_PUSH'       : self.write_push,
            'C_POP'        : self.write_pop,
            # TODO: labelling is done ad-hoc already in write_arithmetic.
            # Factor hit out
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
        print '// %s' % (self.command.command, )
        print '\n'.join(self.assm)

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

        assert self.command.ctype == 'C_ARITHMETIC'

        operand = {'add':  '+',
                   'sub':  '-',
                   'and':  '&',
                   'or' :  '|',
                   'eq' : 'JEQ',
                   'lt' : 'JLT',
                   'gt' : 'JGT',
                   'neg':  '-',
                   'not':  '!'
                   }

        self.assm = []

        if self.command.arg1 in {'neg', 'not'}:
            operand_func, operand_sym = operand[self.command.arg1]

            self.assm.extend(['@SP', 'A=M-1', 'MD=%sM' % (operand_sym, )])

        elif self.command.arg1 in {'add', 'sub', 'and', 'or'}:

            # TODO: get SP value from SP pointer
            self.assm.extend(['@SP'])
            self.assm.extend(['A=M-1'])
            self.assm.extend(['D=M'])
            self.assm.extend(['@SP'])
            self.assm.extend(['M=M-1'])
            self.assm.extend(['@SP'])
            self.assm.extend(['A=M-1'])
            self.assm.extend(['M=M%sD' % operand[self.command.arg1]])

        elif self.command.arg1 in {'eq', 'lt', 'gt'}:
            jmp_op = operand[self.command.arg1]

            label_true  = self.label
            label_false = self.label + 1
            label_cont  = self.label + 2

            # increment for next time we need labels
            self.label = self.label + 3

            # calc D jump condition
            self.assm.extend(['@SP'])  # load SP-1 into D
            self.assm.extend(['A=M-1'])
            self.assm.extend(['D=M']) 
            self.assm.extend(['@SP'])  # decrement SP
            self.assm.extend(['M=M-1']) 
            self.assm.extend(['@SP'])  # load SP -1 
            self.assm.extend(['A=M-1']) 
            self.assm.extend(['D=M-D']) # compare D and M
            self.assm.extend(['@SP'])   # decrement SP
            self.assm.extend(['M=M-1'])

            # jump
            self.assm.extend(['@L%s' % label_true])
            self.assm.extend(['D;%s' % jmp_op])
            self.assm.extend(['@L%s' % label_false])

            # false
            self.assm.extend(['(L%s)' % label_false])

            self.assm.extend(['@SP'])
            self.assm.extend(['A=M'])

            self.assm.extend(['M=0'])
            self.assm.extend(['@L%s' % label_cont])
            self.assm.extend(['0;JMP'])

            # true
            self.assm.extend(['(L%s)' % label_true])
            self.assm.extend(['@SP'])
            self.assm.extend(['A=M'])

            self.assm.extend(['M=-1'])
            self.assm.extend(['@L%s' % label_cont])
            self.assm.extend(['0;JMP'])

            # continue
            self.assm.extend(['(L%s)' % label_cont])
            self.assm.extend(['@SP'])
            self.assm.extend(['M=M+1'])


    def incr_label(self):
        self.label = self.label + 1

    def write_pop(self):
        """ to pop things off the global stack onto other segments """
        assert self.command.ctype == 'C_POP'

        segment = self.seg_map[self.command.arg1]
        address = self.command.arg2
        self.assm = [] # TODO: do this in process_command instead of repeating

        if segment != 'TEMP':
            # this is different for temp. There's no pointer to temp
            self.assm.extend(['@%s' % segment])
            self.assm.extend(['D=M'])
            self.assm.extend(['@%s' % address])
            self.assm.extend(['D=A+D'])
            self.assm.extend(['@R5'])
            self.assm.extend(['M=D'])
            self.assm.extend(['@SP'])
            self.assm.extend(['A=M-1'])
            self.assm.extend(['D=M'])
            self.assm.extend(['@R5'])
            self.assm.extend(['A=M'])
            self.assm.extend(['M=D'])
            self.assm.extend(['@SP'])
            self.assm.extend(['M=M-1'])

        elif segment == 'TEMP':
            address = int(address) + 5
            assert 5 <= address <= 11 # RAM[5-12] are temp addresses
            self.assm.extend(['@SP'])
            self.assm.extend(['A=M-1'])
            self.assm.extend(['D=M'])
            self.assm.extend(['@%s' % address])
            self.assm.extend(['M=D'])
            self.assm.extend(['@SP'])
            self.assm.extend(['M=M-1'])

    def write_push(self):
        assert self.command.ctype == 'C_PUSH'

        self.assm = []
        segment = self.seg_map[self.command.arg1]
        address = self.command.arg2

        if segment == 'TEMP':
            address = int(address) + 5
            assert 5 <= address <= 12 # RAM[5-12] are temp addresses
            self.assm.extend(['@%s' % (address, )])
            self.assm.extend(['D=M'])

        elif segment == 'constant':
            self.assm.extend(['@%s' % ( address, )] )
            self.assm.extend(["D=A"])

        else:
            self.assm.extend(['@%s' % ( segment, )])
            self.assm.extend(['D=M'])
            self.assm.extend(['@%s' % ( address, )])
            self.assm.extend(['A=A+D'])
            self.assm.extend(['D=M'])

        self.assm.extend(["@SP"])
        self.assm.extend(["A=M"])
        self.assm.extend(["M=D"])
        self.assm.extend(['@SP'])
        self.assm.extend(['M=M+1'])

    def close(self):
        """ Closes the output file """
        pass

    def __repr__(self):
        attributes = ['command']
        return ''.join(['%s:\t%r\n' % (_, getattr(self, _, ''),) for _ in
            attributes])
