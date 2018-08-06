#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

class ErrParam(Exception):
    pass
class ErrParamType(ErrParam):
    pass

class ErrIP(ErrParam):
    pass
class ErrPort(ErrParam):
    pass

class ErrParamTooMin(ErrParam):
    pass
class ErrParamTooMax(ErrParam):
    pass

class ErrParamNotIP(ErrParam):
    pass
class ErrParamNotPort(ErrParam):
    pass