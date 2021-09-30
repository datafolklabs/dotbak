# dotBAK - Lazily Backup Files and Directories

[![Built on Cement™](https://img.shields.io/badge/Built%20on%20Cement%E2%84%A2-3.0-yellow)](https://builtoncement.com)
[![Continuous Integration Status](https://app.travis-ci.com/datafolklabs/dotbak.svg?branch=master)](https://travis-ci.com/github/datafolklabs/dotbak)

## Installation

```
$ pip install dotbak
```

## Usage

```
$ dotbak README.md

$ dotbak README.md

$ dotbak README.md

|$ ls -lah README.md*
-rw-r--r--    1 user     user        2.4K Sep 12 12:10 README.md
-rw-r--r--    1 user     user        2.4K Sep 12 12:56 README.md.bak-2021-09-30-17:23:45
-rw-r--r--    1 user     user        2.4K Sep 12 12:56 README.md.bak-2021-09-30-17:23:57
-rw-r--r--    1 user     user        2.4K Sep 12 12:56 README.md.bak-2021-09-30-17:24:14
```

## License

dotBAK is Open Source and is distributed under the BSD License (three clause).  Please see the LICENSE file included with this software.