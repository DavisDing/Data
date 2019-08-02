# -*- coding:utf-8 -*-
import ibm_db
conn = ibm_db.connect("DATABASE=dbname;HOSTNAME=localhost;PORT=50000;PROTOCOL=TCPIP;UID=usename;PWD=password;", "", "")
if conn:
    sql = "SELECT * FROM dual"
    stmt = ibm_db.exec_immediate(conn, sql)
    result = ibm_db.fetch_both(stmt)
    while( result ):
