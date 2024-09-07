# 8 char long
# contain letters, numbers, symbols $%#@

import re

# pattern = re.compile(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[$%#@])[A-Za-z\d$%#@]{8,}$')
pattern = re.compile(r'^[A-Za-z\d#$%@]{7,}\d$')

string = 'ShaktiOP1@1'

check = pattern.fullmatch(string)
print(check)
