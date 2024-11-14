import os
import time
import pyautogui
import pytesseract
from PIL import Image
import numpy as np
import re
import sys

# 檢查 Tesseract OCR 是否已安裝
tesseract_path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
if not os.path.exists(tesseract_path):
    print("Tesseract OCR 未安裝，請先安裝 Tesseract 並設定正確路徑。")
    sys.exit(1)
else:
    pytesseract.pytesseract.tesseract_cmd = tesseract_path


# 設定資料夾路徑
screenshot_folder = os.path.join(os.path.dirname(__file__), "screenshot")
os.makedirs(screenshot_folder, exist_ok=True)

# 顏色設定
complete_answer_color = (38, 206, 136)  # 完成答題顏色 RGB
bookwork_code_background_color = (46, 60, 113)  # Bookwork code 背景顏色 RGB
bookwork_check_text = "Bookwork check"  # Bookwork check 文字
bookwork_check_code_color = (44, 206, 136)  # 假設顏色設定，根據實際顏色調整

# 函數: 截圖整個螢幕
def take_screenshot():
    screenshot = pyautogui.screenshot()
    return screenshot

# 函數: 偵測顏色是否在螢幕上
def detect_color(color, screenshot):
    screenshot_np = np.array(screenshot)
    for x in range(screenshot_np.shape[1]):
        for y in range(screenshot_np.shape[0]):
            if tuple(screenshot_np[y, x]) == color:
                return True
    return False

# 函數: 偵測顏色範圍內的 Bookwork code
def detect_bookwork_code(screenshot):
    screenshot_np = np.array(screenshot)
    for x in range(screenshot_np.shape[1]):
        for y in range(screenshot_np.shape[0]):
            # 偵測到背景顏色，表示可能是 Bookwork code
            if tuple(screenshot_np[y, x]) == bookwork_code_background_color:
                # 假設從這個位置開始提取文字
                region = screenshot.crop((x-100, y-20, x+150, y+20))  # 根據需要調整範圍
                text = extract_text_from_image(region)
                bookwork_code_match = re.search(r"Bookwork\s*(\S+)", text)
                if bookwork_code_match:
                    return bookwork_code_match.group(1)
    return None

# 函數: 使用 OCR 讀取圖片中的文字
def extract_text_from_image(image):
    text = pytesseract.image_to_string(image)
    return text

# 函數: 偵測是否有完成答題顏色並抓取 Bookwork Code
def detect_complete_answer_and_code():
    screenshot = take_screenshot()
    if detect_color(complete_answer_color, screenshot):
        # 找到完成答題顏色後，檢查 Bookwork code:
        text = extract_text_from_image(screenshot)
        bookwork_code_match = re.search(r"Bookwork code:\s*(\S+)", text)
        if bookwork_code_match:
            bookwork_code = bookwork_code_match.group(1)
            screenshot_name = f"{bookwork_code}.png"
            screenshot.save(os.path.join(screenshot_folder, screenshot_name))
            print(f"截圖已保存為 {screenshot_name}")
        else:
            print("未找到 Bookwork code")
    else:
        print("未找到完成答題顏色")

# 函數: 偵測是否有 Bookwork check 並打開對應的截圖
def detect_bookwork_check_and_open():
    print("Loading screenshot...")  # 顯示 loading 訊息
    screenshot = take_screenshot()
    text = extract_text_from_image(screenshot)
    if bookwork_check_text in text:
        # 嘗試偵測 Bookwork code
        bookwork_code = detect_bookwork_code(screenshot)
        if bookwork_code:
            screenshot_path = os.path.join(screenshot_folder, f"{bookwork_code}.png")
            if os.path.exists(screenshot_path):
                screenshot = Image.open(screenshot_path)
                screenshot.show()  # 顯示截圖
                print(f"打開截圖: {screenshot_path}")
            else:
                print(f"找不到對應的截圖：{screenshot_path}")
        else:
            print("未找到 Bookwork code")
    else:
        print("未找到 Bookwork check")

# 函數: 刪除資料夾內的所有圖片
def delete_previous_screenshots():
    for file_name in os.listdir(screenshot_folder):
        file_path = os.path.join(screenshot_folder, file_name)
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f"已刪除圖片：{file_name}")

# 每次啟動時刪除上次保存的圖片
delete_previous_screenshots()

# 主程式循環
def main():
    while True:
        detect_complete_answer_and_code()  # 偵測完成答題顏色及保存截圖
        detect_bookwork_check_and_open()  # 偵測 Bookwork check 並打開截圖
        time.sleep(1)  # 每 1 秒鐘檢查一次

# 開始執行程式
if __name__ == "__main__":
    main()
