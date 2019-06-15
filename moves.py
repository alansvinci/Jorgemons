def chute_jorge(a, b):
    dmg = round(40 * (a.sp_attack / 300))
    dmg -= round(b.defense / 300)
    b.curr_hp -= dmg

def choque_do_jorge(a, b):
    dmg = round(40 * (a.sp_attack / 300))
    dmg -= round(b.defense / 300)
    b.curr_hp -= dmg

def investida_jorge(a, b):
    dmg = round(40 * (a.sp_attack / 300))
    dmg -= round(b.defense / 300)
    b.curr_hp -= dmg

def 