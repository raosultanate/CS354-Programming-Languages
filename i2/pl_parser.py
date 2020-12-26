#!/usr/bin/env python

from pl_syntaxexception import SyntaxException
from pl_node import *
from pl_scanner import Scanner
from pl_token import Token

class Parser(object):
    """ generated source for class Parser """
    def __init__(self):
        self.scanner = None

    def match(self, s):
        """ generated source for method match """
        self.scanner.match(Token(s))

    def curr(self):
        """ generated source for method curr """
        return self.scanner.curr()

    def pos(self):
        """ generated source for method pos """
        return self.scanner.position()

    def parseAssn(self):
        id = self.curr().lexeme
        self.match('id')

        self.match('=')

        # num = self.curr().lexeme
        num = self.curr().lexeme
        self.match('num')
        return NodeAssn(id, num)


    def parseStmt(self):
        assn = self.parseAssn()
        return NodeStmt(assn)

    # block    : stmt ';' block
    def parseBlock(self):
        stmt = self.parseStmt()
        curr = self.curr()
        block_two = None

        if curr.lexeme == ';':
            self.scanner.next()
            block_two = self.parseBlock()
        return NodeBlock(stmt, block_two)

    def parse(self, program):
        """ generated source for method parse """
        if program == '': return None
        self.scanner = Scanner(program)
        self.scanner.next()
        return self.parseBlock()

# python interpreter.py "x=3" 
# block    : stmt ';' block
#          | stmt
# stmt     : assn
# assn     : id '=' num