from replit import db


def save_obj(obj: object) -> bool:
    try:
        if obj.id is None:
            raise AttributeError
    except AttributeError as e:
        print(e)
        return False

    key = f'dc_{obj.__name__}_{obj.id}'
    value = dict(obj)

    db[key] = value

    return True
