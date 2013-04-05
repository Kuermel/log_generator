{
    "fields" : [
        { "templateCount" : {"count":2} },
        { "datetime": {"type": "random", "generate_type":"datetime", "format": "%Y/%d/%m %H:%M:%S" } },
        { "datetime2": {"type": "random", "generate_type":"datetime", "format": "%b %d %H:%M:%S" } },
        { "category" : {"type": "from_list_file", "file" : "category.list", "method":"random" } },
        { "ip" : {"type": "random", "generate_type":"IPv4" } },
        { "ip2" : {"type": "from_list_file", "file" : "ip.list", "method":"random" } },
        { "port" : {"type": "random", "generate_type":"integer", "min":1, "max":10000 } },
        { "port2" : {"type": "random", "generate_type":"integer", "min":1, "max":5000 } },
        { "url" : {"type": "from_list_file", "file" : "url.list", "method":"random" } }
    ],
    "template" : [
          "${datetime2} 1,${datetime},002201000312,THREAT,url,1,${datetime},${ip},${ip2},${ip},${ip2},LOCAL-2-UNT,,,web-browsing,vsys1,trust,untrust,ethernet1/14,ethernet1/15,au_log_profile,${datetime},1390947,1,3684,80,7903,80,0x400000,tcp,block-url,\"${url}\",(9999),${category},informational,client-to-server,0,0x0,10.0.0.0-10.255.255.255,Netherlands,0,",
          "${datetime2} 1,${datetime},002201000312,TRAFFIC,drop,1,${datetime},${ip},${ip2},0.0.0.0,0.0.0.0,REMTOOL-2-UNT,,,not-applicable,vsys1,trust,DMZ,ethernet1/14,,au_log_profile,${datetime},0,1,49207,2222,0,0,0x0,tcp,deny,0,0,0,0,${datetime},0,any,0,0,0x0,10.0.0.0-10.255.255.255,172.16.0.0-172.31.255.255,0"
    ]
}
