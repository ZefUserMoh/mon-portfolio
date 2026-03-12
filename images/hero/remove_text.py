from PIL import Image, ImageFilter

src = r'C:/GeminiProjects/douceurs-gourmandises/images/hero/sophie-atelier-original.png'
dst = r'C:/GeminiProjects/douceurs-gourmandises/images/hero/sophie-atelier.png'

img = Image.open(src)
w, h = img.size
print(f"Taille: {w}x{h}")

# Texte visible sur toute la largeur, ~60% du haut
text_box = (0, 0, w, 420)

region = img.crop(text_box)
for _ in range(15):
    region = region.filter(ImageFilter.GaussianBlur(radius=20))

img.paste(region, text_box)
img.save(dst)
print("Image sauvegardée.")

check = img.convert('RGB').resize((300, 135))
check.save(r'C:/GeminiProjects/douceurs-gourmandises/images/hero/thumb_result.jpg', quality=60)
print("Miniature OK.")
