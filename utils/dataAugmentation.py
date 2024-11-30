import os
import cv2
import numpy as np

def resize_image(img, target_height=224):
    h, w = img.shape[:2]
    aspect_ratio = w / h
    target_width = int(target_height * aspect_ratio)
    return cv2.resize(img, (target_width, target_height))

def flip_image(img):
    return cv2.flip(img, 1)

def rotate_image(img, angle):
    (h, w) = img.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    return cv2.warpAffine(img, M, (w, h))

def blur_image(img, ksize=(5, 5)):
    return cv2.GaussianBlur(img, ksize, 0)

def add_noise(img):
    noise = np.random.normal(0, 25, img.shape).astype(np.uint8)
    return cv2.add(img, noise)

def augment_sequence(sequence_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    
    files = sorted([f for f in os.listdir(sequence_dir) if f.endswith('.jpg')])
    
    augmentations = [flip_image, rotate_image, blur_image, add_noise]
    
    for aug in augmentations:
        if aug == rotate_image:
            angle = np.random.randint(0, 360)
        
        for file in files:
            img = cv2.imread(os.path.join(sequence_dir, file))
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            
            if aug == rotate_image:
                augmented_img = aug(img, angle)
            else:
                augmented_img = aug(img)
            
            filename = f"{os.path.splitext(file)[0]}_{aug.__name__}.jpg"
            output_file = os.path.join(output_dir, filename)
            cv2.imwrite(output_file, cv2.cvtColor(augmented_img, cv2.COLOR_RGB2BGR))