{
    "fields" : [
        { "ipv4" : {"type": "random", "generate_type":"IPv4" } },
        { "src_ipv4" : {"type": "random", "generate_type":"LocalIPv4" } },
        { "date": {"type": "random", "generate_type":"datetime", "format": "%d/%b/%Y:%H:%M:%S" } },
        { "es_date": {"type": "random", "generate_type":"datetime", "format": "%Y-%m-%d %H:%M:%S" } },
        { "url_path" : {"type": "from_list_file", "file" : "url_path.list", "method":"random" } },
        { "url_domain" : {"type": "from_list_file", "file" : "url_domain.list", "method":"random" } },
        { "url_category" : {"type": "from_list_file", "file" : "url_category.list", "method":"random" } },
        { "url_referrer" : {"type": "from_list_file", "file" : "url_referrer.list", "method":"random" } },
        { "http_protocol" : {"type": "from_list_file", "file" : "http_protocol.list", "method":"random" } },
        { "result_code" : {"type": "from_list_file", "file" : "result_code.list", "method":"random" } },
        { "user_agent" : {"type": "from_list_file", "file" : "user_agent.list", "method":"random" } },
        { "method" : {"type": "from_list_file", "file" : "method.list", "method":"random" } },
        { "recv" : {"type": "random", "generate_type":"integer", "min":1100, "max":100000 } },
        { "sent" : {"type": "random", "generate_type":"integer", "min":1100, "max":100000 } },
        { "src_country" : {"type": "from_list_file", "file" : "src_country.list", "method":"random" } },
        { "severity_name" : {"type": "from_list_file", "file" : "severity_name.list", "method":"sequential" } },
        { "user_agent" : {"type": "from_list_file", "file" : "user_agent.list", "method":"random" } },
        { "error_date": {"type": "random", "generate_type":"datetime", "format": "%a %b %d %H:%M:%S %Y" } }
    ],
    "template" : [
        "${ipv4} - - [${date}] \"${method} ${url_path} ${http_protocol}\" ${result_code} ${recv} \"${url_domain}\" \"${user_agent}\"",
        "${src_ipv4} - - [${date}] \"${method} ${url_path} ${http_protocol}\" ${result_code} ${recv} ${sent} \"${url_domain}\" \"${user_agent}\"",
        "[${error_date}] [error] [client ${ipv4}] File does not exist: ${url_path}, ${url_referrer}",
        "[${error_date}] [error] [client ${ipv4}] client denied by server configuration: ${url_path}, ${url_referrer}",
        "[${error_date}] [error] [client ${src_ipv4}] PHP Warning:  Smarty error: unable to read resource: ${url_path} in ${url_referrer}",
        "${ipv4} - - [${date}] \"${method} ${url_path} ${http_protocol}\" 301 ${recv} \"-\" \"${user_agent}\"",
        "${ipv4} - - [${date}] \"-\" 408 0 \"-\" \"-\"",
        "${ipv4} - - [${date}] \"PUT ${url_path} ${http_protocol}\" 500 ${recv}"
    ],
    "json_template": [
        {
            "_es_type": "nastedlog",
            "DataType": "log",
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
                "Directory": "smb://192.168.1.150/apache_webserver",
                "FileName": "access20160215.log",
                "Type": "Application Server",
                "Description": "web_server_1"
            },
            "Event": {
                "VendorID": 4,
                "SystemID": 30084,
                "Info": "Web Access OK"
            },
            "Source": {
                "IP": "src_ipv4",
                "City": "Unknown",
                "Country": "src_country",
                "Position": "in"
            },
            "URL": {
                "Method": "method",
                "Domain": "url_domain",
                "Path": "url_path",
                "Protocol": "HTTP/1.0",
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
            "DataType": "log",
            "Bytes": {
                "Received": "recv"
            },
            "EventMap": {
                "Type": "Web",
                "SubType": "Error",
                "Context": "Application"
            },
            "EventSource": {
                "Vendor": "Apache",
                "IP": "192.168.1.150",
                "PrefixID": 3008,
                "Category": "Web Server",
                "Directory": "smb://192.168.1.150/master_apache",
                "FileName": "access20160113.log",
                "Type": "Application Server",
                "Description": "web_server_master"
            },
            "Event": {
                "VendorID": 41,
                "SystemID": 300841,
                "Info": "Not Found"
            },
            "Source": {
                "IP": "src_ipv4",
                "City": "Unknown",
                "Country": "src_country",
                "Position": "in"
            },
            "URL": {
                "Method": "method",
                "Domain": "url_domain",
                "Path": "url_path",
                "Protocol": "HTTP/1.0",
                "ResultCode": 404
            },
            "Severity": {
                "ID": 4,
                "Name": "warning"
            },
            "Time": {
                "Generated": "es_date",
                "Received": "es_date"
            }
        },
        {
            "_es_type": "nastedlog",
            "DataType": "log",
            "Bytes": {
                "Received": "recv"
            },
            "EventMap": {
                "Type": "Web",
                "SubType": "Redirection",
                "Context": "Application"
            },
            "EventSource": {
                "Vendor": "Apache",
                "IP": "192.168.1.150",
                "PrefixID": 3008,
                "Directory": "smb://192.168.1.150/xamplog",
                "FileName": "access20160217.log",
                "Category": "Web Server",
                "Type": "Application Server",
                "Description": "web_server_master"
            },
            "Event": {
                "VendorID": 15,
                "SystemID": 300815,
                "Info": "Moved Permanently"
            },
            "Source": {
                "IP": "ipv4",
                "City": "Unknown",
                "Country": "src_country",
                "Position": "out"
            },
            "URL": {
                "Method": "method",
                "Domain": "url_domain",
                "Path": "url_path",
                "Protocol": "HTTP/1.0",
                "ResultCode": 301
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
            "DataType": "log",
            "Bytes": {
                "Received": "recv"
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
                "Directory": "smb://192.168.1.150/apacheserver_1",
                "FileName": "access20160212.log",
                "Category": "Web Server",
                "Type": "Application Server",
                "Description": "web_server_master"
            },
            "Event": {
                "VendorID": 10,
                "SystemID": 300810,
                "Info": "Partial Content"
            },
            "Source": {
                "IP": "ipv4",
                "City": "Unknown",
                "Country": "src_country",
                "Position": "out"
            },
            "URL": {
                "Method": "method",
                "Domain": "url_domain",
                "Path": "url_path",
                "Protocol": "HTTP/1.1",
                "ResultCode": 206
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
            "DataType": "log",
            "Bytes": {
                "Received": "recv"
            },
            "EventMap": {
                "Type": "Web",
                "SubType": "Error",
                "Context": "Application"
            },
            "EventSource": {
                "Vendor": "Apache",
                "IP": "192.168.1.150",
                "PrefixID": 3008,
                "Directory": "smb://192.168.1.150/cap_apache_server",
                "FileName": "access20160212.log",
                "Category": "Web Server",
                "Type": "Application Server",
                "Description": "web_server_master"
            },
            "Event": {
                "VendorID": 40,
                "SystemID": 300840,
                "Info": "Forbidden"
            },
            "Source": {
                "IP": "ipv4",
                "City": "Unknown",
                "Country": "src_country",
                "Position": "in"
            },
            "URL": {
                "Method": "method",
                "Domain": "url_domain",
                "Path": "url_path",
                "Protocol": "HTTP/1.1",
                "ResultCode": 403
            },
            "Severity": {
                "ID": 4,
                "Name": "warning"
            },
            "Time": {
                "Generated": "es_date",
                "Received": "es_date"
            }
        },
        {
            "_es_type": "nastedlog",
            "DataType": "log",
            "Bytes": {
                "Received": "recv"
            },
            "EventMap": {
                "Type": "Web",
                "SubType": "Error",
                "Context": "Application"
            },
            "EventSource": {
                "Vendor": "Apache",
                "IP": "192.168.1.150",
                "PrefixID": 3008,
                "Directory": "smb://192.168.1.150/cap_apache_server",
                "FileName": "access20160212.log",
                "Category": "Web Server",
                "Type": "Application Server",
                "Description": "web_server_master"
            },
            "Event": {
                "VendorID": 40,
                "SystemID": 300840,
                "Info": "Forbidden"
            },
            "Source": {
                "IP": "src_ipv4",
                "City": "Unknown",
                "Country": "src_country",
                "Position": "out"
            },
            "URL": {
                "Method": "method",
                "Domain": "url_domain",
                "Path": "url_path",
                "Protocol": "HTTP/1.1",
                "ResultCode": 403
            },
            "Severity": {
                "ID": 4,
                "Name": "warning"
            },
            "Time": {
                "Generated": "es_date",
                "Received": "es_date"
            }
        },
        {
            "_es_type": "nastedlog",
            "DataType": "log",
            "Bytes": {
                "Received": "recv"
            },
            "EventMap": {
                "Type": "Web",
                "SubType": "Error",
                "Context": "Application"
            },
            "EventSource": {
                "Vendor": "Apache",
                "IP": "192.168.1.150",
                "PrefixID": 3008,
                "Directory": "smb://192.168.1.150/apache_weblog",
                "FileName": "access20160202.log",
                "Category": "Web Server",
                "Type": "Application Server",
                "Description": "web_server_master"
            },
            "Event": {
                "VendorID": 63,
                "SystemID": 300863,
                "Info": "Method Not Allowed"
            },
            "Source": {
                "IP": "ipv4",
                "City": "Unknown",
                "Country": "src_country",
                "Position": "in"
            },
            "URL": {
                "Method": "PROPFIND",
                "Path": "url_path",
                "ResultCode": 405
            },
            "Severity": {
                "ID": 4,
                "Name": "warning"
            },
            "Time": {
                "Generated": "es_date",
                "Received": "es_date"
            }
        },
        {
            "_es_type": "nastedlog",
            "DataType": "log",
            "Bytes": {
                "Received": "recv"
            },
            "EventMap": {
                "Type": "Web",
                "SubType": "Redirection",
                "Context": "Application"
            },
            "EventSource": {
                "Vendor": "Apache",
                "IP": "192.168.1.150",
                "PrefixID": 3008,
                "Directory": "smb://192.168.1.150/cap_apache_server",
                "FileName": "access_www_log",
                "Category": "Web Server",
                "Type": "Application Server",
                "Description": "web_server_master"
            },
            "Event": {
                "VendorID": 16,
                "SystemID": 300816,
                "Info": "Found"
            },
            "Source": {
                "IP": "ipv4",
                "City": "Unknown",
                "Country": "src_country",
                "Position": "in"
            },
            "URL": {
                "Method": "method",
                "Path": "url_path",
                "Protocol": "HTTP/1.0",
                "ResultCode": 302
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
            "DataType": "log",
            "EventMap": {
                "Type": "Service",
                "SubType": "Error",
                "Context": "System"
            },
            "EventSource": {
                "Vendor": "Apache",
                "IP": "192.168.1.150",
                "PrefixID": 3008,
                "Category": "Web Server",
                "Type": "Application Server",
                "Description": "web_server_2"
            },
            "Event": {
                "VendorID": 5,
                "SystemID": 30085,
                "Info": "Apache Web Server Error"
            },
            "Source": {
                "IP": "ipv4",
                "City": "Unknown",
                "Country": "src_country",
                "Position": "in"
            },
            "Severity": {
                "ID": 3,
                "Name": "error"
            },
            "Time": {
                "Generated": "es_date",
                "Received": "es_date"
            }
        }
    ]
}
