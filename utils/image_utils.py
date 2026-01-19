from fastapi.responses import FileResponse
import os



def get_image(path: str):
    """
    保存されている画像を取得する関数
    """
    if not os.path.exists(path):
        raise FileNotFoundError("Image not found")
    return FileResponse(path)