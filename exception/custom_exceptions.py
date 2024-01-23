

class DBConnectionNotSet(Exception):

    def __init__(self):
        super().__init__("Database connection not set")
