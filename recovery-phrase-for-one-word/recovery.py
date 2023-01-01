#example python3.6 recovery.py eth 0x914e9670E1A75c506F779F456B626C7bB6c1Ac85
import sys
from pywallet import *

bip39_words=open('../bip39-words/english.txt')

network=sys.argv[1].lower() 
address=sys.argv[2].lower()


for x in bip39_words.read().split("\n"):
     your_seed="glow outside secret rigid now excite fantasy ring solution make gaze "+x
     #print(your_seed)
     w = wallet.create_wallet(network=network, seed=your_seed, children=1)
     if w.get('address')==address:
         print(w.get('address'),'seed found:',your_seed)
         break


