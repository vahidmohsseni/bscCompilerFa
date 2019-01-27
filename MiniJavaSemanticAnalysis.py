# Created by Wang Ao, 15300240004. All rights reserved.
__author__ = 'Wang_Ao'
from antlr4 import *
from MiniJavaVisitor import *
from MiniJavaListener import *

# We overwrite the class Visitor to check the semantic freely
# ctx: context

class identifier_region(object):
    '''
    Using a list (dic) to store the current identifiers and their values in a region
    '''
    def __init__(self):
        self.identifiers = {}
    
    def push(self, identifier, value):
        try:
            self.identifiers[identifier] = value
        except:
            print ('identifier push error')
    
    def pop(self, identifier):
        try:
            self.identifiers.pop(identifier)
        except:
            print ('identifier pop error')
    
    def check(self, identifier):
        try:
            res = self.identifiers[identifier]
        except:
            res = False
        return res

class identifier_region_stack(object):
    '''
    Using a stack to store the valid regions of a identifier
    '''
    def __init__(self):
        self._identifiers = {}   # current identifiers and their values
        self._stack = [] # the items of the stack are regions with their identifiers
        self._history_list = []  # the region history
    
    def print_stack(self):
        for region in self._stack:
            print ([ key for key in region.identifiers ])
            #print ([ (key, region.identifiers[key]) for key in region.identifiers ])
    
    def check(self, identifier):
        res = None
        for region in self._stack:
            try:
                res = region.identifiers[identifier]
            except:
                continue
        if res == None:
            return False
        else:
            return res
    
    def add_new(self):
        # add a new empty region, no new identifier
        r = identifier_region()
        self._stack.append(r)
        self._history_list.append(r)
        return r

    def get_top(self):
        return self._stack[-1]  # return the original one, not the copy
    
    def pop_last(self):
        last = self._stack.pop()
        self._history_list.append('POP')
        return last



