{
    "fields" : [
        { "templateCount" : {"count":1 } },
        { "date": {"type": "random", "generate_type":"datetime", "format": "%Y-%m-%d" } },
        { "time": {"type": "random", "generate_type":"datetime", "format": "%H:%S:%M" } },
        { "ip" : {"type": "from_list_file", "file" : "ip.list", "method":"random" } },
        { "ip2" : {"type": "random", "generate_type":"IPv4" } },
        { "pri" : {"type": "from_list_file", "file" : "pri.list", "method":"random" } },
        { "mailto" : {"type": "from_list_file", "file" : "mail.list", "method":"random" } },
        { "mailfrom" : {"type": "from_list_file", "file" : "mail.list", "method":"random" } }
    ],
    "template" : [
        "date=${date} time=${time} device_id=FE400B3M08600040 log_id=0300001099 type=spam pri=${pri} session_id=\"r2FGI1Lh004217-r2FGI1Li004217\" client_name=\"dsl-189-251-206-113-dyn.prod-infinitum.com.mx [${ip}] (may be forged)\" dst_ip=\"${ip2}\" endpoint=\"\" from=\"${mailfrom}\" to=\"${mailto}\" subject=\"xxxyyyzzz zz yy xx\" msg=\"FortiGuard-AntiSpam: identified: spam ip: ${ip2} score: 3\""
     ]
}
