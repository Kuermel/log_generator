{
    "fields" : [
        { "ipv4" : {"type": "random", "generate_type":"LocalIPv4" } },
        { "src_ipv4" : {"type": "random", "generate_type":"IPv4" } },
        { "dst_ipv4" : {"type": "random", "generate_type":"IPv4" } },
        { "date": {"type": "random", "generate_type":"datetime", "format": "%d/%b/%Y:%H:%M:%S" } },
        { "es_date": {"type": "random", "generate_type":"datetime", "format": "%Y-%m-%d %H:%M:%S" } },
        { "url_path" : {"type": "from_list_file", "file" : "url_path.list", "method":"sequential" } },
        { "url_domain" : {"type": "from_list_file", "file" : "url_domain.list", "method":"sequential" } },
        { "url_category" : {"type": "from_list_file", "file" : "url_category.list", "method":"sequential" } },
        { "application_name" : {"type": "from_list_file", "file" : "application_name.list", "method":"sequential" } },
        { "method" : {"type": "from_list_file", "file" : "method.list", "method":"random" } },
        { "port" : {"type": "from_list_file", "file" : "port.list", "method":"random" } },
        { "dst_port" : {"type": "from_list_file", "file" : "dst_port.list", "method":"random" } },
        { "src_port" : {"type": "from_list_file", "file" : "src_port.list", "method":"random" } },
        { "session_id" : {"type": "from_list_file", "file" : "session_id.list", "method":"random" } },
        { "result_code" : {"type": "from_list_file", "file": "result_code.list", "method":"ratio", "ratio":"50,50" } },
        { "recv" : {"type": "random", "generate_type":"integer", "min":1, "max":10000 } },
        { "sent" : {"type": "random", "generate_type":"integer", "min":1, "max":10000 } },
        { "tot" : {"type": "random", "generate_type":"integer", "min":1, "max":100 } },
        { "src_country" : {"type": "from_list_file", "file" : "src_country.list", "method":"random" } },
        { "username" : {"type": "from_list_file", "file" : "username.list", "method":"random" } },
        { "severity_name" : {"type": "from_list_file", "file" : "severity_name.list", "method":"sequential" } },
        { "error_date": {"type": "random", "generate_type":"datetime", "format": "%a %b %d %H:%M:%S %Y" } }
    ],
    "template" : [],
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
                "Directory": "smb://192.168.1.150/apache_webserver",
                "FileName": "access20160215.log",
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
                "IP": "ipv4",
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
                "Position": "in"
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
                "Position": "in"
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
                "Domain": "url_domain",
                "Path": "url_path",
                "Protocol": "HTTP/1.1",
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
                "FileName": "access20160201.log",
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
                "Domain": "url_domain",
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
                "Position": "out"
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
