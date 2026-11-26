import ctypes

from pyrubicon.objc import ObjCInstance  # api
from pyrubicon.objc import objc_id  # runtime
from pyrubicon.objc.runtime import Foundation, Class


def NSStringFromClass(cls: Class) -> ObjCInstance:
  try:
    _func = NSStringFromClass._cfunc
  except AttributeError:
    _func = Foundation.NSStringFromClass
    _func.restype = objc_id
    _func.argtypes = [Class]
    NSStringFromClass._cfunc = _func

  return ObjCInstance(_func(cls))

