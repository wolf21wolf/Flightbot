import requests

SIMBRIEF_USERNAME = "WOLF21"

ICAO_NAMES = {
    # 北海道
    "RJCC": "新千歳空港",
    "RJCH": "函館空港",
    "RJCK": "釧路空港",
    "RJCM": "女満別空港",
    "RJCN": "稚内空港",
    "RJCO": "札幌飛行場（丘珠空港）",
    "RJCR": "根室中標津空港",
    "RJCS": "旭川空港",
    "RJCT": "帯広空港",
    "RJEB": "紋別空港",
    "RJEC": "利尻空港",
    "RJEO": "奥尻空港",
    "RJER": "礼文空港",
    "RJCB": "とかち帯広空港",

    # 東北
    "RJSA": "青森空港",
    "RJSC": "山形空港",
    "RJSH": "八戸航空基地",
    "RJSI": "花巻空港",
    "RJSK": "秋田空港",
    "RJSM": "三沢飛行場",
    "RJSO": "大館能代空港",
    "RJSR": "大湊航空基地",
    "RJSS": "仙台空港",
    "RJST": "松島飛行場",
    "RJSY": "庄内空港",
    "RJSF": "福島空港",

    # 関東
    "RJAA": "成田国際空港",
    "RJAH": "百里飛行場（茨城空港）",
    "RJAF": "入間基地",
    "RJAT": "富士飛行場",
    "RJTA": "厚木飛行場",
    "RJTC": "立川飛行場",
    "RJTD": "調布飛行場",
    "RJTF": "館山航空基地",
    "RJTK": "木更津飛行場",
    "RJTL": "下総航空基地",
    "RJTO": "大島空港",
    "RJTR": "八丈島空港",
    "RJTT": "東京国際空港（羽田空港）",
    "RJTU": "宇都宮飛行場",
    "RJTY": "横田飛行場",

    # 中部・甲信越・北陸
    "RJBB": "関西国際空港",
    "RJBC": "神戸空港",
    "RJBD": "南紀白浜空港",
    "RJBE": "但馬空港",
    "RJBF": "福井空港",
    "RJBK": "コウノトリ但馬空港",
    "RJFM": "静岡空港",
    "RJNA": "名古屋飛行場（小牧空港）",
    "RJNG": "岐阜基地",
    "RJNH": "浜松基地",
    "RJNK": "小松飛行場",
    "RJNN": "中部国際空港",
    "RJNO": "能登空港",
    "RJNS": "静岡空港",
    "RJNT": "富山空港",
    "RJNW": "新潟空港",
    "RJNZ": "松本空港",
    "RJGG": "中部国際空港",
    "RJAM": "南鳥島空港",

    # 関西
    "RJOO": "大阪国際空港（伊丹空港）",
    "RJOS": "徳島飛行場（徳島阿波おどり空港）",
    "RJOT": "高松空港",
    "RJOM": "松山空港",
    "RJOK": "高知空港",
    "RJOB": "岡山空港",
    "RJOR": "鳥取空港",
    "RJOH": "広島空港",
    "RJOI": "岩国飛行場",
    "RJOA": "広島空港",
    "RJOE": "明野飛行場",
    "RJOW": "石見空港",
    "RJOF": "防府北基地",
    "RJOC": "出雲空港",
    "RJDC": "但馬空港",
    "RJDB": "隠岐空港",
    "RJBH": "広島西飛行場",

    # 九州
    "RJFA": "芦屋基地",
    "RJFC": "壱岐空港",
    "RJFE": "福江空港",
    "RJFF": "福岡空港",
    "RJFG": "佐賀空港",
    "RJFH": "鹿屋航空基地",
    "RJFI": "種子島空港",
    "JFKJ": "新門司空港",
    "RJFK": "鹿児島空港",
    "RJFM": "宮崎空港",
    "RJFN": "新田原基地",
    "RJFO": "大分空港",
    "RJFR": "北九州空港",
    "RJFS": "佐世保空港",
    "RJFT": "熊本空港",
    "RJFU": "長崎空港",
    "RJFY": "海上自衛隊大村航空基地",
    "RJFZ": "屋久島空港",
    "RJKA": "奄美空港",
    "RJKB": "喜界空港",
    "RJKI": "喜界空港",
    "RJKN": "徳之島空港",
    "RJNF": "福井空港",
    "RJNY": "静浜基地",
    "RJKP": "沖永良部空港",
    "RJKR": "与論空港",
    "RJKS": "種子島空港",
    "RJKT": "屋久島空港",
    "RJKY": "指宿飛行場",

    # 沖縄
    "ROAH": "那覇空港",
    "RODN": "嘉手納飛行場",
    "ROIG": "石垣空港",
    "ROKJ": "久米島空港",
    "ROMD": "南大東空港",
    "ROMY": "宮古空港",
    "RORA": "波照間空港",
    "RORH": "波照間空港",
    "RORK": "北大東空港",
    "RORS": "下地島空港",
    "RORT": "多良間空港",
    "RORY": "与那国空港",
    "RORE": "伊江島空港",
    "ROTM": "普天間飛行場",

    #海外
    "RCTP": "台湾桃園",
    "VHHH": "香港国際空港",
    "VHHX": "啓徳空港",
    "RKSI": "仁川国際空港",
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
