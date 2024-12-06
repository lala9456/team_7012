# team_7012
這是 **Team7012** 參與「基於區域微氣候資料預測發電量」競賽所提交的專案，提供了主辦單位要求的預測模型及其重現結果的程式碼。以下是具體說明：

---

## 視覺化網站
提供一個簡單的視覺化網站，用於展示數據分析及模型預測結果，幫助使用者直觀理解模型表現。
網址
[視覺化網站](https://app.powerbi.com/view?r=eyJrIjoiZTRjM2M0NWUtY2RlOS00ZDI3LThkZWUtNDY3MjUyNzVkNmRlIiwidCI6IjlmMzAyYTkwLTc3NjEtNDRkNi05MjgyLTdjY2M0NWYzOGY3YSIsImMiOjEwfQ%3D%3D)
- 第1頁
  
  各裝置發電量時間序列圖，可供使用者自行選擇各裝置跟不同時間段的發電數據
- 第2頁
  
  各裝置發電量以及濕度、溫度、氣壓、光照（主辦所提供之資料）的散佈圖與迴歸直線、相關係數，可供使用者自行選擇各裝置跟不同時間段的資訊查看

- 第3頁
  
  選擇兩個裝置，查看彼此濕度、溫度、氣壓、光照、發電量的散佈圖與迴歸直線、相關係數，其中圖表的-1代表所選的第一個裝置，-2代表所選的第二個裝置

- 第4頁
  
    各裝置發電量以及濕度、溫度、日射量（花蓮市氣象局的外部資料）、太陽仰角的散佈圖與迴歸直線、相關係數，可供使用者自行選擇各裝置跟不同時間段的資訊查看
  

---

## 程式碼使用說明
### 1. 環境設置
- 使用 **Python 3.12** 作為開發環境。
- 安裝所需套件，請使用以下命令安裝套件：
  ```bash
  pip install -r requirements.txt

### 2. 模型訓練與權重檔案
- 由於模型訓練的權重檔案較大，提供下載連結：[Googledrive](https://drive.google.com/drive/folders/10Oxgz7N0iUbgS9COQwB1CwuHbsRITImN?usp=sharing)
- 有關前處理檔案較大的數據，提供下載連結：[Googledrive](https://drive.google.com/drive/folders/1er89_figAMLEFkaXcKVBW1qLy1tR4ukK?usp=drive_link)
- 下載後請將權重檔案放置於指定目錄，具體路徑參見程式碼中的相關註解。

### 3. 模型重現與預測
- 提供分數最高的幾個模型，供使用者進行重現訓練或預測。
- 總共有3種模型訓練模式，分別是同地異時、同時異地、同第同時（有兩種版本，分別是使用氣象站第三方資料以及使用每間隔10分鐘的天氣資料之模式）
- 若需驗證競賽結果，可直接下載權重檔案，並執行predict_private_hightest.ipynb
### 4.注意事項
- 在比賽期間訓練時有些模型未設置隨機種子，
可能導致重新訓練與原比賽結果略有差異。
如需精確驗證結果，建議使用下載檔案連結的比賽權重檔案。
- 所有檔案皆在，[Googledrive](https://drive.google.com/drive/folders/1zxUio2HN6ZE6C5R6WliX3PjrSg4B-v6V?usp=sharing)
  若有遺漏資訊可以透過信箱聯絡作者lala9456@gmail.com