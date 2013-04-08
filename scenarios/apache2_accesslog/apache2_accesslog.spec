{
    "fields" : [
        { "templateCount" : {"count":1} },
        { "remote_ip" : {"type": "random", "generate_type":"IPv4" } },
        { "date": {"type": "random", "generate_type":"datetime", "format": "%Y/%m/%d %H:%S:%M -0200" } },
        { "uri" : {"type": "from_list_file", "file" : "uri.list", "method":"sequential" } },
        { "http_method" : {"type": "from_list_file", "file" : "http_method.list", "method":"random" } },
        { "http_protocol" : {"type": "from_list_file", "file" : "http_protocol.list", "method":"random" } },
        { "respond_code" : {"type": "from_list_file", "file": "respond_codes.list", "method":"ratio", "ratio":"50,50" } },
        { "sent" : {"type": "random", "generate_type":"integer", "min":1, "max":10000 } }
    ],
    "template" : [
          "${remote_ip} - - [${date}] \"${http_method} ${uri} ${http_protocol}\" ${respond_code} ${sent}"
    ]
}
