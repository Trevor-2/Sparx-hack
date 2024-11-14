# Bookwork Code Detection Program

此程式用於檢測並記錄 Bookwork Code 的截圖，偵測完成答題顏色、Bookwork Check 等功能。

## 功能
- 偵測整個螢幕有無完成答題的顏色。
- 偵測 `Bookwork code` 並將截圖保存為指定名稱。
- 支援 `Bookwork check` 檢測，並自動打開相應的截圖。

## 安裝需求
- Python 3.x
- Tesseract OCR

## 使用方式
1. 安裝 [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) 並設定路徑。
2. 安裝 Python 需求庫：(use cmd)(windows->cmd->enter)
   ```bash
   pip install pyautogui pytesseract pillow numpy
3. 執行程式：
   ```bash
   python main.py

## 注意事項
每次執行程式會自動刪除上次的截圖。

# Bookwork Code Detection Program

This program is used to detect and record screenshots of Bookwork Code, detect answer color, Bookwork Check and other functions.

## Function
- Detect whether the color of the entire screen has been completed or not.
- Detect `Bookwork code` and save the screenshot to the specified name.
- Supports `Bookwork check` detection and automatically opens the corresponding screenshot.

## Installation requirements
- Python 3.x
- Tesseract OCR

## Usage
1. Install [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) and set the path.
2. Install the Python requirement library:(use cmd)(windows->cmd->enter)
 ```bash
 pip install pyautogui pytesseract pillow numpy
3. Execute the program:
```bash
 python main.py

## Notes
Each time the program is executed, the last screenshot will be automatically deleted.
