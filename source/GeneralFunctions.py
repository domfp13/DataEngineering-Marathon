
def decoratorGetPath(function):
    def wrapper(file_name):
        from pathlib import Path
        return Path('/tmp',file_name)
    return wrapper
@decoratorGetPath
def getPath(file_name:str):
    """Returns a Path objt, this is a decorator

    Args:
        file_name (str): Marathon-SQ-MPC003-Productivity.xlsx

    Returns:
        Path: If local get local path if not linux
    """
    from os import getcwd
    from pathlib import Path
    return Path(getcwd(), file_name)