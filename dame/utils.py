#/usr/bin/env python
#-*- coding: utf-8

import os
import sys
import pkgutil

from PIL import Image
import pygame


def get_root_path(import_name):
    mod = sys.modules.get(import_name)

    if mod and hasattr(mod, '__file__'):
        return os.path.dirname(os.path.abspath(mod.__file__))

    loader = pkgutil.get_loader(import_name)

    if loader is None or import_name == '__main__':
        return os.getcwd()

    if hasattr(loader, 'get_filename'):
        filepath = loader.get_filename(import_name)
    else:
        __import__(import_name)
        filepath = sys.modules[import_name].__file__

    return os.path.dirname(os.path.abspath(filepath))


def import_string(import_name):
    assert isinstance(import_name, string_types)

    import_name = str(import_name)

    if ':' in import_name:
        module, obj = import_name.split(':', 1)
    elif '.' in import_name:
        module, obj = import_name.rsplit('.', 1)
    else:
        return __import__(import_name)

    if isinstance(obj, unicode):
        obj = obj.encode('utf-8')
    try:
        return getattr(__import__(module, None, None, [obj]), obj)

    except (ImportError, AttributeError):
        modname = module + '.' + obj
        __import__(modname)
        return sys.modules[modname]


def transparent(img, color):
    bgcolor = (color[0], color[1], color[2], 255)
    width, height = img.size
    img = img.convert('RGBA')

    pix = img.load()

    for w in xrange(width):
        for h in xrange(height):
            if pix[w, h] == bgcolor:
                pix[w, h] = (255, 255, 255, 0)

    img.format = 'png'
    return img


def crop_image(src_img, size, position):
    w, h = size
    width, height = src_img.size
    x, y = position

    wrange = width // w
    hrange = height // h

    return src_img.crop((x, y, x+w, y+h))
