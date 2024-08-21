
BIC = '([A-Z]{4})([A-Z]{2})([A-Z0-9]{2})([A-Z0-9]{0,3})'
# pattern = "^([a-zA-Z]{2}\d{2})(\d{4}\d{4}\d{4}\d{4}\d{2})$" #simple iban
IBAN_ACCT = "\/+([A-Z]{2})(\d{2})([A-Z\d]{1,30})" #flexible iban
IBAN = "\/*([A-Z]{2})(\d{2})([A-Z\d]{1,30})" #https://rubular.com/r/erywjQ08BtZR1z
ACCT = '\/+([ a-zA-Z0-9/\-?:().,\'+]{0,34})'
ACCT_WO_SPACE = '\/+([a-zA-Z0-9/\-?:().,\'+]{0,34})'
OPTION_F2_ACCT = '^(ARNU|CCPT|CUST|DRLC|EMPL|NIDN|SOSE|TXID)\/([A-Z]{2})\/(.*)'
CHARS_X = '[a-zA-Z0-9/\-?:().,\'+]{,34}'

# OPTIONA = '(\/+[a-zA-Z0-9\/\-?:().,\'+]{,34})?#([0-9]\/[^#]+)'
# OPTIOND = '(\/+[a-zA-Z0-9\/\-?:().,\'+]{,34})?#([0-9]\/[^#]+)'
# OPTIONF1 = '(\/+[a-zA-Z0-9\/\-?:().,\'+]{,34})?#([0-9]\/[^#]+)'
