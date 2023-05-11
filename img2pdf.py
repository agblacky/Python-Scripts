import glob
from PIL import Image

images = []
file_extensions=["png","jpg","jpeg"]
for file_ext in file_extensions:
    for f in glob.glob(f"*.{file_ext}"):
        try:
            image = Image.open(f).convert("RGB")
            images.append(image)
        except Exception as err:
            print(f"Unable to open file {f} : {err}")

pdf_path = "./output.pdf"
try:
    images[0].save(
        pdf_path, "PDF", resolution=100.0, save_all=True, append_images=images[1:]
    )
except IndexError:
    print("No images found.")
except Exception as e:
    print(f"An error occurred while saving the PDF file: {e}")
finally:
    for image in images:
        image.close()