import ctypes

from pyrubicon.objc import ObjCClass, objc_method  # api
from pyrubicon.objc import send_super, SEL  # runtime

from .lifeCycle import loop
from .enumerations import UIBarButtonSystemItem

from .functions import NSStringFromClass

UINavigationController = ObjCClass('UINavigationController')
UIBarButtonItem = ObjCClass('UIBarButtonItem')


class RootNavigationController(UINavigationController):

  @objc_method
  def dealloc(self) -> None:
    # xxx: 呼ばない-> `send_super(__class__, self, 'dealloc')`
    #print(f'- {NSStringFromClass(__class__)}: dealloc')
    #print('--- loop stop Call ---')
    # >>> (5) <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    loop.call_soon(loop.stop)

  @objc_method
  def loadView(self) -> None:
    send_super(
      __class__,
      self,
      'loadView',
      restype=None,
    )
    #print(f'{NSStringFromClass(__class__)}: loadView')

  @objc_method
  def viewDidLoad(self) -> None:
    send_super(
      __class__,
      self,
      'viewDidLoad',
      restype=None,
    )
    #print(f'{NSStringFromClass(__class__)}: viewDidLoad')
    self.delegate = self

  @objc_method
  def viewWillAppear_(self, animated: bool) -> None:
    send_super(
      __class__,
      self,
      'viewWillAppear:',
      animated,
      restype=None,
      argtypes=[
        ctypes.c_bool,
      ],
    )
    #print(f'{NSStringFromClass(__class__)}: viewWillAppear_')

  @objc_method
  def viewDidAppear_(self, animated: bool) -> None:
    send_super(
      __class__,
      self,
      'viewDidAppear:',
      animated,
      restype=None,
      argtypes=[
        ctypes.c_bool,
      ],
    )
    #print(f'{NSStringFromClass(__class__)}: viewDidAppear_')
    #print('↓ ---')

  @objc_method
  def viewWillDisappear_(self, animated: bool) -> None:
    #print('↑ ---')
    send_super(
      __class__,
      self,
      'viewWillDisappear:',
      animated,
      restype=None,
      argtypes=[
        ctypes.c_bool,
      ],
    )
    #print(f'{NSStringFromClass(__class__)}: viewWillDisappear_')

  @objc_method
  def viewDidDisappear_(self, animated: bool) -> None:
    send_super(
      __class__,
      self,
      'viewDidDisappear:',
      animated,
      restype=None,
      argtypes=[
        ctypes.c_bool,
      ],
    )
    #print(f'{NSStringFromClass(__class__)}: viewDidDisappear_')

  @objc_method
  def closeButtonTapped_(self, sender) -> None:
    #print(f'{NSStringFromClass(__class__)}: doneButtonTapped:')
    self.dismissViewControllerAnimated_completion_(True, None)

  @objc_method
  def navigationController_willShowViewController_animated_(
    self,
    navigationController,
    viewController,
    animated: bool,
  ) -> None:
    closeButtonItem = UIBarButtonItem.alloc().initWithBarButtonSystemItem(
      UIBarButtonSystemItem.close,
      target=navigationController,
      action=SEL('closeButtonTapped:'),
    )

    visibleViewController = navigationController.visibleViewController
    navigationItem = visibleViewController.navigationItem
    navigationItem.rightBarButtonItem = closeButtonItem

