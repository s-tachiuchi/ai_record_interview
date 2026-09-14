"""AI面接官アバターの定義

SVG は app/templates/interview/avatars/<key>.svg に置く。
各 SVG には以下を含めること:
  - id="av-mouth" の <path>  … data-closed / data-open に口の閉じた形・開いた形の d 属性
  - class="av-eye" の要素     … まばたきアニメーション対象
"""

AVATARS = [
    {"key": "robot",  "label": "ロボット"},
    {"key": "female", "label": "女性"},
    {"key": "male",   "label": "男性"},
]

AVATAR_KEYS = [a["key"] for a in AVATARS]
DEFAULT_AVATAR = "robot"


def normalize_avatar_key(value) -> str:
    return value if value in AVATAR_KEYS else DEFAULT_AVATAR
