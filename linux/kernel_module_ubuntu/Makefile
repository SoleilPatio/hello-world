obj-m += hello_module.o


#Cannot assign tool chain path here for latter make file use,dont know why
#$(info $(PATH))
#PATH:=~/P4/ws_clouds.lee_hello/ALPS_SW/MP/KK1.MP11/alps/prebuilts/gcc/linux-x86/arm/arm-linux-androideabi-4.6/bin:$(PATH)
#export PATH
#$(info $(PATH))



#Original
all:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) modules

clean:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) clean

