/*
 * Copyright (C) 2015 MediaTek Inc.
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License version 2 as
 * published by the Free Software Foundation.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * GNU General Public License for more details.
 */

#undef TRACE_SYSTEM
#define TRACE_SYSTEM sample_events

#if !defined(_TRACE_SAMPLE_EVENTS_H) || defined(TRACE_HEADER_MULTI_READ)
#define _TRACE_SAMPLE_EVENTS_H

#include <linux/tracepoint.h>


TRACE_EVENT(sample_tracing,

	TP_PROTO(int value1, unsigned long value2),

	TP_ARGS(value1, value2),

	TP_STRUCT__entry(
		__field(int, value1)
		__field(unsigned long, value2)
	),

	TP_fast_assign(
		__entry->value1 = value1;
		__entry->value2 = value2;
	),

	TP_printk("value1=%d value2=%ld",
		__entry->value1, __entry->value2)
);

#endif /* _TRACE_SAMPLE_EVENTS_H */

/* This part must be outside protection */
#undef TRACE_INCLUDE_PATH
#define TRACE_INCLUDE_PATH .			/*[CLS]: Here onlu can be set ".", not path name. You must add include path in makefile*/
#undef TRACE_INCLUDE_FILE
#define TRACE_INCLUDE_FILE sample_events
#include <trace/define_trace.h>
