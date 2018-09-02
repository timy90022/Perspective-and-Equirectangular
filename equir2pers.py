import os
import cv2 
import lib.Equirec2Perspec as E2P
import lib.Perspec2Equirec as P2E
import lib.multi_Perspec2Equirec as m_P2E
import glob
import argparse



def equir2pers():

    #
    # FOV unit is degree
    # theta is z-axis angle(right direction is positive, left direction is negative)
    # phi is y-axis angle(up direction positive, down direction negative)
    # height and width is output image dimension
    #
    
    input_img = './panorama/world_map.jpeg'
    output_dir = './example/perspective'
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    
    equ = E2P.Equirectangular(input_img)    # Load equirectangular image

    img = equ.GetPerspective(120, 0, 0, 1280, 1280)  # Specify parameters(FOV, theta, phi, height, width)
    output1 = output_dir +  '/perspective_1.png'
    cv2.imwrite(output1, img)

    img = equ.GetPerspective(120, 0, 90, 1280, 1280)  # Specify parameters(FOV, theta, phi, height, width)
    output1 = output_dir +  '/perspective_2.png'
    cv2.imwrite(output1, img)



if __name__ == '__main__':
    equir2pers()