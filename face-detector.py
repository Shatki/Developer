from SimpleCV import *
from time import sleep

# 'face3.xml', 'face4.xml', 'face_cv2.xml', 'left_ear.xml', 'mouth.xml', 'eye.xml', 'lefteye.xml', 'lower_body.xml',
# 'right_ear.xml', 'fullbody.xml', 'upper_body2.xml', 'two_eyes_small.xml',

myCamera = Camera(prop_set={'width':640, 'height':480})
myDisplay = Display(resolution=(640,480),title='Face Detector')
#myHaarCascade = HaarCascade("face4.xml")


# myImage = Image()
# print myImage.listHaarFeatures()

while not myDisplay.isDone():
    frame = myCamera.getImage().flipHorizontal().scale(0.5)
    faces = frame.findHaarFeatures('face.xml')
    if faces:
        #for face in faces:
        #    print "Face at:"  + str(face.coordinates())
    #else:
    #    print  "Not faces detected."
        for face in faces:
            bb = face.boundingBox()
            frame = frame.pixelize(10, region=(bb[0],bb[1], bb[2], bb[3]))
            #frame = frame.draw(10, region=(bb[0], bb[1], bb[2], bb[3]))
    frame.save(myDisplay)
    sleep(.1)