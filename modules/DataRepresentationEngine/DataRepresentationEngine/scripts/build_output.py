#
# This script is used to take the output from the Java build
# process and convert it into the JSON format that the
# Gradescope system expects.
#
import json
import fileinput

data = {}
data['score'] = 0.0
data['output'] = ''

for line in fileinput.input():
        data['output'] += line

print(json.dumps(data, indent=2))