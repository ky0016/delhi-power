#This code is auto generated code, don't Edit it 
outpvar.cur.addfcdata("main2");
outpvar.cur.fcalldata["main2"].open(htmlnode("div", extentattrs(cod([]))));
outpvar.cur.fcalldata["main2"].cur.addfcdata("header4");
outpvar.cur.fcalldata["main2"].addchilds(newtag_header4(cod([]), ginp, outpvar.cur.fcalldata["main2"].cur.fcalldata["header4"].root.content).root.content);
if (int((ginp["uid"] > 0))): 
  outpvar.cur.fcalldata["main2"].cur.addfcdata("profile_chef");
  outpvar.cur.fcalldata["main2"].addchilds(newtag_profile_chef(cod([]), ginp, outpvar.cur.fcalldata["main2"].cur.fcalldata["profile_chef"].root.content).root.content);
outpvar.cur.fcalldata["main2"].close();
outpvar.addchilds(newtag_main2(cod([("js", ["js/profile.js", "https://maps.googleapis.com/maps/api/js?signed_in=true&libraries=drawing,places&callback=initMap"]), ("htmlstyle", cod([("overflow-y", "scroll")]))]), ginp, outpvar.cur.fcalldata["main2"].root.content).root.content);