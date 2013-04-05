{
    "fields" : [
        { "templateCount" : {"count":2} },
        { "datetime": {"type": "random", "generate_type":"datetime", "format": "%b %d %H:%M:%S" } },
        { "datetime2": {"type": "random", "generate_type":"datetime", "format": "%Y-%m-%d %H:%M:%S" } },
        { "date": {"type": "random", "generate_type":"datetime", "format": "%m/%d/%Y" } },
        { "time": {"type": "random", "generate_type":"datetime", "format": "%H:%M:%S" } },
        { "ip" : {"type": "random", "generate_type":"IPv4" } },
        { "ip2" : {"type": "from_list_file", "file" : "ip.list", "method":"random" } },
        { "path" : {"type": "from_list_file", "file" : "path.list", "method":"random" } }
    ],
    "template" : [
          "${datetime} XXXYYYZZZ IISWebLog[0]:${ip}, -, ${date}, ${time}, W3SVC1, TEST, ${ip}, 31, 333, 185196, 200, 0, GET, ${path}, -,",
          "${datetime} XXXYYYZZZ IISWebLog[0]:${datetime2} W3SVC1 TEST ${ip} GET / - 80 - ${ip} HTTP/1.1 Mozilla/5.0+(Windows+NT+6.1;+WOW64;+rv:17.0)+Gecko/17.0+Firefox/17.0 - - ${ip} 200 0 0 888 323 15"
    ]
}
