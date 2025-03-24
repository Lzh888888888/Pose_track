# 姿勢追蹤螢幕錄影工具

(本專案原使用blot.new製作，後續使用Cursor修改)
這是一個基於 Python 開發的螢幕錄影工具，能夠即時追蹤並顯示人體姿勢和手部動作。本工具使用 OpenCV 和 MediaPipe 進行姿勢偵測，並提供即時視覺化效果。

## 功能特點

- 螢幕區域選擇：可自由選擇要錄製的螢幕區域
- 即時姿勢追蹤：顯示人體骨架和手部動作
- 雙重輸出：同時產生原始影像和骨架追蹤的影片
- 簡易操作介面：提供直覺的快捷鍵控制

## 系統需求

- Python 3.7 或以上版本
- OpenCV
- MediaPipe
- NumPy
- 其他相依套件（詳見 requirements.txt）

## 安裝方式

1. 克隆此專案到本地：
```bash
git clone [專案網址]
```

2. 安裝所需套件：
```bash
pip install -r requirements.txt
```

## 使用方式

1. 執行主程式：
```bash
python main.py
```

2. 操作步驟：
   - 程式啟動後，使用滑鼠拖曳選擇要錄製的螢幕區域
   - 按下 Enter 鍵確認選擇區域
   - 使用空白鍵開始/暫停錄製
   - 按 'r' 鍵可重新選擇擷取區域
   - 按 'q' 鍵退出程式並儲存影片

3. 輸出檔案：
   - 錄製的影片將儲存在 `pose_track_videos` 資料夾中
   - 每個錄製會產生兩個檔案：
     - 原始影像（包含骨架顯示）
     - 純骨架追蹤影像

## 專案結構

- `main.py`：主程式入口
- `config.py`：設定檔
- `video_recorder.py`：影片錄製模組
- `screen_capture.py`：螢幕擷取模組
- `pose_detector.py`：姿勢偵測模組
- `hand_detector.py`：手部偵測模組
- `ui_controls.py`：使用者介面控制
- `utils.py`：工具函數

## 注意事項

- 確保系統有足夠的運算效能以進行即時姿勢追蹤
- 建議使用高解析度螢幕以獲得更好的追蹤效果
- 錄製的影片檔案可能較大，請確保有足夠的儲存空間

## 授權說明

本專案採用 MIT 授權條款。詳見 LICENSE 檔案。

## 貢獻指南

歡迎提交 Issue 和 Pull Request 來協助改進此專案。
