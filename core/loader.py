from pathlib import Path

IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".bmp", ".gif"}


def load_images(folder: str) -> list[str]:
    path = Path(folder)

    if not path.exists() or not path.is_dir():
        return []

    images: list[str] = []

    for item in sorted(path.iterdir()):
        if item.is_file() and item.suffix.lower() in IMAGE_EXTENSIONS:
            images.append(str(item))

    images.sort()
    return images
