flights = [[630,1100,1450,1950], [1020,1820], [1250], [1340], [610,1050,1540,2030], [900,1730], [1450], [1020,2100]]
def price(out, ins, money):
  pe=int(input("how many people, max 6? : "))
  if flights[out][ins] <901:
    money = 150*pe
  elif flights[out][ins]>900 and flights[out][ins]<1700:
    money = 90*pe
  elif flights[out][ins]>1659 and flights[out][ins]<2400:
    money = 120*pe
  if flights[out]==flights[4] or flights[out]==flights[5]:
      ()
  else:
    peifm=int(input("how many people will have in flight meals? Max 6 : "))
    money = money+(20*peifm)
  pepb=int(input("how many people will have priority boarding? Max 6 : "))
  money = money+(30*pepb)
  return money
def OUT(out):
  loc = int(input("Paris, Barcelona, Madrid, Lisbon, Dublin, Belfast, Berlin, Amsterdam? Enter 1-8: "))
  out = loc-1
  return out

def INS(out, ins):
  loc = int(input(f"which? {print(flights[out])} pick from 1-{len(flights[out])} : "))
  ins = flights[out][loc-1]
  return ins
