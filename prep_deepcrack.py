import cv2 
import os
import argparse

from glob import glob

def parse_args():
    parser = argparse.ArgumentParser(description='Convert Deep Crack Dataset')
    parser.add_argument('--path', help='path to the dataset')
    args = parser.parse_args()
    return args

def convert_label(labels):
    """
    Args:
        labels: list of paths to the labels
        
    Returns:
        None
    """
    
    for label_path in labels:
        
        label = cv2.imread(label_path, cv2.IMREAD_UNCHANGED)
        label[label == 255] = 1
        
        label_folder, label_name = os.path.split(label_path)
        label_name = label_name.replace('.png', '_binary_label.png')
        label_name = os.path.join(label_folder, label_name)      
        
        cv2.imwrite(label_name, label)


def main():
    args = parse_args()
    
    data_path = args.path
    
    train_labels = glob(os.path.join(data_path, 'train_lab', '*.png'))
    test_labels = glob(os.path.join(data_path, 'test_lab', '*.png'))
    
    convert_label(train_labels)
    convert_label(test_labels)
    

if __name__ == '__main__':
    main()

