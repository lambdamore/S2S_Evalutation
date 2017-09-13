#!/usr/bin/env python
from ecmwfapi import ECMWFDataServer
server = ECMWFDataServer()
server.retrieve({
    "class": "s2",
    "dataset": "s2s",
    "date": "2014-01-01",
    "expver": "prod",
    "hdate": "1981-01-01,1981-01-06",
    "levtype": "sfc",
    "model": "glob",
    "origin": "ammc",
    "param": "151/228228",
    "step": "24/48/72/96/120/144/168/192/216/240/264/288/312/336/360/384/408/432/456/480/504/528/552/576/600/624/648/672/696/720/744/768/792/816/840/864/888/912/936/960/984/1008/1032/1056/1080/1104/1128/1152/1176/1200/1224/1248/1272/1296/1320/1344/1368/1392/1416/1440/1464/1488",
    "stream": "enfh",
    "time": "00:00:00",
    "type": "cf",
    "target": "output",
})
