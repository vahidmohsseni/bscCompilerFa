grammar Project;

// Compile with this Command : antlr4 -Dlanguage=Python2 Project.g4

// LEXER - Tokens

AND             : 'Va';
OR              : 'Ya';
Bool            : 'Bool';
Break           : 'Bepar_biroon';
String          : 'Reshte';
Float           : 'Adad_Ashar_bozorg';
Double          : 'Adad_Ashar_riz';
Int             : 'Adad_Sahih';
Long            : 'Adad_Sahih_bozorg';
Short           : 'Adad_Sahih_riz';
Char            : 'Harf';
Return          : 'Bargardoon';
While           : 'Ta_Vaghti_Ke';
Private         : 'Khoususi';
Public          : 'Omoumi';
If              : 'Agar';
Class_          : 'Kelas';
False_          : 'Ghalat';
True_           : 'Sahih';
Do              : 'Anjam_Bede';
Else            : 'Vagar_Na';
Alias           : 'Mostar';
Switch          : 'Entekhab';
Case            : 'Halat';
Const           : 'Sabet';
Continue        : 'Edame_Bede';
Enum            : 'Shomaresh';
For             : 'Baraye';
NullLiteral     : 'Null' ;
Void            : 'Void';
Default         : 'PishFarz';


// Tokens - Separators

Lparen          : '(';
Rparen          : ')';
Lbrace          : '{';
Rbrace          : '}';
Lbrack          : '[';
Rbrack          : ']';
Semi            : ';';
Comma           : ',';
Dot             : '.';
Colon           : ':';


// Tokens - Operators

Assign          : '=';
Gt              : '>';
Lt              : '<';
Equal           : '==';
Le              : '<=';
Ge              : '>=';
Not_Equal       : '!=';
Inc             : '++';
Dec             : '--';
Add             : '+';
Sub             : '-';
Mul             : '*';
Div             : '/';
Not             : '!';


// Tokens - Others

