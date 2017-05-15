/*
 * [CLS]:
 * 1.屬於 debugfs (/sys/kernel/debug )
 *
 * debugds_XXXX: 只有create kernel_object for debugging, 沒有多一個device
 * misc_register: 則是真正create device
 */

/*
 * in linux/debugfs.h:
 *
 * debugfs_create_file – for creating a file in the debug filesystem.
 * debugfs_create_dir – for creating a directory inside the debug filesystem.
 * debugfs_create_symlink – for creating a symbolic link inside the debug filesystem.
 * debugfs_remove – for removing a debugfs entry from the debug filesytem.
 */



static int user_show(struct seq_file *s, void *unused)
{
	if (s)
		seq_printf(s, "hello:%d", 123);
	return 0;
}

static int user_open(struct inode *inode, struct file *file)
{
	return single_open(file, user_show, inode->i_private);
}

static ssize_t user_write(struct file *flip, const char __user *buffer, size_t count, loff_t *f_pos)
{
	tmp = kzalloc(count + 1, GFP_KERNEL);
	if (!tmp)
		return -ENOMEM;

	ret = copy_from_user(tmp, buffer, count);
	kfree(tmp);

	return ret;

}

static const struct file_operations user_fops = {
                .open = user_open,
                .write = user_write,

                .read = seq_read,
                .llseek = seq_lseek,
                .release = seq_release,
}


void main(void)
{
	struct dentry *debug_root;

	/*
	 * [CLS]: Create Directory
	 *  1. create a directory in "debugfs" filesystem
	 *  2. return a directory entry -- struct dentry
	 *  3. typically path : /sys/kernel/debug by mount -t debugfs none /sys/kernel/debug
	 *  4. CONFIG_DEBUG_FS must be on
	 */
	debug_root = debugfs_create_dir("my_group", NULL); /*==>create  /sys/kernel/debug/my_group/  */
	if (IS_ERR_OR_NULL(debug_root))
		LOG_ERR("Error!");
	/*
	 * [CLS]: Create File
	 *
	 */
	debug_file = debugfs_create_file("user", 0644, debug_root, (void*) NULL, &user_fops); /*==>create  /sys/kernel/debug/my_group/user  */
	if (IS_ERR_OR_NULL(debug_file))
		LOG_ERR("Error!");

}

/**********************************************************************************************/
/* 底下別種簡單做法
/**********************************************************************************************/
/*
 * [CLS]: alternative usage
 * 	也可以用別的做法來定義 struct file_operations
 */
static int user2_set(void *data, u64 val)
{
	my_variable = val & 0xf;
	return 0;
}

static int user2_get(void *data, u64 *val)
{
	*val = my_variable;
	return 0;
}


DEFINE_SIMPLE_ATTRIBUTE(user2_fops, user2_get, user2_set, "%llu\n"); /*[CLS]: fmt "%llu",用在read(get())的時候，在scnprintf()使用,用來show出資料*/
/*
 * <<<<<
		#define DEFINE_SIMPLE_ATTRIBUTE(__fops, __get, __set, __fmt)		\
		static int __fops ## _open(struct inode *inode, struct file *file)	\
		{									\
			__simple_attr_check_format(__fmt, 0ull);			\
			return simple_attr_open(inode, file, __get, __set, __fmt);	\
		}									\
		static const struct file_operations __fops = {				\
			.owner	 = THIS_MODULE,						\
			.open	 = __fops ## _open,					\
			.release = simple_attr_release,					\
			.read	 = simple_attr_read,					\
			.write	 = simple_attr_write,					\
			.llseek	 = generic_file_llseek,					\
		}
 * >>>>>
 *
 */





