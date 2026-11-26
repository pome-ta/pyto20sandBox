__version__ = '0.0.0'

import os
import ctypes

from pyrubicon.objc import ObjCClass, ObjCInstance  # api
from pyrubicon.objc.runtime import Foundation

ObjCClass.auto_rename = True

#############################################################
# --- exception
#############################################################
# todo: from objc_util.py of Pythonista3
#  呼び出し方法と出力先を調整
#    - `~/Documents/_objc_exception.txt`
#    - `~/Documents/_rubicon_objc_exception.txt`
# Set a handler for uncaught ObjC exceptions that writes to a log file:
ExceptionHandlerFuncType = ctypes.CFUNCTYPE(None, ctypes.c_void_p)


def NSSetUncaughtExceptionHandler(_exc: ExceptionHandlerFuncType) -> None:
  _NSSetUncaughtExceptionHandler = Foundation.NSSetUncaughtExceptionHandler
  _NSSetUncaughtExceptionHandler.restype = None
  _NSSetUncaughtExceptionHandler.argtypes = [
    ExceptionHandlerFuncType,
  ]
  _NSSetUncaughtExceptionHandler(_exc)


def _objc_exception_handler(_exc):
  exc = ObjCInstance(_exc)
  _path_str = '~/Documents/_rubicon_objc_exception.txt'
  with open(os.path.expanduser(_path_str), 'w') as f:
    from datetime import datetime
    f.write(
      'The app was terminated due to an Objective-C exception. Details below:\n\n%s\n%s\n'
      % (datetime.now(), exc))


_handler = ExceptionHandlerFuncType(_objc_exception_handler)
NSSetUncaughtExceptionHandler(_handler)
#######################################################

