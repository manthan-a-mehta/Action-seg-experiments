import cv2


final_image=cv2.imread("/home/balaji/Documents/code/RSL/asrf/result/all_labels.png")
with open("/home/balaji/Documents/code/RSL/asrf/dataset/50salads/mapping.txt") as f:
    lines=f.readlines()
x=0
for line in lines:

    cv2.putText(img=final_image, text=line.split()[1], org=(0, x), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=3, color=(0, 255, 0),thickness=3)
    x=x+10
cv2.imwrite("/home/balaji/Documents/code/RSL/asrf/result/all_labels_with_names.png",final_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
# cv2.putText(img=final_image, text='All PG+32/96', org=(0, 180), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=3, color=(0, 255, 0),thickness=3)