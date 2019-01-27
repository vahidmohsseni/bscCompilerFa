grammar MiniJava;

goal    : mainClass ( classDeclaration )* EOF
        ;

mainClass   : 'class' Identifier '{' 'public' 'static' 'void' 'main' '(' 'String' '[' ']' Identifier ')' '{' statement '}' '}'
            #mainclass
            ;

classDeclaration    : 'class' Identifier ('extends' Identifier)? '{' (varDeclaration)* (methodDeclaration)* '}'
                    #dec_class
                    ;

varDeclaration  : mtype Identifier ';'
                #dec_var
                ;

methodDeclaration	:	'public' mtype Identifier '(' ( mtype Identifier ( ',' mtype Identifier )* )? ')' '{' ( varDeclaration )* ( statement )* 'return' expression ';' '}'
					#dec_method
					;

//methodDeclaration   : 'public' mtype Identifier '(' parameters ')' '{' (varDeclaration)* (statement)* 'return' expression ';' '}'
//                    #dec_method
//                    ;

//parameters  : (parameterDeclaration (',' parameterDeclaration)*)?
//            ;

//parameterDeclaration    : mtype Identifier
//                        ;

mtype   : 'int' '[' ']'
        | 'boolean'
        | 'int'
        | Identifier
        ;

statement   : '{' (statement)* '}'
                #state_lrparents
            | 'if' '(' expression ')' statement 'else' statement
                #state_if
            | 'while' '(' expression ')' statement
                #state_while
            | 'System.out.println' '(' expression ')' ';'
                #state_print
            | Identifier '=' expression ';'
                #state_assign
            | Identifier '[' expression ']' '=' expression ';'
                #state_array_assign
            ;

expression  : //expression ('&&' | '<' | '+' | '-' | '*') expression
                //#expr_op
            expression '&&' expression
                #expr_op_and
            | expression '<' expression
                #expr_op_less
            | expression '+' expression
                #expr_op_plus
            | expression '-' expression
                #expr_op_minus
            | expression '*' expression
                #expr_op_multi
            | expression '[' expression ']'
                #expr_array
            | expression '.' 'length'
                #expr_length
            | expression '.' Identifier '(' (expression (',' expression)* )? ')'
                #expr_method_calling
            | Integer
                #expr_int
            | Boolean
                #expr_bool
            | Identifier
                #expr_id
            | 'this'
                #expr_this
            | 'new' 'int' '[' expression ']'
                #expr_int_array
            | 'new' Identifier '(' ')'
                #expr_new_array
            | '!' expression
                #expr_not
            | '(' expression ')'
                #expr_lrparents
            | expression ('&&' | '<' | '+' | '-' | '*')
                {self.notifyErrorListeners('Error: missing the RHS of the operator')}
                #err_miss_RHS
            | ('&&' | '<' | '+' | '-' | '*') expression
                {self.notifyErrorListeners('Error: missing the LHS of the operator')}
                #err_miss_LHS
            | '(' expression ')' ')'
                {self.notifyErrorListeners("Error: too many ')'s")}
                #err_many_rparents
            | '(' '(' expression ')'
                {self.notifyErrorListeners("Error: too many '('s")}
                #err_many_lparents
            | '(' expression
                {self.notifyErrorListeners('Error: need right parent closing')}
                #err_rparent_closing
            | expression ')'
                {self.notifyErrorListeners('Error: need left parent closing')}
                #err_lparent_closing
            ;

Boolean : 'true'
        | 'false'
        ;

Identifier  : [a-zA-Z_][a-zA-Z0-9_]*
            | [0-9]+[a-zA-Z_][a-zA-Z0-9_]*
                {self.notifyErrorListeners('Error: identifier starting with digit')}
            ;

Integer : [0-9]+
        ;

WS  : [ \t\r\n]+ -> skip
    ;

LineComment : '//' .*? ('\r')? '\n' -> skip
            ;

Comment : '/*' .*? '*/' -> skip
        ;