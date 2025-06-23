import numpy as np
import cv2 as cv
from utils.recognize import detect_faces
from utils.match import compare_faces

def main():
    cap = cv.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    print("✅ Press 'q' to quit.")
    while True:
    # Capture frame-by-frame
        ret, frame = cap.read()
    
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        
        faces, frame_with_boxes= detect_faces( frame, draw=True)

        key= cv.waitKey(1) & 0xFF
        # Show result
        cv.imshow("Live Face Detection", frame_with_boxes)

        if cv.waitKey(1) == ord('q'):
            break
        
        elif key== ord('c'):
            print(f"🖼 Detected {len(faces)} face(s)")
            if len(faces) != 2:
                print("❗️Please hold ID next to your face. Need exactly 2 faces.")
                continue
        
            live_path = r"live_face.jpg"
            id_path = r"id_face.jpg"
            cv.imwrite(live_path, cv.cvtColor(faces[0], cv.COLOR_RGB2BGR))
            cv.imwrite(id_path, cv.cvtColor(faces[1], cv.COLOR_RGB2BGR))
            print("Saved images")
            # Match
            print("🔍 Comparing faces...")
            verified, distance = compare_faces(live_path, id_path)    
            if verified:
                print(f"✅ MATCH (distance={distance:.4f})")
            else:
                print(f"❌ NO MATCH (distance={distance:.4f})")
    
    
    
    # When everything done, release the capture
    cap.release()
    cv.destroyAllWindows()
    
    
    
if __name__=="__main__":
    main()