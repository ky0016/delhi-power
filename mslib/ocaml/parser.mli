type exp = N of int | S of string | V of string | Add of (exp*exp) | Sub of (exp*exp) | Mul of (exp*exp) | List of (exp list) | Dictle of (exp*exp) | Dictl of (exp list) | And of (exp*exp) | Or of (exp*exp) | Ife of (exp*exp*exp) | Div of (exp*exp) | Mod of (exp*exp) | Get of (exp*exp) | Listl of (exp list) | Isequal of (exp*exp) | Le of (exp*exp) | Ge of (exp*exp) | Ls of (exp*exp) | Gt of (exp*exp ) | Notequal of (exp*exp) | Not of exp | Attr of (exp*string) | None ;;

type inst = Skip | Tag of (exp*exp*inst) | Defn of (exp*exp*inst) | Forl of (exp*exp*exp*inst) | Listi of ( inst list) | Ifel of ((exp*inst) list) | Assign of (exp*exp);;
type token =
  | NUMBER of (int)
  | STRING of (string)
  | NAME of (string)
  | ADD
  | SUB
  | MUL
  | MOD
  | DIV
  | COLON
  | LPARENM
  | RPARENM
  | LPAREN
  | RPAREN
  | LPARENB
  | RPARENB
  | TRUE
  | FALSE
  | AND
  | OR
  | QUESTION
  | SEMICOLON
  | COMMA
  | EQUAL
  | IF
  | ELIF
  | ELSE
  | FOR
  | ISEQUAL
  | LE
  | GE
  | LS
  | GT
  | NOTEQUAL
  | NOT
  | DOT
  | NONE
  | DEFINE
  | EOF

val main :
  (Lexing.lexbuf  -> token) -> Lexing.lexbuf -> inst list
