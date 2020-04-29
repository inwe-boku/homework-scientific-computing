#!/usr/bin/python3
"""List all forks of the homework repository or add forks as Git remotes."""

import requests
import argparse
import subprocess


GH_ACCOUNT = 'inwe-boku'
GH_REPO = 'homework-scientific-computing'
GH_API_URI = 'https://api.github.com/repos/{}/{}/forks'


def main(mode):
    r = requests.get(GH_API_URI.format(GH_ACCOUNT, GH_REPO))
    r.raise_for_status()
    forks = r.json()
    forks_uri = [fork['clone_url'] for fork in forks]

    if mode == 'print-name':
        for uri in forks_uri:
            print(f"{uri.split('/')[-2]}")
    elif mode == 'print-url':
        print("\n".join(forks_uri))
    elif mode == 'add-remote':
        for uri in forks_uri:
            name = f"{uri.split('/')[-2]}"
            print(f"Adding {name} as remote...")
            subprocess.call(["git", "remote", "add", name, uri])
    else:
        raise ValueError(f"invalid mode: {mode}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')

    # crazy workaround to allow option choices parameter:
    # https://stackoverflow.com/a/40324463/859591
    parser.add_argument('mode',
                        const='print-name',
                        default='print-name',
                        nargs='?',
                        choices=['print-name', 'print-url', 'add-remote'],
                        help='an integer for the accumulator')

    args = parser.parse_args()
    main(mode=args.mode)
