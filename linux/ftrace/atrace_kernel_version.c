#define DEFAULT_POLLING_PERIOD_NS (1000000)

/*
 * mini trace system
 */
#define KATRACE_MESSAGE_LENGTH 1024

static noinline int tracing_mark_write(const char *buf)
{
	TRACE_PUTS(buf);
	return 0;
}

#define KATRACE_BEGIN(name) katrace_begin_body(name)
void katrace_begin_body(const char* name)
{
    char buf[KATRACE_MESSAGE_LENGTH];

    int len = snprintf(buf, sizeof(buf), "B|%d|%s", /*0*/ task_pid_nr(current) /*getpid()*/, name);
    if (len >= (int) sizeof(buf)) {
        LOG_DBG("Truncated name in %s: %s\n", __FUNCTION__, name);
        len = sizeof(buf) - 1;
    }
    tracing_mark_write(buf);
}


#define WRITE_MSG(format_begin, format_end, pid, name, value) { \
    char buf[KATRACE_MESSAGE_LENGTH]; \
    int len = snprintf(buf, sizeof(buf), format_begin "%s" format_end, pid, \
        name, value); \
    if (len >= (int) sizeof(buf)) { \
        /* Given the sizeof(buf), and all of the current format buffers, \
         * it is impossible for name_len to be < 0 if len >= sizeof(buf). */ \
        int name_len = strlen(name) - (len - sizeof(buf)) - 1; \
        /* Truncate the name to make the message fit. */ \
        LOG_DBG("Truncated name in %s: %s\n", __FUNCTION__, name); \
        len = snprintf(buf, sizeof(buf), format_begin "%.*s" format_end, pid, \
            name_len, name, value); \
    } \
    tracing_mark_write(buf); \
}


#define KATRACE_INT(name, value) katrace_int_body(name, value)
void katrace_int_body(const char* name, int32_t value)
{
    WRITE_MSG("C|%d|", "|%d", /*0*/ task_pid_nr(current)/*getpid()*/, name, value);
}



void main(void)
{
	static int count = 0;

	count++;
	count = count % 10;

	KATRACE_INT("CLS_COUNTER", count);
}

