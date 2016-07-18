import csv
import setFinder

###############################################
## TESTS ##
# test_1 - Each Attribute Changes, 4 card sets
# test_2 - 4 Cards, 3 card sets
# test_3 - No sets, 4 card sets
# test_4 - 3 card sets, 4 changing attribbutes
# test_5 - Based on image, 3 card sets, 5 attributes, Flavor attribute has 6 values

def load_test(fName):
  deck = {}
  trueSets = {}
  with open(fName,'rb') as f:
    reader = csv.reader(f)
    reader.next()
    # skip header
    for row in reader:
      # memberships is the sets that the card is a member of
      cid,color,shape,shading,number,taste,memberships = row
      memberships = memberships.split('|')
      cid = int(cid)
      # test data is always kept in increasing cid, so final sets will be ordered
      for m in memberships:
        if m=='':
          continue
        if m not in trueSets:
          trueSets[m] = []
        trueSets[m].append(cid)
      # load attributes into a new card
      # add card to deck
      attributes = {}
      attributes['Color'] = color
      attributes['Shape'] = shape
      attributes['Shading'] = shading
      attributes['Number'] = number
      attributes['Taste'] = taste
      c = setFinder.Card(cid,attributes)
      deck[cid] = c
  return deck,trueSets

def run_test(fName,n=3):
  print 'Running test:',fName
  deck,trueSets = load_test(fName)
  foundSets = [f for f in setFinder.find_all_sets(deck,n)]
  # missing expected sets
  mes = [ts for ts in trueSets.values() if ts not in foundSets]
  # sets found not expected
  ues = [fs for fs in foundSets if fs not in trueSets.values()]
  if len(mes)>0:
    print 'Missing Sets:',len(mes)
    for m in mes:
      print m
  if len(ues)>0:
    print 'Unexpectedly Found Sets:',len(ues)
    for u in ues:
      print u
  if len(mes)==0 and len(ues)==0:
    print 'No issues detected'
  return mes,ues

run_test('TestData/test_1.csv',4)
run_test('TestData/test_2.csv',3)  
run_test('TestData/test_3.csv',4)
run_test('TestData/test_4.csv',3)
run_test('TestData/test_5.csv',3)
