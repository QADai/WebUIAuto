# -*- encoding: utf-8 -*-
"""
@Author  : QADai
@Email   : daibiao83@126.com
"""
import win32gui
import win32con
from time import sleep
from src.utils.log_util import log
from configure.configure import *

AUTOITEXE = {'firefox': 'upfile_autoit_firefox.exe',
             'chrome': 'upfile_autoit_chrome.exe',
             'internet explorer': 'upfile_autoit_ie.exe'
             }


class Error(Exception):
    """Base package Exception."""
    pass


class UploadFileError(Error):
    """Thrown when upload files not available."""
    pass


class UploadWindowNotOpenError(Error):
    """Thrown when upload window not open."""
    pass


class UploadWindowOpenError(Error):
    """Thrown when open upload window error."""
    pass


class FileUpload(object):

    def __init__(self, driver, element, window_name=None):
        self.driver = driver
        self.Element = element
        self.window_open_flag = 0  # 用来标识窗口是否打开

        if window_name is not None:
            self.window_name = window_name
        elif self.driver.name == 'firefox':
            self.window_name = u'文件上传'
        elif self.driver.name == 'chrome':
            self.window_name = u'打开'
        elif self.driver.name == 'internet explorer':
            self.window_name = u'选择要加载的文件'

    def _files(self, files):
        """将files组织成可输入上传文件Edit框的类型

        如果传入的是str类型，则不需要组织。
        如果传入的是list列表，则需要组织成Edit框接受的格式。（主要是应对多文件上传）
        """
        self.files = ''
        if type(files) == list:
            for f in files:
                self.files += '"{0}" '.format(f)
        elif type(files) == str:
            self.files = files

    def _window_open(self):
        """判断窗口标识，如果未打开窗口，则打开上传窗口。"""
        if self.window_open_flag == 0:
            try:
                self.Element.click()
            except:
                log.error('打开文件上传窗口失败！')
                raise UploadWindowOpenError('打开文件上传窗口失败！')
            sleep(1)

    # 三种方式上传
    def upload_by_input(self, files):
        """<input>标签直接send_keys即可。"""
        self._files(files)
        log.info('upload {} by send_keys'.format(self.files))
        self.Element.send_keys(self.files)

    def upload_by_win32(self, files):
        """win32方式 —— 打开窗口，并上传文件。（支持多文件上传，files参数传入list）"""
        self._window_open()
        self._files(files)
        log.info('upload {0} by win32'.format(self.files))

        upload = win32gui.FindWindow('#32770', self.window_name)

        # find Edit
        ComboBoxEx32 = win32gui.FindWindowEx(upload, 0, 'ComboBoxEx32', None)
        ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
        Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)

        # find confirm button
        button = win32gui.FindWindowEx(upload, 0, 'Button', None)

        # 验证是否打开窗口
        if upload and Edit and button:
            self.window_open_flag = 1
        else:
            raise UploadWindowNotOpenError('未发现上传文件对话框！')

        win32gui.SendMessage(Edit, win32con.WM_SETTEXT, 0, self.files)
        win32gui.SendMessage(upload, win32con.WM_COMMAND, 1, button)

        self.window_open_flag = 0

    def upload_by_autoit(self, files):
        """第三种方式是通过autoit工具生成的exe，通过命令行调用传参，实现上传。
        autoit方式 —— 打开窗口，并上传文件（支持多文件上传，files参数传入list）
        <这部分功能参考网络资料没有动手实践，具体情况需要调整>"""
        self._window_open()
        self._files(files)
        log.info('upload {} by autoit'.format(self.files))

        # 验证是否打开窗口
        if win32gui.FindWindow('#32770', self.window_name):
            self.window_open_flag = 1
        else:
            raise UploadWindowNotOpenError('未发现上传文件对话框！')

        upfile = os.path.abspath(tools_path + AUTOITEXE[self.driver.name])
        os.system('{0} {1}'.format(upfile, self.files))  # 调用exe，上传文件

        self.window_open_flag = 0

    # 统一上传方式
    def upload(self, files, autoit=False):
        """综合判断，如果为<input>标签，则直接上传。否则默认用win32方式，如果传入autoit=True，则用autoit上传。"""
        if self.Element.tag_name == 'input' and type(files) != list:
            log.info('it is a <input> tag.')
            self.upload_by_input(files)
        elif not autoit:
            self.upload_by_win32(files)
        else:
            self.upload_by_autoit(files)



