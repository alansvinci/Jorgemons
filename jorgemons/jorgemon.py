from typing import Typing

class Jorgemon:
  def __init__(
    self,
    index,
    name,
    attack,
    defense,
    sp_attack,
    sp_defense,
    speed,
    hp,
    type1,
    type2=Typing.Jornulo
  ) :
    self.index = index
    self.name = name
    self.attack = attack
    self.defense = defense
    self.sp_attack = sp_attack
    self.sp_defense = sp_defense
    self.speed = speed
    self.hp = hp
    self.type1 = type1
    self.type2 = type2

    self.curr_hp = hp
    self.attack_buff = 0
    self.defense_buff = 0
    self.sp_attack_buff = 0
    self.sp_defense_buff = 0
    self.speed_buff = 0

  def status(self):
    type2_text = ""

    if self.type2 != Typing.Jornulo:
      type2_text = self.type2.name

    print (
"""[{}]
HP: {}/{}
ATK: {}
DEF: {}
SP_ATK: {}
SP_DEF: {}
SPD: {}""".format(
        self.name,
        self.curr_hp,
        self.hp,
        self.attack,
        self.defense,
        self.sp_attack,
        self.sp_defense,
        self.speed
    ))

  def do_move(self, other, move):
    move(self, other)

  def fainted(self):
    return self.curr_hp <= 0