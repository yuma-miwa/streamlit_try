# 外部ライブラリをインポート
import streamlit
import requests
import json


# フロントエンドを表示
streamlit.title("どこの天気が知りたい")
question = streamlit.text_input("質問を入力")
button = streamlit.button("質問する")

# ボタンが押されたらナレッジベースを呼び出し
# if button:
#   response = bedrock.retrieve_and_generate(
#     input={'text': question},
#     retrieveAndGenerateConfiguration={
#       'type': 'KNOWLEDGE_BASE',
#       'knowledgeBaseConfiguration': {
#         'knowledgeBaseId': 'XXXXXXXXXX', # ナレッジベースID
#         'modelArn': 'anthropic.claude-3-5-sonnet-20240620-v1:0'}})

if button:
    # # 気象庁データの取得
    # jma_url = "https://www.jma.go.jp/bosai/forecast/data/forecast/130000.json"
    # jma_json = requests.get(jma_url).json()

    # # 取得したいデータを選ぶ
    # jma_date = jma_json[0]["timeSeries"][0]["timeDefines"][0]
    # jma_weather = jma_json[0]["timeSeries"][0]["areas"][0]["weathers"][0]
    # #jma_rainfall = jma_json["Feature"][0]["Property"]["WeatherList"]["Weather"][0]["Rainfall"]
    # # 全角スペースの削除
    # jma_weather = jma_weather.replace('　', '')

    # # 回答を表示
    # #   streamlit.write(response['output']['text'])
    # streamlit.write(jma_weather)
    
    API_URL = "https://weather.tsukumijima.net/api/forecast/city/{0}"

    req_url = API_URL.format(question)
    res = requests.get(req_url).json()
    title = res["description"]["bodyText"]
    streamlit.write(title)
