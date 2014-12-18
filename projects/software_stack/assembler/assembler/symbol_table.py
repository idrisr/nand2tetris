#!/usr/bin/env python

from command_type import CommandType
import re

class SymbolTable(CommandType):
    def __init__(self, lines):
        """ creates a new empty symbol table

        input:
            lines: a whitespace and comments stripped version of the asm file
        """
        self.next_addr = 16
        self.buff = lines
        table = {
             '@SP'    : 0,
            '@LCL'    : 1,
            '@ARG'    : 2,
            '@THIS'   : 3,
            '@THAT'   : 4,
            '@SCREEN' : 16384,
            '@KBD'    : 24576}
        R = {'@R'+str(i): i  for i in xrange(0, 16)}
        table.update(R)
        self.table = table

    def find_symbols(self):
        ROM = 0
        for line in self.buff:
            self.current_command = line.strip()
            self.command_type()
            if self.current_command_type == 'L' and re.match(r'^\(.*\)$', self.current_command):
                command = '@' + self.current_command[1:-1]
                if not self.contains(command):
                    self.addEntry(command, ROM)
            elif self.current_command_type in {'C', 'A'}:
                ROM = ROM + 1

    def addEntry(self, symbol, address):
        """ Adds the pair (symbol, address) to the table """
        self.table[symbol] = address

    def contains(self, symbol):
        """ Does the symbol table contain the given symbol 
            returns Boolean
        """
        return symbol in self.table

    def get_address(self, symbol):
        """ Returns the address associated with the symbol 
            return int
        """
        return self.table[symbol]

    def __repr__(self):
        return '\n'.join(['%s\t%s'  % (k, v,) for k, v in self.table.items()])

if __name__ == '__main__':
    from os import path, environ
    from parser import AssmParser
    dir = environ['HOME']
    file = 'learning/nand2tetris/projects/software_stack/assembler/rect/Rect.asm'
    parser = AssmParser(path.join(dir, file))
    print parser.symbol_table
