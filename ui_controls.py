import cv2
import numpy as np

class UIControls:
    def __init__(self):
        self.is_recording = False
        self.button_height = 50
        self.button_margin = 10
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.font_scale = 0.7
        self.text_thickness = 2
        
    def draw_controls(self, frame):
        """在影像上繪製控制按鈕和狀態"""
        height, width = frame.shape[:2]
        
        # 繪製半透明背景
        overlay = frame.copy()
        cv2.rectangle(overlay, (0, height - self.button_height), 
                     (width, height), (0, 0, 0), -1)
        cv2.addWeighted(overlay, 0.5, frame, 0.5, 0, frame)
        
        # 繪製錄製狀態
        status_text = "Recording" if self.is_recording else "Pause"
        status_color = (0, 0, 255) if self.is_recording else (255, 255, 255)
        cv2.putText(frame, status_text, 
                    (10, height - 15),
                    self.font, self.font_scale, status_color, self.text_thickness)
        
        # 繪製按鍵提示
        instructions = [
            ("Space: start/pause", (200, height - 15))
        ]
        
        for text, pos in instructions:
            cv2.putText(frame, text, pos, self.font, 
                       self.font_scale, (255, 255, 255), self.text_thickness)
        
        return frame
        
    def toggle_recording(self):
        """切換錄製狀態"""
        self.is_recording = not self.is_recording
        return self.is_recording