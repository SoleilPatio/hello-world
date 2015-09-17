obj-m += ftrace_test.o

#LFK specific
TARGET_PRODUCT=full_k35mv1_64-userdebug
export TARGET_PRODUCT

#Cannot assign tool chain path here for latter make file use,dont know why
#$(info $(PATH))
#PATH:=~/P4/ws_clouds.lee_hello/ALPS_SW/MP/KK1.MP11/alps/prebuilts/gcc/linux-x86/arm/arm-linux-androideabi-4.6/bin:$(PATH)
#export PATH
#$(info $(PATH))


#LFK use out directory as kernel buil directory
KERNEL_PATH=/proj/mtk02679/alps.l1.mp3.ppb/out/target/product/evb6735_64/obj/KERNEL_OBJ


alps:
	make ARCH=arm64 -C $(KERNEL_PATH)  M=$(PWD) modules

clean_alps:
	make ARCH=arm64 -C $(KERNEL_PATH)  M=$(PWD) clean

#Original
all:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) modules

clean:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) clean

