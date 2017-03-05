import MySQLdb


class MariaDBData:
    ##conn = None
    # conx
    @property
    def conx(self):
        return self.__conx

    @conx.setter
    def conx(self, conx):
        self.__conx = conx


    def connect_to_db(self, host, uid, pwd, db):
        self.conx = MySQLdb.connect(
            host=host, user=uid, password=pwd, database=db)

    def get_data(self, query):
        cursor = self.conx.cursor()
        cursor.execute(query)
        result = []
        columns = tuple([i[0] for i in cursor.description])

        for row in cursor:
            result.append(dict(zip(columns, row)))

        cursor.close()
        return result

    def execute_query(self, query, values):
        cursor = self.conx.cursor()
        resp = cursor.execute(query, values)
        self.conx.commit()
        cursor.close()
        return cursor.lastrowid

    def disconnect_from_db(self):
        self.conx.close()
