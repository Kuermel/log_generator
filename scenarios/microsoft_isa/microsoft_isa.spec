{
    "fields" : [
        { "templateCount" : {"count":1} },
        { "datetime": {"type": "random", "generate_type":"datetime", "format": "%b %d %H:%M:%S" } },
        { "datetime2": {"type": "random", "generate_type":"datetime", "format": "%Y-%m-%d %H:%M:%S" } },
        { "date": {"type": "random", "generate_type":"datetime", "format": "%m/%d/%Y" } },
        { "time": {"type": "random", "generate_type":"datetime", "format": "%H:%M:%S" } },
        { "ip" : {"type": "random", "generate_type":"IPv4" } },
        { "ip2" : {"type": "from_list_file", "file" : "ip.list", "method":"random" } },
        { "url" : {"type": "from_list_file", "file" : "url.list", "method":"random" } }
    ],
    "template" : [
          "${datetime} XXXYYYZZZ [0]:${ip}, Test\\User, Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; NP06), Y, ${datetime}, ${time}, w3proxy, XXX, -, XXXYYYZZZ, ${ip2}, 80, 16, 1133, 2551, http, TCP, GET, ${url}, image/jpeg, Inet, 200, 0x41a10000, Web Access Only, -, Internal, Internal, 0xd80, Allowed"
    ]
}
