import re

files_size = 0

with open("apache_logs.txt", "r") as file:
    string = file.readlines()

pattern = re.compile(':(((03:[2-5][0-9])|(0[4-9]:[0-5][0-9]))|((11:[0-1][0-7])|'
                     '(10:[0-5][0-9]))):(.*GET.*200\\s([0-9]+)\\s)')

for line in string:
    match = re.search(pattern, line)
    if match:
        files_size += int(match.group(9))
