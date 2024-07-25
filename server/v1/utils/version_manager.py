""" This module contaains VersionManager that handles
    versioning for all classes in order to maintain consistency
    throughout this project development
"""

import os
import json
import requests
from colorama import init, Fore, Style


init()


class VersionManager:
    """ Defines a Version Manager """

    vmversion = '0.1.0'

    def __init__(self):
        """ Initializes a Version Manager """
        self.filepath = self.find_versions_file()

        burl = 'https://raw.githubusercontent.com/CarToFix/CarToFixV2_Backend'
        self.expected = self.fetch_versions(burl + '/main/server/versions.json')

        self.save_version('VersionManger', VersionManager.vmversion)

    def fetch_versions(self, url):
        """ Fetches the correct versions for each class """
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()

    def save_version(self, c, v):
        """ Saves or updates the version for a class in the versions.json file
            - c: class whose version should be saved
            - v: class version
        """
        with open(self.filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        data[c] = v

        with open(self.filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)

    def load_got_versions(self):
        """ Load the versions from the versions.json file """
        with open(self.filepath, 'r', encoding='utf-8') as f:
            return json.load(f)

    def check_versions(self):
        """ Check versions in expected against versions.json """
        got_versions = self.load_got_versions()

        for c, v in got_versions.items():
            if c in self.expected:
                if v != self.expected[c]:
                    # Print warning with color
                    print(f"{Fore.MAGENTA}Warning: {Style.RESET_ALL}"
                          f"{Fore.RED}{c}{Style.RESET_ALL} expected local version "
                          f"{Fore.RED}{self.expected[c]}{Style.RESET_ALL} "
                          f"but got {Fore.RED}{v}{Style.RESET_ALL}")

        keys_a = set(got_versions.keys())
        keys_b = set(self.expected.keys())

        # Find keys in a but not in b
        got_not_exp = keys_a - keys_b
        # Find keys in b but not in a
        exp_not_got = keys_b - keys_a

        for c in got_not_exp:
            print(f"{Fore.MAGENTA}Warning: {Style.RESET_ALL}"
                  f"{Fore.RED}{c}{Style.RESET_ALL} "
                  f"is not found in yet in uploaded {self.filepath}")

        for c in exp_not_got:
            print(f"{Fore.MAGENTA}Warning: {Style.RESET_ALL}"
                  f"{Fore.RED}{c}{Style.RESET_ALL} "
                  f"is not found in local {self.filepath} file")           

    def find_versions_file(self):
        """ Returns the path for the versions.json file """
        for root, dirs, files in os.walk('.'):
            if 'versions.json' in files:
                return os.path.join(root, 'versions.json')
        
        err = "versions.json: file not found, please check file exists"
        raise FileNotFoundError(err)