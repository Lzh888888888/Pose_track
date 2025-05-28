# 姿勢追蹤與影像分析工具

這是一個基於 Python 開發的人體姿勢追蹤與分析工具，提供影片分析和即時螢幕錄影兩種操作模式。使用 OpenCV 和 MediaPipe 技術實現即時姿勢追蹤。

## 功能特點

- 雙模式操作：
  - 模式一 (mode1.py)：影片檔案分析
  - 模式二 (mode2.py)：即時螢幕錄影
- 完整骨架追蹤：支援人體姿勢追蹤與分析
- 雙視圖顯示：同時呈現原始畫面和純骨架視圖
- 自動存檔功能：自動產生原始和骨架追蹤影片

## 系統需求

- Python 3.7+
- OpenCV
- MediaPipe
- NumPy
- tkinter（用於檔案選擇介面）

## 安裝方式

1. 克隆專案：
```bash
git clone https://github.com/Lzh888888888/Pose_track.git
```

2. 安裝相依套件：
```bash
pip install opencv-python mediapipe numpy
```

## 使用說明

### 模式一：影片檔案分析
執行指令：
```bash
python mode1.py
```

功能流程：
1. 自動開啟檔案選擇視窗
2. 選擇要分析的影片檔案（支援 .mp4/.avi/.mov）
3. 自動處理並即時顯示：
   - 左側：原始影片+姿勢骨架標記
   - 右側：純骨架視圖
4. 按 'q' 結束分析並儲存結果

### 模式二：即時螢幕錄影
執行指令：
```bash
python mode2.py
```

操作方式：
1. 使用滑鼠框選要錄製的螢幕區域
2. 快捷鍵操作：
   - 空白鍵：開始/暫停錄製
   - 'r'：重新選擇錄製區域
   - 'q'：結束錄製並儲存

## 輸出說明

所有處理結果會自動儲存在 `pose_track_videos` 資料夾：
- 原始影片：`original_時間戳記.mp4`
- 骨架視圖：`skeleton_時間戳記.mp4`

## 主要檔案說明

- `mode1.py`：影片分析模式主程式
- `mode2.py`：螢幕錄影模式主程式
- `pose_detector.py`：人體姿勢追蹤模組
- `video_recorder.py`：影片錄製處理模組
- `screen_capture.py`：螢幕擷取模組
- `ui_controls.py`：使用者介面控制
- `config.py`：基礎設定檔

## 效能最佳化建議

- 建議使用效能較好的顯示卡
- 螢幕錄影時，選擇較小的區域可提升效能
- 影片分析時，可考慮降低輸入影片解析度

## 演示效果

以下演示影片使用本工具進行姿勢追蹤分析：

### 原始效果影片
[![姿勢追蹤演示](https://img.youtube.com/vi/Sk0zEGuRKkE/0.jpg)](https://youtube.com/shorts/Sk0zEGuRKkE)

### 程式處理效果
#### 原始影片追蹤效果
![原始影片追蹤效果](Demo/original_demo.mp4)

#### 純骨架視圖效果
![純骨架視圖效果](Demo/skeleton_demo.mp4)

> **備註**：
> - 演示影片來源：[YouTube Short - Dance Video](https://youtube.com/shorts/Sk0zEGuRKkE)
> - 使用本工具分析處理後可產生原始追蹤和骨架視圖兩種效果

## 授權說明

本專案採用 MIT 授權條款。

## 問題回報

如有任何問題或建議，歡迎提交 Issue。