#include <linux/module.h>    // included for all kernel modules
#include <linux/kernel.h>    // included for KERN_INFO
#include <linux/init.h>      // included for __init and __exit macros

#include <linux/proc_fs.h>
//#include <linux/seq_file.h>

MODULE_LICENSE("GPL");
MODULE_AUTHOR("Clouds Lee");
MODULE_DESCRIPTION("Clouds Test Module");


#define CLSINFO(format,...) printk(KERN_ALERT "[CLS]%s: "format, __func__, ##__VA_ARGS__)


#define CLSINFOEX(format,...) \
{\
int cls_print(const char *fmt, ...);\
printk(KERN_ALERT "[CLS][EX]%s: "format, __func__, ##__VA_ARGS__);\
cls_print("[CLS][EX]%s: "format, __func__, ##__VA_ARGS__);\
}


/*======================================================================================================*/
/*Export Function Variable                                                                                       */
/*======================================================================================================*/
#define MAX_CHAR (4*1024)

struct _print_buffer
{
    char            buffer[MAX_CHAR];
    unsigned int    w_index;
    unsigned int    r_index;

} 
g_print_buffer =
{
    .w_index = 0,
    .r_index = 0,
    .buffer[0] = '\0',
};

/*======================================================================================================*/
/* Test Hook                                                                                            */
/*======================================================================================================*/

void test_hook_test( void )
{
    CLSINFOEX();
    {   
        unsigned long *ptest = NULL;

        *ptest = 0xFFFFFF;



    }

}


void test_hook_start( void )
{
    CLSINFOEX();

    {
        extern void cls_gator_start( void );
        cls_gator_start();
    }

}

void test_hook_read( void )
{
    CLSINFOEX();
    {
        extern int cls_gator_read( int **buffer , int *buffer_count );
        int     *pBuffer;
        int     count;
        int     i;


        cls_gator_read( &pBuffer, &count );
        CLSINFOEX("pBuffer = 0x%X\n", (unsigned int)(unsigned long)pBuffer );

        if( pBuffer )
        {

            for( i = 0; i < count; i++ )
            {
                CLSINFOEX("count[%d] = %d\n", i, pBuffer[i] );
            }   
        }else
        {
            CLSINFOEX("pBuffer is NULL\n");
        }
    }
}

void test_hook_status( void )
{
    CLSINFOEX();
    {
        extern void cls_gator_status( void );
        cls_gator_status( );
    }
}

void test_hook_loopstart( void )
{
    CLSINFOEX();
    {
        extern void cls_gator_loop_start( void );
        cls_gator_loop_start();
    }
}

void test_hook_loopstop( void )
{
    CLSINFOEX();
    {
        extern void cls_gator_loop_stop( void );
        cls_gator_loop_stop();
    }
}




/*======================================================================================================*/
/* Proc                                                                                                 */
/*======================================================================================================*/
static int b_open = 0;

int open_callback(struct inode *inode, struct file *file)
{
    CLSINFOEX();

    b_open = 1;

    return 0;
}

ssize_t read_callback(struct file *file, char __user *user, size_t size/*size user want to read*/, loff_t *loff)
{
    int ret = 0;

    CLSINFO();

    CLSINFO("size:%d\n",(int)size);
    CLSINFO("loff:0x%X\n",(unsigned int) *loff);

    CLSINFO("(r,w)=(%d,%d)\n",g_print_buffer.r_index, g_print_buffer.w_index );

    if( b_open )
    {
        ret = sprintf( user, &(g_print_buffer.buffer[g_print_buffer.r_index]) );
        g_print_buffer.r_index += ret;

        if( g_print_buffer.r_index == g_print_buffer.w_index ){
            g_print_buffer.r_index = g_print_buffer.w_index = 0;
        }
        g_print_buffer.buffer[g_print_buffer.r_index] = '\0';

        b_open = 0;
    }
    CLSINFO("(r,w)=(%d,%d), %d char read\n",g_print_buffer.r_index, g_print_buffer.w_index, ret );


    return ret;
}

ssize_t write_callback(struct file *file, const char __user *user/*user write buffer*/ , size_t size, loff_t *loff)
{
    CLSINFOEX();

    CLSINFOEX("Input:%s\n", user);
    CLSINFOEX("size:%d\n",(int)size);
    CLSINFOEX("loff:0x%X\n",(unsigned int) *loff);

    /*user test hook*/
    if( strstr( user, "test" ) == user ){
        test_hook_test();
    }

    if( strstr( user, "start" ) == user ){
        test_hook_start();
    }

    if( strstr( user, "read" ) == user ){
        test_hook_read();
    }

    if( strstr( user, "status" ) == user ){
        test_hook_status();
    }

    if( strstr( user, "loopstart" ) == user ){
        test_hook_loopstart();
    }

    if( strstr( user, "loopstop" ) == user ){
        test_hook_loopstop();
    }





    return size;
}



struct proc_dir_entry *proc_file_entry;

static const struct file_operations proc_file_fops = {
    .owner = THIS_MODULE,
    .open  = open_callback,
    .read  = read_callback,
    .write = write_callback,
};

int cls_proc_create( void )
{
    CLSINFOEX();

    proc_file_entry = proc_create("clouds", 0, NULL, &proc_file_fops);
    if(proc_file_entry == NULL)
        return -ENOMEM;


    return 0;
}

void cls_proc_remove( void )
{
    CLSINFOEX();

    proc_remove( proc_file_entry );
}


static int __init clouds_init(void)
{
    CLSINFOEX();

    cls_proc_create();

    return 0;    // Non-zero return means that the module couldn't be loaded.
}

static void __exit clouds_cleanup(void)
{
    CLSINFOEX();

    cls_proc_remove();
}

module_init(clouds_init);
module_exit(clouds_cleanup);


/*==================================================================
    EXPORT function
  ==================================================================*/

void cls_foo( void )
{
    CLSINFOEX();
}


int cls_print(const char *fmt, ...)
{
    va_list args;
    int max_buffer_avl;
    int char_written;
    static char tmp_buffer[1024];

    max_buffer_avl = MAX_CHAR - g_print_buffer.w_index -1;

    CLSINFO("(r,w)=(%d,%d), max_avl = %d \n",g_print_buffer.r_index, g_print_buffer.w_index, max_buffer_avl );

    va_start(args, fmt);
    vsnprintf( tmp_buffer, 1024, fmt, args);
    va_end(args);

    char_written = strlen( tmp_buffer );
    if( char_written >  max_buffer_avl )
    {
        /*Full!!*/
        CLSINFO("Buffer full!Restart\n");
        g_print_buffer.w_index = 0;
        g_print_buffer.r_index = 0;
        g_print_buffer.buffer[0] = '\0';

    }

    strcat( &(g_print_buffer.buffer[g_print_buffer.w_index]), tmp_buffer );

    g_print_buffer.w_index += char_written;

    CLSINFO("(r,w)=(%d,%d), %d char write\n",g_print_buffer.r_index, g_print_buffer.w_index, char_written );

    return char_written;

}


EXPORT_SYMBOL( cls_foo );
EXPORT_SYMBOL( cls_print );


