import tensorflow as tf
import numpy as np
import cv2

# Load the object detection model
model = tf.saved_model.load('path/to/saved_model')

# Define the input and output tensor names
input_name = 'image_tensor:0'
output_names = ['detection_boxes:0', 'detection_classes:0',
                'detection_scores:0', 'num_detections:0']

# Load the image
image = cv2.imread('path/to/image')

# Resize the image
image = cv2.resize(image, (300, 300))

# Convert the image to a numpy array
image = np.array(image)

# Add a new dimension to the image
image = np.expand_dims(image, axis=0)

# Perform object detection
detections = model(image)

# Get the detection results
boxes = detections[output_names[0]][0]
classes = detections[output_names[1]][0]
scores = detections[output_names[2]][0]
num_detections = int(detections[output_names[3]])

# Set the threshold for the detection score
score_threshold = 0.5

# Loop through the detection results
for i in range(num_detections):
    # Check if the detection score is above the threshold
    if scores[i] > score_threshold:
        # Get the box coordinates
        ymin, xmin, ymax, xmax = tuple(boxes[i])
        # Draw a rectangle around the object
        cv2.rectangle(image, (int(xmin * image.shape[1]), int(ymin * image.shape[0])),
                      (int(xmax * image.shape[1]), int(ymax * image.shape[0])), (0, 255, 0), 2)
        # Label the object with its class and score
        cv2.putText(image, f'{classes[i]}: {scores[i]:.2f}',
                    (int(xmin * image.shape[1]),
                     int(ymin * image.shape[0]) - 5),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# Show the labeled image
cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
