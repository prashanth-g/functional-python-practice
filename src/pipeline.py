def assoc(_data, key, value):
    from copy import deepcopy
    data = deepcopy(_data)
    data[key] = value
    return data

def call(func, key):
    def apply_func(record):
        return assoc(record, key, func(record.get(key)))
    return apply_func

def pipeline(data, function):
    import functools
    return functools.reduce(lambda a, x: map(x, a), function, data)