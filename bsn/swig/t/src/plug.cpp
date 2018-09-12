#include "plug.h"
#include <sys/shm.h>
#include <stdlib.h>

int add(int ia, int ib) {
    return ia + ib;
}

int test_shm_new()
{
    return shm_new(12345, 4096);
}


int shm_new(int32_t key, uint32_t size) 
{
    int iShmId = shmget(key, size, IPC_CREAT | IPC_EXCL | 0666);
    return iShmId;
}

int shm_get_id(int32_t key) 
{
    int iShmId = shmget(key, 0, 0666);
    return iShmId;
}

void* shm_attach(int key)
{
    return shmat(key, NULL, 0);
}

int shm_delete(int iShmId)
{
    return shmctl(iShmId, IPC_RMID, NULL);
}

int shm_detach(void const * pVoid)
{
    return shmdt(pVoid);
}

int shm_size(int iShmId)
{
    struct shmid_ds buf;
    int iFlag = shmctl(iShmId, IPC_STAT, &buf);
    if( iFlag == -1 )
    {
        return -1;
    }
    return buf.shm_segsz;
}