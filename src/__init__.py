__all__ = ["core", "browser", "parser", "settings", "text_color"]

from src.settings import DEBUG_PHRASES
from src.text_color import print_debug_text

print_debug_text(DEBUG_PHRASES['__init__']+__name__)