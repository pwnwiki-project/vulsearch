> Vulsearch is a command line vulnerability information query tool, the vulnerability comes from PwnWiki.

#### 1.Installation

```
git clone https://github.com/pwnwikiorg/vulsearch.git
cd vulsearch
pip3 install -r requirements.txt
python3 vulsearch.py
```

#### 2.Usage

```
usage: vulsearch.py [options]

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         Output program version
  -s SEARCH, --search SEARCH
                        Search from PwnWiki
  -l LENS, --lens LENS  How many pieces of data to view
  -n NUMBER, --number NUMBER
                        How many pieces of data do you start with
  -p PAGE, --page PAGE  Open the specified page
```

For example:

*Search for information on CVE-2019-0708*

```
vulsearch -s CVE-2019-0708
```

*Search for CVE-2021 information and output 30 results (Note: 20 results are output by default)*

```
vulsearch -l 30 -s CVE-2021
```



#### 3.Thanks

The program is developed by [6613GitHub6613](https://github.com/6613GitHub6613).



#### 4.License

MIT



#### 5.Other

PwnWiki：[https://www.pwnwiki.org](https://www.pwnwiki.org/)

