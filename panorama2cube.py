import os
import cv2 
import new_Equirec2Perspec as E2P
import glob

if __name__ == '__main__':
    num = 1
    # output_place = './test2/'
    # input_place = '/mnt/data/gasoon/iStage Data/0001~0050/0001'

    output_place = './test3/'
    input_place = './panorama/'

    if not os.path.exists(output_place):
        os.mkdir(output_place)
    # output_place = output_place+'images/'
    # if not os.path.exists(output_place):
    #     os.mkdir(output_place)

    all_image = sorted(glob.glob(input_place + '/*.*'))
    print(all_image)


    for index in range(len(all_image)):
        # image = '../Opensfm/source/library/test-1/frame{:d}.png'.format(i)
        equ = E2P.Equirectangular(all_image[index])    # Load equirectangular image
    #
    # FOV unit is degree
    # theta is z-axis angle(right direction is positive, left direction is negative)
    # phi is y-axis angle(up direction positive, down direction negative)
    # height and width is output image dimension
    #
        # theta = [-150,-120,-90,-60,-30]
        # phi = [0,30,60]
        out_dir = output_place + '/%02d/'%(index)
        if not os.path.exists(out_dir):
            os.mkdir(out_dir)

        img = equ.GetPerspective(30, 0, 0, 1280, 1280)  # Specify parameters(FOV, theta, phi, height, width)
        output = out_dir +  '%03d_1.png'%(index)
        cv2.imwrite(output, img)
        assert False

        img = equ.GetPerspective(90, 90, 0, 1280, 1280)  # Specify parameters(FOV, theta, phi, height, width)
        output = out_dir + '%03d_2.png' % (index)
        cv2.imwrite(output, img)

        img = equ.GetPerspective(90, 180, 0, 1280, 1280)  # Specify parameters(FOV, theta, phi, height, width)
        output = out_dir + '%03d_3.png' % (index)
        cv2.imwrite(output, img)

        img = equ.GetPerspective(90, 270, 0, 1280, 1280)  # Specify parameters(FOV, theta, phi, height, width)
        output = out_dir + '%03d_4.png' % (index)
        cv2.imwrite(output, img)

        img = equ.GetPerspective(90, 0, 90, 1280, 1280)  # Specify parameters(FOV, theta, phi, height, width)
        output = out_dir + '%03d_5.png' % (index)
        cv2.imwrite(output, img)

        img = equ.GetPerspective(90, 0, -90, 1280, 1280)  # Specify parameters(FOV, theta, phi, height, width)
        output = out_dir + '%03d_6.png' % (index)
        cv2.imwrite(output, img)

