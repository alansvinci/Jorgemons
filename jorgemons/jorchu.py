from .jorgemon import Jorgemon
from typing import Typing

class Jorchu (Jorgemon):
  def __init__(self):
    super().__init__(
      25,
      "Jorchu",
      type1=Typing.Jorlétrico,
      hp=85,
      speed=140,
      attack=105,
      defense=90,
      sp_attack=100,
      sp_defense=100,
    )