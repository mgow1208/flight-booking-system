flights = [[630,1100,1450,1950], [1020,1820], [1250], [1340], [610,1050,1540,2030], [900,1730], [1450], [1020,2100]]
def price(out, ins, money, pe):
  if flights[out][ins] <901:
    money = 150*pe
  elif flights[out][ins]>900 and flights[out][ins]<1700:
    money = 90*pe
  elif flights[out][ins]>1659 and flights[out][ins]<2400:
    money = 120*pe
  if flights[out]==flights[4] or flights[out]==flights[5]:
      ()
  else:
    peifm=int(input("how many people will have in flight meals?  : "))
    if peifm>pe:
      t = False
    else:
      money = money+(20*peifm)
    if not t:
      break
  pepb=int(input("how many people will have priority boarding?  : "))
  if pepb>pe:
    t = False
  else:
    money = money+(30*pepb)
  if not t:
    break
  return money

def OUT(out):
  loc = int(input("Paris, Barcelona, Madrid, Lisbon, Dublin, Belfast, Berlin, Amsterdam? Enter 1-8: "))
  out = loc-1
  return out

def INS(out, ins):
  loc = int(input(f"which? {print(flights[out])} pick from 1-{len(flights[out])} : "))
  ins = flights[out][loc-1]
  return ins

def details():
  t=input("what is your title/s")
  frn=input("first name?")
  srn=input("surname?")
  dob=input("date of birth?  dd/mm/yy")
  n=input("nationality?")
  psn=input("passport number?")


t=input("what is your title/s")
frn=input("first name?")
srn=input("surname?")
dob=input("date of birth?  dd/mm/yy")
n=input("nationality?")
psn=input("passport number?")
pe=int(input("how many people, max 6? : "))
print("answer details one by one for others")
for num in range(1,pe):
  details()
dayb=int(input("day of flight? - month and year will be asked in other questions: "))
monb=int(input("month? as a number: "))
yearb=int(input("year?: "))
if dayb > 31:
  valid = False
if (monb==4 or monb==6 or monb==9 or monb==11) and dayb==31:
  valid = False
if monb==2 and dayb>28:
  if yearb in range(2025,2028):
    valid = False
  if yearb==2028 and dayb>29:
    valid = False
if yearb>2028 or yearb<2025:
  valid = False
if yearb==2025:
  if monb<9:
    valid = False
  elif monb==9 and dayb<26:
    valid = False
elif yearb==2028:
  if monb>9:
    valid = False
  elif monb==9 and dayb>26:
    valid = False
