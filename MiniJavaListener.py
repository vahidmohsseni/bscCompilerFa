# Generated from MiniJava.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiniJavaParser import MiniJavaParser
else:
    from MiniJavaParser import MiniJavaParser

# This class defines a complete listener for a parse tree produced by MiniJavaParser.
class MiniJavaListener(ParseTreeListener):

    # Enter a parse tree produced by MiniJavaParser#goal.
    def enterGoal(self, ctx:MiniJavaParser.GoalContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#goal.
    def exitGoal(self, ctx:MiniJavaParser.GoalContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#mainclass.
    def enterMainclass(self, ctx:MiniJavaParser.MainclassContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#mainclass.
    def exitMainclass(self, ctx:MiniJavaParser.MainclassContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#dec_class.
    def enterDec_class(self, ctx:MiniJavaParser.Dec_classContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#dec_class.
    def exitDec_class(self, ctx:MiniJavaParser.Dec_classContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#dec_var.
    def enterDec_var(self, ctx:MiniJavaParser.Dec_varContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#dec_var.
    def exitDec_var(self, ctx:MiniJavaParser.Dec_varContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#dec_method.
    def enterDec_method(self, ctx:MiniJavaParser.Dec_methodContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#dec_method.
    def exitDec_method(self, ctx:MiniJavaParser.Dec_methodContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#mtype.
    def enterMtype(self, ctx:MiniJavaParser.MtypeContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#mtype.
    def exitMtype(self, ctx:MiniJavaParser.MtypeContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#state_lrparents.
    def enterState_lrparents(self, ctx:MiniJavaParser.State_lrparentsContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#state_lrparents.
    def exitState_lrparents(self, ctx:MiniJavaParser.State_lrparentsContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#state_if.
    def enterState_if(self, ctx:MiniJavaParser.State_ifContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#state_if.
    def exitState_if(self, ctx:MiniJavaParser.State_ifContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#state_while.
    def enterState_while(self, ctx:MiniJavaParser.State_whileContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#state_while.
    def exitState_while(self, ctx:MiniJavaParser.State_whileContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#state_print.
    def enterState_print(self, ctx:MiniJavaParser.State_printContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#state_print.
    def exitState_print(self, ctx:MiniJavaParser.State_printContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#state_assign.
    def enterState_assign(self, ctx:MiniJavaParser.State_assignContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#state_assign.
    def exitState_assign(self, ctx:MiniJavaParser.State_assignContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#state_array_assign.
    def enterState_array_assign(self, ctx:MiniJavaParser.State_array_assignContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#state_array_assign.
    def exitState_array_assign(self, ctx:MiniJavaParser.State_array_assignContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#err_miss_RHS.
    def enterErr_miss_RHS(self, ctx:MiniJavaParser.Err_miss_RHSContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#err_miss_RHS.
    def exitErr_miss_RHS(self, ctx:MiniJavaParser.Err_miss_RHSContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#err_lparent_closing.
    def enterErr_lparent_closing(self, ctx:MiniJavaParser.Err_lparent_closingContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#err_lparent_closing.
    def exitErr_lparent_closing(self, ctx:MiniJavaParser.Err_lparent_closingContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#expr_this.
    def enterExpr_this(self, ctx:MiniJavaParser.Expr_thisContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#expr_this.
    def exitExpr_this(self, ctx:MiniJavaParser.Expr_thisContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#err_many_lparents.
    def enterErr_many_lparents(self, ctx:MiniJavaParser.Err_many_lparentsContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#err_many_lparents.
    def exitErr_many_lparents(self, ctx:MiniJavaParser.Err_many_lparentsContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#expr_op_multi.
    def enterExpr_op_multi(self, ctx:MiniJavaParser.Expr_op_multiContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#expr_op_multi.
    def exitExpr_op_multi(self, ctx:MiniJavaParser.Expr_op_multiContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#expr_bool.
    def enterExpr_bool(self, ctx:MiniJavaParser.Expr_boolContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#expr_bool.
    def exitExpr_bool(self, ctx:MiniJavaParser.Expr_boolContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#expr_length.
    def enterExpr_length(self, ctx:MiniJavaParser.Expr_lengthContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#expr_length.
    def exitExpr_length(self, ctx:MiniJavaParser.Expr_lengthContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#err_rparent_closing.
    def enterErr_rparent_closing(self, ctx:MiniJavaParser.Err_rparent_closingContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#err_rparent_closing.
    def exitErr_rparent_closing(self, ctx:MiniJavaParser.Err_rparent_closingContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#expr_op_and.
    def enterExpr_op_and(self, ctx:MiniJavaParser.Expr_op_andContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#expr_op_and.
    def exitExpr_op_and(self, ctx:MiniJavaParser.Expr_op_andContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#expr_lrparents.
    def enterExpr_lrparents(self, ctx:MiniJavaParser.Expr_lrparentsContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#expr_lrparents.
    def exitExpr_lrparents(self, ctx:MiniJavaParser.Expr_lrparentsContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#err_many_rparents.
    def enterErr_many_rparents(self, ctx:MiniJavaParser.Err_many_rparentsContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#err_many_rparents.
    def exitErr_many_rparents(self, ctx:MiniJavaParser.Err_many_rparentsContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#expr_array.
    def enterExpr_array(self, ctx:MiniJavaParser.Expr_arrayContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#expr_array.
    def exitExpr_array(self, ctx:MiniJavaParser.Expr_arrayContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#expr_int.
    def enterExpr_int(self, ctx:MiniJavaParser.Expr_intContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#expr_int.
    def exitExpr_int(self, ctx:MiniJavaParser.Expr_intContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#expr_int_array.
    def enterExpr_int_array(self, ctx:MiniJavaParser.Expr_int_arrayContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#expr_int_array.
    def exitExpr_int_array(self, ctx:MiniJavaParser.Expr_int_arrayContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#expr_op_minus.
    def enterExpr_op_minus(self, ctx:MiniJavaParser.Expr_op_minusContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#expr_op_minus.
    def exitExpr_op_minus(self, ctx:MiniJavaParser.Expr_op_minusContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#expr_op_plus.
    def enterExpr_op_plus(self, ctx:MiniJavaParser.Expr_op_plusContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#expr_op_plus.
    def exitExpr_op_plus(self, ctx:MiniJavaParser.Expr_op_plusContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#expr_new_array.
    def enterExpr_new_array(self, ctx:MiniJavaParser.Expr_new_arrayContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#expr_new_array.
    def exitExpr_new_array(self, ctx:MiniJavaParser.Expr_new_arrayContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#expr_op_less.
    def enterExpr_op_less(self, ctx:MiniJavaParser.Expr_op_lessContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#expr_op_less.
    def exitExpr_op_less(self, ctx:MiniJavaParser.Expr_op_lessContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#err_miss_LHS.
    def enterErr_miss_LHS(self, ctx:MiniJavaParser.Err_miss_LHSContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#err_miss_LHS.
    def exitErr_miss_LHS(self, ctx:MiniJavaParser.Err_miss_LHSContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#expr_method_calling.
    def enterExpr_method_calling(self, ctx:MiniJavaParser.Expr_method_callingContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#expr_method_calling.
    def exitExpr_method_calling(self, ctx:MiniJavaParser.Expr_method_callingContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#expr_not.
    def enterExpr_not(self, ctx:MiniJavaParser.Expr_notContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#expr_not.
    def exitExpr_not(self, ctx:MiniJavaParser.Expr_notContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#expr_id.
    def enterExpr_id(self, ctx:MiniJavaParser.Expr_idContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#expr_id.
    def exitExpr_id(self, ctx:MiniJavaParser.Expr_idContext):
        pass


