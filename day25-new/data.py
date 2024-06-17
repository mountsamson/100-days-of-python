import requests

url = "https://api.glideapp.io/api/function/queryTables"
headers = {"Authorization": "Bearer 75324064-5c9e-4c50-9919-d0b6d39d531d"}
params = {
    "appID": "kcyCfSuKi2vldRANArmH",
    "tableName": "native-table-LszMJZFio40jrgNxl6eK",
    "utc": True
}

try:
    r = requests.get(url, headers=headers, params=params)
    r.raise_for_status()  # Raise an exception for HTTP errors

    result = r.json()

    if 'data' in result:
        for row in result['data']:
            print(row)
    else:
        print("No data returned.")

except requests.exceptions.RequestException as e:
    print("Error:", e)
