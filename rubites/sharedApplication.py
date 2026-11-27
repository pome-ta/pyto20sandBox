import ctypes

# todo: main ################################################
from pyrubicon.objc import (
  NSObject,
  ObjCClass,
  ObjCInstance,
  objc_method,
  objc_property,
)  # api
from pyrubicon.objc import (
  SEL,
  objc_id,
  send_super,
)  # runtime

from rbedge import pdbr

UIApplication = ObjCClass('UIApplication')

sharedApplication = UIApplication.sharedApplication
objectEnumerator = sharedApplication.connectedScenes.objectEnumerator()



while (s := objectEnumerator.nextObject()):
  print(s)
#print(objectEnumerator.nextObject)

'''
next(sharedScene for _scene in iter(objectEnumerator.nextObject, None)
     if (sharedScene := _scene).activationState == 0)

sceneWindow = sharedScene.keyWindow if (
  _delegate := sharedScene.delegate) is None else _delegate.window


pdbr.state(sharedScene.keyWindow.rootViewController)
'''

