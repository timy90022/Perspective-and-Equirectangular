import vrProjector

eq = vrProjector.EquirectangularProjection()
eq.loadImage("cuber.jpg")
# eq.set_use_bilinear(True)
cb = vrProjector.CubemapProjection()
cb.initImages(256,256)
cb.reprojectToThis(eq)
cb.saveImages("front.png", "right.png", "back.png", "left.png", "top.png", "bottom.png")


#
# sbs = SideBySideFisheyeProjection()
# sbs.initImage(2048, 1024)
## sbs.reprojectToThisThreaded(eq, 8)
# sbs.reprojectToThis(eq)
# sbs.saveImage("foo.png")
#
# sbs2 = SideBySideFisheyeProjection()
# sbs2.loadImage("foo.png")
#
# eq2 = EquirectangularProjection()
# eq2.initImage(2048,1024)
# eq2.reprojectToThis(sbs2)
# eq2.saveImage("foo2.png")

# eq = EquirectangularProjection()
# eq.loadImage("cuber.jpg")
# eq.set_use_bilinear(True)
# cb = CubemapProjection()
# cb.initImages(256,256)
# cb.reprojectToThis(eq)
# cb.saveImages("front.png", "right.png", "back.png", "left.png", "top.png", "bottom.png")
#

# cb2 = CubemapProjection()
# cb2.loadImages("front.png", "right.png", "back.png", "left.png", "top.png", "bottom.png")
# eq2 = EquirectangularProjection()
# eq2.initImage(2048,1024)
# eq2.reprojectToThis(cb2)
# eq2.saveImage("foo.png")
