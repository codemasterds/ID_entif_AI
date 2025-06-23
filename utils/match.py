from deepface import DeepFace
import os
def compare_faces(live_face, id_face):
    """
    Compare two face images using DeepFace and return match result.

    Args:
        face1_path (str): Path to first face image
        face2_path (str): Path to second face image

    Returns:
        (bool, float): (Match result, distance score)
    """ 
    try:
        if not os.path.exists(live_face) or not os.path.exists(id_face):
            print("❌ One or both face files not found.")
            return False, None
        result= DeepFace.verify(live_face, id_face, enforce_detection=False, model_name="ArcFace")
        return result["verified"], result["distance"]
    except Exception as err:
        print("❌ DeepFace Error:", err)
        return  False, None