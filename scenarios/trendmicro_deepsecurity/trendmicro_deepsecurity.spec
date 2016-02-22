{
    "fields" : [
        { "ipv4" : {"type": "random", "generate_type":"LocalIPv4" } },
        { "src_ipv4" : {"type": "random", "generate_type":"IPv4" } },
        { "dst_ipv4" : {"type": "random", "generate_type":"IPv4" } },
        { "local_dst_ipv4" : {"type": "random", "generate_type":"LocalIPv4" } },
        { "date": {"type": "random", "generate_type":"datetime", "format": "%d/%b/%Y:%H:%M:%S" } },
        { "es_date": {"type": "random", "generate_type":"datetime", "format": "%Y-%m-%d %H:%M:%S" } },
        { "url_path" : {"type": "from_list_file", "file" : "url_path.list", "method":"sequential" } },
        { "url_domain" : {"type": "from_list_file", "file" : "url_domain.list", "method":"sequential" } },
        { "url_scheme" : {"type": "from_list_file", "file" : "url_scheme.list", "method":"random" } },
        { "url_category" : {"type": "from_list_file", "file" : "url_category.list", "method":"random" } },
        { "url_requesttype" : {"type": "from_list_file", "file" : "url_requesttype.list", "method":"random" } },
        { "application_name" : {"type": "from_list_file", "file" : "application_name.list", "method":"sequential" } },
        { "method" : {"type": "from_list_file", "file" : "method.list", "method":"random" } },
        { "result_code" : {"type": "from_list_file", "file": "result_code.list", "method":"ratio", "ratio":"50,50" } },
        { "sent" : {"type": "random", "generate_type":"integer", "min":1, "max":10000 } },
        { "port" : {"type": "from_list_file", "file" : "port.list", "method":"random" } },
        { "dst_port" : {"type": "from_list_file", "file" : "dst_port.list", "method":"random" } },
        { "src_port" : {"type": "from_list_file", "file" : "src_port.list", "method":"random" } },
        { "recv" : {"type": "random", "generate_type":"integer", "min":1, "max":10000 } },
        { "duration_time" : {"type": "random", "generate_type":"integer", "min":1, "max":1000 } },
        { "src_country" : {"type": "from_list_file", "file" : "src_country.list", "method":"random" } },
        { "dst_country" : {"type": "from_list_file", "file" : "dst_country.list", "method":"random" } },
        { "severity_name" : {"type": "from_list_file", "file" : "severity_name.list", "method":"sequential" } },
        { "username" : {"type": "from_list_file", "file" : "username.list", "method":"random" } },
        { "computer_name" : {"type": "from_list_file", "file" : "computer_name.list", "method":"random" } },
        { "error_date": {"type": "random", "generate_type":"datetime", "format": "%a %b %d %H:%M:%S %Y" } }
    ],
    "template" : [],
    "json_template": [
             {
                 "_es_type": "nastedlog",
                 "EventMap": {
                     "Type": "User",
                     "SubType": "Login",
                     "Context": "Identity"
                 },
                 "EventSource": {
                     "Vendor": "TrendMicro",
                     "Product": "DeepSecurity",
                     "IP": "192.168.1.153",
                     "Type": "SecuritySystem",
                     "PrefixID": 3061,
                     "Category": "IPS"
                 },
                 "Event": {
                     "VendorID": 600,
                     "SystemID": 3061600,
                     "Info": "UserSignedIn",
                     "Note": "Usersignedinfrom10"
                 },
                 "Source": {
                     "IP": "ipv4",
                     "City": "Unknown",
                     "Country": "country",
                     "Location": "Unknown",
                     "UserName": "username",
                     "Position": "out"
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
                      "Type": "User",
                      "SubType": "Logout",
                      "Context": "Identity"
                  },
                  "EventSource": {
                      "Vendor": "TrendMicro",
                      "Product": "DeepSecurity",
                      "IP": "192.168.1.153",
                      "Type": "SecuritySystem",
                      "PrefixID": 3061,
                      "Category": "IPS"
                  },
                  "Event": {
                      "VendorID": 600,
                      "SystemID": 3061600,
                      "Info": "UserTimedOut"
                  },
                  "Source": {
                      "IP": "ipv4",
                      "City": "Unknown",
                      "Country": "country",
                      "Location": "Unknown",
                      "UserName": "username",
                      "Position": "out"
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
                     "Sent": "sent"
                 },
                 "EventMap": {
                     "Type": "Session",
                     "SubType": "Deny",
                     "Context": "Network"
                 },
                 "EventSource": {
                     "Vendor": "TrendMicro",
                     "Product": "DeepSecurity",
                     "IP": "192.168.1.153",
                     "PrefixID": 3061,
                     "Category": "IPS",
                     "Type": "Security System"
                 },
                 "Event": {
                     "VendorID": 20,
                     "SystemID": 306120,
                     "Action": "IDS: Deny",
                     "Info": "RemoteDomainEnforcement(SplitTunnel)"
                 },
                 "Source": {
                     "IP": "ipv4",
                     "HostName": "computer_name",
                     "MAC": "9F1760280553",
                     "City": "Unknown",
                     "Country": "country",
                     "Location": "Unknown",
                     "Port": "src_port",
                     "Position": "out"
                 },
                 "Destination": {
                     "IP": "local_dst_ipv4",
                     "Country": "dst_country",
                     "City": "Unknown",
                     "Location": "Unknown",
                     "MAC": "07DBBF14C788",
                     "Port": "dst_port",
                     "Position": "in"
                 },
                 "Severity": {
                     "ID": 6,
                     "Name": "information"
                 },
                 "Protocol": {
                     "Name": "TCP"
                 },
                 "Time": {
                     "Generated": "es_date",
                     "Received": "es_date"
                 }
             },
             {
                 "_es_type": "nastedlog",
                 "Bytes": {
                     "Sent": "sent"
                 },
                 "EventMap": {
                     "Type": "Attack",
                     "SubType": "Info",
                     "Context": "Security"
                 },
                 "EventSource": {
                     "Vendor": "TrendMicro",
                     "Product": "DeepSecurity",
                     "IP": "192.168.1.153",
                     "PrefixID": 3061,
                     "Category": "IPS",
                     "Type": "Security System"
                 },
                 "Event": {
                     "VendorID": 1000780,
                     "SystemID": 30611000780,
                     "Info": "MicrosoftOutlookExpressNNTPResponseParsingBufferOverflow",
                     "Action": "IDS: Delete"
                 },
                 "Source": {
                     "IP": "ipv4",
                     "HostName": "computer_name",
                     "MAC": "D69E46FACE50",
                     "City": "Unknown",
                     "Country": "src_country",
                     "Location": "Unknown",
                     "Port": "src_port",
                     "Position": "out"
                 },
                 "Destination": {
                     "IP": "local_dst_ipv4",
                     "MAC": "F91800F5834B",
                     "City": "Unknown",
                     "Country": "dst_country",
                     "Location": "Unknown",
                     "Port": "dst_port",
                     "Position": "in"
                 },
                 "Severity": {
                     "ID": 2,
                     "Name": "critical"
                 },
                 "Protocol": {
                     "Name": "TCP"
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
                      "Type": "Attack",
                      "SubType": "Info",
                      "Context": "Security"
                  },
                  "EventSource": {
                      "Vendor": "TrendMicro",
                      "Product": "DeepSecurity",
                      "IP": "192.168.1.153",
                      "PrefixID": 3061,
                      "Category": "IPS",
                      "Type": "Security System"
                  },
                  "Event": {
                      "VendorID": 1000823,
                      "SystemID": 30611000823,
                      "Info": "OracleDatabaseServerSQLInjectionInCONVERT_TO_LRS_LAYERProcedureOfMDSYS.SDO_LRSPackage",
                      "Action": "Replace"
                  },
                  "Source": {
                      "IP": "src_ipv4",
                      "HostName": "computer_name",
                      "MAC": "D69E46FACE50",
                      "City": "Unknown",
                      "Country": "src_country",
                      "Location": "Unknown",
                      "Port": "src_port",
                      "Position": "out"
                  },
                  "Destination": {
                      "IP": "local_dst_ipv4",
                      "MAC": "F91800F5834B",
                      "City": "Unknown",
                      "Country": "dst_country",
                      "Location": "Unknown",
                      "Port": "dst_port",
                      "Position": "in"
                  },
                  "Severity": {
                        "ID": 2,
                        "Name": "critical"
                  },
                  "Protocol": {
                        "Name": "ICMP"
                  },
                  "Time": {
                        "Generated": "es_date",
                        "Received": "es_date"
                  }
             },
             {
                 "_es_type": "nastedlog",
                 "EventMap": {
                        "Type": "FileIntegrity",
                        "SubType": "Info",
                        "Context": "Security"
                 },
                 "EventSource": {
                        "Vendor": "TrendMicro",
                        "Product": "DeepSecurity",
                        "IP": "192.168.1.153",
                        "PrefixID": 3061,
                        "Category": "IPS",
                        "Type": "Security System"
                 },
                 "Event": {
                        "VendorID": 2006797,
                        "SystemID": 30612006797,
                        "Info": "TMTR-0006: SuspiciousFilesDetectedInApplicationDirectories",
                        "Action": "deleted"
                 },
                 "Source": {
                        "HostName": "computer_name"
                 },
                 "Severity": {
                        "ID": 2,
                        "Name": "critical"
                 },
                 "Time": {
                       "Generated": "es_date",
                       "Received": "es_date"
                 }
             },
             {
                "_es_type": "nastedlog",
                 "EventMap": {
                        "Type": "Malware",
                        "SubType": "Info",
                        "Context": "Security"
                 },
                 "EventSource": {
                        "Vendor": "TrendMicro",
                        "Product": "DeepSecurity",
                        "IP": "192.168.1.153",
                        "PrefixID": 3061,
                        "Category": "IPS",
                        "Type": "Security System"
                 },
                 "Event": {
                        "VendorID": 4000013,
                        "SystemID": 30614000013,
                        "Info": "SPYWARE_KEYL_DESKTOPSCOUT",
                        "Note": "Quickscan",
                        "Action": "Delete"
                 },
                 "Source": {
                        "HostName": "computer_name"
                 },
                 "Severity": {
                        "ID": 2,
                        "Name": "critical"
                 },
                 "Time": {
                       "Generated": "es_date",
                       "Received": "es_date"
                 }
             },
             {
                "_es_type": "nastedlog",
                "EventMap": {
                        "Type": "Malware",
                        "SubType": "Info",
                        "Context": "Security"
                },
                "EventSource": {
                        "Vendor": "TrendMicro",
                        "Product": "DeepSecurity",
                        "IP": "192.168.1.153",
                        "PrefixID": 3061,
                        "Category": "IPS",
                        "Type": "Security System"
                },
                "Event": {
                        "VendorID": 4000001,
                        "SystemID": 30614000001,
                        "Info": "F_WORD.GR",
                        "Note": "Manuel",
                        "Action": "Quarantine"
                },
                "Source": {
                        "HostName": "computer_name"
                },
                "Severity": {
                        "ID": 2,
                        "Name": "critical"
                },
                "Time": {
                       "Generated": "es_date",
                       "Received": "es_date"
                }
             },
             {
                "_es_type": "nastedlog",
                 "EventMap": {
                       "Type": "URL",
                       "SubType": "Info",
                       "Context": "Security"
                 },
                 "EventSource": {
                       "Vendor": "TrendMicro",
                       "Product": "DeepSecurity",
                       "IP": "192.168.1.153",
                       "PrefixID": 3061,
                       "Category": "IPS",
                       "Type": "Security System"
                 },
                 "Event": {
                       "VendorID": 5000000,
                       "SystemID": 30615000000,
                       "Info": "WebReputation",
                       "Note": "Dangerous"
                 },
                 "Source": {
                       "HostName": "computer_name"
                 },
                 "URL": {
                       "Domain": "hu.g7jjhis6ttt0o.com",
                       "Path": "/K6a7/OYDgV/A.bat",
                       "Scheme": "http"
                 },
                 "Severity": {
                       "ID": 2,
                       "Name": "critical"
                 },
                 "Time": {
                       "Generated": "es_date",
                       "Received": "es_date"
                 }
             }
    ]
}
