# 外部ライブラリをインポート
import streamlit
import requests
import json


# フロントエンドを表示
streamlit.title("どこの天気が知りたい？")
question = streamlit.text_input("地域コードを入力")
button = streamlit.button("教えてもらう")
streamlit.markdown("[地域コード一覧](https://weather.tsukumijima.net/primary_area.xml)")
streamlit.markdown("[API仕様](https://weather.tsukumijima.net/)")

if button:    
    API_URL = "https://weather.tsukumijima.net/api/forecast/city/{0}"

    req_url = API_URL.format(question)
    res = requests.get(req_url).json()
    title = res["description"]["bodyText"]
    streamlit.write(title)
