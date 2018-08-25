import vrProjector
import glob
import os

input_place = './test1/'
output_place = './panorama/'

dirs = os.listdir( input_place )
source = vrProjector.CubemapProjection()

if not os.path.exists(output_place):
	os.mkdir(output_place)


for dir_path in dirs:
	all_image = sorted(glob.glob(input_place + dir_path + '/*.*'))
	source.loadImages(all_image[0], all_image[1], all_image[2], all_image[3], all_image[4], all_image[5])

	eq2 = vrProjector.EquirectangularProjection()
	eq2.initImage(2048,1024)
	eq2.reprojectToThis(source)
	eq2.saveImage(output_place + dir_path + ".png")
	print('Sucess...%s'%(dir_path))
	assert False



'''

print(all_image[0])
source.loadImages(all_image[0], all_image[1], all_image[2], all_image[3], all_image[4], all_image[5])

# source.set_use_bilinear(True)

eq2 = vrProjector.EquirectangularProjection()
eq2.initImage(2048,1024)
eq2.reprojectToThis(source)
eq2.saveImage("foo.png")
'''