# from typing import final
import cv2
import argparse
import numpy as np
def get_arguments() -> argparse.Namespace:
    """
    parse all the arguments from command line inteface
    return a list of parsed arguments
    """

    parser = argparse.ArgumentParser(
        description="train a network for action recognition"
    )
    parser.add_argument("root_folder", type=str, help="path of a root folder")
    parser.add_argument("image_path", type=str, help="name of the image")


    return parser.parse_args()

def combine_vertically(image_names,padding=40):
    images = []
    max_width = 0  # find the max width of all the images
    total_height = 0  # the total height of the images (vertical stacking)
    for name in image_names:
        # open all images and find their sizes
        img=cv2.imread(name)
        images.append(img)
        print(img)
        image_width=img.shape[1]
        image_height=img.shape[0]
        if image_width > max_width:
            max_width = image_width
        #add all the images heights
        total_height += image_height
    # create a new array with a size large enough to contain all the images
    # also add padding size for all the images except the last one
    final_image = np.zeros((total_height+(len(image_names)-1)*padding,max_width,3),dtype=np.uint8)
    current_y = 0 # keep track of where your current image was last placed in the y coordinate
    for image in images:
        # add an image to the final array and increment the y coordinate
        height = image.shape[0]
        width = image.shape[1]
        final_image[current_y:height+current_y,:width,:] = image
        # add the padding between the images
        current_y += height+ padding
    return final_image
if __name__ == '__main__':
    args=get_arguments()
    print(args)
    root_folder=args.root_folder
    image_path=args.image_path
    print(root_folder,image_path)
    image_names=[root_folder+"asrf_allwt_pg/"+image_path+"_gt.png",root_folder+"asrf_allwt_pg/"+image_path+"_refined_pred.png",root_folder+"vanilla_asrf/"+image_path+"_refined_pred.png"]
    # image_names = ['./opencv.jpg','./python.jpg','./windows.jpg']
    final_image=combine_vertically(image_names,padding=10)
    
    # cv2.imshow('out',final_image)
    
    cv2.putText(img=final_image, text='GT', org=(0, 75), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=3, color=(0, 255, 0),thickness=3)
    cv2.putText(img=final_image, text='All PG+32/96', org=(0, 180), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=3, color=(0, 255, 0),thickness=3)
    cv2.putText(img=final_image, text='ASRF', org=(0, 285), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=3, color=(0, 255, 0),thickness=3)


    cv2.imwrite(image_path+"asrf_allwt_pg"+'.PNG',final_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
