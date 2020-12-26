#!/usr/bin/env python
""" generated source for module Scanner """
#  (C) 2013 Jim Buffenbarger
#  All rights reserved.
from pl_syntaxexception import SyntaxException
from pl_token import Token
import sys


class Scanner(object):
    """ generated source for class Scanner """
    program = ""
    whitespace = {' ','\n','\t'}
    digits = set("0123456789")
    letters = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    # math = set("=+-/;,")
    legits = set("_").union(digits).union(letters)
    symbols = set("@[\]^_`!\"#$%&',)(*+-./:;<=>?")
    operators = {}
    keywords = {}
    token = ""
    lexeme = ""


    def __init__(self, program):
        """ generated source for method __init__ """
        self.program = program
        self.pos = 0
        self.token = None

    def done(self):
        """ generated source for method done """
        return self.pos >= len(self.program)

    def many(self, s):
        """ generated source for method many """
        while not self.done() and self.program[self.pos] in s:
            self.pos += 1

# abc
    def past(self, c):
        """ generated source for method past """
        while not self.done() and c != self.program[self.pos]:
            self.pos += 1
        if not self.done() and c == self.program[self.pos]:
            self.pos += 1

    def nextNumber(self):
        """ generated source for method nextNumber """
        ### fill in here
        startingPos = self.pos
        self.many(self.digits)
        lexeme = self.program[startingPos:self.pos]
        self.token = Token("num", lexeme)

    def nextKwId(self):
        """ generated source for method nextKwId """
        ### fill in here
        startingPos = self.pos  
        self.many(self.letters)
        lexeme = self.program[startingPos:self.pos]
        self.token = Token("id", lexeme)


    def nextOp(self):
        """ generated source for method nextOp """
        ### fill in here
        startingPos = self.pos  
        self.many(self.symbols)
        lexeme = self.program[startingPos:self.pos]
        self.token = Token(self.program[startingPos:self.pos], lexeme)


# python3 pl_scanner.py "x=1; myvar=32"

    def next(self):
        """ generated source for method next """
        self.many(self.whitespace)
        if self.done():
            return False
        c = self.program[self.pos]

         ### fill in here (is c a digit? keyword? id?)
        if c in self.letters:
            self.nextKwId()
        elif c in self.digits:
            self.nextNumber()
        else:
           self.token = Token(c, c)
           self.pos+=1
        return True

    def match(self, t):
        """ generated source for method match """
        if not t == self.curr():
            raise SyntaxException(self.pos, t, self.curr())
        self.next()

    def curr(self):
        """ generated source for method curr """
        if self.token == None:
            raise SyntaxException(self.pos, Token("ANY"), Token("EMPTY"))
        return self.token

    def position(self):
        """ generated source for method pos """
        return self.pos


if __name__ == '__main__':
    scanner = Scanner(sys.argv[1])
    while scanner.next():
        print(scanner.curr())

# Note how whitespace is handled (i.e., there is a dictionary (i.e., a hash map) that has a list of the acceptable whitespace characters, which is initialized, and then is used in the next() method.
# You will likely need to add provisions for handling digits, letters, keywords, and operators in the next() method.
#  If you don't like the Scanner that is provided, then you are free to write your own, but it must be written in Python and it must have the methods mentioned above.

