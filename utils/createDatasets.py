from videoToImg import extract_frames
from tqdm import tqdm
import os

video_dir = '../datasets/videos'
output_dir = '../datasets/frames'
frame_rate = 10

video_files = [f for f in os.listdir(video_dir) if f.endswith(('.mp4', '.webm', '.avi'))]

for video in tqdm(video_files, desc="Extracting frames"):
    video_path = os.path.join(video_dir, video)
    extract_frames(video_path, output_dir, frame_rate)