#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from bsn.common import file_import_tree
file_import_tree.file_begin(__name__)

class ErrParam(Exception):
    pass
class ErrParamType(ErrParam):
    pass

class ErrIP(ErrParam):
    pass
class ErrHost(ErrParam):
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

class ErrState(Exception):
    pass
class ErrHadRun(Exception):
    pass
class ErrArg(Exception):
    pass

class ErrPkgLength(Exception):
    pass

class ErrListenFail(Exception):
    pass
class ErrConnectFail(Exception):
    pass

file_import_tree.file_end(__name__)