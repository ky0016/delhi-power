#This code is auto generated code, don't Edit it 
outpvar.cur.addfcdata("main2");
outpvar.cur.fcalldata["main2"].open(htmlnode("div", extentattrs(cod([("class", "container")]))));
for i in forlist(ginp["allt"], False ) :
  outpvar.cur.fcalldata["main2"].open(htmlnode("div", extentattrs(cod([("class", "row")]))));
  outpvar.cur.fcalldata["main2"].open(htmlnode("div", extentattrs(cod([("class", "")]))));
  outpvar.cur.fcalldata["main2"].cur.addfcdata("table1");
  outpvar.cur.fcalldata["main2"].addchilds(newtag_table1(cod([("thead", i["data"]["thead"]), ("rows", i["data"]["rows"]), ("class", "bordered")]), ginp, outpvar.cur.fcalldata["main2"].cur.fcalldata["table1"].root.content).root.content);
  outpvar.cur.fcalldata["main2"].close();
  outpvar.cur.fcalldata["main2"].close();
outpvar.cur.fcalldata["main2"].close();
outpvar.addchilds(newtag_main2(cod([]), ginp, outpvar.cur.fcalldata["main2"].root.content).root.content);