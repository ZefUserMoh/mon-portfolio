from PIL import Image
img = Image.open(r'C:/GeminiProjects/douceurs-gourmandises/images/hero/sophie-atelier.png')
print("Taille:", img.size, img.mode)
thumb = img.convert('RGB').resize((300, 200))
thumb.save(r'C:/GeminiProjects/douceurs-gourmandises/images/hero/thumb_result.jpg', quality=60)
print("OK")
