#include <linux/hrtimer.h>

static struct hrtimer hr_timer;

static enum hrtimer_restart vpu_profile_polling(struct hrtimer *timer)
{
	/*
	 * DO YOUR WORK!
	 */

#if 1
	hrtimer_forward_now(&hr_timer, ns_to_ktime(1000000)); /*1ms latter*/
	return HRTIMER_RESTART; /*[CLS]: if not call forward(), system will HANG!!!*/
#else
	return HRTIMER_NORESTART;
#endif
}



int init_vpu_profile_timer(void) {
	ktime_t ktime;

	ktime = ktime_set( 0, 1000000 ); /*[CLS]:1ms*/


	/*[CLS]: defined in ./include/linux/time.h
	 *	 list the available clocks in this system
	 */

	/*
	 * The IDs of the various system clocks (for POSIX.1b interval timers):
	 */
	/*
	#define CLOCK_REALTIME			0
	#define CLOCK_MONOTONIC			1
	#define CLOCK_PROCESS_CPUTIME_ID	2
	#define CLOCK_THREAD_CPUTIME_ID		3
	#define CLOCK_MONOTONIC_RAW		4
	#define CLOCK_REALTIME_COARSE		5
	#define CLOCK_MONOTONIC_COARSE		6
	#define CLOCK_BOOTTIME			7
	#define CLOCK_REALTIME_ALARM		8
	#define CLOCK_BOOTTIME_ALARM		9
	#define CLOCK_SGI_CYCLE			10	//Hardware specific
	#define CLOCK_TAI			11

	#define MAX_CLOCKS			16
	*/

	/*
	HRTIMER_MODE_ABS = 0x0,		//Time value is absolute
	HRTIMER_MODE_REL = 0x1,		//Time value is relative to now
	HRTIMER_MODE_PINNED = 0x02,	//Timer is bound to CPU
	HRTIMER_MODE_ABS_PINNED = 0x02,
	HRTIMER_MODE_REL_PINNED = 0x03, //[CLS] MET used for each core?
	*/

	hrtimer_init( &hr_timer, CLOCK_MONOTONIC, HRTIMER_MODE_REL );

	hr_timer.function = vpu_profile_polling;

	//hrtimer_start( &hr_timer, ktime, HRTIMER_MODE_REL );   /*[CLS]: should be OK*/
	hrtimer_start( &hr_timer, ns_to_ktime(1000000), HRTIMER_MODE_REL );



	return 0;

}

void stop_hrtimer(void)
{

	hrtimer_cancel(hr_timer);
}
