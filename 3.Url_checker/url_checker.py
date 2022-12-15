#!/usr/bin/python3

import urllib.request  

def main(url):

  print("Checking connectivity")

  response = urllib.request.urlopen(url)
  print('Connected to', url, ' succesfull ')
  print("The response code was: ", response.getcode())


print("This is a site connectibity checker script")
print("Please follow some rule add http/https and www before domain")
input_url = input("Input the url: ")
main(input_url)
