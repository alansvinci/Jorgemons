from .jorgemon import Jorgemon
from typing import Typing

class Jorgesaur(Jorgemon):
  def __init__(self):
    super().__init__(
      index=1,
      name="Jorgesaur",
      type1=Typing.Jorgrama,
      hp=45,
      attack=49,
      defense=49,
      sp_attack=65,
      sp_defense=65,
      speed=45
    )