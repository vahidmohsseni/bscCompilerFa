from ProjectListener import ProjectListener
from ProjectErrorListener import DeclarationException
from ProjectLexer import ProjectLexer


class ProjectPrintListener(ProjectListener):
    def __init__(self, name):
        super(ProjectPrintListener, self).__init__()
        self.code = ""
        self.name = name
        self.block_number = 0
        self.variables = {}


    def get_bytecode(self):
        return self.code


    def newVariable(self, name):
        new_id = len(self.variables) + 1 
        self.variables[(name, self.block_number)] = new_id
        return new_id


    def getVariable(self, name, block):
        while True:
            if (name, block) in self.variables:
                break
            block = block - 1
            if block < 0:
                raise DeclarationException(name)
        return self.variables[(name, block)]


    def enterProgram(self, ctx):
        self.code += '.class public %s' % self.name + '\n'
        self.code += '.super java/lang/Object' + '\n'
        self.code += '.method public <init>()V' + '\n'
        self.code += 'aload_0' + '\n'
        self.code += 'invokenonvirtual java/lang/Object/<init>()V' + '\n'
        self.code += 'return' + '\n'
        self.code += '.end method' + '\n'
        self.code += '.method public static main([Ljava/lang/String;)V' + '\n'
        self.code += '.limit stack 10000' + '\n'


    def exitProgram(self, ctx):
        self.code += "return" + '\n'
        self.code += ".end method" + '\n'


    def enterCompoundStatement(self, ctx):
        self.block_number +=1

    def exitCompoundStatement(self, ctx):
        self.block_number -=1


    def getLastChild(self, ctx):
        if ctx.getChildCount() == 0 or ctx.getChildCount() > 1:
            return ctx
        return self.getLastChild(ctx.getChild(0))


    def enterDeclaration(self, ctx):
        vartype, ids, _ = list(ctx.getChildren())
        v = vartype.getText()

        for child in ids.getChildren():
            if child.getChildCount() == 1:
                var_id = self.newVar(child.getChild(0).getText())
                if v == 'Adad_Sahih':
                    self.code += "bipush 0" + '\n'
                    self.code += "istore %s" % var_id + '\n'
                elif v == 'Adad_Ashar_bozorg':
                    self.code += "bipush 0" + '\n'
                    self.code += "fstore %s" % var_id + '\n'
                elif v == 'Adad_Ashar_riz':
                    self.code += "bipush 0" + '\n'
                    self.code += "dstore %s" % var_id + '\n'
                elif v == 'Harf':
                    self.code += "bipush 0" + '\n'
                    self.code += "istore %s" % var_id + '\n'

            elif child.getChildCount() == 3:
                if child.getChild(0).getChild(0).getChildCount() == 1:
                    var_id = self.newVar(child.getChild(0).getText())
                    if v == 'Adad_Sahih':
                        c = self.getLastChild(child.getChild(2))
                        if c.getChildCount() > 1:
                            self.calculateExpression(c)
                        else:
                            self.code += "bipush %s" % child.getChild(2).getText() + '\n'
                        self.code += "istore %s" % var_id + '\n'
                    elif v == 'Adad_Ashar_bozorg':
                        self.code += "bipush %s" % child.getChild(2).getText() + '\n'
                        self.code += "fstore %s" % var_id + '\n'
                    elif v == 'Adad_Ashar_riz':
                        self.code += "bipush %s" % child.getChild(2).getText() + '\n'
                        self.code += "dstore %s" % var_id + '\n'
                    elif v == 'Harf':
                        self.code += "bipush %s" % ord(child.getChild(2).getText()[1]) + '\n'
                        self.code += "istore %s" % var_id + '\n'
                else:
                    size = child.getChild(0).getChild(0).getChild(2).getText()
                    var_id = self.newVar(child.getChild(0).getChild(0).getChild(0).getText())
                    self.code += "bipush %s" % size + '\n'
                    self.code += "newarray %s" % v + '\n'
                    self.code += "astore %s" % var_id + '\n'


    def calculateExpression(self, ctx):
        ctx = self.getLastChild(ctx)

        if ctx.getChildCount() == 0:
            if ctx.getSymbol().type == ProjectLexer.Identifier:
                var_id = self.getVar(ctx.getText(), self.block_number)
                self.code += "iload %s" % var_id + '\n'
            else:
                self.code += "bipush %s" % ctx.getText() + '\n'

        elif ctx.getChildCount() == 3:
            if ctx.getChild(0).getText() == '(':
                self.calculateExpression(ctx.getChild(1))
            else:
                i1, o, i2 = ctx.getChildren()
                o = o.getText()

                self.calculateExpression(i1)
                self.calculateExpression(i2)
                if o == '+':
                    self.code += "iadd" + '\n'
                elif o == '-':
                    self.code += "isub" + '\n'
                elif o == '*':
                    self.code += "imul" + '\n'
                elif o == '/':
                    self.code += "idiv" + '\n'


