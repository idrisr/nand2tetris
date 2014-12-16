#!/usr/bin/env python

import sys

class Code(object):
    def dest(self, nem):
        """
        Returns the binary code of the dest mnemonic
        returns 3 bits
        """
        try:
            dest_codes = {
                'null' : '000',
                'M'    : '001',
                'D'    : '010',
                'MD'   : '011',
                'A'    : '100',
                'AM'   : '101',
                'AD'   : '110',
                'AMD'  : '111'}
            return dest_codes[nem]
        except KeyError:
            print 'invalid destination'
            sys.exit(1)

    def comp(self, nem):
        """
        Returns the binary code of the comp mnemonic
        returns 7 bits
        """
        try:
            comp_codes = {
                '0':     ('101010', '0'),
                '1':     ('111111', '0'),
                '-1':    ('111010', '0'),
                'D':     ('001100', '0'),
                'A':     ('110000', '0'),
                '!D':    ('001101', '0'),
                '!A':    ('110001', '0'),
                '-D':    ('001111', '0'),
                '-A':    ('110011', '0'),
                'D+1':   ('011111', '0'),
                'A+1':   ('110111', '0'),
                'D-1':   ('001110', '0'),
                'A-1':   ('110010', '0'),
                'D+A':   ('000010', '0'),
                'D-A':   ('010011', '0'),
                'A-D':   ('000111', '0'),
                'D&A':   ('000000', '0'),
                'D|A':   ('010101', '0'),

                'M':     ('110000', '1'),
                '!M':    ('110001', '1'),
                '-M':    ('110011', '1'),
                'M+1':   ('110111', '1'),
                'M-1':   ('110010', '1'),
                'D+M':   ('000010', '1'),
                'D-M':   ('010011', '1'),
                'M-D':   ('000111', '1'),
                'D&M':   ('000000', '1'),
                'D|M':   ('010101', '1')
                }
            return comp_codes[nem]
        except KeyError:
            print 'invalid comp'
            sys.exit(1)

    def jump(self, nem):
        """
        Returns the binary code of the jump mnemonic
        returns 3 bits
        """
        try:
            jump_codes = {
                'null' : '000',
                'JGT'  : '001',
                'JEQ'  : '010',
                'JGE'  : '011',
                'JLT'  : '100',
                'JNE'  : '101',
                'JLE'  : '110',
                'JMP'  : '111'
                }
            return jump_codes[nem]

        except KeyError:
            print 'invalid jump'
            sys.exit(1)
