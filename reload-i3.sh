#!/bin/bash

DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
cd "${DIR}/src"

if [ -f i3wm-themer.py ]; then
    python i3wm-themer.py --config config.yaml --install defaults/

    if [ -f themes/${1}.json ]; then
        sleep 3
        python i3wm-themer.py --config config.yaml --load themes/${1}.json
    fi
fi

