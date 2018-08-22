import enum

class EState(enum.Enum):
    '''
    枚举类型命名
        E 开头
        大写开头驼峰式命名
    枚举变量命名
        大写开头驼峰式命名
    '''
    Null = 0
    Connected = 1


 
class CBaseClass(object): 
    '''
    类名 
        C 开头
        大写开头驼峰式命名
    以object作为继承类
    '''

    def __init__(self, u32Id):  
        '''
        构造函数
        '''

        '''
        成员变量 
            _ + 变量命名
        '''
        self._strVar = 'inst_var'  
        self._u8Var = 'inst_var'  

    def obj_method(self):  
        '''
        模块或者public方法
        '''
        pass

    def _protected_method(self):  
        '''
        模块或者protected方法，以单个下划线开头
        其他模块import * from时候不会导入
        '''
        pass

    def __private_method(self):  
        '''
        私有方法，以双下划线开头
        '''
        pass

    @classmethod
    def class_method(cls, var):  
        '''
        类方法，第一个参数是cls，用classmethod修饰
        '''
        print(var)

    @staticmethod
    def static_method(param):  
        '''
        静态方法，没有self或者cls作为第一个参数，同时以staticmethod修饰
        '''
        print(param)

class CDerivedClass(CBaseClass):
    def __init__(self):  
        super().__init__(1) # 基类构造函数


'''
变量命名
'''
u8Var   = 1 #uint8
u16Var  = 1 #uint16
u32Var  = 1 #uint32
u64Var  = 1 #uint64

i8Var   = 1 #int8
i16Var  = 1 #int16
i32Var  = 1 #int32
i64Var  = 1 #int64

fVar = 1 #float
dVar = 1 #double

strVar = 'a' #string
bVar = True #bool
oCBaseClassVar = CBaseClass(1) #class
eEStateVar = EState.Connected #enum
