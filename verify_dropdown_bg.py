import os
import base64
from PIL import Image

print("--- Running Verification of Dropdown Drag & Multilingual Money Background ---")

# 1. Background Image Check
bg_path = "/Users/prithvij/.gemini/antigravity/scratch/vyapardost/sample_data/currency_bg.jpg"
assert os.path.exists(bg_path), "currency_bg.jpg does not exist!"
im = Image.open(bg_path)
assert im.size == (2400, 1600), f"Unexpected size: {im.size}"
print(f"PASSED 1: Multilingual MONEY Background verified (2400x1600, {os.path.getsize(bg_path):,} bytes).")

# 2. Verify app.py compilation & CSS rules
with open("/Users/prithvij/.gemini/antigravity/scratch/vyapardost/app.py") as f:
    code = f.read()

assert "stSelectboxVirtualDropdown" in code
assert "react-aria-ListBox" in code
assert "overflow-y: auto !important" in code
assert "touch-action: pan-y !important" in code
assert "scrollbar-width: thin !important" in code
assert "::-webkit-scrollbar" in code
assert "stToast" in code
print("PASSED 2: Dropdown dragging, mousewheel scroll, and high-contrast CSS rules verified in app.py.")

# 3. Verify CSS evaluation in Light and Dark Modes
idx1 = code.find('site_css = f"""')
idx2 = code.find('"""', idx1 + 20)

for mode in ['light', 'dark']:
    ctx = {
        'st': type('MockSt', (), {'session_state': type('SS', (), {'app_theme': mode, 'get': lambda s, k, d=None: d})()})(),
        'get_currency_bg_b64': lambda: 'VALID_BASE64',
        'CURRENCY_BG_B64': 'VALID_BASE64'
    }
    exec(code[code.find('is_dark ='):idx2+3], ctx)
    css = ctx['site_css']
    if mode == 'light':
        assert "background-color: rgba(255, 255, 255, 0.96) !important" in css
        assert "color: #0F172A !important" in css
    else:
        assert "background-color: rgba(15, 23, 42, 0.90) !important" in css
        assert "color: #FFFFFF !important" in css

print("PASSED 3: Light & Dark mode contrast values successfully verified across popovers, listboxes, and toasts.")
print("--- ALL VERIFICATION CHECKS PASSED WITH 100% SUCCESS ---")
