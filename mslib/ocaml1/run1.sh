ocamllex lexer1.mll       # generates lexer.ml
ocamlyacc parser1.mly     # generates parser.ml and parser.mli
ocamlc -c parser.mli
ocamlc -c lexer.ml
ocamlc -c parser.ml
ocamlc -c calc1.ml
ocamlc -o calc lexer.cmo parser.cmo calc.cmo