

my_c_code_main.exe: my_c_code.c my_c_code.h my_c_code_main.c
	gcc -O2 -fopenmp my_c_code_main.c my_c_code.c -o my_c_code_main.exe -Wall -lm
