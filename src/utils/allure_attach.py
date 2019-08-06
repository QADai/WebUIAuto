# -*- encoding: utf-8 -*-
"""
@Author  : QADai
@Email   : daibiao83@126.com
"""
import pathlib
import allure
import sys
sys.path.append(r'../../')
sys.path.append(r'../')
sys.path.append(r'.')


def attach(screen_shot_path, png_display_name= "失败截图" ):
    if pathlib.Path(screen_shot_path).exists():
        with open(screen_shot_path, 'rb') as png:
            shot_path = png.read()
        allure.attach(png_display_name, shot_path, allure.attach_type.PNG)