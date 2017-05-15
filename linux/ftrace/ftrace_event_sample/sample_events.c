#define  MET_USER_EVENT_SUPPORT /*Turn met user event*/

#include <mt-plat/met_drv.h>

/*your ftrace event difinition header file*/
/*[CLS]: 
	1st. define CREATE_TRACE_POINTS
	2nd. then include "sample_event.h" to create trace point functions

   if you use DEFINE_TRACE() macro, then no node in sys/kernel/debug/tracing/events/ been found
*/

#define CREATE_TRACE_POINTS
#include "sample_events.h"


/*
 * Sample Code
 */
static void sample_polling1(unsigned long long stamp, int cpu)
{
	static int value1;
	static unsigned long value2 = 10;


	value1++;
	value2++;
	/* FTRACE tag */
	trace_sample_tracing(value1, value2);


	met_tag_oneshot(0, "vpu-polling1", 1);
	met_tag_oneshot(0, "vpu-polling1", 0);

}


