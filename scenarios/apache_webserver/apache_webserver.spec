{
    "fields" : [
        { "ipv4" : {"type": "random", "generate_type":"IPv4" } },
        { "date": {"type": "random", "generate_type":"datetime", "format": "%d/%b/%Y:%H:%M:%S" } },
        { "es_date": {"type": "random", "generate_type":"datetime", "format": "%Y-%m-%d %H:%M:%S" } },
        { "url_path" : {"type": "from_list_file", "file" : "url_path.list", "method":"sequential" } },
        { "url_domain" : {"type": "from_list_file", "file" : "url_domain.list", "method":"sequential" } },
        { "method" : {"type": "from_list_file", "file" : "method.list", "method":"random" } },
        { "protocol" : {"type": "from_list_file", "file" : "protocol.list", "method":"random" } },
        { "result_code" : {"type": "from_list_file", "file": "result_code.list", "method":"ratio", "ratio":"50,50" } },
        { "sent" : {"type": "random", "generate_type":"integer", "min":1, "max":10000 } },
        { "recv" : {"type": "random", "generate_type":"integer", "min":1, "max":10000 } },
        { "error_date": {"type": "random", "generate_type":"datetime", "format": "%a %b %d %H:%M:%S %Y" } }
    ],
    "template" : [
          "${remote_ip} - - [${date}] \"${http_method} ${uri} ${http_protocol}\" ${respond_code} ${sent}",
          "[${error_date}] [error] [client ${remote_ip}] PHP Warning:  Smarty error: unable to read resource: \"settings/admin.tpl\" in /opt/project/admin.class.php on line 1144, referer: http://127.0.0.1/admin.php"
    ],
    "json_template": [
        {
            "_es_type": "nastedlog",
            "Bytes": {
                "Received": "recv",
                "Sent": "sent"
            },
            "EventMap": {
                "Type": "Web",
                "SubType": "Access",
                "Context": "Application"
            },
            "EventSource": {
                "Vendor": "Apache",
                "IP": "192.168.1.150",
                "PrefixID": 3008,
                "Category": "Web Server",
                "Type": "Application Server",
                "Description": "web_server_1"
            },
            "Event": {
                "VendorID": 6,
                "SystemID": 30086,
                "Info": "Web Access OK"
            },
            "Source": {
                "IP": "ipv4",
                "City": "Istanbul",
                "Country": "Turkey",
                "Position": "in"
            },
            "URL": {
                "Method": "method",
                "Domain": "url_domain",
                "Path": "url_path",
                "Protocol": "protocol",
                "ResultCode": 200
            },
            "Severity": {
                "ID": 6,
                "Name": "information"
            },
            "Time": {
                "Generated": "es_date",
                "Received": "es_date"
            }
        },
        {
            "_es_type": "nastedlog",
            "Bytes": {
                "Received": "recv",
                "Sent": "sent"
            },
            "EventMap": {
                "Type": "Web",
                "SubType": "Access",
                "Context": "HEDE"
            },
            "EventSource": {
                "Vendor": "Apache",
                "IP": "192.168.1.150",
                "PrefixID": 3008,
                "Category": "Web Server",
                "Type": "Application Server",
                "Description": "web_server_1"
            },
            "Event": {
                "VendorID": 6,
                "SystemID": 30086,
                "Info": "Web Access OK"
            },
            "Source": {
                "IP": "ipv4",
                "City": "Istanbul",
                "Country": "Turkey",
                "Position": "in"
            },
            "URL": {
                "Method": "method",
                "Domain": "url_domain",
                "Path": "url_path",
                "Protocol": "protocol",
                "ResultCode": 200
            },
            "Severity": {
                "ID": 0,
                "Name": "emergency"
            },
            "Time": {
                "Generated": "es_date",
                "Received": "es_date"
            }
        }
    ]
}
