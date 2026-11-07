import os
from PIL import Image, ImageDraw, ImageFont

W, H = 2400, 1600
img = Image.new("RGB", (W, H), color="#FFFFFF")
draw = ImageDraw.Draw(img)

def get_font(path, size, idx=0):
    try:
        return ImageFont.truetype(path, size, index=idx)
    except Exception:
        try:
            return ImageFont.truetype(path, size)
        except Exception:
            return ImageFont.load_default()

# Typography Palette
F_HELV_ULTRALIGHT = lambda sz: get_font("/System/Library/Fonts/HelveticaNeue.ttc", sz, 5)
F_HELV_LIGHT      = lambda sz: get_font("/System/Library/Fonts/HelveticaNeue.ttc", sz, 0)
F_HELV_BOLD       = lambda sz: get_font("/System/Library/Fonts/HelveticaNeue.ttc", sz, 1)
F_FUTURA_MED      = lambda sz: get_font("/System/Library/Fonts/Supplemental/Futura.ttc", sz, 0)
F_FUTURA_BOLD     = lambda sz: get_font("/System/Library/Fonts/Supplemental/Futura.ttc", sz, 2)
F_FUTURA_COND     = lambda sz: get_font("/System/Library/Fonts/Supplemental/Futura.ttc", sz, 4)
F_ARIAL_BLACK     = lambda sz: get_font("/System/Library/Fonts/Supplemental/Arial Black.ttf", sz)
F_ARIAL_NARROW    = lambda sz: get_font("/System/Library/Fonts/Supplemental/Arial Narrow.ttf", sz)
F_ARIAL_NARROW_B  = lambda sz: get_font("/System/Library/Fonts/Supplemental/Arial Narrow Bold.ttf", sz)
F_IMPACT          = lambda sz: get_font("/System/Library/Fonts/Supplemental/Impact.ttf", sz)
F_UNICODE         = lambda sz: get_font("/Library/Fonts/Arial Unicode.ttf", sz)
F_DEVA_BOLD       = lambda sz: get_font("/System/Library/Fonts/Supplemental/DevanagariMT.ttc", sz, 1)
F_KAN_BOLD        = lambda sz: get_font("/System/Library/Fonts/Supplemental/Kannada Sangam MN.ttc", sz, 1)
F_TAM_BOLD        = lambda sz: get_font("/System/Library/Fonts/Supplemental/Tamil Sangam MN.ttc", sz, 1)
F_TEL_BOLD        = lambda sz: get_font("/System/Library/Fonts/Supplemental/Telugu Sangam MN.ttc", sz, 1)
F_ARABIC          = lambda sz: get_font("/System/Library/Fonts/GeezaPro.ttc", sz, 1)

# Exact balanced layout
items = [
    # Row 0: Top Bleed (y ~ -100 to 110)
    ("CURRENCY", F_FUTURA_BOLD, 290, 40, -110),
    ("Geld", F_HELV_LIGHT, 230, 1260, -90),
    ("деньги", F_ARIAL_BLACK, 250, 1680, -95),

    # Row 1: (y ~ 130 to 450)
    ("argent", F_HELV_LIGHT, 270, 30, 140),
    ("money", F_ARIAL_BLACK, 350, 580, 140),
    ("ಹಣ", F_KAN_BOLD, 360, 1440, 140),
    ("CASH", F_IMPACT, 330, 1850, 160),

    # Row 2: (y ~ 470 to 760)
    ("dinero", F_FUTURA_BOLD, 270, 30, 480),
    ("rokad", F_ARIAL_NARROW, 270, 680, 480),
    ("रुपया", F_DEVA_BOLD, 320, 1150, 450),
    ("dinheiro", F_HELV_LIGHT, 250, 1720, 500),

    # Row 3: (y ~ 770 to 1060)
    ("مال", F_ARABIC, 320, 50, 770),
    ("soldi", F_ARIAL_BLACK, 280, 680, 800),
    ("כסף", F_UNICODE, 270, 1260, 800),
    ("पैसा", F_DEVA_BOLD, 310, 1780, 770),

    # Row 4: (y ~ 1070 to 1360)
    ("₹", F_FUTURA_BOLD, 380, 40, 1070),
    ("お金", F_UNICODE, 250, 270, 1120),
    ("tiền", F_ARIAL_NARROW_B, 280, 760, 1100),
    ("гроші", F_FUTURA_MED, 270, 1180, 1100),
    ("பணம்", F_TAM_BOLD, 300, 1740, 1070),

    # Row 5: Bottom Bleed (y ~ 1380 to 1650)
    ("χρήματα", F_ARIAL_BLACK, 280, 40, 1400),
    ("para", F_HELV_LIGHT, 280, 1060, 1400),
    ("ಡబ్బు", F_TEL_BOLD, 310, 1580, 1370),
]

for text, font_fn, sz, x, y in items:
    fnt = font_fn(sz)
    draw.text((x, y), text, font=fnt, fill="#000000")

target_sample = "/Users/prithvij/.gemini/antigravity/scratch/vyapardost/sample_data/currency_bg.jpg"
target_static = "/Users/prithvij/.gemini/antigravity/scratch/vyapardost/static/currency_bg.jpg"
preview_path = "/Users/prithvij/.gemini/antigravity/brain/2d47eb75-fe44-43db-9fbd-7281256c8a82/money_typography_bg.png"

img.save(target_sample, "JPEG", quality=95)
img.save(target_static, "JPEG", quality=95)
img.save(preview_path, "PNG")
print(f"SUCCESS: Generated 2400x1600 typographic MONEY background with all multilingual scripts!")
