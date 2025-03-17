import pymysql.cursors
import sys  # Import sys to exit the program

class MySqlDatabase:
    def __init__(self):
        self._host = "srv-web-full-gestor.eastus2.cloudapp.azure.com"
        self._username = "usr_sistema"
        self._passwd = "7pstSwOqYES4"
        self._database = "fullhouse_gestor"
        self._connect()

    def _connect(self):
        try:
            self.cnn = pymysql.connect(
                host=self._host,
                user=self._username,
                password=self._passwd,
                database=self._database,
                cursorclass=pymysql.cursors.DictCursor
            )
        except pymysql.MySQLError as e:
            print(f"Error: {e}")
            sys.exit(1)
    
    def begin_transaction(self):
        """Start a transaction."""
        if self.cnn is None:
            self._connect()
        self.cnn.begin()  # Use pymysql's built-in transaction management

    def commit_transaction(self):
        """Commit the current transaction."""
        if self.cnn is not None:
            self.cnn.commit()

    def rollback_transaction(self):
        """Rollback the current transaction."""
        if self.cnn is not None:
            self.cnn.rollback()

    def _querying(self, query: str):
        if self.cnn is None:  # Check if the connection is None
            self._connect()  # Reconnect if necessary

        try:
            cursor = self.cnn.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            return result
        
        except pymysql.MySQLError as e:
            print(f"Error during querying: {e}")
            self.cnn = None  # Set connection to None to force a reconnect
            return []
            
    def executar_consulta(self, query: str, params):
        if self.cnn is None:  
            self._connect() 
        try:
            cursor = self.cnn.cursor()
            cursor.execute(query, params)
            result = cursor.fetchall()
            self.cnn.commit()  # Se você estiver fazendo uma operação de inserção/atualização
            cursor.close()
            return result
        
        except pymysql.MySQLError as e:
            print(f"Error during querying: {e}")
            self.cnn = None  # Set connection to None to force a reconnect
            return []
        
            
    def closing(self):
        if self.cnn is not None:  # Check if the connection is not None
            self.cnn.close()
            self.cnn = None  # Set connection to None after closing
