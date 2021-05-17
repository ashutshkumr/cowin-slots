import requests
import datetime
import json

# login to cowin using your phone number, search for your district, open dev tools using F12 and select the GET request
# click on Headers tab and under "Request Headers", copy the contents of after "Bearer" in "authorization" key and paste it here
BEARER_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX25hbWUiOiIzMzk4ZGQxNC01MDhmLTRkOTgtODhmOC1hYTIzYTE2N2ZiM2YiLCJ1c2VyX2lkIjoiMzM5OGRkMTQtNTA4Zi00ZDk4LTg4ZjgtYWEyM2ExNjdmYjNmIiwidXNlcl90eXBlIjoiQkVORUZJQ0lBUlkiLCJtb2JpbGVfbnVtYmVyIjo5NzQ5MDcxMjA5LCJiZW5lZmljaWFyeV9yZWZlcmVuY2VfaWQiOjM3ODQ3Njk2MzI0ODUwLCJzZWNyZXRfa2V5IjoiYjVjYWIxNjctNzk3Ny00ZGYxLTgwMjctYTYzYWExNDRmMDRlIiwidWEiOiJNb3ppbGxhLzUuMCAoWDExOyBMaW51eCB4ODZfNjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS85MC4wLjQ0MzAuMjEyIFNhZmFyaS81MzcuMzYiLCJkYXRlX21vZGlmaWVkIjoiMjAyMS0wNS0xN1QwODoxMzowMi4wMzBaIiwiaWF0IjoxNjIxMjM5MTgyLCJleHAiOjE2MjEyNDAwODJ9.FdqFaEpX2SJ1hKRW8G7fXJ1D6DhVLTWn6_acNkLZz3Q"
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
        # 'Content-Type': 'application/json',
        "authorization": "Bearer %s" % BEARER_TOKEN,
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