#include <linux/module.h>    // included for all kernel modules
#include <linux/kernel.h>    // included for KERN_INFO
#include <linux/init.h>      // included for __init and __exit macros

#include <linux/proc_fs.h>
//#include <linux/seq_file.h>

MODULE_LICENSE("GPL");
MODULE_AUTHOR("Clouds Lee");
MODULE_DESCRIPTION("Clouds Test Module");

#define CLSINFO(format,...) printk(KERN_ALERT "[CLS]%s: "format, __func__, ##__VA_ARGS__);



static int b_open = 0;

int open_callback(struct inode *inode, struct file *file)
{
    CLSINFO();

    b_open = 1;

    return 0;
}

ssize_t read_callback(struct file *file, char __user *user, size_t size/*size user want to read*/, loff_t *loff)
{
    int ret = 0;

    CLSINFO();

    CLSINFO("size:%d\n",size);
    CLSINFO("loff:0x%X\n",(unsigned int) *loff);

    if( b_open )
    {
        ret = sprintf( user,"I am clouds\n");
        b_open = 0;
    }


    return ret;
}

ssize_t write_callback(struct file *file, const char __user *user/*user write buffer*/ , size_t size, loff_t *loff)
{
    CLSINFO();

    CLSINFO("Input:%s\n", user);
    CLSINFO("size:%d\n",size);
    CLSINFO("loff:0x%X\n",(unsigned int) *loff);

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
    CLSINFO();

    proc_file_entry = proc_create("clouds", 0, NULL, &proc_file_fops);
    if(proc_file_entry == NULL)
        return -ENOMEM;


    return 0;
}

void cls_proc_remove( void )
{
    CLSINFO();

    proc_remove( proc_file_entry );
}



static int __init clouds_init(void)
{
    CLSINFO();

    cls_proc_create();

    return 0;    // Non-zero return means that the module couldn't be loaded.
}

static void __exit clouds_cleanup(void)
{
    CLSINFO();

    cls_proc_remove();
}

module_init(clouds_init);
module_exit(clouds_cleanup);

