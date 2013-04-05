{
    "fields" : [
        { "templateCount" : {"count":6} },
        { "datetime": {"type": "random", "generate_type":"datetime", "format": "%b %d %H:%M:%S" } },
        { "date": {"type": "random", "generate_type":"datetime", "format": "%m/%d/%y" } },
        { "time": {"type": "random", "generate_type":"datetime", "format": "%H:%M:%S" } },
        { "ip" : {"type": "random", "generate_type":"IPv4" } }
    ],
    "template" : [
          "${datetime} ServerXYZ [info] 30,${date},${time},DNS Update Request,${ip},XYZ-PC.ServerXYZ,,,0,6,,,",
          "${datetime} ServerXYZ [info] 16,${date},${time},Deleted,${ip},,0001A8C0C9E2,ServerXYZ\\Administrator",
          "${datetime} ServerXYZ dhcp1[0]:12,${date},${time},Renew,${ip},XYZ-PHONE,30694B3E3480",
          "${datetime} ServerXYZ [0]:02        The log was temporarily paused due to low disk space.",
          "${datetime} ServerXYZ [info] 30,${date},${time},DNS Update Request,${ip},XYZ-PC.ServerXYZ,,,0,6,,,",
          "${datetime} ServerXYZ [info] 30,${date},${time},DNS Update Request,${ip},XYZ-PC.ServerXYZ,,,0,6,,,"
    ]
}
