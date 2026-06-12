from __future__ import annotations

from pathlib import Path

import cv2
import face_recognition


PROJECT_DIR = Path(__file__).resolve().parent
KNOWN_FACE_PATH = PROJECT_DIR / "FaceRecognitionProject" / "images" / "known_face.jpg"


def main() -> None:
    known_image = face_recognition.load_image_file(str(KNOWN_FACE_PATH))
    known_encodings = face_recognition.face_encodings(known_image)

    if not known_encodings:
        raise ValueError(f"No face found in reference image: {KNOWN_FACE_PATH}")

    known_encoding = known_encodings[0]
    video_capture = cv2.VideoCapture(0)

    if not video_capture.isOpened():
        raise RuntimeError("Could not open webcam.")

    while True:
        ret, frame = video_capture.read()
        if not ret:
            break

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            is_match = face_recognition.compare_faces([known_encoding], face_encoding, tolerance=0.6)[0]
            label = "Access granted" if is_match else "Access denied"
            color = (0, 255, 0) if is_match else (0, 0, 255)

            cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
            cv2.putText(frame, label, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

        cv2.imshow("Webcam Face Recognition", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    video_capture.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
