from collections import deque, defaultdict
import sys
import traceback
import pandas


numPoints = sys.argv[1]
fileName = sys.argv[2]
payer_points = defaultdict(int)

"""
check that numPoints is valid i.e. digits (whole numbers)
This method either raises a ValueError or returns True
"""
def arePointsValid(points):
    for c in str(points):
        if (ord("0") <= ord(c) <= ord("9")):
            pass
        else:
            raise ValueError("""Invalid number of points, points can only be a positive integer.
            Your command should look something like this: python3 getBalances.py <point amount> <filename.csv>""")
    return True

"""
check that .csv is a valid csv file (maybe check if the columns are what we expect as well?)
This method either raises a ValueError or returns True
"""
def isFileValid(file):
    if file.endswith(".csv"):
        return True
    raise ValueError("""This program can only take .csv files as an argument
    Your command should look something like this: python3 getBalances.py <point amount> <filename.csv>""")

"""
this method will return a deque giving us the sorted order of transactions where the oldest transaction 
is the far left and the newest is furthest right
"""
def getQ(df):
    sorted_df = df.sort_values(by = "timestamp") # oldest is at the top 
    q = deque()
    for i, row in sorted_df.iterrows():   
        q.append(df.iloc[i])
    return q
# also want something to keep track of each person's points so we can return at the end
"""
this function will initialize our dictionary mapping people to their points
"""
def getTotals(df):
    global payer_points
    for payer in df["payer"].unique():
        payer_points[payer]
        
    for i, row in df.iterrows():
        payer_points[row["payer"]] += row["points"]
    # payer_points is the totals that we will keep track of and eventually display

try:
    isFileValid(fileName)
    arePointsValid(numPoints)
except ValueError:
    tb = traceback.format_exc()
    print(tb)
    sys.exit()
    
df = pandas.read_csv(fileName)
q = getQ(df)
getTotals(df)

# start peeking and popping from q until we are out of points (numPoints <= 0)
# everytime you pop, edit the payer_points dict accordingly

