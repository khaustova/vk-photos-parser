from PySide6 import QtSql, QtWidgets


class Connection:
    """ Подключение к базе данных SQLite
    """

    def __init__(self):
        super(Connection, self).__init__()
        self.create_connection()

    def create_connection(self) -> bool:
        """ Создаёт (открывает) базу данных с таблицей для хранения последнего
        сохранённого токена и ID приложения.
        Если в таблице нет записей, то создаёт её с пустыми значениями
        """

        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("parser.db")

        if not db.open():
            QtWidgets.QMessageBox.critical(
                self,
                "Ошибка",
                "Произошла ошибка открытия базы данных.",
                buttons=QtWidgets.QMessageBox.Ok,
                defaultButton=QtWidgets.QMessageBox.Ok,
            )

            return False

        query = QtSql.QSqlQuery()
        query.exec(
            "CREATE TABLE IF NOT EXISTS parser (ID integer primary key AUTOINCREMENT, "
            "Token VARCHAR(100), Client_ID VARCHAR(100))"
        )
        query.exec("SELECT Token FROM parser WHERE ID=1")

        if not query.first():
            query.exec('INSERT INTO parser (ID, Token, Client_ID) VALUES (1, "", "")')

        return True

    def update_value(self, sql_query: str, value: str) -> QtSql.QSqlQuery:
        """ Подставляет значение value в SQL-запрос и выполняет его
        """

        query = QtSql.QSqlQuery()
        query.prepare(sql_query)
        query.addBindValue(value)
        query.exec()

        return query

    def update_token(self, token: str) -> None:
        """ Обновляет значение токена в базе данных
        """

        sql_query = "UPDATE parser SET Token=? WHERE ID=1"
        self.update_value(sql_query, token)

    def update_client_id(self, client_id: str) -> None:
        """ Обновляет значение ID приложения в базе данных
        """

        sql_query = "UPDATE parser SET Client_ID=? WHERE ID=1"
        self.update_value(sql_query, client_id)

        query = QtSql.QSqlQuery()
        query.exec(sql_query)

    def get_token(self) -> str:
        """ Возвращает последнее сохранённое значение токена
        """

        query = QtSql.QSqlQuery()
        query.exec("SELECT Token FROM parser WHERE ID=1")
        query.first()

        return query.value(0)

    def get_client_id(self) -> str:
        """ Возвращает последнее сохранённое значение ID приложения
        """

        query = QtSql.QSqlQuery()
        query.exec("SELECT Client_ID FROM parser WHERE ID=1")
        query.first()

        return query.value(0)
