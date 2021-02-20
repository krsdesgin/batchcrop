from PIL import Image
import pathlib

maxsize = (5000, 50000)
box = (10, 610, 1080, 1690) 


for input_img_path in pathlib.Path("/Users/****/Desktop/input").iterdir(): # need to figure out how to ignore .Ds_store

    output_img_path = str(input_img_path).replace("/Users/****/Desktop/input","/Users/****/Desktop/output")
    with Image.open(input_img_path) as im:
        im.crop(box) # need to figure out why this is not implementing
        im.save(output_img_path, "png",) # need to figure out why this is not implementing
        print(f"processing file {input_img_path} done...")
