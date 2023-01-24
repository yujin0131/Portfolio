import pymysql

dbConn = pymysql.connect(
    host='152.67.200.79',
    user='yujin',
    password='Wlsehf0014@',
    db='yujin',
    charset = 'utf8mb4',
    use_unicode=True
)
    
db = dbConn.cursor()

