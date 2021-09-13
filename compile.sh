# compiler eos shell metamorph

## python to c++
cython3 --embed -o shelleos.c shelleos.py  -X language_level=3
## compile c
gcc -static shelleos.c -o shelleos -I /usr/include/python3.5 $(pkg-config --libs --cflags python3) -lpython2.7 -lm -lutil -ldl -lz -lexpat -lpthread -lc



