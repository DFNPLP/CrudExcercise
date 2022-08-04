from tinydb import TinyDB

path_to_db_file = 'recipes_db.json'


# this pattern of code is called a "singleton"
class DbConnection:
    """
    This class is a singleton that helps to manage your interaction with
    the local file hosted DB called TinyDB. (TinyDB is super simple,
    really useful for small projects and non-production ready content.)
    """
    _instance = None

    def __init__(self):
        """
        Basically the constructor.
        """
        self._db = None

    @staticmethod
    def get_instance():
        """
        This is a static method, not technically a member of a single
        instance. It's associated with the class. Gets the singleton
        instance of the class.

        :return: The singleton instance of DbConnection.
        """
        # note, I don't think this is technically thread safe
        if not DbConnection._instance:
            DbConnection._instance = DbConnection()
            DbConnection._instance.initialize_db_if_needed()

        return DbConnection._instance

    def initialize_db_if_needed(self):
        """
        Function to initialize the internal db instance.
        """
        if not self._db:
            self._db = TinyDB(path_to_db_file)

    def get_db(self) -> TinyDB:
        """
        :return: The internal TinyDb instance.
        """
        self.initialize_db_if_needed()

        return self._db


async def get_db_connection():
    """
    Function external to DbConnection to return the singleton
    instance of the class.
    :return: The singleton instance of DbConnection.
    """
    return DbConnection.get_instance()
