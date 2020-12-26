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

    def parseRelop(self):
        """ generated source for method parseMulop """
        if self.curr() == Token("<"):
            self.match("<")
            return NodeRelop(self.pos(), "<")
        if self.curr() == Token("<="):
            self.match("<=")
            return NodeRelop(self.pos(), "<=")
        if self.curr() == Token(">"):
            self.match(">")
            return NodeRelop(self.pos(), ">")
        if self.curr() == Token(">="):
            self.match(">=")
            return NodeRelop(self.pos(), ">=")
        if self.curr() == Token("<>"):
            self.match("<>")
            return NodeRelop(self.pos(), "<>")
        if self.curr() == Token("=="):
            self.match("==")
            return NodeRelop(self.pos(), "==")
        return None

    def parseMulop(self):
        """ generated source for method parseMulop """
        if self.curr() == Token("*"):
            self.match("*")
            return NodeMulop(self.pos(), "*")
        if self.curr() == Token("/"):
            self.match("/")
            return NodeMulop(self.pos(), "/")
        return None

    def parseAddop(self):
        """ generated source for method parseAddop """
        if self.curr() == Token("+"):
            self.match("+")
            return NodeAddop(self.pos(), "+")
        if self.curr() == Token("-"):
            self.match("-")
            return NodeAddop(self.pos(), "-")
        return None
    
    def parseBoolExpr(self):
        expr1 = self.parseExpr()
        relop = self.parseRelop()
        expr2 = self.parseExpr()
        return NodeBoolExpr(expr1, relop, expr2)



    def parseFact(self):
        """ generated source for method parseFact """
        if self.curr() == Token("("):
            self.match("(")
            expr = self.parseExpr()
            self.match(")")
            return NodeFactExpr(expr)
        if self.curr() == Token("-"):
            self.match("-")
            fact = self.parseFact()
            return NodeFactFact(fact)
        if self.curr() == Token("id"):
            nid = self.curr()
            self.match("id")
            # if self.curr() == Token("("):
            #     self.match("(")
            #     expr = self.parseExpr()
            #     self.match(")")
            #     return NodeFuncCall(self.pos(), nid.lex(), expr)
            return NodeFactId(self.pos(), nid.lex())
        num = self.curr()
        self.match("num")
        return NodeFactNum(num.lex())

    def parseTerm(self):
        """ generated source for method parseTerm """
        fact = self.parseFact()
        mulop = self.parseMulop()
        if mulop == None:
            return NodeTerm(fact, None, None)
        term = self.parseTerm()
        term.append(NodeTerm(fact, mulop, None))
        return term

    def parseExpr(self):
        """ generated source for method parseExpr """
        term = self.parseTerm()
        addop = self.parseAddop()
        if addop == None:
            return NodeExpr(term, None, None)
        expr = self.parseExpr()
        expr.append(NodeExpr(term, addop, None))
        return expr

    def parseAssn(self):
        """ generated source for method parseAssn """
        nid = self.curr()
        self.match("id")
        self.match("=")
        expr = self.parseExpr()
        assn = NodeAssn(nid.lex(), expr)
        return assn

    def parseWr(self):
        """ generated source for method parseWr """
        self.match("wr")
        expr = self.parseExpr()
        wr = NodeWr(expr)
        return wr

    def parseRd(self):
        """ generated source for method parseWr """
        self.match("rd")
        nid = self.curr()
        self.match("id")
        value = NodeRd(nid.lex())
        return value

    def parseIf(self):
        self.match("if")
        boolExpr = self.parseBoolExpr()
        self.match("then")
        stmt = self.parseStmt()

        rest = None
        if self.curr() == Token("else"):
            self.match("else")
            rest = self.parseStmt()

        iffNode = NodeparseIf(boolExpr, stmt, rest)
        return iffNode

    def parseWhile(self):
        self.match("while")
        boolExpr = self.parseBoolExpr()
        self.match("do")
        stmt = self.parseStmt()
        return NodeParseWhile(boolExpr, stmt)
    
    def parseBegin(self):
        self.match("begin")
        blk = self.parseBlock()
        self.match("end")
        return NodeBegin(blk)


    def parseStmt(self):
        """ generated source for method parseStmt """
        if self.curr() == Token("begin"):
            beginCon = self.parseBegin()
            return NodeStmt(beginCon)
        if self.curr() == Token("while"):
            whileCon = self.parseWhile()
            return NodeStmt(whileCon)
        if self.curr() == Token("if"):
            iff = self.parseIf()
            return NodeStmt(iff)
        if self.curr() == Token("rd"):
            rd = self.parseRd()
            return NodeStmt(rd)
        if self.curr() == Token("wr"):
            wr = self.parseWr()
            return NodeStmt(wr)
        if self.curr() == Token("id"):
            assn = self.parseAssn()
            return NodeStmt(assn)
        return None

    def praseProg(self): 
        blk = self.parseBlock()
        prog = NodeProg(blk)
        return prog

    def parseBlock(self):
        """ generated source for method parseBlock """
        stmt = self.parseStmt()
        rest = None
        if self.curr() == Token(";"):
            self.match(";")
            rest = self.parseBlock()
        block = NodeBlock(stmt, rest)
        return block


    def parse(self, program):
        """ generated source for method parse """
        self.scanner = Scanner(program)
        self.scanner.next()
        return self.parseBlock()

