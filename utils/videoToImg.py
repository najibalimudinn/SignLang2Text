'''Code modified from https://medium.com/@wayandadangunsri/converting-video-to-images-using-python-and-opencv-72b2ea66a692'''

import cv2
import os

# Function to extract frames from a video until reaching the desired frame count
def extract_frames(video_path, output_directory, frame_rate=2): # Desired frame rate (1 frame every 0.5 seconds)
    cap = cv2.VideoCapture(video_path)
    
    frame_count = 0
    i = 0
    
    # Get the video file's name without extension
    video_name = os.path.splitext(os.path.basename(video_path))[0]
    
    # Create an output folder with a name corresponding to the video
    output_directory = f"{output_directory}/{video_name}"
    os.makedirs(output_directory, exist_ok=True)
    
    while True:
        ret, frame = cap.read()
        
        if not ret:
            break
        
        frame_count += 1
        
        # Only extract frames at the desired frame rate
        if frame_count % int(cap.get(5) / frame_rate) == 0:
            i += 1 
            output_file = f"{output_directory}/{i}.jpg"
            cv2.imwrite(output_file, frame)
    
    cap.release()
    cv2.destroyAllWindows()