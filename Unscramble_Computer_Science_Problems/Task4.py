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

call_list     = []
receiver_list = []
sms_list      = []
telemarketers = set()

for call in calls:
    call_list.append(call[0])
    receiver_list.append(call[1])

for contact in texts:
    sms_list.append(contact[0])
    sms_list.append(contact[1])
    
for telemarker in call_list:
    if (telemarker not in receiver_list) and (telemarker not in sms_list):
        telemarketers.add(telemarker)
        
print("telemarketers numbers: ", len(telemarketers))
print("These numbers could be telemarketers: {} ".format(telemarketers))