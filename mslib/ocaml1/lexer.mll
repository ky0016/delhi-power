{
open Parser        (* The type token is defined in parser.mli *)
exception Eof
}

let letter = ['a'-'z' 'A'-'Z']
let digit = ['0'-'9']
let name = (letter | "_" ) ((letter | digit | "_")*)
let number = ("-" | "") (digit+)
let space = " " | "\t" | "\n"
let linecomment = "//" ([^'\n']*) '\n'
let astring = "'" ((("/") _) | [^ '\'' ])* "'"
let dstring = '"' ((("/") _) | [^ '\"' ])* '"'



rule token = parse
	space | linecomment    { token lexbuf }
	|"/*" { comment lexbuf }
	| number as lxm { NUMBER(int_of_string lxm) }
	| (astring | dstring) as lxm { STRING(lxm) }

	| "not" { NOT }

	| "None" { NONE }

	| "define" { DEFINE }
	| "Define" { DEFINE }

	| "if" { IF }
	| "else" { ELSE }
	| "elif" { ELIF }

	| "for" { FOR }

	|"True" { TRUE }
	|"true" { TRUE }
	|"False" { FALSE }
	|"false" { FALSE }

	| name as lxm { NAME(lxm) }

	| "&&"            { AND }
	| "||"            { OR }
	| '?'            { QUESTION }
	| ';'			 {SEMICOLON}
	| ','			 {COMMA}
	| '+'            { ADD }
	| '-'            { SUB }
	| '*'            { MUL }
	| ':'            { COLON }
	| '{'            { LPARENM }
	| '}'            { RPARENM }
	| '['            { LPARENB }
	| ']'            { RPARENB }
	| '('            { LPAREN }
	| ')'            { RPAREN }
	| '='            { EQUAL }
	| '.'            { DOT }
	| "=="            { ISEQUAL }
	| "<="            { LE }
	| ">="            { GE }
	| "<"            { LS }
	| ">"            { GT }
	| "!="            { NOTEQUAL }
	| "!"            { NOT }

	| eof            { EOF }
	| eof            { raise Eof }

and comment = parse 
	 "*/" { token lexbuf }
	| _ { comment lexbuf }
