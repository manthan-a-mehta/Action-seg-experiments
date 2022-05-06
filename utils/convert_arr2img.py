import argparse
import glob
import os
from typing import List

import numpy as np
from PIL import Image


def get_arguments() -> argparse.Namespace:
    """
    parse all the arguments from command line inteface
    return a list of parsed arguments
    """

    parser = argparse.ArgumentParser(description="convert np.array to images.")
    parser.add_argument(
        "dir",
        type=str,
        help="path to a directory containing arrays you want to convert",
    )

    return parser.parse_args()


def convert_arr2img(arr: np.ndarray, palette: List[int]) -> Image.Image:
    """
    Args:
        arr: 1d array(T, )
        palette: color palette
    """
    # pal=np.array(palette)
    # answer=pal[arr]
    # print(answer)
    arr = arr.astype(np.uint8)
    
    # print(palette)

    arr = np.tile(arr, (100, 1))
    img = Image.fromarray(arr)
    img = img.convert("P")
    
    # print((palette))
    img.putpalette(palette)

    return img


def main() -> None:
    args = get_arguments()

    voc = Image.open("./imgs/voc_sample.png")
    voc = voc.convert("P")
    palette = voc.getpalette()
    # arr_paths = glob.glob(os.path.join(args.dir, "*.npy"))
    arr_paths=[]
    for i in os.listdir(args.dir):
    # List files with .py
        if i.endswith(".npy"):
            arr_paths.append(i)
    # print(arr_paths)
    for path in arr_paths:
        print(path)
        name = os.path.basename(path)[:-4]  # remove .npy
        arr = np.load(args.dir+"/"+path)
        print(arr)

        img = convert_arr2img(arr, palette)
        img.save(os.path.join(args.dir, name + ".png"))

    print("Done")


if __name__ == "__main__":
    main()
