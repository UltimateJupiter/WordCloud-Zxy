import cv2
import numpy as np
from IPython import embed
import os
import matplotlib.pyplot as plt


backstage = './output1.png'

def output_show(mat):
    plt.imshow(mat)
    plt.show()

def im_pre(img_dest):

    img = cv2.imread(img_dest)
    _, img = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)
    assert img is not None
    
    img = img[:, :, 0]
    img = img / 255

    print(img.shape)
    return img

def load_base():
    
    print('Loading Name Single Images')
    name_imgs = []
    base_dest = "./names_pics/"
    items = os.listdir(base_dest)

    img_fls = []
    for name in items:
        if name.endswith(".png"):
            img_fls.append(name)
            tmp = im_pre(base_dest + name)

            name_imgs.append(tmp)
    
    print('Finished')
    return name_imgs

def slice_analysis(mat):
    
    # print(mat)
    whole = mat.shape[0] * mat.shape[1]
    return sum(sum(mat)) / whole

def mat_scan(num):
    
    mat = im_pre(backstage)
    mat_h, mat_w = mat.shape

    fix_q = 180 / 64

    mat_trans = np.transpose(mat)
    for i in range(mat_h):
        if sum(mat[i]) > 0:
            h_start = i
            break
    
    for j in range(mat_w):
        if sum(mat_trans[j]) > 0:
            w_start = j
            break
    
    print(h_start, w_start)
    
    for name_h in range(300, 50, -2):
        name_w = int(name_h * fix_q)

        boxes = []

        for y in list(range(h_start, mat_h, name_h))[:-1]:
            for x in list(range(w_start + int(np.random.randint(-name_w/2, name_w/2)), mat_w, name_w))[:-1]:
            #for x in list(range(w_start, mat_w, name_w))[:-1]:
                boxes.append([y, y + name_h, x, x + name_w])
        
        evals = []
        available_boxes = []
        spare_boxes = []

        for mark in boxes:

            if mark[0] > 0 and mark[2] > 0:
                pass
            else:
                continue

            box = mat[mark[0]: mark[1], mark[2]: mark[3]]
            # print(box.shape, mark)
            result = slice_analysis(box)
            evals.append(result)
            if result > 0.9:
                available_boxes.append(mark)
            elif 0.9 > result > 0.3:
                spare_boxes.append(mark)

        print('H:{}, Nums:{}'.format(name_h, len(available_boxes)))
        
        if len(available_boxes) > num:
            return available_boxes, spare_boxes, mat, (name_w, name_h)
    
    return None, None, None, None

def main():
    
    name_imgs = load_base()
    name_imgs.extend(name_imgs)
    # name_imgs.extend(name_imgs)

    f_boxes, s_boxes, mat, scale = mat_scan(len(name_imgs))

    blank_mat = np.zeros([mat.shape[0], mat.shape[1]])
    
    np.random.shuffle(name_imgs)
    
    mk = 0
    
    for box_mark in f_boxes:
    
        if mk < len(name_imgs) - 1:
            load_img = name_imgs[mk]
        else:
            load_img = name_imgs[np.random.randint(0, len(name_imgs))]
        insert_img = cv2.resize(load_img, (scale[0], scale[1]))
        print(insert_img.shape)
        mk += 1
        blank_mat[box_mark[0]: box_mark[1], box_mark[2]: box_mark[3]] = insert_img

    for box_mark in s_boxes:
    
        load_img = name_imgs[np.random.randint(0, len(name_imgs))]
        insert_img = cv2.resize(load_img, (scale[0], scale[1]))
        print(insert_img.shape)
        mk += 1
        blank_mat[box_mark[0]: box_mark[1], box_mark[2]: box_mark[3]] = insert_img

    final_mat = blank_mat * mat
    print(f_boxes, s_boxes)
    final_mat = final_mat * 255

    cv2.imwrite('out_test_cls172.png', final_mat)
    cv2.imwrite('out_test_cls172_nc.png', blank_mat*255)
    
    embed()

main()
