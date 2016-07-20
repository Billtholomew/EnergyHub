from itertools import combinations

############################################
## USED CLASSES ##

class Card:

  def __init__(self,cid,attributes={}):
    self.cid = cid
    self.attributes = attributes

  def update_attribute(self,attrName,attrData):
    self.attributes[attrName] = attrData

#############################################
## MAIN FUNCTIONS ##

def find_all_sets(deck,n=3):
  # iterate through all combinations of n SET cards
  # note that this only creates combinations of cids
  for cids in combinations(deck.keys(),n):
    cards = [deck[c] for c in cids]
    # assume all cards will have the same attributes, so just pull from first card
    attributes = cards[0].attributes.keys() 
    validSet = True
    for a in attributes:
      # get the values for the current attribute for all cards
      # there should be 1 unique value (all same) or n unique values (all different)
      # if not, break early and set validSet to False
      aVals = set(map(lambda x:x.attributes[a],cards))
      if not (len(aVals)==1 or len(aVals)==n):
        validSet = False
        break
    if validSet:
      yield sorted(cids)
