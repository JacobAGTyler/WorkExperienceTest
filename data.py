from replit import db
from dataclasses import dataclass, asdict


def save_obj(obj: dataclass) -> bool:
    if obj.id is None:
        raise AttributeError

    key = f'dc_{obj.__class__.__name__}_{obj.id}'
    value = asdict(obj)

    db[key] = value

    return True


def list_objects(retrieval_class):
    prefix = f'dc_{retrieval_class.__name__}'
    matches = db.prefix(prefix)

    object_list = []
    match: dict
    for match in matches:
        match['id'] = int(match['id'].replace(f'{prefix}_', ''))
        object_list.append(retrieval_class(**match))

    return object_list
