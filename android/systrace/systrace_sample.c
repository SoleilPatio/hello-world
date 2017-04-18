
/*[CLS]: NOTE: How to enable?
 *
 * 	adb shell "setprop debug.atrace.tags.enableflags 0xFFFFFFFF"
 *	adb shell "atrace --poke_services"   ==> LFK special
 *
 */

#include <utils/Trace.h> /*[CLS]:use this*/
/*#include <android/trace.h>*/


#define L1(def) #def
#define L2(def) L1(def)

/*[CLS]:check if ATRACE_TAG defined*/
#pragma message ("[CLS]ATRACE_TAG=" L2(ATRACE_TAG))

/*[CLS]:check if ATRACE_CALL defined*/
#pragma message ("[CLS]ATRACE_CALL()=" L2(ATRACE_CALL()))



void my_test_function(void)
{
	/*[CLS]:just call this*/
	ATRACE_CALL();

	ALOGD("[CLS] test"); /*Logcat message*/
}


/*[CLS]:another way to do atrace*/
void my_test_function2(void)
{
	ATrace_beginSection("my_test_function2");

	... // trace-worthy work here

	ATrace_endSection();
}


