"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

senders_list   = [call[0] for call in calls]
receivers_list = [call[1] for call in calls]

sms_list       = []
telemarketers  = set()

for contact in texts:
    sms_list.append(contact[0])
    sms_list.append(contact[1])
    
for telemarketer in senders_list:
    if (telemarketer not in receivers_list) and (telemarketer not in sms_list):
        telemarketers.add(telemarketer)
        
print("These numbers could be telemarketers: \n{}".format('\n'.join(sorted(telemarketers))))