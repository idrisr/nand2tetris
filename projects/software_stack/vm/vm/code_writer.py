#!/usr/bin/env python

from stack import SP, LCL, ARG, THIS, THAT

class CodeWriter(object):
    """
        I feel this object should simply take a command and return its assm equivalent
        Most likely the VMParser objet will have a CodeWriter
        currently CodeWriter holds the state of the stack and other memory segments
        I might break this out into another class
    """

    def __init__(self):
        """ opens the output file/stream and gets ready to write into it """
        self.sp = SP()
        self.lcl = LCL()
        self.arg = ARG()
        self.THIS = THIS()
        self.THAT = THAT()
        self.label = 0

    def process_command(self, command):
        """ call proper methods of this class based on the command type """
        self.command = command
        self.command.parse_command()
        ctypes = {
            'C_ARITHMETIC' : self.write_arithmetic,
            'C_PUSH'       : self.write_push,
            'C_POP'        : self.write_pop,
            # TODO: labelling is done ad-hoc already in write_arithmetic. Factor it out
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

        bool_map = {1:-1, 0:0}
        operand = {'add': (lambda x: x[0] + x[1], '+'),
                   'sub': (lambda x: x[0] - x[1], '-'),
                   'and': (lambda x: x[0] & x[1], '&'),
                   'or' : (lambda x: x[0] | x[1], '|'),
                   'eq' : ('JEQ', lambda x : bool_map[x[0]==x[1]]),
                   'lt' : ('JLT', lambda x : bool_map[x[0]< x[1]]),
                   'gt' : ('JGT', lambda x : bool_map[x[0]> x[1]]),
                   'neg': (lambda x: -x, '-'),
                   'not': (lambda x: ~x, '!')
                   }

        self.assm = []

        if self.command.arg1 in {'neg', 'not'}:
            a = int(self.sp.pop())
            operand_func, operand_sym = operand[self.command.arg1]

            self.assm.extend(['@SP', 'A=M-1', 'MD=%sM' % (operand_sym, )])
            result = operand_func(a)

        elif self.command.arg1 in {'add', 'sub', 'and', 'or'}:
            a = self.sp.pop()
            b = self.sp.pop()

            self.assm.extend(['@%s' % self.sp.location ])
            operand_func, operand_sym = operand[self.command.arg1]

            self.assm.extend(['M=M%sD' % (operand_sym, )])
            self.assm.extend(['@SP', 'M=M-1'])

            result = operand_func((b, a))

        elif self.command.arg1 in {'eq', 'lt', 'gt'}:
            self.assm.extend(['@%s' % (self.sp.location-1)])
            self.assm.extend(['D=M']) # TODO: put this into write_pop

            a = self.sp.pop()
            b = self.sp.pop()
            jmp_op, result_func = operand[self.command.arg1]
            result = result_func((a, b, ))

            label_true  = self.label
            label_false = self.label + 1
            label_cont  = self.label + 2

            # increment for next time we need labels
            self.label = self.label + 3

            # calc D jump condition
            self.assm.extend(['@%s' % self.sp.location])
            self.assm.extend(['D=M-D'])

            # jump
            self.assm.extend(['@L%s' % label_true])
            self.assm.extend(['D;%s' % jmp_op])
            self.assm.extend(['@L%s' % label_false])

            # false
            self.assm.extend(['(L%s)' % label_false])
            self.assm.extend(['@%s' % self.sp.location])
            self.assm.extend(['M=0'])
            self.assm.extend(['@L%s' % label_cont])
            self.assm.extend(['0;JMP'])

            # true
            self.assm.extend(['(L%s)' % label_true])
            self.assm.extend(['@%s' % self.sp.location])
            self.assm.extend(['M=-1'])
            self.assm.extend(['@L%s' % label_cont])
            self.assm.extend(['0;JMP'])

            # continue
            self.assm.extend(['(L%s)' % label_cont])
            self.assm.extend(['@SP'])
            self.assm.extend(['M=M-1'])

        self.sp.push(result)

    def incr_label(self):
        self.label = self.label + 1

    def write_pop(self):
        print 'write pop'

    def write_push(self):
        assert self.command.ctype == 'C_PUSH'
        self.sp.push(self.command.arg2)

        self.assm = []
        self.assm.extend(['@%s' % ( self.command.arg2, )] )
        self.assm.extend(["D=A"])
        self.assm.extend(['@%s'  % (self.sp.location - 1, )])
        self.assm.extend(['M=D'])

        self.assm.extend(['@SP', 'M=M+1'])

    def close(self):
        """ Closes the output file """
        pass

    def __repr__(self):
        attributes = ['stack', 'SP', 'command']
        return ''.join(['%s:\t%r\n' % (_, getattr(self, _, ''),) for _ in attributes])
