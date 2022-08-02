from PIL import Image


def check_if_pics_same(pic_path_1, pic_path_2):
    first = Image.open(pic_path_1)
    second = Image.open(pic_path_2)
    return list(first.getdata()) == list(second.getdata())