grammar MiniJava;

goal : MainClass ( ClassDeclaration ) * ;
MainClass : 'class' Identifier '{' 'public' 'static' 'void' 'main' '(' 'String' '['']' Identifier ')' '{' Statement '}' '}' ;
ClassDeclaration : 'class' Identifier ('extends' Identifier )?'{'(VarDeclaration)*(MethodDeclaration)* '}' ;

VarDeclaration : Type Identifier';' ;

MethodDeclaration : 'public' Type Identifier '(' (Type Identifier (',' Type Identifier)* )? ')' '{' (VarDeclaration)* (Statement)* 'return' Experession ';' '}' ;

Type : 'int' '['']' | 'boolean' | 'int' | Identifier ;

Statement 
            : '{' (Statement)* '}' 
            | 'if' '(' Experession ')' Statement 'else' Statement
            | 'while' '(' Experession ')' Statement
            | 'System.out.println' '(' Experession ')' ';'
            | Identifier '=' Experession ';'
            | Identifier '[' Experession ']' '=' Experession ';' ;

Experession
            : LiteralInteger Temp
            | 'true' Temp
            | 'false' Temp
            | Identifier Temp
            | 'this' Temp
            | 'new' 'int' '[' Experession ']' Temp
            | 'new' Identifier '('')' Temp
            | '!' Experession Temp
            | '(' Experession ')' Temp;

Temp 
            : (Experession ('&&' | '<' | '+' | '-' | '*' ) Experession
            | '[' Experession ']' Experession
            | '.' 'length' Experession
            | '.' Identifier '('(Experession(','Experession)*)?')' Experession)? ;


Digit : [0-9];

LiteralInteger : Digit+ ;

Letter : [a-zA-Z];


Identifier : Letter (Letter | Digit)*;
