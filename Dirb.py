import os
import requests
import sys
import argparse
try:
    parser = argparse.ArgumentParser()
    parser.add_argument("url",help="url of the desired website")
    parser.add_argument("wordlist",help="wordlist to start dirring")
    args = parser.parse_args()
    if args.url[:8] != "https://" and args.url[:7] !="http://":
        print("You didn't specify any application protocol.\n What do you want?\n1.https\n2.http")
        choice = int(input("Enter respective number:"))
        if choice == 1:
            args.url = "https://" + args.url
        if choice == 2:
            args.url = "http://" + args.url


    def dirb(url, wordlist):
        availdir =[]
        print(url)
        try:
            r = requests.get(url)
        except:
            sys.exit("url--> Domain down or Maybe doesn't exists or you interrupted the process")


        file = os.path.isfile(wordlist)
        if not file:
            sys.exit("File does not exist, please enter correct path or correct filename")

        with open(wordlist,'r') as wordfile:
            user_agent = {'User-agent': 'Mozilla 5.0'}
            print("\nDirring in Progress......")
            for i in wordfile:
                if i[0] == "#":
                    continue
                i = i.rstrip('\r\n')
                if url[-1] == "/":
                    requrl = url + i
                else:
                    requrl = url + '/' + i
                print(requrl,end="")
                r = requests.get(requrl,headers = user_agent)
                if r.status_code == 200:
                    availdir.append(requrl)
                    print(" --> found",end="")
                print("\n")
        print("\nList of available Directories")
        print("-----------------------------")
        if(len(availdir) == 0):
            sys.exit("Nothing found from given wordlist, try a different one")
        for i in range(len(availdir)):
            print(f"{i+1}. {availdir[i]}")

    dirb(args.url,args.wordlist)
except KeyboardInterrupt:
    sys.exit("\n\nInterrupted  [-.-]")
