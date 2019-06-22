from typing import Typing

class Move:
    def __init__(self, name, type, function):
        self.name = name
        self.type = type
        self.function = function

    def execute(jorge_a, jorge_a)
        mult = 1.0

        # Bonus de mesmo tipo do ataque
        if self.type in {jorge_a.type1, jorge_a.type2}:
            mult += 0.5

        self.function(jorge_a, jorge_b, mult)

    def __str__(self):
        return self.name

def chute_jorge(a, b, mult):
    dmg = round(40 * (a.sp_attack / 300))
    dmg -= round(b.defense / 300)
    dmg*= mult
    b.curr_hp -= dmg

def choque_do_jorge(a, b, mult):
    dmg = round(40 * (a.sp_attack / 300))
    dmg -= round(b.defense / 300)
    dmg*= mult
    b.curr_hp -= dmg

def investida_jorge(a, b, mult):
    dmg = round(40 * (a.sp_attack / 300))
    dmg -= round(b.defense / 300)
    dmg*= mult
    b.curr_hp -= dmg

def fogo_do_jorge(a, b, mult):
    dmg = round(50 * (a.sp_attack / 300))
    dmg -= round(b.defense / 300)
    dmg*= mult
    b.curr_hp -= dmg

move_list = [
    Move("investida_jorge", Typing.Jormal, investida_jorge),
    Move("chute_jorge", Typing.Jormal, chute_jorge),
    Move("fogo_do_jorge", Typing.Jormal, fogo_do_jorge),
    Move("choque_do_jorge", Typing.Jorlétrico, choque_do_jorge),
    
    