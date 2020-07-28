# code reducer

## file tree

```
.
├── README.md
├── example
│   ├── Makefile
│   ├── a.out
│   ├── lighttpd_bug.c
│   ├── lighttpd_bug.c.orig.c
│   └── test.sh
└── reducer.py
```
## How to run

### 1. If you want to reduce your program code, you have to write ``test.sh``.

- [filename] : write your file name.
- [original program answer] : Output when running an existing program

```bash
rm -f a.out
gcc -o a.out [filename].c 2> /dev/null || exit 1
./a.out
if [ $? -eq [original program answer] ]; then
    exit 0
else
    exit 1
fi

```

### 2. Copy your origin program to ``[filename].c.orig.c`` and run ```reducer.py```

```bash
# reduce file : [filename].c original file : [filename].c.orig.c
cp [filename].c.orig.c [filename].c
python3 reducer.py [filename].c ./test.sh
```

## Tutorial
**The files in the tutorial are in the ``example`` folder.**

### 1. If you want to reduce your program code, you have to write ``test.sh``.

- I want to reduce program ``lighttpd_bug.c``

```bash
rm -f a.out
gcc -o a.out lighttpd_bug.c 2> /dev/null || exit 1
./a.out
if [ $? -eq 134 ]; then
    exit 0
else
    exit 1
fi

```

### 2. Copy your origin program to ``[filename].c.orig.c`` and run ```reducer.py```

1. copy ``lighttpd_bug.c`` file to ``lighttpd_bug.c.orgin.c``


```bash
# back up your original file
cp -f lighttpd_bug.c lighttpd_bug.c.orig.c
```

2. then command following codes.

```bash
cp lighttpd_bug.c.orig.c lighttpd_bug.c
python3 reducer.py lighttpd_bug.c ./test.sh
```

### output

```
$ cp lighttpd_bug.c.orig.c lighttpd_bug.c
$ python3 reducer.py lighttpd_bug.c ./test.sh
ORIGINAL FILE SIZE IS  29
./test.sh: line 3: 65049 Abort trap: 6           ./a.out
Delete 6 group...

./test.sh: line 3: 65135 Abort trap: 6           ./a.out
Delete 4 group...

./test.sh: line 3: 65161 Segmentation fault: 11  ./a.out
./test.sh: line 3: 65177 Abort trap: 6           ./a.out
Delete 12 group...

./test.sh: line 3: 65319 Abort trap: 6           ./a.out
Delete 2 group...

./test.sh: line 3: 65388 Abort trap: 6           ./a.out
Delete 17 group...

./test.sh: line 3: 65394 Segmentation fault: 11  ./a.out
./test.sh: line 3: 65400 Abort trap: 6           ./a.out
Delete 18 group...

./test.sh: line 3: 65417 Abort trap: 6           ./a.out
Delete 20 group...

./test.sh: line 3: 65424 Abort trap: 6           ./a.out
Delete 20 group...

./test.sh: line 3: 65430 Abort trap: 6           ./a.out
Delete 20 group...

./test.sh: line 3: 65437 Abort trap: 6           ./a.out
Delete 20 group...

./test.sh: line 3: 65443 Abort trap: 6           ./a.out
Delete 20 group...

./test.sh: line 3: 65449 Abort trap: 6           ./a.out
Delete 20 group...

===========================================
                Report                     
===========================================
original file's Total # of lines :  29
reduced file's Total # of lines :  20
```

