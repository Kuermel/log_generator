{
    "fields" : [
        { "templateCount" : {"count":2} },
        { "datetime": {"type": "random", "generate_type":"datetime", "format": "%b %d %H:%M:%S" } },
        { "datetime2": {"type": "random", "generate_type":"datetime", "format": "%Y-%m-%dT%H:%M:%S.%f" } },
        { "date": {"type": "random", "generate_type":"datetime", "format": "%m/%d/%y" } },
        { "time": {"type": "random", "generate_type":"datetime", "format": "%H:%M:%S" } },
        { "ip" : {"type": "random", "generate_type":"IPv4" } },
        { "ip2" : {"type": "from_list_file", "file" : "ip.list", "method":"random" } },
        { "mailto" : {"type": "from_list_file", "file" : "mail.list", "method":"random" } },
        { "mailfrom" : {"type": "from_list_file", "file" : "mail.list", "method":"random" } }
    ],
    "template" : [
          "${datetime} ServerXYZ[0]:${datetime2}Z,${ip},server.domain.com,${ip2},XYZ,08CEC3A7A05FF3DC${datetime2}Z;0,XYZ\\DefaultXYZ,SMTP,RECEIVE,988234,<6969BC6C7B9D7B45879A15833A0E2738BBD2D8@company.com>,${mailto},,694350,1,,,\"mail subject's data\",${mailfrom},prvs=405a67079=${mailfrom},00A: NTS:,Incomi3ng,,${ip},${ip2},S:countdataHop=server.domain.com",
          "${datetime} ServerXYZ[0]:${datetime2}Z,${ip},server.domain.com,${ip2},XYZ,08CEC3A7A05FF3DC${datetime2}Z;0,XYZ\\DefaultXYZ,SMTP,RECEIVE,988234,<6969BC6C7B9D7B45879A15833A0E2738BBD2D8@company.com>,${mailto};asd@cvz.net.tr,,694350,1,,,\"mail subject's data\",${mailfrom},prvs=405a67079=${mailfrom},00A: NTS:,Incomi3ng,,${ip},${ip2},S:countdataHop=server.domain.com"
    ]
}
