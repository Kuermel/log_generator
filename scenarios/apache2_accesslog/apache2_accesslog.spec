{
    "fields" : [
        { "templateCount" : {"count":1} },
        { "remote_ip" : {"type": "random", "generate_type":"IPv4" } },
        { "date": {"type": "random", "generate_type":"datetime", "format": "%d/%b/%Y:%H:%M:%S" } },
        { "es_date": {"type": "random", "generate_type":"datetime", "format": "%Y-%m-%d %H:%M:%S" } },
        { "uri" : {"type": "from_list_file", "file" : "uri.list", "method":"sequential" } },
        { "http_method" : {"type": "from_list_file", "file" : "http_method.list", "method":"random" } },
        { "http_protocol" : {"type": "from_list_file", "file" : "http_protocol.list", "method":"random" } },
        { "respond_code" : {"type": "from_list_file", "file": "respond_codes.list", "method":"ratio", "ratio":"50,50" } },
        { "sent" : {"type": "random", "generate_type":"integer", "min":1, "max":10000 } },
        { "recv" : {"type": "random", "generate_type":"integer", "min":1, "max":10000 } }
    ],
    "template" : [
          "${remote_ip} - - [${date}] \"${http_method} ${uri} ${http_protocol}\" ${respond_code} ${sent}"
    ],
    "json_template": [
        {
            "_es_type": "nastedlog",
            "Bytes": {
                "Received": "recv",
                "Sent": "sent"
            },
            "EventMap": {
                "Type": "event_map_type",
                "SubType": "event_map_sub_type",
                "Context": "event_map_context"
            },
            "Event": {
                "VendorID": 1,
                "SystemID": 2,
                "Category": "event_category",
                "Info": "event_info",
                "Note": "note"
            },
            "Source": {
                "IP": "remote_ip"
            },
            "URL": {
                "Method": "method",
                "Domain": "uri",
                "Path": "path",
                "Protocol": "protocol",
                "ResultCode": 200
            },
            "Severity": {
                "ID": 1,
                "Name": "info"
            },
            "Time": {
                "Generated": "es_date"
            }
        }
    ]
}
