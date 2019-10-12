from graph import CRG
from save import Save
import random

pin = random.random()
pout = 1 - pin
G = CRG("G", PIN=pin, POUT=pout)


A = CRG("A", PIN=.9, POUT=0)
B = CRG("B", PIN=.8, POUT=.2)
C = CRG("C", PIN=.6, POUT=.4)

Save(A)
Save(B)
Save(C)
Save(G)