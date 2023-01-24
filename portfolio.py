import mysqlConn as dbConn

def selectPjt():
    print("###### start selectPjt #############")
    sql_select = 'select * from profile'
    dbConn.db.execute(sql_select)
    pjt = dbConn.db.fetchall()
    for record in pjt:
        print(record)

    return pjt