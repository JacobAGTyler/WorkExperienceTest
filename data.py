from replit import db
from dataclasses import DataClass


class Persistence:
  def save_obj(self, obj: DataClass) -> bool:
    if obj.id == None:
      raise AttributeError

    obj.
