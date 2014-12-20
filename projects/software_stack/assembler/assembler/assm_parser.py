#!/usr/bin/env python

import sys
from parser import Parser

import re
from os import path, environ
from code import Code
from symbol_table import SymbolTable
from command_type import AssmCommandType


class AssmParser(AssmCommandType, Parser):
    def __init__(self, file_name):
        """ Open the input file/stream and gets ready to parse it """
        super(AssmParser, self).__init__(file_name)
        self.RAM = 16

        self.symbol_table = SymbolTable(self.buff)
        self.symbol_table.find_symbols()

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

        Should be called only when AssmCommandType() is C_COMMAND

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
        self.bin_current = '111' + self.current_a + self.current_comp + self.current_dest + self.current_jump


    def binarize_a_symbol(self):
        if not self.symbol_table.contains(self.current_command):
            self.symbol_table.addEntry(self.current_command, self.RAM)
            self.RAM = self.RAM + 1

        address = self.symbol_table.get_address(self.current_command)
        bin_address = bin(address)[2:]
        self.bin_current = '0' * (16 - len(bin_address))  + bin_address

    def binarize_a_address(self):
        address = int(self.current_command[1:])
        bin_address = bin(address)[2:]
        self.bin_current = '0'*(16 - len(bin_address))  + bin_address

    def binarize_a_command(self):
        if re.match(r'^@[0-9].*$', self.current_command):
            self.binarize_a_address()
        else:
            self.binarize_a_symbol()

def main(asmfile):
    parser = AssmParser(asmfile)
    while True:
        parser.advance()

        if parser.current_command_type == 'A':
            parser.binarize_a_command()
        elif parser.current_command_type == 'C':
            parser.binarize_c_command()
        elif parser.current_command_type == 'L':
            continue

        print parser.bin_current
        if not parser.has_more_commands():
            break

if __name__ == '__main__':
    try:
        asmfile = sys.argv[1]
    except IndexError:
        dir = environ['HOME']
        file = 'learning/nand2tetris/projects/software_stack/assembler/add/Add.asm'
        asmfile = path.join(dir, file)
    main(asmfile)
