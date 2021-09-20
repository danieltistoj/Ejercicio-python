import pymysql
class BasedeDatos:
    def __init__(self):
        self.connection = pymysql.connect(
            host ='165.227.192.109',
            user ='analisis',
            password='1234',
            db = 'analisisdatos'
        )
        try:
            self.cursor = self.connection.cursor()
            print("conexion exitoso con mysql")
        except:
            print("valio verga la conexion")


database = BasedeDatos()

