# igclib

[![build status](https://img.shields.io/circleci/build/github/teobouvard/igclib/master?style=flat-square)](https://circleci.com/gh/teobouvard/igclib)
[![docs status](https://img.shields.io/readthedocs/igclib?style=flat-square)](https://igclib.readthedocs.io/en/latest/)

## Get started

```shell
git clone https://github.com/teobouvard/igclib.git
cd igclib
make install
```

[Documentation (in progress)](https://igclib.readthedocs.io/en/latest/)

---

## Build the documentation locally

Once installed, run `make docs` and go to http://0.0.0.0:8000/build/html/

---

## Todo

### Library

* safety check on task and tracks 
* change task validation method to closeness of next fast waypoint
* add tests
* test base64 inside task and not race ?

### Data collection

* refactor constants
* task _build_wpt task=None ?
* superfinal result not on the same index !
* maybe not rm downloaded tracks zip ?


### Misc

---

## Requirements

* Python 3.5 or higher
