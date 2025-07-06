import psycopg2
from psycopg2.extras import RealDictCursor

class PostgresClient:
    def __init__(self, db_name='docsearch', user='postgres', password='admin', host='localhost', port='5432'):

        """
        Initialize the PostgreSQL connection and create the documents table if it doesn't exist.
        
        Args:
            db_name (str): Name of the database to connect.
            user (str): Database user.
            password (str): Password for the user.
            host (str): Database host address.
            port (str): Port number.
        """

        # Establish a connection to the PostgreSQL database
        self.conn = psycopg2.connect(dbname=db_name, user=user, password=password, host=host, port=port)

        # Ensure the documents table exists
        self._create_table()

    def _create_table(self):

        """
        Create the 'documents' table in the database if it does not already exist.
        The table has three columns:
        - id: auto-incrementing primary key
        - file_name: name of the document file
        - content: textual content of the document
        """

        with self.conn.cursor() as cur:
            # Create the documents table if it doesn't exist
            cur.execute('''
                CREATE TABLE IF NOT EXISTS documents (
                    id SERIAL PRIMARY KEY,
                    file_name TEXT,
                    content TEXT
                )
            ''')

            # Create a GIN index for full-text search on the content column
            cur.execute('''
                CREATE INDEX IF NOT EXISTS idx_content_fulltext 
                ON documents 
                USING GIN (to_tsvector('english', content))
            ''')

            self.conn.commit()



    def index_file(self, file_name, content):

        """
        Insert a new document record into the 'documents' table.
        
        Args:
            file_name (str): Name of the file to index.
            content (str): Text content of the file to store.
        """

        with self.conn.cursor() as cur:
            cur.execute('INSERT INTO documents (file_name, content) VALUES (%s, %s)', (file_name, content))
            self.conn.commit()

    def search(self, query):

        """
        Searches for documents in the database whose content matches the given query

        Args:
            query (str): The search string or keywords.

        Returns:
            List of dictionaries with matching file names.
        """
        
        with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
            # cur.execute("SELECT file_name FROM documents WHERE content ILIKE %s", ('%' + query + '%',))
            cur.execute("SELECT file_name FROM documents WHERE to_tsvector('english', content) @@ plainto_tsquery('english', %s)", (query,))
            return cur.fetchall()
        
    def list_file_name(self):
        """
        Retrieves a list of all file names currently indexed in the 'documents' table.

        Returns:
            List[str]: A list of file names.
        """
        with self.conn.cursor() as cur:
            # Execute a query to fetch all file names from the documents table
            cur.execute("SELECT file_name from documents;")
            response = cur.fetchall()
            # Extract and return just the file name strings from the fetched rows
            return [file[0] for file in response]
    

    