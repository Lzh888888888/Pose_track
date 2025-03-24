import os

# 影片儲存路徑設定
VIDEO_SAVE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pose_track_videos")

# 確保影片儲存路徑存在
def ensure_video_path():
    if not os.path.exists(VIDEO_SAVE_PATH):
        os.makedirs(VIDEO_SAVE_PATH, exist_ok=True)
    return VIDEO_SAVE_PATH