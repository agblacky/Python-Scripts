import glob
from PIL import Image

images = [
    Image.open("./" + f)
    for f in glob.glob("*.png")
]
index=0
while index < len(images):
    images[index]=images[index].convert("RGB")
    index+=1

pdf_path = "./test.pdf"
    
images[0].save(
    pdf_path, "PDF" ,resolution=100.0, save_all=True#, append_images=images[1:]
)