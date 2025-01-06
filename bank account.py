# IBAN Validator.
"""
https://edube.org/learn/pe-2/four-simple-programs-15
An IBAN-compliant account number consists of:

a two-letter country code taken from the ISO 3166-1 standard (e.g., FR for France, GB for Great Britain, DE for Germany, and so on)
two check digits used to perform the validity checks – fast and simple, but not fully reliable, tests, showing whether a number is invalid (distorted by a typo) or seems to be good;
the actual account number (up to 30 alphanumeric characters – the length of that part depends on the country)
"""

iban = input("Enter IBAN, please: ")
iban = iban.replace(' ','')

if not iban.isalnum():
    print("You have entered invalid characters.")
elif len(iban) < 15:
    print("IBAN entered is too short.")
elif len(iban) > 31:
    print("IBAN entered is too long.")
else:
    iban = (iban[4:] + iban[0:4]).upper()
    iban2 = ''
    for ch in iban:
        if ch.isdigit():
            iban2 += ch
        else:
            iban2 += str(10 + ord(ch) - ord('A'))
    iban = int(iban2)
    if iban % 97 == 1:
        print("IBAN entered is valid.")
    else:
        print("IBAN entered is invalid.")
