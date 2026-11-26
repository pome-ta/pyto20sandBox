import ctypes
import functools

from pyrubicon.objc import (
  Block,
  ObjCClass,
  ObjCInstance,
)  # api
from pyrubicon.objc import objc_block, objc_id  # runtime
from pyrubicon.objc.runtime import load_library

libSystem = load_library('System')
NSThread = ObjCClass('NSThread')


class struct_dispatch_queue_s(ctypes.Structure):
  pass  # No _fields_, because this is an opaque structure.


_dispatch_main_q = struct_dispatch_queue_s.in_dll(
  libSystem,
  '_dispatch_main_q',
)


def dispatch_get_main_queue():
  return ObjCInstance(ctypes.cast(
    ctypes.byref(_dispatch_main_q),
    objc_id,
  ))


def dispatch_async(queue, block_obj: objc_block):
  try:
    _func = dispatch_async._cfunc
  except AttributeError:
    _func = libSystem.dispatch_async
    _func.restype = None
    _func.argtypes = [
      objc_id,
      objc_block,
    ]
    dispatch_async._cfunc = _func

  _func(queue, block_obj)


def onMainThread(func):

  @functools.wraps(func)
  def wrapper(*args, **kwargs):
    if NSThread.isMainThread:
      func(*args, **kwargs)
      return
    block = Block(functools.partial(func, *args, **kwargs), None)
    dispatch_async(dispatch_get_main_queue(), block)

  return wrapper

