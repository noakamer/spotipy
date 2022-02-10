import inspect

from log import debug_log, info_log, warning_log, error_log


class Song:
    def __init__(self, data: dict):
        import const
        self.popularity = data.get(const.POPULARITY)
        self.id = data.get(const.ID)
        self.name = data.get(const.NAME)
        call_stack = inspect.stack()
        func_name = call_stack[0][3]
        info_log(__name__, func_name, f"created {self.name} song successfully")

    def to_string(self):
        return f"name: {self.name}"
