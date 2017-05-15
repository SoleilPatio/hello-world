/*
 * [CLS]:
 * 1. 屬於sysfs的變形 (/sys/class/misc/), 應該是sysfs的wrapper
 * 2. sysfs跟kernel object 都是為了device driver服務產生
 * 3. misc driver使用major number 10 , 大家共用這個major number
 */

/*
 * [CLS]:三種linux file system
 * procfs: proc on /proc  (kernel 交換訊息)
 *	struct proc_dir_entry *proc_mkdir()
 * 	struct proc_dir_entry *proc_create()
 *
 * debugfs: debugfs on /sys/kernel/debug (debug用)
 * 	struct dentry *debugfs_create_dir()
 * 	struct dentry *debugfs_create_file()
 *
 *		(*1):procfs & debugfs較相似，可以用seq_*實現,都用"struct file_operations"
 *		(*2):struct file_operations:
 *			owner, read, write, llseek,.....一狗票...
 *
 *
 * sysfs:  sysfs on /sys  (device driver 交換訊息)
 *	struct kobject *kobject_create_and_add()
 *	int sysfs_create_file()
 *	int sysfs_create_link()
 *	int device_create_file()
 *
 *		(*1):沒有struct file_operations，而是用 "struct device_attribute"
 *		(*2): struct device_attribute:
 * 	 		show,store ==> 就只有這兩個
 *
 */



static const struct file_operations mydev_file_ops = {
                .owner = THIS_MODULE
};

struct miscdevice mydev_miscdevice = {
                .minor = MISC_DYNAMIC_MINOR,
                .name = "mydev",
                .mode = 0664,
                .fops = &mydev_file_ops
};






static ssize_t ksym_show(struct device *dev, struct device_attribute *attr, char *buf)
{
	int i;

	mutex_lock(&dev->mutex);
	i = snprintf(buf, PAGE_SIZE, "%s\n", "hello");
	mutex_unlock(&dev->mutex);
	return i;


}

static ssize_t ksym_store(struct device *dev, struct device_attribute *attr, const char *buf, size_t count)
{
	mutex_lock(&dev->mutex);
	kstrtoint(buf, 10, &var);
	mutex_unlock(&dev->mutex);
	return count;
}

/*
 * [CLS]:
 * 1.這裡create 一個 device_attribute "資料結構"
 * 2.一個device_attribute 就是一個node file的敘述
 * 3.等等使用device_create_file()將他實際create出來，需要依附在一個device身上
*/
static DEVICE_ATTR(ksym, 0664, ksym_show, ksym_store);
/*
 * <<<<<
 * #define DEVICE_ATTR(_name, _mode, _show, _store) \
 *		struct device_attribute dev_attr_##_name = __ATTR(_name, _mode, _show, _store)
 * >>>>>
 */

/*
<<<<<
		==> in <linux/sysfs.h>:
		struct attribute {
			const char *name;
			umode_t mode;
			#ifdef CONFIG_DEBUG_LOCK_ALLOC
			bool ignore_lockdep:1;
			struct lock_class_key *key;
			struct lock_class_key skey;
			#endif
		};


		==> in <linux/device.h>:
		//interface for exporting device attributes
		struct device_attribute {
			struct attribute attr;
			ssize_t (*show)(struct device *dev, struct device_attribute *attr,
					char *buf);
			ssize_t (*store)(struct device *dev, struct device_attribute *attr,
					const char *buf, size_t count);
		};
>>>>>
*/




void main()
{

	/*
	 * [CLS]: step 1
	 *  1. 建立一個 名為 "mydev" 的 struct device
	 *  2. 在 /sys/class/misc/ 建立一個 "mydev" 的目錄(groups)
	 *
	 */

	ret = misc_register(&mydev_miscdevice); /*[CLS]:會填入mydev_miscdevice.this_device ( struct device 結構)*/
	/*
	 <<<<<
		 dev = MKDEV(MISC_MAJOR, misc->minor); ==> 建立 (majoe,minor)

		 misc->this_device = device_create_with_groups(
					 misc_class, ==> 統一建立的 class.  misc_class = class_create(THIS_MODULE, "misc");
					 misc->parent, ==> parent struct device
					 dev, ==> (major, minor) pair
					 (void*) misc,  ==> data pass for callback?
					 misc->groups, ==> list of attribute grops to be created
					 "%s",  ==> string for the device name
					 misc->name
	 	 	 	 	 );
	 >>>>>
	 */



	/*
	 * [CLS]:step 2
	 * 為何要設定dma ops?
	 */
	arch_setup_dma_ops(mydev_miscdevice.this_device, 0, 0, NULL, false);
	/*
	>>>>>
		dev->archdata.dma_ops = &swiotlb_dma_ops;
	<<<<<
	*/


	/*
	 * [CLS]:step 3
	 * Create device node
	 * dev_attr_ksym : 是之前 DEVICE_ATTR(ksym, 0664, ksym_show, ksym_store) 建立的"struct device_attribute" instance
	 */

	device_create_file(mydev_miscdevice.this_device, &dev_attr_ksym);

}

