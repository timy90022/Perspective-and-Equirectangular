# Perspective and Equirectangular
## Introduction
<strong> Perspective2Equirectangular </strong> is a python code to help you transfer image between equirectangular and perspective. Four transfer is in the list.


1.  equirectangular to perspective.
2.  perspective to equirectangular. 
3.  equirectangular to cube.  
4.  cube to equirectangular.

## Equirectangular to Perspective
Given an input of 360 degree panorama
<center><img src="panorama/world_map.jpeg"></center>
Setting the (FOV, theta, phi, height, width) in the code <strong>equir2pers.py</strong>

```
equ = E2P.Equirectangular(input_img)    # Load equirectangular image
img = equ.GetPerspective(120, 0, 0, 1280, 1280)  # Specify parameters(FOV, theta, phi, height, width)
output1 = output_dir +  '/perspective_1.png'
cv2.imwrite(output1, img)
```
**Run:**  ```python equir2pers.py```.

<center><img width="200" height="200" src="example/perspective/perspective_1.png"></center>

## Perspective to Equirectangular
Given multiple perspective images and infromation(FOV, theta, phi, height, width).  
If the equirectangle image is overlapping, the pixel calculate the average in multiple image.

<img width="200" height="200" src="example/perspective/perspective_1.png"> <img width="200" height="200" src="example/perspective/perspective_2.png">  
Setting the image information (FOV, theta, phi) in the code <strong>pers2equir.py</strong>.

```
input1 = input_dir + '/perspective_1.png'
input2 = input_dir + '/perspective_2.png'

equ = m_P2E.Perspective([input1,input2],
                        [[120, 0, 0],[120, 0, 90]])   #[FOV,theta,phi]
img = equ.GetEquirec(height,width)
```
**Run:**  ```python pers2equir.py```.
<center><img width="318" height="159" src="example/equirectangle/output.png"></center>

## Panorama to Cube
Put image in `./panorama`.   
<center><img src="panorama/world_map.jpeg"></center>

**Run:**  ```python panorama2cube.py```.   
<img width="150" height="150" src="output/00/front.png"> <img width="150" height="150" src="output/00/right.png"> <img width="150" height="150" src="output/00/back.png">  
<img width="150" height="150" src="output/00/left.png"> <img width="150" height="150" src="output/00/top.png"> <img width="150" height="150" src="output/00/bottom.png">

## Cube to Panorama
Put image in `./in_path`.  
If you do not want to change code, remeber to set the image name (front,right,black,left,top,bottom).png. 

**Run:**  ```python panorama2cube.py --mode cube --input ./in_path --output ./out_path```.

<center><img src="output/output.png"></center>




