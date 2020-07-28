all:
    cp lighttpd_bug.c.orig.c lighttpd_bug.c
    python3 reducer.py lighttpd_bug.c ./test.sh
    rm -rf a.out
clean:
    rm -rf a.out