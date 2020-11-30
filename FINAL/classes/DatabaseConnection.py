import pymysql.cursors

class DatabaseConnection:
    def __init__(self, HOST, USER, PW, DB):
        try:
            self.connection = pymysql.connect(host=HOST,
                                    user=USER,
                                    password=PW,
                                    db=DB,
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor)
            print("Conexión correcta")
        except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
            print("Ocurrió un error al conectar: ", e)
    
    
