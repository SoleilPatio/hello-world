#include <linux/module.h>    // included for all kernel modules
#include <linux/kernel.h>    // included for KERN_INFO
#include <linux/init.h>      // included for __init and __exit macros

/*of include*/
#include <linux/of.h>
#include <linux/of_address.h>

MODULE_LICENSE("GPL");
MODULE_AUTHOR("Lakshmanan");
MODULE_DESCRIPTION("A Simple Hello World module");


#if 0

SMI_COMMON@0x14017000 {
			compatible = "LFK,SMI_COMMON";
			reg = <0x14017000 0x1000>,  /* SMI_COMMON_EXT */
				<0x14016000 0x1000>,  /* LARB 0 */
				<0x16010000 0x1000>,  /* LARB 1 */
				<0x15001000 0x1000>;  /* LARB 2 */  
		};

#endif


void device_tree_test( void )
{
	int i;
	struct device_node	*node = NULL;
	struct resource res;
	unsigned long		addr;

	node = of_find_compatible_node(NULL, NULL, "LFK,SMI_COMMON");
	
	for( i = 0; i < 10; i++ )
	{

		/*
		 * Get PHY Address
		 */
		if( of_address_to_resource(node, i /*index*/, &res) == 0 ){

			printk(KERN_EMERG "[CLS][%d] phy addr = 0x%lx size=%ld\n", i , (unsigned long)res.start, (unsigned long)resource_size(&res) );


			/*
			 * Get Address and ioremap it
			 */
			addr = (unsigned long)of_iomap(node, i);
			of_node_put(node);

			printk(KERN_EMERG "[CLS][%d] addr = 0x%lx\n",i, addr );
		}
	}

}


static int __init hello_init(void)
{
	int i=10;
	while(i--)
		printk(KERN_EMERG "[CLS] Hello world!\n");


	device_tree_test();

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

