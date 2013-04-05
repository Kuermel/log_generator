{
    "fields" : [
        { "templateCount" : {"count":1} },
        { "url" : {"type": "from_list_file", "file" : "url.list", "method":"sequential" } },
        { "date": {"type": "random", "generate_type":"datetime", "format": "%b %d %H:%M:%S" } },
        { "ip" : {"type": "random", "generate_type":"IPv4" } },
        { "ip2" : {"type": "from_list_file", "file" : "ip.list", "method":"random" } },
        { "port" : {"type": "random", "generate_type":"integer", "min":1, "max":10000 } },
        { "port2" : {"type": "random", "generate_type":"integer", "min":1, "max":5000 } },
        { "number" : {"type": "random", "generate_type":"integer", "min":0, "max":100 } }
    ],
    "template" : [
          "${date} ${ip2} CisACS_01_PassedAuth 1832pg1iq 1 0 Response Time=${number},Message-Type=Authen OK,User-Name=work\\pc,Group-Name=Staff Group,Caller-ID=00-00-xx-yy-xx-zz,NAS-IP-Address=${ip},NAS-Port=${port},EAP Type=${number},EAP Type Name=CISCO-PEAP,Access Device=WLC,Filter Information=No Filters activated.,"
    ]
}
