# Author : Salvador Hernandez Mendoza
# Email  : salvadorhm@gmail.com
# Twitter: @salvadorhm

import web

db_host = 'localhost'
db_name = 'kuorra_login'
db_user = 'root'
db_pw = '0573'
#db_port = 3308

db = web.database(
    dbn = 'mysql',
    host = db_host,
    db = db_name,
    user = db_user,
    pw = db_pw,
    #port = db_port
    )
