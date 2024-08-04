import os
import shutil
import random

def split_data(root_dir, train_ratio=0.8, seed=42):
    # Set random seed for reproducibility
    random.seed(seed)

    # Define paths for images and labels
    images_dir = os.path.join(root_dir, 'images', 'train2017')
    labels_dir = os.path.join(root_dir, 'labels', 'train2017')

    # Create directories for training and validation
    train_images_dir = os.path.join(root_dir, 'train', 'images', 'train2017')
    train_labels_dir = os.path.join(root_dir, 'train', 'labels', 'train2017')
    val_images_dir = os.path.join(root_dir, 'val', 'images', 'train2017')
    val_labels_dir = os.path.join(root_dir, 'val', 'labels', 'train2017')

    # Create directories if they don't exist
    for directory in [train_images_dir, train_labels_dir, val_images_dir, val_labels_dir]:
        os.makedirs(directory, exist_ok=True)

    # Get the list of all image and label files
    image_files = os.listdir(images_dir)
    label_files = os.listdir(labels_dir)

    # Shuffle the file lists
    random.shuffle(image_files)
    random.shuffle(label_files)

    # Calculate the split indices
    num_train = int(len(image_files) * train_ratio)

    # Copy training data
    for img_file, lbl_file in zip(image_files[:num_train], label_files[:num_train]):
        shutil.copy(os.path.join(images_dir, img_file), os.path.join(train_images_dir, img_file))
        shutil.copy(os.path.join(labels_dir, lbl_file), os.path.join(train_labels_dir, lbl_file))

    # Copy validation data
    for img_file, lbl_file in zip(image_files[num_train:], label_files[num_train:]):
        shutil.copy(os.path.join(images_dir, img_file), os.path.join(val_images_dir, img_file))
        shutil.copy(os.path.join(labels_dir, lbl_file), os.path.join(val_labels_dir, lbl_file))

# Example usage
root_directory = 'Dataset'
split_data(root_directory)
