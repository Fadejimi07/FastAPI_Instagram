from fastapi import UploadFile
import os
import uuid


def save_image(file: UploadFile):
    try:
        os.makedirs("images", exist_ok=True)  # Ensure the directory exists

        _, ext = os.path.splitext(str(file.filename))
        unique_filename = f"{uuid.uuid4()}{ext}"

        contents = file.file.read()
        with open(f"images/{unique_filename}", "wb") as f:
            f.write(contents)
        return os.path.join("images", unique_filename)
    except Exception as e:
        print(e)
        return None
