import cv2
import os
from datetime import datetime

class VideoRecorder:
    def __init__(self, save_path):
        """
        初始化影片錄製器
        
        Args:
            save_path (str): 影片儲存路徑
        """
        self.save_path = save_path
        self.ensure_save_path()
        self.original_writer = None
        self.skeleton_writer = None
        self.original_path = None
        self.skeleton_path = None
        
    def ensure_save_path(self):
        """確保儲存路徑存在"""
        if not os.path.exists(self.save_path):
            os.makedirs(self.save_path, exist_ok=True)
            
    def create_video_filename(self, prefix):
        """建立帶有時間戳記的影片檔名"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'{prefix}_{timestamp}.mp4'
        return os.path.join(self.save_path, filename)
        
    def start_recording(self, frame_size, fps):
        """開始錄影，初始化影片寫入器"""
        if self.original_writer is None and self.skeleton_writer is None:
            self.original_path = self.create_video_filename('original')
            self.skeleton_path = self.create_video_filename('skeleton')
            
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            self.original_writer = cv2.VideoWriter(self.original_path, fourcc, fps, frame_size)
            self.skeleton_writer = cv2.VideoWriter(self.skeleton_path, fourcc, fps, frame_size)
            
            return True
        return False
        
    def write_frames(self, original_frame, skeleton_frame):
        """寫入原始和骨架影格"""
        if self.original_writer and self.skeleton_writer:
            self.original_writer.write(original_frame)
            self.skeleton_writer.write(skeleton_frame)
            return True
        return False
            
    def release(self):
        """釋放影片寫入器資源"""
        if self.original_writer:
            self.original_writer.release()
        if self.skeleton_writer:
            self.skeleton_writer.release()
            
    def get_recording_paths(self):
        """取得錄影檔案路徑"""
        return self.original_path, self.skeleton_path