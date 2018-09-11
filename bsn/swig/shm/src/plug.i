%module plug
 
%{
#include "plug.h"
%}
 

%typemap(in) int32_t,uint32_t {
    $1 = PyInt_AsLong($input);
}

int add(int ia, int ib);
int shm_new(int32_t key, uint32_t size);
int test_shm_new();

void* shm_open(int key);