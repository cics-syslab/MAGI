#!/bin/sh
# Source: https://github.com/nodejs/docker-node/blob/f05fbf88068ba29ac9b544a72c9471ba60243e4b/18/bullseye/Dockerfile
NODE_VERSION=18.17.0

dpkgArch="$(dpkg --print-architecture)"
case "${dpkgArch##*-}" in
amd64) ARCH='x64' ;;
ppc64el) ARCH='ppc64le' ;;
s390x) ARCH='s390x' ;;
arm64) ARCH='arm64' ;;
armhf) ARCH='armv7l' ;;
i386) ARCH='x86' ;;
*)
    echo "unsupported architecture"
    exit 1
    ;;
esac

curl -fsSLO --compressed "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-$ARCH.tar.xz"
tar -xJf "node-v$NODE_VERSION-linux-$ARCH.tar.xz" -C /usr/local --strip-components=1 --no-same-owner
rm "node-v$NODE_VERSION-linux-$ARCH.tar.xz"
ln -s /usr/local/bin/node /usr/local/bin/nodejs
npm install -g npm@latest
