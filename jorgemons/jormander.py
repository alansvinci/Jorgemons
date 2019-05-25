from .jorgemon import Jorgemon
from typing import Typing

class Jormander(Jorgemon):
  def __init__(self):
    super().__init__(
      index=4,
      name="Jormander",
      type1=Typing.Jorfogo,
      hp=39,
      attack=52,
      defense=43,
      sp_attack=60,
      sp_defense=50,
      speed=65
    )