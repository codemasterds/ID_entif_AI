from mtcnn.mtcnn import MTCNN
import cv2

detector= MTCNN()

def detect_faces(frame, draw=False):
    
    """
    Detect faces in a frame and return their cropped versions and positions.

    Args:
        frame (np.array): BGR image frame from webcam
        draw (bool): Whether to draw bounding boxes on frame

    Returns:
        cropped_faces (List[np.array]): List of cropped face images (RGB)
        frame_with_boxes (np.array): Original frame with boxes (if draw=True)
    """
    # Convert to RGB for MTCNN
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    detections = detector.detect_faces(rgb_frame)
    cropped_faces = []

    for face in detections:
        x, y, w, h = face['box']
        x, y = max(0, x), max(0, y)
        face_crop = rgb_frame[y:y+h, x:x+w]
        resized = cv2.resize(face_crop, (224, 224))
        cropped_faces.append(resized)

        if draw:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    return cropped_faces, frame
