#-*- coding: utf-8 -*-

from antlr4 import *

if __name__ is not None and "." in __name__:
	from .MiniJavaParser import MiniJavaParser
	from .MiniJavaVisitor import MiniJavaVisitor
else:
	from MiniJavaParser import MiniJavaParser
	from MiniJavaVisitor import MiniJavaVisitor


def get_ctx_label(ctx):
	s = ctx.__class__.__name__
	s = s[:-7]
	return s


hash_table = {}  # record the ctx and its corresponding node (list)


# Use visitor to build AST
class AST_Builder(MiniJavaVisitor):
	def __init__(self):
		self.tree_list = []

	def visitGoal(self, ctx: MiniJavaParser.GoalContext):
		global hash_table
		node = ['Goal', []]
		self.tree_list = node
		hash_table[ctx] = node
		# it doesn't have parent
		return self.visitChildren(ctx)

	# Visit a parse tree produced by MiniJavaParser#mainclass.
	def visitMainclass(self, ctx: MiniJavaParser.MainclassContext):
		global hash_table
		node = ['Main Class, name: %s' % ctx.Identifier(0).getText(), []]
		hash_table[ctx] = node
		try:
			parent_list = hash_table[ctx.parentCtx]
			parent_list[1].append(node)
		except:
			pass
		return self.visitChildren(ctx)

	# Visit a parse tree produced by MiniJavaParser#dec_class.
	def visitDec_class(self, ctx: MiniJavaParser.Dec_classContext):
		global hash_table
		node = ['New Class, name: %s' % ctx.Identifier(0).getText(), []]
		hash_table[ctx] = node
		try:
			parent_list = hash_table[ctx.parentCtx]
			parent_list[1].append(node)
		except:
			pass
		return self.visitChildren(ctx)

	# Visit a parse tree produced by MiniJavaParser#dec_var.
	def visitDec_var(self, ctx: MiniJavaParser.Dec_varContext):
		# ?
		global hash_table
		node = ['New Identifier, name: %s' % ctx.Identifier().getText(), []]
		hash_table[ctx] = node
		try:
			parent_list = hash_table[ctx.parentCtx]
			parent_list[1].append(node)
		except:
			pass
		return self.visitChildren(ctx)

	# Visit a parse tree produced by MiniJavaParser#dec_method.
	def visitDec_method(self, ctx: MiniJavaParser.Dec_methodContext):
		global hash_table
		node = ['New Method, name: %s' % ctx.Identifier(0).getText(), []]
		hash_table[ctx] = node
		try:
			parent_list = hash_table[ctx.parentCtx]
			parent_list[1].append(node)
		except:
			pass
		return self.visitChildren(ctx)

	# Visit a parse tree produced by MiniJavaParser#mtype.
	def visitMtype(self, ctx: MiniJavaParser.MtypeContext):
		'''
		global hash_table
		node = [ 'Mtype', [] ]
		hash_table[ctx] = node
		try:
			parent_list = hash_table[ctx.parentCtx]
			parent_list[1].append(node)
		except:
			pass
		'''
		return self.visitChildren(ctx)

	# Visit a parse tree produced by MiniJavaParser#state_lrparents.
	def visitState_lrparents(self, ctx: MiniJavaParser.State_lrparentsContext):
		global hash_table
		node = ['{ }', []]
		hash_table[ctx] = node
		try:
			parent_list = hash_table[ctx.parentCtx]
			parent_list[1].append(node)
		except:
			pass
		return self.visitChildren(ctx)

	# Visit a parse tree produced by MiniJavaParser#state_if.
	def visitState_if(self, ctx: MiniJavaParser.State_ifContext):
		global hash_table
		node = ['If', []]
		hash_table[ctx] = node
		try:
			parent_list = hash_table[ctx.parentCtx]
			parent_list[1].append(node)
		except:
			pass
		return self.visitChildren(ctx)

	# Visit a parse tree produced by MiniJavaParser#state_while.
	def visitState_while(self, ctx: MiniJavaParser.State_whileContext):
		global hash_table
		node = ['While', []]
		hash_table[ctx] = node
		try:
			parent_list = hash_table[ctx.parentCtx]
			parent_list[1].append(node)
		except:
			pass
		return self.visitChildren(ctx)

	# Visit a parse tree produced by MiniJavaParser#state_print.
	def visitState_print(self, ctx: MiniJavaParser.State_printContext):
		global hash_table
		node = ['Print', []]
		hash_table[ctx] = node
		try:
			parent_list = hash_table[ctx.parentCtx]
			parent_list[1].append(node)
		except:
			pass
		return self.visitChildren(ctx)

	# Visit a parse tree produced by MiniJavaParser#state_assign.
	def visitState_assign(self, ctx: MiniJavaParser.State_assignContext):
		global hash_table
		node = ['Assign, identifier: %s' % ctx.Identifier().getText(), []]
		hash_table[ctx] = node
		try:
			parent_list = hash_table[ctx.parentCtx]
			parent_list[1].append(node)
		except:
			pass
		return self.visitChildren(ctx)

	# Visit a parse tree produced by MiniJavaParser#state_array_assign.
	def visitState_array_assign(self, ctx: MiniJavaParser.State_array_assignContext):
		global hash_table
		node = ['Assign, array: %s' % ctx.Identifier().getText(), []]
		hash_table[ctx] = node
		try:
			parent_list = hash_table[ctx.parentCtx]
			parent_list[1].append(node)
		except:
			pass
		return self.visitChildren(ctx)

	# Visit a parse tree produced by MiniJavaParser#err_miss_RHS.
	def visitErr_miss_RHS(self, ctx: MiniJavaParser.Err_miss_RHSContext):
		return self.visitChildren(ctx)

	# Visit a parse tree produced by MiniJavaParser#err_lparent_closing.
	def visitErr_lparent_closing(self, ctx: MiniJavaParser.Err_lparent_closingContext):
		return self.visitChildren(ctx)

	# Visit a parse tree produced by MiniJavaParser#expr_this.
	def visitExpr_this(self, ctx: MiniJavaParser.Expr_thisContext):
		global hash_table
		node = ['This', []]
		hash_table[ctx] = node
		try:
			parent_list = hash_table[ctx.parentCtx]
			parent_list[1].append(node)
		except:
			pass
		return self.visitChildren(ctx)

	# Visit a parse tree produced by MiniJavaParser#err_many_lparents.
	def visitErr_many_lparents(self, ctx: MiniJavaParser.Err_many_lparentsContext):
		return self.visitChildren(ctx)

	# Visit a parse tree produced by MiniJavaParser#expr_bool.
	def visitExpr_bool(self, ctx: MiniJavaParser.Expr_boolContext):
		global hash_table
		node = ['Boolean', []]
		hash_table[ctx] = node
		try:
			parent_list = hash_table[ctx.parentCtx]
			parent_list[1].append(node)
		except:
			pass
		return self.visitChildren(ctx)

	# Visit a parse tree produced by MiniJavaParser#expr_length.
	def visitExpr_length(self, ctx: MiniJavaParser.Expr_lengthContext):
		global hash_table
		node = ['Length', []]
		hash_table[ctx] = node
		try:
			parent_list = hash_table[ctx.parentCtx]
			parent_list[1].append(node)
		except:
			pass
		return self.visitChildren(ctx)

	# Visit a parse tree produced by MiniJavaParser#err_rparent_closing.
	def visitErr_rparent_closing(self, ctx: MiniJavaParser.Err_rparent_closingContext):
		return self.visitChildren(ctx)

	# Visit a parse tree produced by MiniJavaParser#expr_lrparents.
	def visitExpr_lrparents(self, ctx: MiniJavaParser.Expr_lrparentsContext):
		global hash_table
		node = ['( )', []]
		hash_table[ctx] = node
		try:
			parent_list = hash_table[ctx.parentCtx]
			parent_list[1].append(node)
		except:
			pass
		return self.visitChildren(ctx)

	# Visit a parse tree produced by MiniJavaParser#err_many_rparents.
	def visitErr_many_rparents(self, ctx: MiniJavaParser.Err_many_rparentsContext):
		return self.visitChildren(ctx)

	# Visit a parse tree produced by MiniJavaParser#expr_array.
	def visitExpr_array(self, ctx: MiniJavaParser.Expr_arrayContext):
		global hash_table
		node = ['Array', []]
		hash_table[ctx] = node
		try:
			parent_list = hash_table[ctx.parentCtx]
			parent_list[1].append(node)
		except:
			pass
		return self.visitChildren(ctx)

	# Visit a parse tree produced by MiniJavaParser#expr_int.
	def visitExpr_int(self, ctx: MiniJavaParser.Expr_intContext):
		global hash_table
		node = ['Integer, value: %s' % ctx.getText(), []]  # change
		hash_table[ctx] = node
		try:
			parent_list = hash_table[ctx.parentCtx]
			parent_list[1].append(node)
		except:
			pass
		return self.visitChildren(ctx)

	def visitExpr_op_multi(self, ctx: MiniJavaParser.Expr_op_multiContext):
		global hash_table
		node = ['Operation *', []]
		hash_table[ctx] = node
		try:
			parent_list = hash_table[ctx.parentCtx]
			parent_list[1].append(node)
		except:
			pass
		return self.visitChildren(ctx)

	def visitExpr_op_and(self, ctx: MiniJavaParser.Expr_op_andContext):
		global hash_table
		node = ['Operation &&', []]
		hash_table[ctx] = node
		try:
			parent_list = hash_table[ctx.parentCtx]
			parent_list[1].append(node)
		except:
			pass
		return self.visitChildren(ctx)

	def visitExpr_op_less(self, ctx: MiniJavaParser.Expr_op_lessContext):
		global hash_table
		node = ['Operation <', []]
		hash_table[ctx] = node
		try:
			parent_list = hash_table[ctx.parentCtx]
			parent_list[1].append(node)
		except:
			pass
		return self.visitChildren(ctx)

	def visitExpr_op_minus(self, ctx: MiniJavaParser.Expr_op_minusContext):
		global hash_table
		node = ['Operation -', []]
		hash_table[ctx] = node
		try:
			parent_list = hash_table[ctx.parentCtx]
			parent_list[1].append(node)
		except:
			pass
		return self.visitChildren(ctx)

	def visitExpr_op_plus(self, ctx: MiniJavaParser.Expr_op_plusContext):
		global hash_table
		node = ['Operation +', []]
		hash_table[ctx] = node
		try:
			parent_list = hash_table[ctx.parentCtx]
			parent_list[1].append(node)
		except:
			pass
		return self.visitChildren(ctx)

	# Visit a parse tree produced by MiniJavaParser#expr_int_array.
	def visitExpr_int_array(self, ctx: MiniJavaParser.Expr_int_arrayContext):
		global hash_table
		node = ['Int Array', []]
		hash_table[ctx] = node
		try:
			parent_list = hash_table[ctx.parentCtx]
			parent_list[1].append(node)
		except:
			pass
		return self.visitChildren(ctx)

	# Visit a parse tree produced by MiniJavaParser#expr_new_array.
	def visitExpr_new_array(self, ctx: MiniJavaParser.Expr_new_arrayContext):
		global hash_table
		s = ctx.getText()[3:]
		node = ['New Object, name: %s' % s, []]
		hash_table[ctx] = node
		try:
			parent_list = hash_table[ctx.parentCtx]
			parent_list[1].append(node)
		except:
			pass
		return self.visitChildren(ctx)

	# Visit a parse tree produced by MiniJavaParser#err_miss_LHS.
	def visitErr_miss_LHS(self, ctx: MiniJavaParser.Err_miss_LHSContext):
		return self.visitChildren(ctx)

	# Visit a parse tree produced by MiniJavaParser#expr_method_calling.
	def visitExpr_method_calling(self, ctx: MiniJavaParser.Expr_method_callingContext):
		global hash_table
		node = ['Calling Method: %s' % ctx.Identifier().getText(), []]
		hash_table[ctx] = node
		try:
			parent_list = hash_table[ctx.parentCtx]
			parent_list[1].append(node)
		except:
			pass
		return self.visitChildren(ctx)

	# Visit a parse tree produced by MiniJavaParser#expr_not.
	def visitExpr_not(self, ctx: MiniJavaParser.Expr_notContext):
		global hash_table
		node = ['Not', []]
		hash_table[ctx] = node
		try:
			parent_list = hash_table[ctx.parentCtx]
			parent_list[1].append(node)
		except:
			pass
		return self.visitChildren(ctx)

	# Visit a parse tree produced by MiniJavaParser#expr_id.
	def visitExpr_id(self, ctx: MiniJavaParser.Expr_idContext):
		global hash_table
		node = ['Identifier: %s' % ctx.Identifier().getText(), []]
		hash_table[ctx] = node
		try:
			parent_list = hash_table[ctx.parentCtx]
			parent_list[1].append(node)
		except:
			pass
		return self.visitChildren(ctx)
