
import cv2
import numpy as np
import os
import glob
import json

def cv_imread(file_path):
    cv_img = cv2.imdecode(np.fromfile(file_path, dtype=np.uint8), -1)
    return cv_img

def load_config(config_path='config.json'):
    with open(config_path, 'r') as config_file:
        return json.load(config_file)

def add_white_sticker_effect(image_path, output_path, config):
    # 使用cv_imread讀取圖片，以處理中文路徑
    image = cv_imread(image_path)
    if image is None:
        print(f"無法讀取圖片: {image_path}")
        return

    # 找到非透明區域的輪廓
    alpha_channel = image[:, :, 3]
    _, thresh = cv2.threshold(alpha_channel, 0, 255, cv2.THRESH_BINARY)
    
    # 使用膨脹使輪廓稍微擴大
    kernel_size = tuple(config['dilation_kernel_size'])
    kernel = np.ones(kernel_size, np.uint8)
    dilated_thresh = cv2.dilate(thresh, kernel, iterations=config['dilation_iterations'])
    
    contours, _ = cv2.findContours(dilated_thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # 對每個輪廓進行平滑處理並繪製圓滑的白色邊框
    for cnt in contours:
        # 對輪廓點進行多邊形近似，使邊緣更平滑
        epsilon = config['epsilon_factor'] * cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, epsilon, True)
        
        # 繪製圓滑的白色邊框
        cv2.drawContours(image, [approx], -1, (255, 255, 255, 255), thickness=config['border_thickness'])

    # 保存圖片
    cv2.imencode('.png', image)[1].tofile(output_path)

# Load configuration settings
config = load_config()

# 使用相對路徑指定輸入和輸出資料夾
input_dir = "./input"
output_dir = "./output"

# 確保輸出資料夾存在
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 獲取當前工作目錄的完整路徑
current_dir = os.getcwd()

# 處理輸入資料夾中的每張圖片
for image_file in glob.glob(os.path.join(current_dir, input_dir, "*.png")):
    image_name = os.path.basename(image_file)
    print(image_name)
    output_file = os.path.join(current_dir, output_dir, image_name)
    add_white_sticker_effect(image_file, output_file, config)
