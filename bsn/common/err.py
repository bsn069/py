#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

class ErrParam(Exception):
    pass
class ErrParamType(ErrParam):
    pass
class ErrParamTooMin(ErrParam):
    pass
class ErrParamTooMax(ErrParam):
    pass