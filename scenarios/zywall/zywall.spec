{
    "fields" : [
        { "templateCount" : {"count":1} },
        { "datetime": {"type": "random", "generate_type":"datetime", "format": "%b %d %H:%M:%S" } },
        { "pri" : {"type": "random", "generate_type":"integer", "min":0, "max":8 } },
        { "ip" : {"type": "random", "generate_type":"IPv4" } },
        { "ip2" : {"type": "from_list_file", "file" : "ip.list", "method":"random" } },
        { "port" : {"type": "random", "generate_type":"integer", "min":1, "max":10000 } },
        { "port2" : {"type": "random", "generate_type":"integer", "min":1, "max":5000 } },
        { "sent" : {"type": "random", "generate_type":"integer", "min":1, "max":10000 } },
        { "rcvd" : {"type": "random", "generate_type":"integer", "min":1, "max":10000 } },
        { "duration" : {"type": "random", "generate_type":"integer", "min":0, "max":20 } }
    ],
    "template" : [
        "${datetime} ZyWall src=\"${ip}:${port}\" dst=\"${ip2}:${port2}\" msg=\"Traffic Log\" note=\"Traffic Log\" devID=\"001349FAFEB0\" cat=\"Traffic Log\" duration=${duration} send=${sent} rcvd=${rcvd} dir=\"LAN:WAN\" protoID=6 proto=\"http\" trans=\"Normal\""
    ]
}
