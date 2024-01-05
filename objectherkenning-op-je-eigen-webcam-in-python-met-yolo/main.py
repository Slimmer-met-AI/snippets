# 1. Import modules 
#  - ultralytics, for object recognition
#  - cvs, for video capturing
#  - math, for rounding results from Yolo
from ultralytics import YOLO
import cv2
import math 

# 2. Create a video capture 1280 by 960 format
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 960)

# 3. Create a Yolo model - version 8
model = YOLO("yolo-Weights/yolov8n.pt")

# 4. Define all classes that Yolo can recognize
classNames = [
    "person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
    "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
    "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
    "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
    "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
    "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
    "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
    "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
    "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
    "teddy bear", "hair drier", "toothbrush"
]

# 5. Loop infinitely, so we never stop capturing and recognizing
while True:
    # 6. Capture video and process with Yolo model
    success, img = cap.read()
    results = model(img, stream=True)

    # 7. Loop over all processed video frames
    for r in results:
        boxes = r.boxes
        
        # 8. Loop over all detected objects' bounding boxes
        for box in boxes:
            # 9. Get bounding box coordinates
            x1, y1, x2, y2 = [int(value) for value in box.xyxy[0]]
            
            # 10. Draw rectangle on bounding box
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

            # 11. Get class name of object and draw into image, and also print to output
            className = classNames[int(box.cls[0])]
            cv2.putText(img, className, [x1, y1], cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
            print("Class name -->", className)
            
            # 12. Get confidence of found classs and print to output
            confidence = math.ceil((box.conf[0] * 100)) / 100
            print("Confidence --->", confidence)
    
    # 13. Show the altered image with detected objects 
    cv2.imshow('Webcam', img)
    if cv2.waitKey(1) == ord('q'):
        break

# 14. Cleanup capture windows
cap.release()
cv2.destroyAllWindows()