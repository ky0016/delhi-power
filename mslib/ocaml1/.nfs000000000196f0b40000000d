function e() {
	echo "-------------";
}

function addbefore () {
	cat $1 $2 > /tmp/null
	mv /tmp/null $2
}

function f() {
	ocamllex lexer.mll       # generates lexer.ml
	e
	ocamlyacc parser.mly     # generates parser.ml and parser.mli
	e
	ocamlc -c lexer.ml
}

function g() {
	addbefore add.ml parser.mli
	e
	ocamlc -c parser.mli
	e
	addbefore add.ml parser.ml
}

function h() {
	ocamlc -c parser.ml
	e
	ocamlc -c calc.ml
	e
	ocamlc -o calc lexer.cmo parser.cmo calc.cmo
}


#rm *.cmi *.cmo parser.ml lexer.ml 

e
f
e
g
e
h
