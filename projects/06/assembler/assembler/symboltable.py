#!/usr/bin/env python

from parser import CommandType

class SymbolTable(CommandType):
    def __init__(self, lines):
        """ creates a new empty symbol table

        input:
            lines: a whitespace and comments stripped version of the asm file
        """
        self.next_addr = 1024
        self.buff = lines
        self.table = {
             '@SP'    : 0,
            '@LCL'    : 1,
            '@ARG'    : 2,
            '@THIS'   : 3,
            '@THAT'   : 4,
            '@SCREEN' : 16384,
            '@KBD'    : 24576}
        R = {'@R'+str(i): i  for i in xrange(0, 16)}
        self.table.update(R)


    def find_symbols(self):
        for line in self.buff:
            self.current_command = line.strip()
            self.command_type()
            if self.current_command_type == 'L':
                if not self.contains(self.current_command):
                    self.addEntry(self.current_command, self.next_addr)
                    self.increment_address()

    def increment_address(self):
        self.next_addr = self.next_addr + 1

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
    from parser import Parser
    dir = environ['HOME']
    file = 'learning/nand2tetris/projects/06/rect/Rect.asm'
    parser = Parser(path.join(dir, file))
    symbol_table = SymbolTable(parser.buff)
    symbol_table.find_symbols()
