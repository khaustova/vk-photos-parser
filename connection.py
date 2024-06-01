from PySide6 import QtSql, QtWidgets


class Connection:
    def __init__(self):
        super(Connection, self).__init__()
        self.create_connection()

    def create_connection(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('parser.db')

        if not db.open():
            QtWidgets.QMessageBox.critical(None, "Не получается открыть базу данных", QtWidgets.QMessageBox.Cancel)
            return False

        query = QtSql.QSqlQuery()
        query.exec("CREATE TABLE IF NOT EXISTS parser (ID integer primary key AUTOINCREMENT, "
                   "Token VARCHAR(100), Client_ID VARCHAR(100))")
    
        return True
    
    def update_value(self, sql_query, value):
        query = QtSql.QSqlQuery()
        query.prepare(sql_query)
        query.addBindValue(value)
        query.exec()
        
        return query

    def update_token(self, token):
        sql_query = "UPDATE parser SET Token=? WHERE ID=1"
        self.update_value(sql_query, token)
        
    def update_client_id(self, client_id):
        sql_query = "UPDATE parser SET Client_ID=? WHERE ID=1"  
        self.update_value(sql_query, client_id)
        
    def get_value(self, sql_query, index):
        query = QtSql.QSqlQuery()
        query.exec(sql_query)

        if not query.first():
            insert_query = QtSql.QSqlQuery()
            insert_query.exec('INSERT INTO parser (ID, Token, Client_ID) VALUES (1, "", "")')
            return ""
        else:
            return query.value(index)
        
    def get_token(self):
        sql_query = "SELECT Token FROM parser WHERE ID=1"
        return self.get_value(sql_query, 0)
        
    def get_client_id(self):
        sql_query = "SELECT Client_ID FROM parser WHERE ID=1"
        return self.get_value(sql_query, 0)

        