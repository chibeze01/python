# Dependencies
import TLeveler as tl
from helpers import helpers
import GUI as gui

def main():
    helpers.data.get('https://tradingeconomics.com', "table-responsive")
    tl.pairs ('United States', 'United Kingdom')

if __name__ == "__main__":
    main()
