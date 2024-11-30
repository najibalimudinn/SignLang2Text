from utils.videoToImg import extract_frames
from utils.dataAugmentation import augment_sequence, resize_image
from tqdm import tqdm
import cv2
import os

video_dir = 'datasets/videos'
output_dir = 'datasets/frames'
frame_rate = 10

video_files = [f for f in os.listdir(video_dir) if f.endswith(('.mp4', '.webm', '.avi'))]

for video in tqdm(video_files, desc="Extracting frames"):
    video_path = os.path.join(video_dir, video)
    extract_frames(video_path, output_dir, frame_rate)

frame_dirs = [f for f in os.listdir(output_dir) if os.path.isdir(os.path.join(output_dir, f))]

for frame_dir in tqdm(frame_dirs, desc="Resizing frame"):
    sequence_dir = os.path.join(output_dir, frame_dir)
    files = [f for f in os.listdir(sequence_dir) if f.endswith('.jpg')]
    for file in files:
        img = cv2.imread(os.path.join(sequence_dir, file))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = resize_image(img)
        cv2.imwrite(os.path.join(sequence_dir, file), cv2.cvtColor(img, cv2.COLOR_RGB2BGR))

for frame_dir in tqdm(frame_dirs, desc="Augmenting data"):
    sequence_dir = os.path.join(output_dir, frame_dir)
    augment_sequence(sequence_dir, sequence_dir)