import pickle
import os

def save_known_encodings(known_face_names, known_face_encodings):
    with open("known_encodings.pickle", "wb") as f:
        pickle.dump((known_face_names, known_face_encodings), f)

def load_known_encodings():
    if os.path.exists("known_encodings.pickle"):
        with open("known_encodings.pickle", "rb") as f:
            return pickle.load(f)
    else:
        return [], []
