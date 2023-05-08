from PIL import Image
import sys, os, time

def get_concat_h_repeat(im, column):
    dst = Image.new('RGB', (im.width * column, im.height))
    for x in range(column):
        dst.paste(im, (x * im.width, 0))
    return dst

def get_concat_v_repeat(im, row):
    dst = Image.new('RGB', (im.width, im.height * row))
    for y in range(row):
        dst.paste(im, (0, y * im.height))
    return dst

def get_concat_tile_repeat(im, row, column):
    dst_h = get_concat_h_repeat(im, column)
    return get_concat_v_repeat(dst_h, row)

args = sys.argv[1:]
if len(args) != 1:
    print("Usage: python x4.py <path>")
    exit(1)

input_filepath = args[0]
im = Image.open(input_filepath)

width, height = im.size
if max(width, height) * 2 > 4000:
    im_s = im.resize((im.width // 2, im.height // 2))
    im = im_s

im_c = get_concat_tile_repeat(im, 2, 2)
basename = os.path.basename(input_filepath)
root, ext = os.path.splitext(basename)
im_c.save(f"{root}_x4_{int(time.time())}.png")
