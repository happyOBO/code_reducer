rm -f a.out
gcc -o a.out lighttpd_bug.c 2> /dev/null || exit 1
./a.out
if [ $? -eq 134 ]; then
    exit 0
else
    exit 1
fi
