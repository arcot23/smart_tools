import warnings
from smart_tools.common.smartsys import print
from smart_tools.banking.mtparty import parse
import json

def main():
    warnings.warn("only for testing purposes")
    text1 = ['/DE89370400440532013000 _ BARCGB22', 'A']
    text2 = ['/GB82WEST12345698765432 _ 1/John Doe _ 2/25 Street Name, Apt 5 _ 3/SE-12345 City Name _ 4/US _ 5/Wrong one', 'F']
    text3 = ['/GB82WEST12345698765432 _ 1/John Doe _ 2/25 Street Name, Apt 5 _ 3/SE-12345 City Name _ 4/US', 'F']
    text4 = ['1/John Doe _ 2/25 Street Name, Apt 5 _ 3/SE-12345 City Name', 'F']
    text5 = [None, 'F']
    text6 = ['CUST/KY/BNPP/1381913/DKJSKDJSKSK _ 1/John Doe _ 2/25 Street Name, Apt 5 _ 3/SE-12345 City Name', 'F']

    temp = text6
    result = parse(temp[0], temp[1],False)
    result_json = json.dumps(result, indent=4)
    print(result_json)

if __name__ == '__main__':
    main()
