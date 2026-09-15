"""AI面接官アバターの定義

表示方法は 2 通りあり、画像ファイルがあればそちらを優先する。

1. 画像: app/static/avatars/<key>.(png|jpg|jpeg|webp)
     - <key>_open.(png|...) があれば読み上げ中に口の開閉として切り替える
2. SVG:  app/templates/interview/avatars/<key>.svg（画像が無い場合のフォールバック）
     - id="av-mouth" の <path>  … data-closed / data-open に口の閉じた形・開いた形の d 属性
     - class="av-eye" の要素     … まばたきアニメーション対象
"""
import os

AVATARS = [
    {"key": "robot",  "label": "ロボット"},
    {"key": "female", "label": "女性"},
    {"key": "male",   "label": "男性"},
]

AVATAR_KEYS = [a["key"] for a in AVATARS]
DEFAULT_AVATAR = "robot"

AVATAR_IMAGE_DIR = os.path.join(os.path.dirname(__file__), "static", "avatars")
IMAGE_EXTS = ("png", "jpg", "jpeg", "webp")


def normalize_avatar_key(value) -> str:
    return value if value in AVATAR_KEYS else DEFAULT_AVATAR


def _find_image(basename: str):
    """static/avatars 内の画像を探し、あれば URL（更新時刻付き）を返す"""
    for ext in IMAGE_EXTS:
        path = os.path.join(AVATAR_IMAGE_DIR, f"{basename}.{ext}")
        if os.path.isfile(path):
            return f"/static/avatars/{basename}.{ext}?v={int(os.path.getmtime(path))}"
    return None


def avatar_assets(key) -> dict:
    """テンプレートから使う。画像があれば image、無ければ svg を返す"""
    key = normalize_avatar_key(key)
    closed = _find_image(key)
    if closed:
        return {"key": key, "type": "image", "src": closed, "src_open": _find_image(f"{key}_open")}
    return {"key": key, "type": "svg", "template": f"interview/avatars/{key}.svg"}
