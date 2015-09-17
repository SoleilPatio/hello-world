#undef TRACE_SYSTEM
#define TRACE_SYSTEM clouds

#if !defined(_MYPOINT_H) || defined(TRACE_HEADER_MULTI_READ)
#define _MYPOINT_H

#include <linux/tracepoint.h>

/*
 * Tracepoint for calling kthread_stop, performed to end a kthread:
 */
TRACE_EVENT(mytracepoint,

	TP_PROTO(int arg),

	TP_ARGS(arg),

	TP_STRUCT__entry(
		__field(	int,	arg			)
	),

	TP_fast_assign(
		__entry->arg	= arg;
	),

	TP_printk("[CLS] arg=%d", __entry->arg)
);

#endif /* _MYPOINT_H */

/* This part must be outside protection */
#undef TRACE_INCLUDE_PATH
#define TRACE_INCLUDE_PATH .
#define TRACE_INCLUDE_FILE mypoint

/* This part must be outside protection */
#include <trace/define_trace.h>
