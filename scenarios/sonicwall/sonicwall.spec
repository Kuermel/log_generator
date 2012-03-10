{
    "fields" : [
        { "dst" : {"type": "random", "generate_type":"IPv4" } },
        { "date": {"type": "random", "generate_type":"datetime", "format": "%Y-%m-%d %H:%S:%M -0200" } },
        { "url" : {"type": "from_list_file", "file" : "url.list", "method":"sequential" } },
        { "protocol" : {"type": "from_list_file", "file" : "protocol.list", "method":"random" } },
        { "src" : {"type": "from_list_file", "file" : "ip.list", "method":"random" } },
        { "port" : {"type": "random", "generate_type":"integer", "min":1, "max":10000 } },
        { "sent" : {"type": "random", "generate_type":"integer", "min":1, "max":10000 } }
    ],
    "template" : "id=firewall sn=0017C5654B7A time=\"${date}\" fw=172.16.20.2 pri=6 c=1024 m=97 url=${url} f=2 sess=Web n=5395848 usr=\"admin\" src=${src}:${port}:X0: dst=${dst}:${port}:X2: proto=udp/dns sent=${sent} appcat=\"${protocol}\" appid=1283"
}