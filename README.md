# Dirbpy

Dirbpy is a simple url directory bruteforcing tool using word list.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements or dependencies.

```bash
pip3 install -r requirements.txt
```
Then run the tool
```bash
python Dirb.py -h
```
Output
```bash
usage: Dirb.py [-h] url wordlist

positional arguments:
  url         url of the desired website
  wordlist    wordlist to start dirring

optional arguments:
  -h, --help  show this help message and exit
```

## Example
1.Specifying application protocol in url:
```bash
>> python Dirb.py https://github.com/MeganViga/dirbtest/tree/master/ tested_simple_wl.txt
```
Output
```bash
https://github.com/MeganViga/dirbtest/tree/master/

Dirring in Progress......
https://github.com/MeganViga/dirbtest/tree/master/search --> found

https://github.com/MeganViga/dirbtest/tree/master/videos --> found

https://github.com/MeganViga/dirbtest/tree/master/abc

https://github.com/MeganViga/dirbtest/tree/master/files --> found

https://github.com/MeganViga/dirbtest/tree/master/photos --> found

https://github.com/MeganViga/dirbtest/tree/master/def


List of available Directories
-----------------------------
1. https://github.com/MeganViga/dirbtest/tree/master/search
2. https://github.com/MeganViga/dirbtest/tree/master/videos
3. https://github.com/MeganViga/dirbtest/tree/master/files
4. https://github.com/MeganViga/dirbtest/tree/master/photos
```
2.When apllication protocol not sepcified in url
```bash
>> python Dirb.py github.com/MeganViga/dirbtest/tree/master/ tested_simple_wl.txt
```
Output
```bash
You did not specify any application protocol.
 What do you want?
1.https
2.http
Enter respective number:1
https://github.com/MeganViga/dirbtest/tree/master/

Dirring in Progress......
https://github.com/MeganViga/dirbtest/tree/master/search --> found

https://github.com/MeganViga/dirbtest/tree/master/videos --> found

https://github.com/MeganViga/dirbtest/tree/master/abc

https://github.com/MeganViga/dirbtest/tree/master/files --> found

https://github.com/MeganViga/dirbtest/tree/master/photos --> found

https://github.com/MeganViga/dirbtest/tree/master/def


List of available Directories
-----------------------------
1. https://github.com/MeganViga/dirbtest/tree/master/search
2. https://github.com/MeganViga/dirbtest/tree/master/videos
3. https://github.com/MeganViga/dirbtest/tree/master/files
4. https://github.com/MeganViga/dirbtest/tree/master/photos
```
