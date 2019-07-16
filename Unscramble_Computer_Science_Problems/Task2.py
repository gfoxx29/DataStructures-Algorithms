"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
call_log   = {}
duration   = 0
total_time = 0

for call in calls:
    call_log[call[0]] = call_log.get(call[0], 0) + int(call[3])
    call_log[call[1]] = call_log.get(call[1], 0) + int(call[3])
    

duration, call_number = max(zip(call_log.values(), call_log.keys()))

print("{} spent the longest time, {} seconds, on the phone \
during September 2016.".format(call_number, duration))
