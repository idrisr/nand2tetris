#!/usr/bin/env python

class CodeWriter(object):
    def __init__(self, file_name):
        """ opens the output file/stream and gets ready to write into it """
        self.f = open(file_name, 'w')

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
        pass

    def write_push_pop(self):
        """
        Write the assembly code that is the translation of the given
        command where command is either C_PUSH or C_POP
        """
        pass

    def close(self):
        """ Closes the output file """
        pass
