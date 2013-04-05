{
    "fields" : [
        { "templateCount" : {"count":1} },
        { "datetime": {"type": "random", "generate_type":"datetime", "format": "%b %d %H:%M:%S" } },
        { "datetime2": {"type": "random", "generate_type":"datetime", "format": "%Y-%m-%dT%H:%M:%S.%f" } },
        { "date": {"type": "random", "generate_type":"datetime", "format": "%m/%d/%y" } },
        { "time": {"type": "random", "generate_type":"datetime", "format": "%H:%M:%S" } },
        { "ip" : {"type": "random", "generate_type":"IPv4" } },
        { "mail" : {"type": "from_list_file", "file" : "mail.list", "method":"random" } }
    ],
    "template" : [
          "${datetime} ServerXYZ \t0\t${datetime2}Z,${ip},XYZ00,,XYZ00,\"MDB:ddf64239-893c-440e-998a-6562aeb84fc4, Mailbox:8cddb393-96de-457c-a13a-8b3ea038df4e, Event:28848005, MessageClass:REPORT.IPM.Note.IPNRN, CreationTime:${datetime2}Z, ClientType:User\",,STOREDRIVER,SUBMIT,,<8DE7C7606E6D924E91F245221FED21FF9375E6128E@company.local>,,,,,,,mail subject,${mail},,"
    ]
}
