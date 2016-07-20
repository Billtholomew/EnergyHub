import csv
import sys
import setFinder

def load_test(fName):
  deck = {}
  trueSets = {}
  with open(fName,'rb') as f:
    reader = csv.reader(f)
    header = reader.next()
    _,attrTypes,_ = header[0],header[1:-1],header[-1]
    # skip header
    for row in reader:
      # memberships is the sets that the card is a member of
      # a row in the csv is the card id, followed by N attributes, and a membership
      cid,attrData,memberships = row[0],row[1:-1],row[-1]
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
      attributes = dict(zip(attrTypes,attrData))
      c = setFinder.Card(cid,attributes)
      deck[cid] = c
  return deck,trueSets

def run_test(fName,n=3):
  print 'Running test:',fName
  ##
  # Process data
  deck,trueSets = load_test(fName)
  foundSets = [f for f in setFinder.find_all_sets(deck,n)]
  # sets in both
  matches = [ts for ts in trueSets.values() if ts in foundSets]
  # missing expected sets
  mes = [ts for ts in trueSets.values() if ts not in foundSets]
  # sets found not expected
  ues = [fs for fs in foundSets if fs not in trueSets.values()]
  ##
  # Output results
  print '# Sets Found:',len(foundSets)
  print '# Sets Expected:',len(trueSets)
  print '# Sets in Both:',len(matches)
  if len(matches) is not len(trueSets):
    print 'Issue Detected, See below'
  if len(mes)>0:
    print 'Missing Sets:',len(mes)
    for m in mes:
      print '>',m
  if len(ues)>0:
    print 'Unexpectedly Found Sets:',len(ues)
    for u in ues:
      print '>',u
  if len(mes)==0 and len(ues)==0:
    print 'No issues detected'
  print '---------------------------'
  return mes,ues

###############################################
## TESTS ##
# test_1 - Each Attribute Changes, 4 card sets
# test_2 - 4 Cards, 3 card sets
# test_3 - No sets, 4 card sets
# test_4 - 3 card sets, 4 attribbutes each with 3 values
# test_5 - 3 card sets, 5 attributes, Flavor attribute has 6 values

# run all 4 tests
if __name__=="__main__":
  args = sys.argv[1:3]
  if len(args)==0:
    run_test('TestData/test_1.csv',4)
    run_test('TestData/test_2.csv',3)  
    run_test('TestData/test_3.csv',4)
    run_test('TestData/test_4.csv',3)
    run_test('TestData/test_5.csv',3)
  else:
    try:
      testFile,setSize = args
      setSize = int(setSize)
      run_test(testFile,setSize)
    except Exception as e:
      print e
      
