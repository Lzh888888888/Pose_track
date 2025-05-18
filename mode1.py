import cv2
import numpy as np
from pose_detector import PoseDetector
from video_recorder import VideoRecorder
from config import ensure_video_path
from tkinter import filedialog
import tkinter as tk

def select_video_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="選擇要分析的影片",
        filetypes=[("Video files", "*.mp4 *.avi *.mov")]
    )
    return file_path

def main():
    # 初始化檢測器
    pose_detector = PoseDetector()
    
    # 選擇輸入影片
    input_video_path = select_video_file()
    if not input_video_path:
        print("未選擇影片檔案")
        return
        
    # 開啟影片檔案
    video_cap = cv2.VideoCapture(input_video_path)
    if not video_cap.isOpened():
        print("無法開啟影片檔案")
        return
    
    # 獲取影片參數
    frame_size = (int(video_cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
                 int(video_cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    fps = video_cap.get(cv2.CAP_PROP_FPS)
    
    # 取得影片總幀數
    total_frames = int(video_cap.get(cv2.CAP_PROP_FRAME_COUNT))
    current_frame = 0
    
    # 設定影片儲存路徑
    save_path = ensure_video_path()
    video_recorder = VideoRecorder(save_path)
    # 直接開始錄製
    video_recorder.start_recording(frame_size, fps)
    print("開始錄製影片")
    
    print("\n操作說明:")
    print("- 按 'q' 退出程式並儲存影片")
    print(f"\n影片將儲存在: {save_path}")
    
    try:
        while True:
            # 讀取影片幀
            ret, frame = video_cap.read()
            if not ret:
                print("影片讀取完畢")
                break
            
            current_frame += 1
            progress = (current_frame / total_frames) * 100
            
            # 更新視窗標題以顯示進度
            cv2.setWindowTitle("Original Detection", f"Analysis Progress: {progress:.1f}%")
            cv2.setWindowTitle("Skeleton View", f"Analysis Progress: {progress:.1f}%")
            
            # 每隔 50 幀顯示進度
            if current_frame % 50 == 0:
                print(f"Processing Progress: {progress:.1f}%")
                
            original_frame = frame.copy()
            
            # 進行姿態檢測
            pose_results = pose_detector.process_frame(frame)
            
            # 在原始影像上繪製
            pose_detector.draw_landmarks(original_frame, pose_results)
            
            # 在黑色背景上繪製骨架
            skeleton_frame = np.zeros(frame.shape, dtype=np.uint8)
            pose_detector.draw_landmarks(skeleton_frame, pose_results, draw_on_black=True)
            
            # 直接寫入影片
            video_recorder.write_frames(original_frame, skeleton_frame)
            
            # 調整顯示視窗大小
            display_width = 600
            aspect_ratio = frame.shape[1] / frame.shape[0]
            display_height = int(display_width / aspect_ratio)
            
            display_original = cv2.resize(original_frame, (display_width, display_height))
            display_skeleton = cv2.resize(skeleton_frame, (display_width, display_height))
            
            # 顯示結果
            cv2.imshow("Original Detection", display_original)
            cv2.imshow("Skeleton View", display_skeleton)
            
            # 按鍵處理
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break
    
    except Exception as e:
        print(f"執行時發生錯誤: {str(e)}")
    
    finally:
        # 釋放資源
        video_cap.release()
        video_recorder.release()
        cv2.destroyAllWindows()
        
        # 顯示儲存訊息
        original_path, skeleton_path = video_recorder.get_recording_paths()
        print(f"\n錄製完成！")
        print(f"原始影片已儲存至: {original_path}")
        print(f"骨架影片已儲存至: {skeleton_path}")

if __name__ == "__main__":
    main()
