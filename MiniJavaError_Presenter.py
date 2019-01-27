#-*- coding: utf-8 -*-

from antlr4.error.ErrorListener import *


class MiniJava_ErrorListener(ErrorListener):
	'''
	An inherited listener class to listen to the syntax errors.
	The error triger is defined in the .g4 file.
	'''

	def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
		'''
		An overwrite of the original method.
		See https://www.antlr.org/api/Java/org/antlr/v4/runtime/ANTLRErrorListener.html for more details
		recognizer: What parser got the error
		offendingSymbol: The offending token in the input token stream
		'''
		print('line ' + str(line) + ':' + str(column) + '\t' + msg, file=sys.stderr)
		self.print_detail(recognizer, offendingSymbol, line, column, msg, e)

	def print_detail(self, recognizer, offendingSymbol, line, column, msg, e):
		token = recognizer.getCurrentToken()
		in_stream = token.getInputStream()
		string = str(in_stream)
		string = string.split('\n')[line - 1]  # get the error line
		print(string)

		# Using '↑' to show the wrong token
		# e.g. int 0number
		#          ↑
		underline = ''
		for i in range(column):
			if string[i] == '\t':
				underline += '\t'
			else:
				underline += ' '
		underline += '↑'

		print(underline)
