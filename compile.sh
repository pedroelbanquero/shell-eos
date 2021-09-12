# compiler eos shell metamorph

cython3 --embed -o shelleos.c shell-eos.py
gcc -static shelleos.c -o shelleos -I /usr/include/python3.5 $(pkg-config --libs --cflags python3) -lpython2.7 -lm -lutil -ldl -lz -lexpat -lpthread -lc



