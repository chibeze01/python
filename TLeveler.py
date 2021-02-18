# Dependancies
import pandas as pd

# getting the table as a Dataframe in pandas
table = pd.read_csv("./.data/table/table.csv")
# print(table.head())
# print (table.columns)

# here we sellect for the Dataframe the table of intrest
tOI = table[["country","GDP QoQ","Interest rate"]]
# print (tOI)

# we want to look at the top 10 most used currency pairs
#
# EUR/USD, GBP/USD, USD/JPY, USD/CAD, AUD/USD
##

def pairs(x, y):
    table = tOI
    # first we want to comap
    x_ = []
    y_ = []
    x_.append( float (table.loc[table["country"] == x].iloc[0]['GDP QoQ'].strip('%') ))
    x_.append( float (table.loc[table["country"] == x].iloc[0]['Interest rate'].strip('%') ))
    y_.append( float (table.loc[table["country"] == y].iloc[0]['GDP QoQ'].strip('%') ))
    y_.append( float (table.loc[table["country"] == y].iloc[0]['Interest rate'].strip('%') ))

# here we calculate the direction of the trade
    # sum = [a_i - b_i for a_i, b_i in zip(x_, y_)]
    # print(sum)
# x_, y_ = [GDP, interest rates]
# compare the trade direction to the x_
    if ( x_[0] > y_[0] and x_[1] > y_[1] ):
        print (f"For {x}/{y} you buy")
    elif ( x_[0] < y_[0] and x_[1] < y_[1] ):
        print (f"For {y}/{x} Buy")
    else:
        print(f"Undefined: {x} has a GDP rate of {x_[0]}% with interest rate of {x_[1]}%, \n"
        f"and {y} has a GDP rate of {y_[0]}% with interest rate of {y_[1]}% ")

# pairs("United States", "France")
# print (table)
