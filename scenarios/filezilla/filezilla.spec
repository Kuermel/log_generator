{
    "fields" : [
            { "templateCount" : {"count":1} },
            { "datetime": {"type": "random", "generate_type":"datetime", "format": "%b %d %H:%M:%S" } },
            { "date": {"type": "random", "generate_type":"datetime", "format": "%d.%m.%Y" } },
            { "time": {"type": "random", "generate_type":"datetime", "format": "%H:%M:%S" } },
            { "ip" : {"type": "from_list_file", "file" : "ip.list", "method":"random" } },
            { "number" : {"type": "random", "generate_type":"integer", "min":1, "max":500 } }
    ],
    "template" : [
          "${datetime} Asctristv053.ascroot.com [0]:(116431) ${date} ${time} - vips (${ip})> ${number} Entering Passive Mode (10,155,40,142,242,8)"
    ]
}