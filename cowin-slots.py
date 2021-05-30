import requests
import datetime
import json

AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
# ID for Kolkata
DISTRICT_ID = 725
# change the date if needed
DATE = datetime.datetime.now().date().strftime("%d-%m-%Y")

URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/calendarByDistrict"

MIN_AGE = 18
MIN_CAP = 0

response = requests.request(
    "GET", URL, verify=False, allow_redirects=True,
    headers={
        "user-agent": AGENT
    },
    params={
        "district_id": DISTRICT_ID,
        "date": DATE
    }
)


centers = json.loads(response.text)
for center in centers['centers']:
    try:
        out = 'Name: %s\n' % center['name']
        dump = False
        for session in center['sessions']:
            if session['min_age_limit'] <= MIN_AGE and MIN_CAP <= session['available_capacity']:
                dump = True
                out += 'Slot %s: total %d dose1 %d dose2: %d\n' % (
                    session['date'], session['available_capacity'],
                    session['available_capacity_dose1'],
                    session['available_capacity_dose2']
                )

        if dump:
            print()
            print(out)
            print()
    except Exception as err:
        print('Something wrong with center %s: %s' % (center['name'], err))
