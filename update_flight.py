import requests

SIMBRIEF_USERNAME = "WOLF21"

ICAO_NAMES = {
    "RJTT": "羽田空港",
    "RJAA": "成田空港",
    "RCTP": "台湾桃園",
    "VHHH": "香港国際空港",
    "VHHX": "啓徳空港",
    "RKSI": "仁川国際空港",
    "RJBB": "関西国際空港",
    "RPLL": "マニラ",
    "WSSS": "シンガポール",
}

def safe_get(dct, *keys, default=""):
    cur = dct
    for key in keys:
        if not isinstance(cur, dict):
            return default
        cur = cur.get(key, default)
    return cur if cur is not None else default

url = f"https://www.simbrief.com/api/xml.fetcher.php?username={SIMBRIEF_USERNAME}&json=v2"
data = requests.get(url, timeout=20).json()

dep = safe_get(data, "origin", "icao_code", default="----").upper()
arr = safe_get(data, "destination", "icao_code", default="----").upper()
callsign = safe_get(data, "atc", "callsign", default="N/A")
aircraft = safe_get(data, "aircraft", "icaocode", default="N/A").upper()

dep_name = ICAO_NAMES.get(dep, dep)
arr_name = ICAO_NAMES.get(arr, arr)

text = f"{dep_name} ({dep}) → {arr_name} ({arr}) | {callsign} | {aircraft}"

with open("flight.txt", "w", encoding="utf-8") as f:
    f.write(text)
