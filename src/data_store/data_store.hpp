#ifndef TEST_HEADER_HPP_
#define TEST_HEADER_HPP_

#include <stdio.h>

#include "SMS_MemMap_Sample_V8/SharedMemory.h"

class DataStore {
private:
    SharedMemory *_shared_data;

public:
    DataStore();

    SharedMemory* get_shared_data();
    void set_windspeed(float windspeed);
};

#endif