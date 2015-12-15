
%token <int> NUMBER
%token <string> STRING
%token <string> NAME

%token ADD SUB MUL MOD DIV COLON LPARENM RPARENM LPAREN RPAREN LPARENB RPARENB TRUE FALSE AND OR QUESTION SEMICOLON COMMA EQUAL IF ELIF ELSE FOR ISEQUAL LE GE LS GT NOTEQUAL NOT DOT NONE DEFINE
%token EOF
%left ADD SUB        /* lowest precedence */
%left MUL DIV         /* medium precedence */
%nonassoc UMINUS        /* highest precedence */
%start main             /* the entry point */
%type <inst list> main
%%
main:
		statements                { $1 }
;
expr:
	NUMBER                { N $1 }
	| TRUE                { N 1 }
	| FALSE                { N 0 }
	| NONE                { None }
	| expr OR expr          { Or ($1, $3) }
	| expr AND expr          { And ($1, $3) }
	| expr QUESTION expr COLON expr  { Ife ($1, $3, $5) }
	| STRING 			{ S $1 }
	| LPAREN expr RPAREN      { $2 }
	| dict                      { $1 }
	| expr MUL expr           { Mul($1, $3) }
	| expr ADD expr           { Add($1, $3) }
	| expr SUB expr           { Sub($1, $3) }
	| expr DIV expr           { Div($1, $3) }
	| expr MOD expr           { Mod($1, $3) }
	| expr LPARENB expr RPARENB { Get($1, $3) }
	| list                      { Listl $1 }
	| NAME 				{ V $1}
	| expr ISEQUAL expr { Isequal ($1, $3) }
	| expr LE expr { Le ($1, $3) }
	| expr GE expr { Ge ($1, $3) }
	| expr LS expr { Ls ($1, $3) }
	| expr GT expr { Gt ($1, $3) }
	| expr NOTEQUAL expr { Notequal ($1, $3) }
	| expr DOT NAME { Attr ($1, $3) }
	| NOT expr { Not ($2) }
;

dicte:
	expr COLON expr      { Dictle ($1, $3) }
;

dictel:
	dicte { [$1] }
	| dictel COMMA dicte { $3::$1}
;

dict:
	LPARENM RPARENM { Dictl [] }
	| LPARENM dictel RPARENM { Dictl $2 }
;

listl:
	expr { [$1] }
	| expr COMMA listl { $1::$3 }
;

list:
	LPARENB RPARENB { [] }
	| LPARENB listl RPARENB { $2 }
;

shead:
	NAME LPAREN RPAREN { [V $1; Dictl([])] }
	| NAME LPAREN expr RPAREN { [V $1; $3] }
	| NAME LPAREN dictel RPAREN { [V $1; (Dictl $3)] }
;

statement:
	shead SEMICOLON { Tag((List.nth $1 0), (List.nth $1 1), (Listi []))}	
	| DEFINE shead statement { Defn( (List.nth $2 0), (List.nth $2 1), $3) }
	| shead statement { Tag( (List.nth $1 0), (List.nth $1 1), $2) }
	| LPARENM statements RPARENM { Listi $2 }	
	| LPARENM RPARENM { Listi [] }	
	| ifelif { Ifel (List.rev $1) }
	| ifelif ELSE statement { Ifel( List.rev((N 1, $3 )::$1)) }
	| expr EQUAL expr SEMICOLON { Assign ($1, $3 ) }
	| FOR LPAREN NAME COMMA NAME COMMA expr RPAREN statement { Forl(V $3, V $5, $7, $9) }
	| FOR LPAREN NAME COMMA expr RPAREN statement { Forl(V $3, V "", $5, $7	) }
	| expr SEMICOLON { Skip }
	| statement SEMICOLON { $1 }
;

statements:
	statement { [$1] }
	| statement statements  { $1::$2 }
;

ifelif:
	IF expr statement { [($2, $3)] } 
	| ifelif ELIF expr statement { ($3, $4)::$1 }