Letter         : [a-zA-Z_];
Digit          : [0-9];
ID             : Letter (Letter | Digit)*;
NonZeroDigit   : [1-9];
Zero           : '0';
IntegerConst   : (NonZeroDigit Digit*) | Zero;
DigitSeq       : Digit+;
FloatConst     : DigitSeq? '.' DigitSeq | DigitSeq '.';
CharConst      : '\'' (CChar+)? '\'';
CChar          : ~['\\\r\n] | EscSeq;
EscSeq         : '\\' ['"?abfnrtv\\];
Constant       : IntegerConst | FloatConst | CharConst;

StrLiteral     : '"' (SChar+)? '"';
SChar          : ~["\\\r\n] | EscSeq | '\\\n' | '\\\r\n';

Whitespace     : [ \t]+ -> skip;
Newline        : ('\r' '\n'? | '\n') -> skip;
BlockComment   :'/*' .*? '*/' -> skip;
LineComment    : '//' ~[\r\n]* -> skip;
Str	           :'"' ~('\r' | '\n' | '"')* '"';

// Rules

primaryExpr : ID | Constant | StrLiteral+ | '(' expr ')';

postfixExpr : primaryExpr | postfixExpr '[' expr ']' | postfixExpr '(' argumentExprList? ')' | postfixExpr '.' ID | '(' typeName ')' '{' initializerList '}' | '(' typeName ')' '{' initializerList ',' '}';

argumentExprList : assignmentExpr | argumentExprList ',' assignmentExpr;

unaryExpr : postfixExpr | unaryOperator castExpr;

unaryOperator : '+' | '-' | '!';

castExpr : unaryExpr | '(' typeName ')' castExpr;

multiplicativeExpr : castExpr | multiplicativeExpr '*' castExpr | multiplicativeExpr '/' castExpr | multiplicativeExpr '%' castExpr;

additiveExpr : multiplicativeExpr | additiveExpr '+' multiplicativeExpr | additiveExpr '-' multiplicativeExpr;

relationalExpr : additiveExpr | relationalExpr '<' additiveExpr | relationalExpr '>' additiveExpr | relationalExpr '<=' additiveExpr | relationalExpr '>=' additiveExpr;

equalityExpr : relationalExpr | equalityExpr '==' relationalExpr | equalityExpr '!=' relationalExpr;

logicalAndExpr : equalityExpr | logicalAndExpr 'Va' equalityExpr;

logicalOrExpr : logicalAndExpr | logicalOrExpr 'Ya' logicalAndExpr;

assignmentExpr : logicalOrExpr | unaryExpr '=' assignmentExpr;

expr : assignmentExpr | expr ',' assignmentExpr;

constantExpr : logicalOrExpr;

declaration : declarationSpecifiers initDeclaratorList ';'|	declarationSpecifiers ';';

declarationSpecifiers : declarationSpecifier+;

declarationSpecifiers2 : declarationSpecifier+;

declarationSpecifier : typeSpecifier | typeQualifier;

initDeclaratorList : initDeclarator | initDeclaratorList ',' initDeclarator;

initDeclarator : declarator | declarator '=' initializer;

typeSpecifier : ('Void' | 'Harf' | 'Adad_Sahih_riz' | 'Adad_Sahih' | 'Adad_Sahih_bozorg' | 'Adad_Ashar_bozorg' | 'Adad_Ashar_riz') | classSpecifier | enumSpecifier;

classSpecifier : Class_ ID? '{' classDeclarationList '}' | Class_ ID;

classDeclarationList : classDeclaration | classDeclarationList classDeclaration;

classDeclaration : specifierQualifierList classDeclaratorList? ';';

specifierQualifierList : typeSpecifier specifierQualifierList?| typeQualifier specifierQualifierList?;

classDeclaratorList : classDeclarator | classDeclaratorList ',' classDeclarator;

classDeclarator : declarator | declarator? ':' constantExpr;

enumSpecifier : 'Shomaresh' ID? '{' enumeratorList '}'| 'Shomaresh' ID? '{' enumeratorList ',' '}'| 'Shomaresh' ID;

enumeratorList : enumerator | enumeratorList ',' enumerator;

enumerator : enumerationConstant | enumerationConstant '=' constantExpr;

enumerationConstant : ID;

typeQualifier : 'Sabet';

declarator : directDeclarator;

directDeclarator
    : ID
    | '(' declarator ')'
    | directDeclarator '[' typeQualifier? assignmentExpr? ']'
    | directDeclarator '[' typeQualifier  assignmentExpr ']'
    | directDeclarator '[' typeQualifier? '*' ']'
    | directDeclarator '(' parameterTypeList ')'
    | directDeclarator '(' identifierList? ')';

nestedParenthesesBlock : ( ~('(' | ')') | '(' nestedParenthesesBlock ')')*;

parameterTypeList : parameterList;

parameterList : parameterDeclaration | parameterList ',' parameterDeclaration;

parameterDeclaration : declarationSpecifiers declarator| declarationSpecifiers2 abstractDeclarator?;

identifierList : ID | identifierList ',' ID;

typeName : specifierQualifierList abstractDeclarator?;

abstractDeclarator : directAbstractDeclarator;

directAbstractDeclarator
    : '(' abstractDeclarator ')'
    | '[' typeQualifier? assignmentExpr? ']'
    | '[' typeQualifier? assignmentExpr ']'
    | '[' typeQualifier assignmentExpr ']'
    | '(' parameterTypeList? ')'
    | directAbstractDeclarator '[' typeQualifier? assignmentExpr? ']'
    | directAbstractDeclarator '[' typeQualifier? assignmentExpr ']'
    | directAbstractDeclarator '[' typeQualifier assignmentExpr']'
    | directAbstractDeclarator '(' parameterTypeList? ')';

initializer : assignmentExpr | '{' initializerList '}' | '{' initializerList ',' '}';

initializerList : designation? initializer | initializerList ',' designation? initializer;

designation : designatorList '=';

designatorList : designator | designatorList designator;

designator : '[' constantExpr ']' | '.' ID;

statement : labeledStatement | compoundStatement | expressionStatement | selectionStatement | iterationStatement | jumpStatement;

labeledStatement : ID ':' statement | 'Halat' constantExpr ':' statement | 'PishFarz' ':' statement;

compoundStatement : '{' blockItemList? '}';

blockItemList : blockItem | blockItemList blockItem;

blockItem : declaration | statement;

expressionStatement : expr? ';';

selectionStatement : 'Agar' '(' expr ')' statement ('Vagar_Na' statement)? | 'Entekhab' '(' expr ')' statement;

iterationStatement : 'Ta_Vaghti_Ke' '(' expr ')' statement | 'Baraye' '(' expr? ';' expr? ';' expr? ')' statement | 'Baraye' '(' declaration expr? ';' expr? ')' statement;

jumpStatement : 'Edame_Bede' ';' | 'Bepar_biroon' ';' | 'Bargardoon' expr? ';';

program : translationUnit? EOF;

translationUnit : externalDeclaration | translationUnit externalDeclaration;

externalDeclaration : functionDefinition | declaration | ';';

functionDefinition : declarationSpecifiers? declarator declarationList? compoundStatement;

declarationList : declaration | declarationList declaration;
