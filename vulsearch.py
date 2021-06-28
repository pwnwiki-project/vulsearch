import re
import time
import urllib
import requests
import argparse
import webbrowser
from rich.table import Table
from bs4 import BeautifulSoup
from urllib.parse import quote
from urllib.parse import unquote
from rich.console import Console



text_list = []
url = 'https://www.pwnwiki.org/index.php?title='
console = Console()
table = Table(show_header=True, header_style="bold magenta")
table.add_column("id", style="dim", width=8)
table.add_column("Title")

parser = argparse.ArgumentParser(usage='%(prog)s [options]')
parser.add_argument("-v", "--version", help="Output program version", action="store_true", default=True)
parser.add_argument("-s", "--search", help="Search from PwnWiki", type=str)
parser.add_argument("-l", "--lens", help="How many pieces of data to view", type=str, default='20')
parser.add_argument("-n", "--number", help="How many pieces of data do you start with", type=str, default='0')
parser.add_argument("-p", "--page", help="Open the specified page", type=int)

args = parser.parse_args()


def openpage(value, count):
    if 0 <= int(value - 1) <= count - 1:
        if int(args.number) <= int(value - 1) <= int(args.lens) - 1:
            if not text_list:
                print("\033[1;31mYou haven't queried the data yet\0330m")
            else:
                time.sleep(.5)
                webbrowser.open(url + urllib.parse.quote(str(text_list[value - 1])))
        else:
            print("\033[1;31mThe page you are opening is not within the scope of view\033[0m")
    else:
        print("\033[1;31mThe ID of the open page cannot be greater than the total number of searches\033[0m")


if args.version:
    print("\033[1;34m[Version]\033[0m PwnDatas-DB-Project(PDDP) & vulsearch 1.0.2")  # Blue

if args.number:
    number = args.number

if not args.search:
    print("\033[1;31m[ERROR]\033[0m Please input search keyword")
else:
    keyword = args.search

    print("\033[1;34m[INFO]\033[0m Searching the database: \033[32m%s\033[0m" % (keyword))

    print("\033[1;34m[INFO]\033[0m According to your settings, the program outputs %s pieces of content." % (args.lens))

    header = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0', }
    html = requests.get(
        "https://www.pwnwiki.org/index.php?title=Special:Search&limit=" + args.lens + "&offset=" + number + "&search=" + keyword,
        headers=header)
    soup = BeautifulSoup(html.text, "html.parser")
    lis = soup.find_all(name="li", attrs={"class": "mw-search-result"})

    if not lis:
        print("\033[1;31mThere were no results matching the query.\033[0m")
    else:

        f1 = re.findall('(\d+)', str(soup.find_all(name="div", attrs={"class": "results-info"})))

        for li in lis:
            text = unquote(li.a.get("href"), encoding="utf8").split("=")

            text_list.append(text[1])

        for k, v in enumerate(text_list):
            if "/" in v:
                r = requests.get(url + v)
                r.encoding = None
                v = BeautifulSoup(r.text, 'html.parser').html.body.h1.text

            table.add_row(str(k + 1), v)

        console.print(table)
        print(
            "\033[1;34m[INFO]\033[0m In this search of %s data, you have consulted %s data." % (int(f1[1]), args.lens))

        if args.page:
            page = args.page
            openpage(page, int(f1[1]))

        while True:
            op = input("\033[1;34m[INFO]\033[0m Open the specified web page?(yes/y/Yes/YES/Y/Press any key to exit)：")
            if op == "yes" or op == "Yes" or op == "y" or op == "YES" or op == "Y":
                op1 = input(
                    "\033[1;34m[INFO]\033[0m Please enter ID(values：%s - %s)：" % (int(args.number) + 1, args.lens))
                page = int(op1)
                openpage(page, int(f1[1]))
            else:
                exit(0)
