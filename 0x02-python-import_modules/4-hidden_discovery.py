#!/usr/bin/python3
import hidden_4
import re

if __name__ == "__main__":
    hidden_names_list = dir(hidden_4)
    for hidden_name in hidden_names_list:
        if not re.search("^_", hidden_name):
            print(hidden_name)
