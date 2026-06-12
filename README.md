# Face Recognition Access Control

Bachelor thesis project that compares a reference face image with a test image and marks the result as access granted or access denied.

The project uses `face_recognition`, OpenCV and Pillow to:

- detect faces in two images
- compare face embeddings
- calculate face distance
- draw the result on the test image
- save a visual output image
- write a simple access log

## Project Structure

```text
FaceRecognitionProject/
  images/
    known_face.jpg
    test_face.jpg
  main.py
screenshots/
  access_granted.jpg
  access_denied.jpg
face_compare_visual.py
requirements.txt
run_face_comparison.bat
```

## Screenshots

Access granted example:

![Access granted example](screenshots/access_granted.jpg)

Access denied example:

![Access denied example](screenshots/access_denied.jpg)

## Setup

Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Note: the `face_recognition` package depends on `dlib`, which may require C++ build tools on Windows.

## Usage

Run the image comparison:

```bash
python FaceRecognitionProject/main.py
```

Show the result in an OpenCV window:

```bash
python FaceRecognitionProject/main.py --show
```

Use custom images:

```bash
python FaceRecognitionProject/main.py --known path/to/reference.jpg --test path/to/person.jpg
```

Run the webcam demo:

```bash
python face_compare_visual.py
```

Press `q` to close the webcam window.

## Output

By default, the program writes:

- result image: `FaceRecognitionProject/output/result.jpg`
- log file: `FaceRecognitionProject/log/access_log.txt`

Both folders are ignored by Git because they are generated runtime artifacts.

## Privacy Note

Do not commit private face images without permission. For a public portfolio repository, use demo images that are either your own or licensed for public use.
