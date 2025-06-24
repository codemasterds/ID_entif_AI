from utils.match import compare_faces

v, d = compare_faces(r"S:\python projects\Id_entif_AI\id_face.jpg", r"S:\python projects\Id_entif_AI\live_face.jpg")
print("Result:", v, d)
