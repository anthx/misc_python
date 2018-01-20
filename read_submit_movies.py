import requests
import sys
import os
import time


# This is the "Location" question whose answer is where this
# script is being run from. It should match one of the entries in your Google
# Form.
this_location = sys.argv[2]
directory_to_scan = sys.argv[1]

# copy the form ID to here
form_id = ""

# modify the submission url as you need
url = f"https://docs.google.com/forms/d/e/{form_id}/formResponse"

if form_id == "":
    print("You need to update the form ID (and questions) in the source code...")
    exit()

for entry in os.listdir(directory_to_scan):
    last_dot = entry.rfind(".")
    if last_dot == -1:
        last_dot = len(entry)
    # update the dictionary to reflect your own Form Question IDs
    # (Use the pre-filled link as a guide)
    data = {"entry.yyyyyyyyy": entry[:last_dot],
            "entry.zzzzzzzzz": this_location}
    request = requests.post(url, data)
    print(entry[:last_dot], request.status_code)
    request.close()

    # let's pause for a couple of seconds to be a nice internet citizen
    time.sleep(2)

