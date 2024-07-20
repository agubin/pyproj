import time
import functools

def clock(func):
    #замыкание clocked включает свободную переменную func
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print(f'[{elapsed:0.8f}]s {name}({arg_str}) -> {result!r}')
        return result
    
    return clocked

def improved_clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = [repr(arg) for arg in args]
        arg_str.extend([f'{k}={v!r}' for k,v in kwargs.items()])
        arg_str = ', '.join(arg_str)
        print(f'[{elapsed:0.8f}]s {name}({arg_str}) -> {result!r}')
        return result
    
    return clocked