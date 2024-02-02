#! /bin/bash
pm2 start server.py --interpreter /usr/bin/python3 -- --production -p 27995 --store-history -D output
