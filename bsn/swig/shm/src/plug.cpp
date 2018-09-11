#include "plug.h"
#include <sys/shm.h>
#include <stdlib.h>

int add(int ia, int ib) {
    return ia + ib;
}

int shm_new(int32_t key, uint32_t size) 
{
    int iShmId = shmget(key, size, IPC_CREAT | IPC_EXCL);
    return iShmId;
}

int test_shm_new()
{
    return shm_new(12345, 4096);
}

void* shm_open(int key)
{
    return shmat(key, NULL, 0);
}
