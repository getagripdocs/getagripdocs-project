from PIL import Image
import shutil
import os

import fire

def resize(img, size, in_place = False, delete = True):
    im = Image.open(img)
    path, extn = img.split(".")
    new_path = path +"_resized" + "." + extn

    if in_place == False:
        split = new_path.split("/")
        folders = "/".join(split[:-1]) + "/resized"
        fn = split[-1]
        if os.path.isdir(folders) and delete:
            shutil.rmtree(folders)
        if not os.path.isdir(folders):
            os.mkdir(folders)
        new_path = folders + "/" + fn

    im.thumbnail(size, Image.ANTIALIAS)
    im.save(new_path)

def bulk_resize(images, size):
    for i in images:
        resize(i, size, delete = False)

def folder_resize(folder, sizex, sizey):
    size = int(sizex), int(sizey)
    images = list(map(lambda x: folder + "/" + x, os.listdir(folder)))
    bulk_resize(images, size)


def combine_images(way, *images):
    if way == "sbs": # assumes two images
        im1 = Image.open(images[0])
        im2 = Image.open(images[1])

        path1, extn1 = images[0].split(".")
        path2, extn2 = images[1].split(".")
        path1_fn = path1.split("/")[-1]
        path2_fn = path2.split("/")[-1]
        folders1 = "/".join(path1.split("/")[:-1])

        new_fn = path1_fn + "_" + path2_fn

        new_path = folders1 + "/" + new_fn + "." + extn1

        images_ = im1, im2

        widths, heights = zip(*(i.size for i in images_))

        total_width = sum(widths)
        max_height = max(heights)

        new_im = Image.new('RGB', (total_width, max_height))

        x_offset = 0
        for im in images_:
            new_im.paste(im, (x_offset,0))
            x_offset += im.size[0]

        new_im.save(new_path)

    elif way == "down": # assumes three images
        im1 = Image.open(images[0])
        im2 = Image.open(images[1])
        im3 = Image.open(images[2])

        path1, extn1 = images[0].split(".")
        path2, extn2 = images[1].split(".")
        path3, extn3 = images[1].split(".")
        path1_fn = path1.split("/")[-1]
        path2_fn = path2.split("/")[-1]
        path3_fn = path2.split("/")[-1]
        folders1 = "/".join(path1.split("/")[:-1])

        new_fn = path1_fn + "_" + path2_fn + "_" + path3_fn

        new_path = folders1 + "/" + new_fn + "." + extn1

        images_ = im1, im2, im3

        widths, heights = zip(*(i.size for i in images_))

        max_width = max(widths)
        total_height = sum(heights)

        new_im = Image.new('RGB', (max_width, total_height))

        y_offset = 0
        for im in images_:
            new_im.paste(im, (0,y_offset))
            y_offset += im.size[1]

        new_im.save(new_path)

    elif way == "square": # assumes four images
        pass

    

if __name__ == "__main__":
    fire.Fire()
    #folder_resize("content/group/images", (256, 256))