flights = [[630,1100,1450,1950], [1020,1820], [1250], [1340], [610,1050,1540,2030], [900,1730], [1450, [1020,2100]]
def price(out, ins

loc = input("Paris, Barcelona, Madrid, Lisbon, Dublin, Belfast, Berlin, Amsterdam? ")
loc = loc.lower()
if loc == "paris":
  out = 0
  ft = int(input("6:30,11,14:50,19:50 (1,2,3,4)"))
  ins = ft-1



def OUT(out):
  loc = int(input("Paris, Barcelona, Madrid, Lisbon, Dublin, Belfast, Berlin, Amsterdam? Enter 1-8: "))
  out = loc-1
  return out

def INS(out, ins):
  loc = int(input(f"which? {print(flights[out]} pick from 1-{len(flights[out])} : "))
  ins = loc-1
  return ins
