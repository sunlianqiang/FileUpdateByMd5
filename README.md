# FileUpdateByMd5
  using in mac shell, like: python fileUpdateByMd5.py srcdir destdir
  The script will run like this: 
    1. traversal the dest dir recursively and delete files and dirs recurvely which doesn't exist in src dir; 
    2. traversal the src dir recursively,
        a.  and copy files and dirs recurvely which doesn't exist in dest dir but existed in src dir;
        b.  then check the md5 files which both exist in src dir and dest dir, if the md5 string are not same, then copy the file in src dir to cover the file in dest dir with the same name.

