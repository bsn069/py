#include <stdint.h>
int add(int ia, int ib);

int shm_new(int32_t key, uint32_t size);
int shm_get_id(int32_t key);
int shm_delete(int iShmId);

int shm_size(int iShmId);

void* shm_attach(int key);
int shm_detach(void const * pVoid);

int test_shm_new();