import sys
import os
import subprocess
import jinja2
from UI.forms.InputForm import InputForm
from UI.forms.TokensForm import TokensForm
from antlr4 import *
from ProjectLexer import ProjectLexer
from ProjectParser import ProjectParser
from ProjectErrorListener import ProjectLexerErrorListener, ProjectParserErrorListener, CompilerException
from ProjectPrintListener import ProjectPrintListener
from antlr4.error.ErrorListener import ErrorListener
from flask import Flask, url_for, render_template, request, flash, redirect

project_directory = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, static_folder=project_directory + '/UI/static')

my_loader = jinja2.ChoiceLoader([
    app.jinja_loader,
    jinja2.FileSystemLoader(project_directory + '/UI/templates'),
])
app.jinja_loader = my_loader

app.secret_key = "Compiler Lab Project"


@app.route('/', methods=['GET', 'POST'])
def open_main_page():

    if request.method == 'GET':

        input_form = InputForm()
        return render_template('index.html', form=input_form, method='GET')

    if request.method == 'POST':

        input_form = InputForm()
        code = input_form.code_text.data
        file_name = input_form.upload_file.data

        ############## LEXER PART ##############

        lexer = ProjectLexer(InputStream(code))
        lexer.removeErrorListeners()
        lexer.addErrorListener(ProjectLexerErrorListener())
        stream = CommonTokenStream(lexer)
        tokens = []
        lexer_errors = []
        items = []
        while True:
            try:
                next_token = lexer.nextToken()
                if next_token.type == next_token.EOF:
                    break
                tokens.append((lexer.symbolicNames[next_token.type], next_token))
                an_item=dict(line=str(next_token.line),column=str(next_token.column),text=str(next_token.text))
            	items.append(an_item)
            except CompilerException as e:
                lexer_errors.append(e)
                lexer.recover(e)

        print 'tokens : ' , tokens
        print 'lexer errors : ' , lexer_errors

        ############## PARSER PART ##############

        parser = ProjectParser(stream)
        parser.removeErrorListeners()
        parser.addErrorListener(ProjectParserErrorListener());
        project_tree = parser.program()
        project_printer = ProjectPrintListener(file_name)
        project_walker = ParseTreeWalker()
        project_walker.walk(project_printer, project_tree)
        project_bytecode = project_printer.get_bytecode()
        parser_errors = []
        parser_errors = parser._listeners[-1].errors
        print 'parser errors : ' , parser_errors
        if not lexer_errors and not parser_errors:
        	if not os.path.exists('output'):
        		os.mkdir('output')
    		bytecode_file = os.path.join('output', file_name + '.bc')

    		with open(bytecode_file, 'w') as f:
        		f.write(project_bytecode)

    		p = subprocess.Popen(['java', '-jar', 'jasmin.jar', '-d', 'output', bytecode_file], 
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    		p = p.communicate()
    		if p[0]:
        		print p[0]
    		if p[1]:
        		print p[1]
        tokens_form = TokensForm()
        return render_template('index.html', items=items, method='POST')


if __name__ == '__main__':
    app.debug = True
    app.run()
