# -*- coding: utf-8 -*-

import os, sys, re
from antlr4 import *
from antlr4.error import ErrorListener
import argparse

if __name__ is not None and "." in __name__:
	from .MiniJavaParser import MiniJavaParser
	from .MiniJavaLexer import MiniJavaLexer
	from .MiniJavaVisitor import MiniJavaVisitor
	from .MiniJavaListener import MiniJavaListener
	from .MiniJavaError_Presenter import MiniJava_ErrorListener
	from .MiniJavaSemanticAnalysis import *
	from .MiniJavaASTBuilder import *
	from .utilities import *
else:
	from MiniJavaParser import MiniJavaParser
	from MiniJavaLexer import MiniJavaLexer
	from MiniJavaVisitor import MiniJavaVisitor
	from MiniJavaListener import MiniJavaListener
	from MiniJavaError_Presenter import MiniJava_ErrorListener
	from MiniJavaSemanticAnalysis import *
	from MiniJavaASTBuilder import *
	from utilities import *


def semantic_check(parser_ret):
	visitor = My_Vistor()
	visitor.visit(parser_ret)


def draw(treelist, name):
	draw_pic(treelist, name)
	return treelist


def process(args):
	data = open(args.input_file).read()
	input = InputStream(data)
	lexer = MiniJavaLexer(input)
	stream = CommonTokenStream(lexer)
	parser = MiniJavaParser(stream)
	# setup the error listener
	parser.removeErrorListeners()
	parser.addErrorListener(MiniJava_ErrorListener())  # ()!!!
	tree = parser.goal()
	# semantic analysis

	try:
		semantic_check(tree)
	except:
		print('Error during semantic check')
	treelist = TreeList.toStringTreeList(tree, recog=parser)

	if not os.path.exists(args.output_dir):
		os.makedirs(args.output_dir)

	file_name = args.input_file.split('/')[-1].split('.')[-2]

	if args.cst:
		cst_image = os.path.join(args.output_dir, file_name + '_cst')
		cst_image = os.path.join(os.path.abspath(os.path.curdir), cst_image)
		print(cst_image)
		draw(treelist, cst_image)
		# print('* CST image saved at %s.' % cst_image)
	if args.ast:
		ast_image = os.path.join(args.output_dir, file_name + '_ast')
		visitor = AST_Builder()
		visitor.visit(tree)
		res = visitor.tree_list
		draw(res, ast_image)
		# print('* AST image saved at %s.' % ast_image)

	return tree


def main():

	aparser = argparse.ArgumentParser()

	aparser.add_argument('--input_file', '-i', type=str, default=None,
	                     help='minijava file for parsing')
	aparser.add_argument('--cst', action='store_true', default=False,
	                     help='show parse tree')
	aparser.add_argument('--ast', action='store_true', default=False,
	                     help='show abstract syntax tree')
	aparser.add_argument('--output_dir', '-o', type=str, default='output/',
	                     help='output directory of ast/cst trees')

	args = aparser.parse_args()

	print('* Working...')
	if os.path.exists(args.input_file) and os.path.isfile(args.input_file):
		process(args)
	else:
		print("[ERROR] file: %s not exist" % os.path.normpath(args.input_file))

	print('* Done.')


if __name__ == '__main__':
	''' 
	```bash
	python3 Project.py -i testfiles/Factorial.java --ast --cst
	```
	'''
	main()
