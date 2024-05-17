from functools import wraps

def ensure_session_key(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        session_key = request.session.session_key
        if not session_key:
            request.session.cycle_key()
        return func(request, *args, **kwargs)
    return wrapper