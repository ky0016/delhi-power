        (* File calc.ml *)
open Parser;;
open List;;
open String;;
let myconcat x = String.concat "" x;;

let id x = x;;

(* let tostr name explist f = myconcat ["("; String.concat ", " ((myconcat ["'"; name; "'"])::(map f explist)); ")"];;
 *)
let tostr name explist f = myconcat ["("; String.concat ", " ((myconcat ["'"; name; "'"])::(map f explist)); ",)"];;


        let _ =
          try
            let lexbuf = Lexing.from_channel (open_in Sys.argv.(1)) in
            while true do
              let result = Parser.main Lexer.token lexbuf in
              let rec f x = match x with 
              Dictle (y1,y2) -> tostr "Dictle" [y1; y2] f;
              | Add (y1,y2) -> tostr "Add" [y1; y2] f;
              | None  -> tostr "None" [] id;
              | Sub (y1,y2) -> tostr "Sub" [y1; y2] f;
              | Mul (y1,y2) -> tostr "Mul" [y1; y2] f;
              | Div (y1,y2) -> tostr "Div" [y1; y2] f;
              | Mod (y1,y2) -> tostr "Mod" [y1; y2] f;
              | And (y1,y2) -> tostr "And" [y1; y2] f;
              | Or (y1,y2) -> tostr "Or" [y1; y2] f;
              | Ife(y1, y2, y3) -> tostr "Ife" [y1;y2;y3] f;
              | Attr (y1,y2) -> tostr "Attr" [f y1; myconcat ["'";y2;"'"]] id;
              | Isequal(y1,y2) -> tostr "Isequal" [y1; y2] f;
              | Le(y1,y2) -> tostr "Le" [y1; y2] f;
              | Ge(y1,y2) -> tostr "Ge" [y1; y2] f;
              | Ls(y1,y2) -> tostr "Ls" [y1; y2] f;
              | Gt(y1,y2) -> tostr "Gt" [y1; y2] f;
              | Notequal(y1,y2) -> tostr "Notequal" [y1; y2] f;
              |  Not(y1) -> tostr "Not" [y1] f;
              | Get (y1,y2) -> tostr "Get" [y1; y2] f;
              | Dictl (y1) -> tostr "Dictl" y1 f;
              | Listl (y1) -> tostr "Listl" y1 f;
              | N (y1) -> tostr "N" [y1] string_of_int;
              | V (y1) -> tostr "V" [myconcat(["'";y1;"'"])] id;
              | S (y1) -> tostr "S" [y1] id;
              | _ -> "";

            in let rec pstatement x = match x with
              Tag (e1, e2, e3) -> tostr "Tag" [f e1; f e2; pstatement e3] id;
              | Defn (e1, e2, e3) -> tostr "Defn" [f e1; f e2; pstatement e3] id;
              | Forl (e1, e2, e3, e4) -> tostr "Forl" [f e1; f e2; f e3; pstatement e4 ] id;
              | Assign (e1, e2) -> tostr "Assign" [e1;e2] f;
              | Listi e1 -> tostr "Listi" e1 pstatement;
              | Ifel e1 -> tostr "Ifel" (map (function (x1, x2) -> tostr "Ifepair" [f x1; pstatement x2] id) e1) id;
              | _ -> "";


(* type inst = Skip | Tag of (exp*exp*inst) | Defn of (string*exp*(inst list)) | Forl of (string*string*exp*inst) | Listi of ( inst list) | Ifel of ((exp*inst) list) | Assign of (exp*exp);;
 *)

	          in
                print_string (String.concat ",\n" (map pstatement result)); print_newline(); flush stdout
            done
          with Lexer.Eof ->
            exit 0