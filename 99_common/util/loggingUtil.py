#!/usr/bin/env python
# -*- coding: utf-8 -*-

from logging import getLogger, StreamHandler, FileHandler, DEBUG

def get_logger(name, log_filename):
    logger = getLogger(name)
    #handler = StreamHandler()
    handler = FileHandler(filename=log_filename)
    handler.setLevel(DEBUG)
    logger.setLevel(DEBUG)
    logger.addHandler(handler)
    logger.propagate = False
    return logger
