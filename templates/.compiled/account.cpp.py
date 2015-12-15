#This code is auto generated code, don't Edit it 
outpvar.cur.addfcdata("main2");
outpvar.cur.fcalldata["main2"].open(htmlnode("div", extentattrs(cod([]))));
outpvar.cur.fcalldata["main2"].cur.addfcdata("header4");
outpvar.cur.fcalldata["main2"].addchilds(newtag_header4(cod([]), ginp, outpvar.cur.fcalldata["main2"].cur.fcalldata["header4"].root.content).root.content);
if (int((ginp["islogin"] == "a"))): 
  outpvar.cur.fcalldata["main2"].open(htmlnode("div", extentattrs(cod([("class", "continer")]))));
  outpvar.cur.fcalldata["main2"].open(htmlnode("div", extentattrs(cod([("class", "row")]))));
  outpvar.cur.fcalldata["main2"].open(htmlnode("div", extentattrs(cod([("class", "col l8 offset-l2 m10 offset-m1 s12")]))));
  outpvar.cur.fcalldata["main2"].cur.addfcdata("account_admin");
  outpvar.cur.fcalldata["main2"].addchilds(newtag_account_admin(cod([("users", ginp["users"])]), ginp, outpvar.cur.fcalldata["main2"].cur.fcalldata["account_admin"].root.content).root.content);
  outpvar.cur.fcalldata["main2"].close();
  outpvar.cur.fcalldata["main2"].close();
  outpvar.cur.fcalldata["main2"].close();
outpvar.cur.fcalldata["main2"].close();
outpvar.addchilds(newtag_main2(cod([("js", ["js/menu.js"]), ("htmlstyle", cod([("overflow-y", "scroll")]))]), ginp, outpvar.cur.fcalldata["main2"].root.content).root.content);