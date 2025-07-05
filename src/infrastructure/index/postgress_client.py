import psycopg2
from psycopg2.extras import RealDictCursor

class PostgresClient:
    def __init__(self, db_name='docsearch', user='postgres', password='admin', host='localhost', port='5432'):
        self.conn = psycopg2.connect(dbname=db_name, user=user, password=password, host=host, port=port)
        self._create_table()

    def _create_table(self):
        with self.conn.cursor() as cur:
            cur.execute('''
                CREATE TABLE IF NOT EXISTS documents (
                    id SERIAL PRIMARY KEY,
                    file_name TEXT,
                    content TEXT
                )
            ''')
            self.conn.commit()

    def index_file(self, file_name, content):
        with self.conn.cursor() as cur:
            cur.execute('INSERT INTO documents (file_name, content) VALUES (%s, %s)',
                        (file_name, content))
            self.conn.commit()

    def search(self, query):
        with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT file_name FROM documents WHERE content ILIKE %s", ('%' + query + '%',))
            return cur.fetchall()
        
    def list_file_name(self):
        with self.conn.cursor() as cur:
            cur.execute("SELECT file_name from documents;")
            response = cur.fetchall()
            return [file[0] for file in response]
    

    