{
    "fields" : [
        { "templateCount" : {"count":9} },
        { "datetime": {"type": "random", "generate_type":"datetime", "format": "%b %d %H:%M:%S" } },
        { "datetime2": {"type": "random", "generate_type":"datetime", "format": "%d/%b/%Y:%H:%M:%S" } },
        { "datetime3": {"type": "random", "generate_type":"datetime", "format": "%Y-%m-%d %H:%M:%S" } },
        { "time": {"type": "random", "generate_type":"datetime", "format": "%H:%M:%S" } },
        { "category" : {"type": "from_list_file", "file" : "category.list", "method":"random" } },
        { "ip" : {"type": "random", "generate_type":"IPv4" } },
        { "ip2" : {"type": "from_list_file", "file" : "ip.list", "method":"random" } },
        { "port" : {"type": "random", "generate_type":"integer", "min":1, "max":10000 } },
        { "port2" : {"type": "random", "generate_type":"integer", "min":1, "max":5000 } },
        { "url" : {"type": "from_list_file", "file" : "url.list", "method":"random" } }
    ],
    "template" : [
        "${datetime} pf: ${time}.000120 rule 33/0(match): pass in on de0: (tos 0x0, ttl 64, id 26534, offset 0, flags [none], proto TCP (6), length 40)   ${ip}.${port} > ${ip2}.${port}: Flags [S], cksum 0x27f4 (correct), seq 791405069, win 512, length 0",
        "${datetime} squid[28408]: ${ip} - - [${datetime2} +0000] \"GET ${url} HTTP/1.1\" 200 1037 TCP_MISS:DIRECT",
        "${datetime} logportalauth[37624]: LOGIN: admin, x8:y0:xz:8t:aa:bb, ${ip}",
        "${datetime} dhcpd: DHCPREQUEST for ${ip} from x0:yy:x8:t1:a0:x0 via em1: wrong network.",
        "${datetime} dhcpd: DHCPNAK on ${ip} to y0:zt:z8:1y:x8:xx via em1",
        "${datetime} dhcpd: DHCPDISCOVER from y0:zt:z8:1y:x8:xx via em1",
        "${datetime} dhcpd: DHCPOFFER on ${ip} to a8:26:d9:91:0c:64 ",
        "${datetime} dhcpd: unexpected ICMP Echo Reply from ${ip}",
        "${datetime} ntpd[52938]: adjusting local clock by 43.656597s stamp:${datetime3}"
    ]
}
