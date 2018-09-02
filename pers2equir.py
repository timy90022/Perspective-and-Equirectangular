import os
import cv2 
import lib.Equirec2Perspec as E2P
import lib.Perspec2Equirec as P2E
import lib.multi_Perspec2Equirec as m_P2E
import glob
import argparse



def pers2equir():
    #
    # FOV unit is degree
    # theta is z-axis angle(right direction is positive, left direction is negative)
    # phi is y-axis angle(up direction positive, down direction negative)
    # height and width is output image dimension
    #
    
    input_dir = './example/perspective'
    output_dir = './example/equirectangle'

    width = 1920
    height = 960

    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    
    input1 = input_dir + '/perspective_1.png'
    input2 = input_dir + '/perspective_2.png'

    # this can turn cube to panorama
    equ = m_P2E.Perspective([input1,input2],
                            [[120, 0, 0],[120, 0, 90]])    
    
    
    img = equ.GetEquirec(height,width)  
    cv2.imwrite(output_dir + '/output.png', img)



if __name__ == '__main__':
    pers2equir()