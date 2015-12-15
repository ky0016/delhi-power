execfile("includes/setting.py");

_agent = "poorvi";

import time, urlparse, datetime;

from msl import *
from msl.help import *
from msl.sql import *
from msl.mtime import *;

execfile(_mslib+"py/webd.py");
execfile(ROOT+"py/main.py");



idate = '12-12-2015';
int_date = s2t(idate);
obj_date = timeint2obj(int_date);
sql_date = t2f("%Y-%m-%d", int_date);

print _sql.g1("select cast(sum(actual) as unsigned) as actual, cast(sum(target) as unsigned) as target from "+tname+" where date = {date} ", {"date": t2f("%Y-%m-%d", int_date)})

_sql.sval("tbl_total_power", "actual, target", {"date": t2f("%Y-%m-%d", int_date)}, limit=1);


#mapp(mappl(lambda x: sifu(x, "percent",  (100.0*intf(x["actual"]))/intf(x["target"], 1)), row), ;


#print  mappl(lambda x: sifu(x, "percent",  (100.0*intf(x["actual"]))/intf(x["target"], 1)), row)

# v2 = _sql.sval(tname, "*", {"day(date)": " <= 11 AND (month(date), year(date))": t2f("%Y-%m-%d", int_date)}  );

#_sql.sval(tname, "*", {"date": int_date });




#print _sql.sval("tbl_total_power");




_sql.close_db();

