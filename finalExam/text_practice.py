import pandas as pd
import re

re.search(r"[kr, mkr]", "chanceee mkrkr")
re.search(r"a.", "chanceee mkrkr")
re.search(r"[^ch]", "chanceee mkrkr")

re.search(r"c[a-z]a", "chance")
re.match(r"c[a-z]a", "chance")

re.findall(r"(ce)", "cecece")

z = re.compile("an")
z.search("chance")


strings = '''
    Beomjin Park : 010-1234-5678
    SangjunMoon : 010-2345-6789
    Sion Park : 010-431-1234
    Younghee Kim : 01056561234
'''

z = re.compile(r'''
               (\w+\s*\w+)
               \s:\s
               (\d+-*\d+-*\d+)
               ''', re.VERBOSE)
               

a = pd.DataFrame(z.findall(strings))
a.columns = ["name", "phone number"]
a