# the implementation of the real visitor class
class My_Vistor(MiniJavaVisitor):
    '''
    visitChildren is the core
    what we do is to check the identifiers when traversing the tree
    '''
    def __init__(self):
        self.regions = identifier_region_stack()
    
    def print_error(self, s, token):
        line = token.line   # number of the wrong line
        column = token.column   # number of wrong column
        msg = s
        print ('line ' + str(line) + ':' + str(column) + '\t' + 'Semantic Fault: ' + msg)

    def err_id_undetected(self, s, ctx):
        # identifier not defined
        self.print_error(s, ctx)
    
    def err_id_multidef(self, s, ctx):
        # identifier multi defined
        self.print_error(s, ctx)
    
    def check(self, identifier):
        return self.regions.check(identifier)
    
    def visitGoal(self, ctx):
        # enter a new start, allocate a NEW region
        self.regions.add_new()  # allocate a NEW region, discard the return
        res = self.visitChildren(ctx)
        self.regions.pop_last() # retrieve the allocated region
        return res

    def visitMainclass(self, ctx):
        '''
        A new MAIN class. Check whether it has been defined and
        put it in the current region
        Start a new region
        '''
        current_region = self.regions.get_top()

        class_name = ctx.Identifier(0).getText()
        if not self.check(class_name):
            # this mainclass has never been defined in any region
            # correct, ut it in the current region
            current_region.push(class_name, 'main_class')
        else:
            self.err_id_multidef("Multiple Mainclass Declare: " + class_name , ctx.Identifier(0).getSymbol())
        
        # start a new region
        self.regions.add_new()  # allocate a NEW region, discard the return
        res = self.visitChildren(ctx)
        self.regions.pop_last() # retrieve the allocated region
        return res
    
    def visitDec_class(self, ctx):
        '''
        A new class. Check whether it has been defined and
        put it in the current region
        Start a new region
        '''
        current_region = self.regions.get_top()

        class_name = ctx.Identifier(0).getText()
        if not self.check(class_name):  # not declared
            current_region.push(class_name, 'declared class')
        else:
            self.err_id_multidef("Multiple Class Declare: " + class_name , ctx.Identifier(0).getSymbol())
        
        # start a new region
        self.regions.add_new()  # allocate a new region, discard the return
        res = self.visitChildren(ctx)
        self.regions.pop_last() # retrieve the allocated region
        return res
    
    def visitDec_var(self, ctx):
        '''
        check whether the new declared variable
        has been multiple declared
        No new region
        '''
        current_region = self.regions.get_top()
        var_name = ctx.Identifier().getText()
        var_type = ctx.mtype().getText()

        if not self.check(var_name):
            # put it in the current region
            current_region.push(var_name, var_type)
        else:
            self.err_id_multidef("Multiple Variance Declare: " + var_name, ctx.Identifier().getSymbol())
        return self.visitChildren(ctx)
    
    def visitDec_method(self, ctx):
        '''
        Check whether the method name has been defined
        Start a new region
        '''
        #print (dir(ctx))
        #print (ctx.children)
        #print (type(ctx.parentCtx))
        current_region = self.regions.get_top()
        method_name = ctx.Identifier(0).getText()
        method_type = ctx.mtype(0).getText()
        if not self.check(method_name):
            current_region.push(method_name, method_type)
        else:
            self.err_id_multidef("Multiple Method Declare: " + method_name, ctx.Identifier(0).getSymbol())
        
        new_region = self.regions.add_new() # new region for the method
        # can't get the accurate number of parameters, check the former 12 parameters
        try:
            for i in range(1, 12):
                # mtype(0) is the method name
                para = ctx.Identifier(i)
                para_name = ctx.Identifier(i).getText()
                para_type = ctx.mtype(i).getText()

                # check whether having two same parameters
                # it's ok if another region has parameter with the same name
                if not new_region.check(para_name):
                    new_region.push(para_name, para_type)
                else:
                    self.err_id_multidef("Multiple Parameter Declare: " + para_name, para.getSymbol())
        except:
            pass    # for the concern of parameter overflow
        
        res = self.visitChildren(ctx)
        self.regions.pop_last() # retrieve the allocated region
        return res

    def visitExpr_id(self, ctx):
        id_name = ctx.Identifier().getText()
        token = ctx.Identifier().getSymbol()
        if not self.check(id_name):
            # the identifier has not been defined
            self.err_id_undetected("Undefined Identifer: "+ id_name, ctx.Identifier().getSymbol())
        return self.visitChildren(ctx)  # ? return self.check(id_name)
        
    def visitState_lrparents(self, ctx):
        # start a new region
        self.regions.add_new()  # allocate a NEW region, discard the return
        res = self.visitChildren(ctx)
        self.regions.pop_last() # retrieve the allocated region
        return res
    
    def visitState_assign(self, ctx):
        # no new region
        current_region = self.regions.get_top()
        id_name = ctx.Identifier().getText()
        if not self.check(id_name):
            self.err_id_undetected("Undefined Identifer: " + id_name, ctx.Identifier().getSymbol())
        res = self.visitChildren(ctx)
        return res
    
    def visitState_array_assign(self, ctx):
        # no new region
        current_region = self.regions.get_top()
        id_name = ctx.Identifier().getText()
        if not self.check(id_name):
            self.err_id_undetected("Undefined Identifer: " + id_name, ctx.Identifier().getSymbol())
        res = self.visitChildren(ctx)
        return res
    
    def visitExpr_new_array(self, ctx):
        # no new region
        # can't habe been declared
        current_region = self.regions.get_top()
        array_name = ctx.Identifier().getText()
        if not self.check(array_name):
            current_region.push(array_name, 'used')
        else:
            self.err_id_multidef("Multiple Array Declare: " + array_name, ctx.Identifier().getSymbol())
        res = self.visitChildren(ctx)
        return res
    
    '''
    def visitExpr_method_calling(self, ctx):
        # no new region
        # must have been declared
        current_region = self.regions.get_top()
        method_name = ctx.Identifier().getText()

        if not self.check(method_name):
            self.err_id_undetected("Undefined Method: " + method_name, ctx.Identifier().getSymbol())
        res = self.visitChildren(ctx)
        return res
    '''