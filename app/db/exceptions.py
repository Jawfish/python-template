class DatabaseSessionNotInitializedError(Exception):
    def __init__(self) -> None:
        super().__init__('Database session is not initialized')
