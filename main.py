from trainer import Trainer
import jorgemons

jorge = Trainer("Jorge", 6, [
  jorgemons.Jorchu(),
  jorgemons.Jormander(),
  jorgemons.Jorquirtle(),
  jorgemons.Jorgesaur(),
  jorgemons.Joroakie(),
  jorgemons.Joriolu()
])
jorge.list_jorgemons()

def jorackle(a, b):
  b.curr_hp -= round(40 * (a.attack / 255))

jorchu = jorge.jorgemons[0]
jormander = jorge.jorgemons[1]
jorchu.do_move(jormander, jorackle)

jorchu.status()
jormander.status()