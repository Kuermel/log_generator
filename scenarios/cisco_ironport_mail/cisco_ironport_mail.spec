{
    "fields" : [
        { "templateCount" : {"count":3} },
        { "date": {"type": "random", "generate_type":"datetime", "format": "%a %b %d %H:%M:%S %Y" } },
        { "ip" : {"type": "random", "generate_type":"IPv4" } },
        { "mail" : {"type": "from_list_file", "file" : "mail.list", "method":"random" } },
        { "number" : {"type": "random", "generate_type":"integer", "min":0, "max":100 } }
    ],
    "template" : [
          "${date} Info: ICID 282204970 SBRS None",
          "${date} Info: Start MID 200257070 ICID 282204970",
          "${date} Info: MID 200257070 ICID 282204970 From:<${mail}>"
    ]
}
