{
    "fields" : [
        { "templateCount" : {"count":2 } },
        { "ip" : {"type": "random", "generate_type":"IPv4" } },
        { "date": {"type": "random", "generate_type":"datetime", "format": "%Y-%m-%d %H:%S:%M" } },
        { "url" : {"type": "from_list_file", "file" : "url.list", "method":"sequential" } },
        { "protocol" : {"type": "from_list_file", "file" : "protocol.list", "method":"random" } },
        { "src" : {"type": "from_list_file", "file" : "ip.list", "method":"random" } },
        { "port" : {"type": "random", "generate_type":"integer", "min":1, "max":10000 } },
        { "sent" : {"type": "random", "generate_type":"integer", "min":1, "max":10000 } },
        { "rcvd" : {"type": "random", "generate_type":"integer", "min":1, "max":10000 } },
        { "pri" : {"type": "random", "generate_type":"integer", "min":0, "max":8 } },
        { "m" : {"type": "from_list_file", "file" : "m.list", "method":"random" } }
    ],
    "template" : [
      "id=firewall sn=0017C5654B7A time=\"${date}\" fw=${ip} pri=${pri} c=1024 m=${m} n=2128645 src=${src}:${port}:X0: dst=${ip}:${port}:X2: proto=tcp/https op=GET sent=${sent} rcvd=${rcvd} result=0 dstname=${url} arg=/ code=64 Category=\"Not Rated\"",
      "id=firewall sn=0017C5D88A98 time=\"${date}\" fw=${ip} pri=${pri} c=0 m=${m}  msg=\"Application Control Prevention Alert: MISC-APPS Google -- SSL Any Google Domain 2\" sid=9379 appcat=MISC-APPS appid=995   n=10572 src=${ip}:${port}:X1 dst=${ip}:${port}:X0"
     ]
}
