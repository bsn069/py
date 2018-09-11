#include <stdint.h>
int add(int ia, int ib);

int shm_new(int32_t key, uint32_t size);
void* shm_open(int key);

int test_shm_new();