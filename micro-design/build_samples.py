from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


OUT = Path(__file__).parent / "assets"
OUT.mkdir(parents=True, exist_ok=True)


def font(size, bold=False):
    roots = [
        Path("C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf"),
        Path("C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf"),
    ]
    for path in roots:
        if path.exists():
            return ImageFont.truetype(str(path), size)
    return ImageFont.load_default()


def fit(draw, text, max_width, start_size, bold=False):
    size = start_size
    while size > 16:
        f = font(size, bold)
        if draw.textbbox((0, 0), text, font=f)[2] <= max_width:
            return f
        size -= 2
    return font(size, bold)


def sample_thumbnail():
    img = Image.new("RGB", (1280, 720), "#111318")
    d = ImageDraw.Draw(img)
    d.rectangle((0, 0, 1280, 720), fill="#111318")
    d.polygon([(0, 720), (430, 0), (720, 0), (315, 720)], fill="#1f6f64")
    d.rectangle((810, 0, 1280, 720), fill="#e8c24a")
    d.rounded_rectangle((78, 78, 560, 642), radius=28, fill="#f7f7ee")
    d.ellipse((140, 150, 492, 502), fill="#303844")
    d.ellipse((190, 120, 448, 378), fill="#d5b089")
    d.rectangle((180, 360, 460, 535), fill="#151820")
    d.text((610, 96), "I TRIED", font=font(88, True), fill="#f7f7ee")
    d.text((610, 184), "THE 15 MINUTE", font=font(58, True), fill="#f7f7ee")
    d.rounded_rectangle((606, 260, 1204, 402), radius=18, fill="#111318")
    d.text((632, 270), "RESET", font=font(112, True), fill="#e8c24a")
    d.text((610, 440), "and it actually worked", font=font(48, True), fill="#111318")
    d.rounded_rectangle((610, 530, 1038, 594), radius=10, fill="#ffffff")
    d.text((636, 542), "Sample thumbnail", font=font(32, True), fill="#111318")
    img.save(OUT / "sample-thumbnail.png", quality=95)


def sample_social_card():
    img = Image.new("RGB", (1200, 630), "#f4f0e8")
    d = ImageDraw.Draw(img)
    d.rectangle((0, 0, 1200, 630), fill="#f4f0e8")
    d.rounded_rectangle((70, 66, 1130, 564), radius=34, fill="#ffffff", outline="#d7d0c2", width=3)
    d.rounded_rectangle((96, 92, 448, 538), radius=24, fill="#1a5d55")
    d.text((132, 132), "FAST", font=font(74, True), fill="#ffffff")
    d.text((132, 208), "MICRO", font=font(74, True), fill="#f3c84b")
    d.text((132, 284), "DESIGN", font=font(74, True), fill="#ffffff")
    d.line((514, 138, 1048, 138), fill="#111318", width=5)
    d.text((514, 180), "One clean social graphic", font=font(54, True), fill="#111318")
    d.text((514, 250), "for a launch, post, product,", font=font(38, False), fill="#35413e")
    d.text((514, 300), "or simple promo.", font=font(38, False), fill="#35413e")
    d.rounded_rectangle((514, 396, 778, 462), radius=10, fill="#111318")
    d.text((544, 410), "$5 sample offer", font=font(34, True), fill="#ffffff")
    d.text((514, 496), "Watermarked preview first", font=font(28, True), fill="#1a5d55")
    img.save(OUT / "sample-social-card.png", quality=95)


def sample_banner():
    img = Image.new("RGB", (1500, 500), "#151820")
    d = ImageDraw.Draw(img)
    d.rectangle((0, 0, 1500, 500), fill="#151820")
    d.rectangle((0, 0, 520, 500), fill="#e6bb3d")
    d.polygon([(520, 0), (700, 0), (500, 500), (320, 500)], fill="#1d7569")
    d.text((76, 94), "LAUNCH", font=font(86, True), fill="#151820")
    d.text((76, 180), "BANNER", font=font(86, True), fill="#151820")
    d.text((760, 116), "Clean header graphics", font=font(62, True), fill="#ffffff")
    d.text((760, 200), "for links, profiles, and posts", font=font(42, False), fill="#d7ddd9")
    d.rounded_rectangle((760, 318, 1112, 390), radius=12, fill="#ffffff")
    d.text((792, 334), "same-day sample", font=font(36, True), fill="#151820")
    img.save(OUT / "sample-banner.png", quality=95)


if __name__ == "__main__":
    sample_thumbnail()
    sample_social_card()
    sample_banner()
