import cv2
import numpy as np
import pyautogui
from typing import Tuple, Optional

class ScreenCapture:
    def __init__(self):
        # 獲取螢幕解析度
        self.screen_width, self.screen_height = pyautogui.size()
        self.region: Optional[Tuple[int, int, int, int]] = None
        
    def select_region(self):
        """讓使用者選擇要擷取的螢幕區域"""
        # 先擷取一次完整螢幕作為背景
        full_screen = self.capture_screen()
        
        # 創建視窗和回調函數
        window_name = "選擇擷取區域 (拖曳滑鼠選擇區域，按Enter確認，按c取消)"
        cv2.namedWindow(window_name)
        
        # 調整顯示大小
        display_width = 1280
        aspect_ratio = full_screen.shape[1] / full_screen.shape[0]
        display_height = int(display_width / aspect_ratio)
        display_screen = cv2.resize(full_screen, (display_width, display_height))
        
        # 使用ROI選擇
        roi = cv2.selectROI(window_name, display_screen, False)
        cv2.destroyWindow(window_name)
        
        if roi[2] and roi[3]:  # 確認是否有選擇區域
            # 轉換回原始螢幕座標
            scale_x = self.screen_width / display_width
            scale_y = self.screen_height / display_height
            
            x = int(roi[0] * scale_x)
            y = int(roi[1] * scale_y)
            w = int(roi[2] * scale_x)
            h = int(roi[3] * scale_y)
            
            self.region = (x, y, w, h)
            return True
        return False
        
    def capture_screen(self):
        """擷取螢幕畫面並轉換為OpenCV格式"""
        if self.region:
            # 擷取指定區域
            x, y, w, h = self.region
            screenshot = pyautogui.screenshot(region=(x, y, w, h))
        else:
            # 擷取全螢幕
            screenshot = pyautogui.screenshot()
        
        # 將PIL圖像轉換為numpy陣列
        frame = np.array(screenshot)
        
        # 將RGB轉換為BGR (OpenCV格式)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        
        return frame