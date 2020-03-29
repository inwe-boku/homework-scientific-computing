#!/bin/bash
#
# Add all forks as Git remote repositories, download commits, checkout encrypted group files,
# decrypt files and write data to CSV files for each group.
#
# Should be save to be called multiple times (overwrites previous files).

set -e

cd "$(dirname "$0")"

echo Adding remotes...
python3 ../list-forks.py

echo
echo Fetch from all remotes...
git fetch --all

echo
echo Checkout encrypted files...
names=$(python3 ../list-forks.py)

echo
echo Decrypt files and create CSVs...
for name in $names; do
    echo Group $name
    # git ls-tree does not support wildcards, need grep... :-/
    if ! git ls-tree --name-only -r $name/master |grep 'group-member-.*.txt' > /dev/null; then
        echo No file found for group $name.
        continue
    fi

    git checkout $name/master -- 'group-member-*.txt'

    # delete file to be sure, if script is re-run...
    rm -f group-members-$name.csv
    for member in $(ls group-member-*.txt); do
        echo Decrpyting: $name/$member...
        python3 decrypt.py $member  >> group-members-$name.csv
    done
    git rm -f group-member-*.txt
done
