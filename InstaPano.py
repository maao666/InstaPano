import cv2
import sys

def _load_img_from_cmd():
    if len(sys.argv) <= 1:
        print('Usage: InstaPano.py path_to_your_image.jpg')
        exit(0)
    return cv2.imread(sys.argv[1])

def split(img, filename:str, split=5):
    results = []
    h = img.shape[0]
    w = img.shape[1] // split
    for i in range(split):
        if (i + 1) * w + 1 > img.shape[1]:
            break
        crop = img[0:, i * w : (i + 1) * w + 1]
        cv2.imwrite('{}-{}.jpg'.format(filename,str(i+1)),crop)

def main():
    img = _load_img_from_cmd()
    print(img.shape)
    height, weight = img.shape[0], img.shape[1]
    print(weight // height)
    print(weight % height)
    split(img, 'pano')

if __name__ == '__main__':
    main()
