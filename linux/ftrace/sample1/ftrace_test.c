#include <linux/module.h>    // included for all kernel modules
#include <linux/kernel.h>    // included for KERN_INFO
#include <linux/init.h>      // included for __init and __exit macros

#include <linux/hrtimer.h>	//For Timer

MODULE_LICENSE("GPL");
MODULE_AUTHOR("CloudsLee");
MODULE_DESCRIPTION("A Simple Hello World module");

#define CREATE_TRACE_POINTS
#include "mypoint.h"

/*Start a timer to test*/

static struct hrtimer htimer;
static ktime_t kt_periode;

static enum hrtimer_restart timer_function(struct hrtimer * timer)
{
	static int count = 1;

	count++;
	// @Do your work here. 
	trace_mytracepoint(count);
	printk(KERN_EMERG "[CLS] Timer %d!\n", count);




	hrtimer_forward_now(timer, kt_periode);

	return HRTIMER_RESTART;
}


static void timer_init(void)
{
	kt_periode = ktime_set(1, 0); //seconds,nanoseconds
	hrtimer_init (& htimer, CLOCK_REALTIME, HRTIMER_MODE_REL);
	htimer.function = timer_function;
	hrtimer_start(& htimer, kt_periode, HRTIMER_MODE_REL);
}

static void timer_cleanup(void)
{
	hrtimer_cancel(& htimer);
}



/*Module initial*/

static int __init hello_init(void)
{
	int i=10;
	while(i--){
		printk(KERN_EMERG "[CLS] Hello world!\n");
		trace_mytracepoint(1);
	}

	printk(KERN_EMERG "[CLS] Timer Initial\n");
	timer_init();

	return 0;    // Non-zero return means that the module couldn't be loaded.
}

static void __exit hello_cleanup(void)
{
	int i=10;
	while(i--) {
		printk(KERN_EMERG "[CLS] Cleaning up module.\n");
		trace_mytracepoint(0);
	}
	
	printk(KERN_EMERG "[CLS] Timer Cleanup\n");
	timer_cleanup();
}

module_init(hello_init);
module_exit(hello_cleanup);

