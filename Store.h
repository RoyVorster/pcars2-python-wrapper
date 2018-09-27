#ifndef STORE_H
#define STORE_H

#include "SMS_MemMap_Sample_V8/SharedMemory.h"

#include <windows.h>
#include <string>

#define MAPPED_OBJECT "$pcars2$"

class Store {
private:
    const SharedMemory* data;
    HANDLE file_handle;

public:
    Store();

    void map_file();
    void update();

    unsigned int steps;
    unsigned int step_size;

    SharedMemory* local;
    ~Store();
};

#endif // STORE_H
