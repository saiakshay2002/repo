import requests
URL = "https://docs.google.com/spreadsheets/d/1Fs61LL3-uGEUqCzToMt0D3a8Mxd3jWGivT_qalcYkZA/edit#gid=0&range=Q:Q"
# 2. download the data behind the URL
response = requests.get(URL)
# 3. Open the response into a new file called instagram.ico
open("folder", "wb").write(response)
