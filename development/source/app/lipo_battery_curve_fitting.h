#ifndef _LIPO_BATTERY_CURVE_FITTING_H_
#define _LIPO_BATTERY_CURVE_FITTING_H_

#include "platform_common.h"

#define LIPO_CUTOFF_LEVEL_MV     (3000)
#define LIPO_LOWEST_LEVEL_MV     (3100)
#define LIPO_LOWER_PART_MV       (3400)
#define LIPO_UPPER_PART_MV       (3900)
#define LIPO_HIGHEST_LEVEL_MV    (4200)
#define LIPO_LOWER_PART_PERCENT  (5)
#define LIPO_UPPER_PART_PERCENT  (10)
#define LIPO_MIDDLE_PART_PERCENT (100 - LIPO_LOWER_PART_PERCENT - LIPO_UPPER_PART_PERCENT)
#define LIPO_UPPER_PART_RANGE    (LIPO_HIGHEST_LEVEL_MV - LIPO_UPPER_PART_MV)
#define LIPO_MIDDLE_PART_RANGE   (LIPO_UPPER_PART_MV - LIPO_LOWER_PART_MV)
#define LIPO_LOWER_PART_RANGE    (LIPO_LOWER_PART_MV - LIPO_LOWEST_LEVEL_MV)

STATIC_INLINE_T s32 LiPoVoltageToPercentage(s32 voltage) {

    s32 percentage;

    if(voltage > LIPO_HIGHEST_LEVEL_MV)                                 //it is in higher than operating range
        percentage = 100;
    else if(voltage > LIPO_UPPER_PART_MV)                               //it is in upper part of operating range
        percentage = ((voltage - LIPO_UPPER_PART_MV)*LIPO_UPPER_PART_PERCENT)/LIPO_UPPER_PART_RANGE   + (100 - LIPO_UPPER_PART_PERCENT);
    else if(voltage > LIPO_LOWER_PART_MV)                               //it is in middle part of operating range
        percentage = ((voltage - LIPO_LOWER_PART_MV)*LIPO_MIDDLE_PART_PERCENT)/LIPO_MIDDLE_PART_RANGE + (LIPO_LOWER_PART_PERCENT);
    else if(voltage > LIPO_LOWEST_LEVEL_MV)                             //it is in lower part of operating range
        percentage = ((voltage - LIPO_LOWEST_LEVEL_MV)*LIPO_LOWER_PART_PERCENT)/LIPO_LOWER_PART_RANGE + (0);                        
    else if(voltage > LIPO_LOWEST_LEVEL_MV)                             //it is lower than operating range
        percentage = 0;
    else                                                                //not ready to report yet
        percentage = 100;

    return percentage;
}

#endif
