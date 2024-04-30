import datetime
from inspect import getcallargs

def logging_decorator(logger):
    def decorator(function):
        def wrapper(*args, **kwargs):
            call_time = datetime.datetime.now()
            result = function(*args, **kwargs)
            logger.append({
                "name": function.__name__,
                "arguments": getcallargs(function, *args, **kwargs),
                "call_time": call_time,
                "result": result
            })
            return result
        return wrapper
    return decorator
