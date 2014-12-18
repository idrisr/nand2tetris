#!/usr/bin/env python

import re

class Parser(object):
    """ Interface for Parser objects """
    def file_clean(self):
        self.strip_comments()
        self.strip_inline_comments()
        self.strip_blank_lines()

    def strip_inline_comments(self):
        self.buff = [line.split('//')[0] for line in self.buff]

    def strip_parens(self):
        self.buff = [line.strip() for line in self.buff if not re.match(r'\(.*\)', line)]

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
