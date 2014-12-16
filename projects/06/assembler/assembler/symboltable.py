#!/usr/bin/env python

class SymbolTable(object):
    def __init__(self):
        """ creates a new empty symbol table"""
        pass

    def addEntry(self, symbol, address):
        """ Adds the pair (symbol, address) to the table """
        pass

    def contains(self, symbol):
        """ Does the symbol table contain the given symbol 
            returns Boolean
        """
        pass

    def get_address(self, symbol):
        """ Returns the address associated with the symbol 
            return int
        """
        pass
