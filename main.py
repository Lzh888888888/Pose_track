import cv2
import numpy as np
from hand_detector import HandDetector
from pose_detector import PoseDetector
from screen_capture import ScreenCapture
from video_recorder import VideoRecorder
from ui_controls import UIControls
from config import ensure_video_path

def main():
    # 初始化檢測器和螢幕擷取
    screen_capture = ScreenCapture()
    hand_detector = HandDetector()
    pose_detector = PoseDetector()
    ui_controls = UIControls()
    
    # 設定影片儲存路徑
    save_path = ensure_video_path()
    video_recorder = VideoRecorder(save_path)
    
    # 讓使用者選擇擷取區域
    print("請選擇要擷取的螢幕區域...")
    if not screen_capture.select_region():
        print("未選擇區域，將擷取全螢幕")
    
    # 取得第一幀來設定影片參數
    first_frame = screen_capture.capture_screen()
    if first_frame is None:
        print("無法擷取螢幕畫面")
        return
        
    frame_size = (first_frame.shape[1], first_frame.shape[0])
    fps = 13
    
    print("\n操作說明:")
    print("- 按空白鍵開始/暫停錄製")
    print("- 按 'r' 重新選擇擷取區域")
    print("- 按 'q' 退出程式並儲存影片")
    print(f"\n影片將儲存在: {save_path}")
    
    try:
        while True:
            # 擷取螢幕畫面
            frame = screen_capture.capture_screen()
            if frame is None:
                print("無法擷取螢幕畫面")
                continue
                
            original_frame = frame.copy()
            
            # 進行手部和姿態檢測
            hand_results = hand_detector.process_frame(frame)
            pose_results = pose_detector.process_frame(frame)
            
            # 在原始影像上繪製
            hand_detector.draw_landmarks(original_frame, hand_results)
            pose_detector.draw_landmarks(original_frame, pose_results)
            
            # 在黑色背景上繪製骨架
            skeleton_frame = np.zeros(frame.shape, dtype=np.uint8)
            hand_detector.draw_landmarks(skeleton_frame, hand_results, draw_on_black=True)
            pose_detector.draw_landmarks(skeleton_frame, pose_results, draw_on_black=True)
            
            # 如果正在錄製，寫入影片
            if ui_controls.is_recording:
                if video_recorder.start_recording(frame_size, fps):
                    print("開始錄製影片")
                video_recorder.write_frames(original_frame, skeleton_frame)
            
            # 調整顯示視窗大小
            display_width = 600
            aspect_ratio = frame.shape[1] / frame.shape[0]
            display_height = int(display_width / aspect_ratio)
            
            display_original = cv2.resize(original_frame, (display_width, display_height))
            display_skeleton = cv2.resize(skeleton_frame, (display_width, display_height))
            
            # 在顯示畫面上添加控制介面
            display_original = ui_controls.draw_controls(display_original)
            display_skeleton = ui_controls.draw_controls(display_skeleton)
            
            # 顯示結果
            cv2.imshow("Original Detection", display_original)
            cv2.imshow("Skeleton View", display_skeleton)
            
            # 按鍵處理
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break
            elif key == ord('r'):
                if not screen_capture.select_region():
                    print("未選擇區域，將擷取全螢幕")
                    screen_capture.region = None
            elif key == ord(' '):  # 空白鍵
                is_recording = ui_controls.toggle_recording()
                status = "開始" if is_recording else "暫停"
                print(f"錄製{status}")
    
    except Exception as e:
        print(f"執行時發生錯誤: {str(e)}")
    
    finally:
        # 釋放資源
        video_recorder.release()
        cv2.destroyAllWindows()
        
        # 只有在有實際錄影時才顯示儲存訊息
        original_path, skeleton_path = video_recorder.get_recording_paths()
        if original_path and skeleton_path:
            print(f"\n錄製完成！")
            print(f"原始影片已儲存至: {original_path}")
            print(f"骨架影片已儲存至: {skeleton_path}")
        else:
            print("\n未進行任何錄製")

if __name__ == "__main__":
    main()