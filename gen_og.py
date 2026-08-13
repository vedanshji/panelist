from PIL import Image, ImageDraw, ImageFilter, ImageFont
import os

W, H = 1200, 630
img = Image.new("RGB", (W, H), (5, 6, 10))

# Aurora blobs (draw large soft circles onto a temp layer then blur)
blob_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
bd = ImageDraw.Draw(blob_layer)
def blob(cx, cy, r, color, alpha=140):
    bd.ellipse([cx-r, cy-r, cx+r, cy+r], fill=color + (alpha,))
blob(150, 100, 320, (124, 92, 255))       # purple top-left
blob(1080, 500, 340, (34, 211, 238))      # cyan bottom-right
blob(700, 300, 260, (255, 92, 244), 100)  # magenta center
blob_layer = blob_layer.filter(ImageFilter.GaussianBlur(radius=90))
img.paste(blob_layer, (0, 0), blob_layer)

# Grid overlay (subtle)
grid = Image.new("RGBA", (W, H), (0, 0, 0, 0))
gd = ImageDraw.Draw(grid)
for x in range(0, W, 60):
    gd.line([(x, 0), (x, H)], fill=(255, 255, 255, 10), width=1)
for y in range(0, H, 60):
    gd.line([(0, y), (W, y)], fill=(255, 255, 255, 10), width=1)
img.paste(grid, (0, 0), grid)

draw = ImageDraw.Draw(img)

# Try to load nice fonts, fall back gracefully
def find_font(names, size):
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
    ]
    for c in candidates:
        if os.path.exists(c):
            try:
                return ImageFont.truetype(c, size)
            except Exception:
                pass
    return ImageFont.load_default()

font_brand = find_font(["Space Grotesk"], 32)
font_title = find_font(["Space Grotesk"], 78)
font_tag = find_font(["Inter"], 30)
font_small = find_font(["Inter"], 22)

# Brand mark (logo square + name)
draw.rounded_rectangle([60, 60, 120, 120], radius=14, fill=(124, 92, 255))
draw.text((70, 63), "P", font=find_font([], 56), fill=(255, 255, 255))
draw.text((140, 78), "Panelist", font=font_brand, fill=(244, 245, 250))

# Title
title_lines = ["Interviews on demand.", "Signal on delivery."]
y = 220
for i, line in enumerate(title_lines):
    color = (244, 245, 250) if i == 0 else (34, 211, 238)  # cyan pop for line 2
    draw.text((60, y), line, font=font_title, fill=color)
    y += 92

# Subtitle
draw.text((60, 440),
          "A vetted network of expert interviewers.",
          font=font_tag, fill=(160, 164, 184))
draw.text((60, 480),
          "Structured feedback in under 24 hours.",
          font=font_tag, fill=(160, 164, 184))

# Bottom URL bar
draw.text((60, 560), "panelist.io", font=font_small, fill=(107, 112, 133))

img.save("/sessions/keen-practical-thompson/mnt/outputs/og-image.png", "PNG", optimize=True)
print("wrote og-image.png", os.path.getsize("/sessions/keen-practical-thompson/mnt/outputs/og-image.png"), "bytes")
