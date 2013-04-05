{
    "fields" : [
            { "templateCount" : {"count":1} },
            { "datetime": {"type": "random", "generate_type":"datetime", "format": "%Y-%m-%d %H:%M:%S" } },
            { "ip" : {"type": "from_list_file", "file" : "ip.list", "method":"random" } },
            { "number" : {"type": "random", "generate_type":"integer", "min":1, "max":500 } }
    ],
    "template" : [
          "Juniper: ${datetime} - ive - [${ip}] xx(YY)[] - Login failed using auth server YY (Local Authentication).  Reason: ShortPasswd"
    ]
}