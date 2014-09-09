obj-m += clouds_module.o

#LFK specific
TARGET_PRODUCT=k95v2_1
export TARGET_PRODUCT

#Cannot assign tool chain path here for latter make file use,dont know why
#$(info $(PATH))
#PATH:=~/P4/ws_clouds.lee_hello/ALPS_SW/MP/KK1.MP11/alps/prebuilts/gcc/linux-x86/arm/arm-linux-androideabi-4.6/bin:$(PATH)
#export PATH
#$(info $(PATH))


#LFK use out directory as kernel buil directory
alps:
	make -C /proj/mtk02679/P4/ws_clouds.lee_hello/ALPS_SW/MP/KK1.MP11/alps/out/target/product/k95v2_1/obj/KERNEL_OBJ M=$(PWD) modules

clean_alps:
	make -C /proj/mtk02679/P4/ws_clouds.lee_hello/ALPS_SW/MP/KK1.MP11/alps/out/target/product/k95v2_1/obj/KERNEL_OBJ M=$(PWD) clean

all:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) modules

clean:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) clean

