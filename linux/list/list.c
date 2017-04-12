#define  MET_USER_EVENT_SUPPORT /*Turn met user event*/
#define DEBUG 1

/*kmalloc*/
#include <linux/slab.h>



#define MAX_CHAR 31
struct client_list {
	char name[MAX_CHAR+1];
	int on;
	unsigned int period_multiply;
	struct list_head list; /*[CLS]: every entry has its own list_head , and need to be initialized*/
};


static LIST_HEAD(udmet_client_head); /*[CLS]: this declare and init the "list head", use "list head" to do operation with it*/


void add_new_entry(char *mod_name, MET_UDMET_POLLING_FUNC polling_func, unsigned int period_multiply)
{
	struct client_list *clientPtr = kmalloc(sizeof(struct client_list), GFP_KERNEL);

	if (clientPtr != NULL) {

		strncpy(clientPtr->name, mod_name, MAX_CHAR);
		clientPtr->on = 0;
		clientPtr->polling_func = polling_func;
		clientPtr->period_multiply = period_multiply;
		INIT_LIST_HEAD(&clientPtr->list); /*[CLS]: every entry has its own list_head , and need to be initialized*/

		list_add(&clientPtr->list, &udmet_client_head); /*[CLS]: insert entry to list*/
	}
}


static void traversal_list(void)
{
	struct list_head *iter;
	struct client_list *clientPtr;

	/*[CLS]: Traversal list*/
	list_for_each(iter, &udmet_client_head) { 
		clientPtr = list_entry(iter, struct client_list, list);
		clientPtr->on = 0;
	}

}

