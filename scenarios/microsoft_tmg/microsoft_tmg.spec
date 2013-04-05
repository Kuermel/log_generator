{
    "fields" : [
        { "templateCount" : {"count":2} },
        { "datetime": {"type": "random", "generate_type":"datetime", "format": "%b %d %H:%M:%S" } },
        { "datetime2": {"type": "random", "generate_type":"datetime", "format": "%Y-%m-%d %H:%M:%S" } },
        { "date": {"type": "random", "generate_type":"datetime", "format": "%m/%d/%Y" } },
        { "time": {"type": "random", "generate_type":"datetime", "format": "%H:%M:%S" } },
        { "port" : {"type": "random", "generate_type":"integer", "min":1, "max":10000 } },
        { "port2" : {"type": "random", "generate_type":"integer", "min":1, "max":5000 } },
        { "ip" : {"type": "random", "generate_type":"IPv4" } },
        { "ip2" : {"type": "from_list_file", "file" : "ip.list", "method":"random" } },
        { "url" : {"type": "from_list_file", "file" : "url.list", "method":"random" } },
        { "url2" : {"type": "from_list_file", "file" : "url.list", "method":"random" } }
    ],
    "template" : [
          "${datetime} XXXYYYZZZ \t0\tTMG, ${date}, ${time}, UDP, ${ip}:${port}, ${ip2}:${port2}, ${ip}, Local Host, Internal, Terminate, 0x80074e20, [System] Allow DNS from Forefront TMG to selected servers, DNS, Y, 71, 71, 116, 116, 61000, 61000, -, -, -, 2, 3105840, -, -, -, ${date} ${time}, -, -, ::, -, -, -, Trusted, -, -, -, -, -, 0, -, -",
          "${datetime} XXXYYYZZZ \t0\t${ip}, anonymous, Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; InfoPath.2; OfficeLiveConnector.1.3; OfficeLivePatch.0.0; .NET4.0C; .NET4.0E), Y, ${date}, ${time}, w3proxy, FOREFRONT, ${url}, -, ${ip2}, 80, 187, 1474, 2944, http, TCP, GET, ${url2}, image/jpeg, Inet, 200, 0x41a00000, Merkez, Req ID: 1144e36a; Compression: client=No` server=Yes` compress rate=0% decompress rate=0%, Internal, Internal, 0x580, Allowed, ${date} ${time}, -, Allowed, -, -, Allowed, Malware Inspection Disabled, Unknown, -, -, 0, -, 0, -, -, -, -, -, -, 0, 0, -, 0, -, -, Feature disabled, None, domain.com, 2309, -"
    ]
}
