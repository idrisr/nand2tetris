#!/usr/bin/env python

import sys
import re
from os import path, environ
from code import Code
from symboltable import SymbolTable

class Parser(object):
    def __init__(self, asmfile):
        """ Open the input file/stream and gets ready to parse it """
        self.command_i = 0
        try:
            f = open(asmfile, 'r')
            self.asmfile = asmfile
            self.buff = f.readlines()
            self.file_clean()

        except IOError, e:
            print e
            sys.exit(1)

    def file_clean(self):
        self.strip_comments()
        self.strip_blank_lines()

    def strip_comments(self):
        comment = '//'
        self.buff = [line.strip() for line in self.buff if not line.startswith(comment)]

    def strip_blank_lines(self):
        self.buff = [line.strip() for line in self.buff if not line.strip() == '']

    def has_more_commands(self):
        """ 
        Are there more commands in the input? 
        returns Boolean
        """
        return len(self.buff) > self.command_i 

    def advance(self):
        """ 
        Reads the next command from the input and makes it the current
        command.  Should be called only if hasMoreCommands is True.  Initially
        there is no current command
        """
        if self.has_more_commands():
            self.current_command = self.buff[self.command_i]
            self.command_i = self.command_i + 1
            self.command_type()
        else:
            self.current_command = None

    def command_type(self):
        """
        returns the type of the current command

        returns one of:
        A_COMMAND for @Xxx where Xxx is either a symbol or a decimal number
        C_COMMAND for dest=comp; jump
        L_COMMAND (actually, pseudo-command) for (Xxx) where Xxx is a symbol
        """
        commands = {'A': (lambda x: re.match(r'^@[0-9]*$', x)),
                    'C': ((lambda x: re.match(r'^.*=.*$', x)),
                          (lambda x: re.match(r'^.*;.*$', x))),
                    'L': (lambda x: re.match(r'^@[^0-9].*$', x))}

        if commands['A'](self.current_command):
            self.current_command_type = 'A'
        elif commands['C'][0](self.current_command) or commands['C'][1](self.current_command):
            self.current_command_type = 'C'
        elif commands['L'](self.current_command):
            self.current_command_type = 'L'
        else:
            print '%s\tinvalid syntax' % (self.current_command, )
            sys.exit(1)

    def symbol(self):
        """
        returns the symbol or decimal Xxx of the current command @Xxx of (Xxx).
        Should be called only when commandType() is A_COMMAND or L_COMMAND

        return string
        """
        self.current_symbol = self.current_command[1:]

    def dest(self):
        """
        returns the dest mnemonic in the current C_COMMAND (8 possibilities).

        Should be called only when CommandType() is C_COMMAND

        returns string
        """
        # semicolon: 000 dest
        if '=' in self.current_command:
            d = self.current_command.split('=')[0]
        else:
            d='null'

        code = Code()
        self.current_dest = code.dest(d)

    def comp(self):
        """
        Returns the comp menomonic in the current C_COMMAND (28 possibilities)
        Should be called only when commandType() is C_COMMAND

        return string
        """
        if '=' in self.current_command:
            c = self.current_command.split('=')[1]
        elif ';' in self.current_command:
            c = self.current_command.split(';')[0]

        code = Code()
        self.current_comp, self.current_a = code.comp(c)

    #def a(self):
        ##TODO: figure out how to know 'a' bit
        ## I believe it has to do whether the previous command is an l or a command
        #self.current_a = '0'

    def jump(self):
        """
        Returns the jump mnemonic in the current C_COMMAND (8 possibilities)
        Should be called only when commandType() is C_COMMAND

        returns string
        """
        # equal: 000 jump 
        if ';' in self.current_command:
            j = self.current_command.split(';')[1]
        elif '=' in self.current_command:
            j='null'
        else:
            j = None
        code = Code()
        self.current_jump = code.jump(j)

    def __repr__(self):
        return self.asmfile + '\n'.join(self.buff)

    def binarize_c_command(self):
        self.comp() 
        self.dest()
        self.jump()
        #self.a()
        self.bin_current = '111' + self.current_a + self.current_comp + self.current_dest + self.current_jump

    def binarize_a_command(self):
        address = int(self.current_command[1:])
        bin_address = bin(address)[2:]
        self.bin_current = '0'*(16 - len(bin_address))  + bin_address

def main(asmfile):
    parser = Parser(asmfile)
    while True:
        parser.advance()
        if parser.current_command_type == 'A':
            parser.binarize_a_command()
        elif parser.current_command_type == 'C':
            parser.binarize_c_command()
        print parser.bin_current
        if not parser.has_more_commands():
            break

if __name__ == '__main__':
    try:
        asmfile = sys.argv[1]
    except IndexError:
        dir = environ['HOME']
        file = 'learning/nand2tetris/projects/06/add/Add.asm'
        asmfile = path.join(dir, file)
    main(asmfile)
