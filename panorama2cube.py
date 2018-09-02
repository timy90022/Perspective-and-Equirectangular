import os
import cv2 
import lib.Equirec2Perspec as E2P
import lib.Perspec2Equirec as P2E
import lib.multi_Perspec2Equirec as m_P2E
import glob
import argparse



def panorama2cube(input_dir,output_dir):

    cube_size = 640

    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    all_image = sorted(glob.glob(input_dir + '/*.*'))

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

        out_dir = output_dir + '/%02d/'%(index)
        if not os.path.exists(out_dir):
            os.mkdir(out_dir)

        img = equ.GetPerspective(90, 0, 0, cube_size, cube_size)  # Specify parameters(FOV, theta, phi, height, width)
        output1 = out_dir +  'front.png'
        cv2.imwrite(output1, img)

        img = equ.GetPerspective(90, 90, 0, cube_size, cube_size)  # Specify parameters(FOV, theta, phi, height, width)
        output2 = out_dir + 'right.png' 
        cv2.imwrite(output2, img)


        img = equ.GetPerspective(90, 180, 0, cube_size, cube_size)  # Specify parameters(FOV, theta, phi, height, width)
        output3 = out_dir + 'back.png' 
        cv2.imwrite(output3, img)

        img = equ.GetPerspective(90, 270, 0, cube_size, cube_size)  # Specify parameters(FOV, theta, phi, height, width)
        output4 = out_dir + 'left.png' 
        cv2.imwrite(output4, img)

        img = equ.GetPerspective(90, 0, 90, cube_size, cube_size)  # Specify parameters(FOV, theta, phi, height, width)
        output5 = out_dir + 'top.png' 
        cv2.imwrite(output5, img)

        img = equ.GetPerspective(90, 0, -90, cube_size, cube_size)  # Specify parameters(FOV, theta, phi, height, width)
        output6 = out_dir + 'bottom.png' 
        cv2.imwrite(output6, img)


def cube2panorama(input_dir,output_dir):

    width = 1920
    height = 960

    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    
    front = input_dir + '/front.png'
    right = input_dir + '/right.png'
    back = input_dir + '/back.png'
    left = input_dir + '/left.png'
    top = input_dir + '/top.png'
    bottom = input_dir + '/bottom.png'

    # this can turn cube to panorama
    per = m_P2E.Perspective([front,right,back,left,top,bottom],
                            [[90, 0, 0],[90, 90, 0],[90, 180, 0],
                            [90, 270, 0],[90, 0, 90],[90, 0, -90]])    
    
    
    img = per.GetEquirec(height,width)  
    cv2.imwrite(output_dir + '/output.png', img)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--mode', type=str, default='panorama', choices=['panorama', 'cube'])
    parser.add_argument('--input', type=str, default='./panorama')
    parser.add_argument('--output', type=str, default='./output')

    config = parser.parse_args()

    if config.mode == 'panorama':
        panorama2cube(config.input,config.output)
    else:
        cube2panorama(config.input,config.output)
