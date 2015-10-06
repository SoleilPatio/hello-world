/* 
 * DEBUG must place at the first line of .c (before linux header file include,
 * or the pr_debug won't take effect.
 */
#define DEBUG
 
#include <linux/module.h>    // included for all kernel modules
#include <linux/kernel.h>    // included for KERN_INFO
#include <linux/init.h>      // included for __init and __exit macros

MODULE_LICENSE("GPL");
MODULE_AUTHOR("Lakshmanan");
MODULE_DESCRIPTION("A Simple Hello World module");

#define CLSINFO(format,...) pr_debug(KERN_ALERT "[CLSINFO]%s: "format, __func__, ##__VA_ARGS__);

static int __init hello_init(void)
{
    int i=10;
    while(i--){
        printk(KERN_EMERG "[CLS] Hello world!pr_debug test\n");
	CLSINFO("HiHi!%s\n","Clouds");
	pr_debug("Pure Debug\n");
    }
    return 0;    // Non-zero return means that the module couldn't be loaded.
}

static void __exit hello_cleanup(void)
{
    int i=10;
    while(i--)
        printk(KERN_EMERG "[CLS] Cleaning up module.\n");
}

module_init(hello_init);
module_exit(hello_cleanup);

