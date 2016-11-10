{
    "fields" : [
        { "ipv4" : {"type": "random", "generate_type":"LocalIPv4" } },
        { "src_ipv4" : {"type": "random", "generate_type":"IPv4" } },
        { "dst_ipv4" : {"type": "random", "generate_type":"IPv4" } },
        { "date": {"type": "random", "generate_type":"datetime", "format": "%d/%b/%Y:%H:%M:%S" } },
        { "es_date": {"type": "random", "generate_type":"datetime", "format": "%Y-%m-%d %H:%M:%S" } },
        { "url_path" : {"type": "from_list_file", "file" : "url_path.list", "method":"sequential" } },
        { "url_domain" : {"type": "from_list_file", "file" : "url_domain.list", "method":"sequential" } },
        { "url_scheme" : {"type": "from_list_file", "file" : "url_scheme.list", "method":"random" } },
        { "application_name" : {"type": "from_list_file", "file" : "application_name.list", "method":"sequential" } },
        { "object_name" : {"type": "from_list_file", "file" : "object_name.list", "method":"random" } },
        { "share_name" : {"type": "from_list_file", "file" : "share_name.list", "method":"random" } },
        { "share_path" : {"type": "from_list_file", "file" : "share_path.list", "method":"random" } },
        { "method" : {"type": "from_list_file", "file" : "method.list", "method":"random" } },
        { "username" : {"type": "from_list_file", "file" : "username.list", "method":"random" } },
        { "dst_username" : {"type": "from_list_file", "file" : "dst_username.list", "method":"random" } },
        { "src_username" : {"type": "from_list_file", "file" : "src_username.list", "method":"random" } },
        { "domain_name" : {"type": "from_list_file", "file" : "domain_name.list", "method":"random" } },
        { "computer_name" : {"type": "from_list_file", "file" : "computer_name.list", "method":"random" } },
        { "dst_computer_name" : {"type": "from_list_file", "file" : "dst_computer_name.list", "method":"random" } },
        { "group_name" : {"type": "from_list_file", "file" : "group_name.list", "method":"random" } },
        { "result_code" : {"type": "from_list_file", "file": "result_code.list", "method":"ratio", "ratio":"50,50" } },
        { "sent" : {"type": "random", "generate_type":"integer", "min":1, "max":10000 } },
        { "port" : {"type": "from_list_file", "file" : "port.list", "method":"random" } },
        { "src_port" : {"type": "from_list_file", "file" : "src_port.list", "method":"random" } },
        { "dst_port" : {"type": "from_list_file", "file" : "dst_port.list", "method":"random" } },
        { "recv" : {"type": "random", "generate_type":"integer", "min":1, "max":10000 } },
        { "duration_time" : {"type": "random", "generate_type":"integer", "min":1, "max":1000 } },
        { "severity_name" : {"type": "from_list_file", "file" : "severity_name.list", "method":"sequential" } },
        { "error_date": {"type": "random", "generate_type":"datetime", "format": "%a %b %d %H:%M:%S %Y" } }
    ],
    "template" : [],
    "json_template": [
                {
                    "_es_type": "nastedlog",
                    "DataType": "log",
                    "EventMap": {
                        "Type": "User",
                        "SubType": "Login",
                        "Context": "Identity"
                    },
                    "Event": {
                        "Category": "LOGON/LOGOFF",
                        "Info": "An account was successfully logged on",
                        "SubCategory": "LOGON",
                        "SystemID": 10014624,
                        "Type": "Audit Success",
                        "VendorID": "4624"
                    },
                    "Source": {
                        "Domain": "domain_name",
                        "IP": "ipv4",
                        "HostName": "computer_name",
                        "LogonID": "0x250308a5",
                        "LogonTypeID": 3,
                        "Port": "port",
                        "UserName": "username"
                    },
                    "Severity": {
                        "ID": 6,
                        "Name": "information"
                    },
                    "Category": {
                        "ID": 12544
                    },
                    "EventSource": {
                        "Category": "Operating System",
                        "Collector": "wmicollector",
                        "Description": "Windows Server",
                        "IP": "192.168.1.154",
                        "PrefixID": 1001,
                        "Product": "Windows",
                        "Type": "Operating System",
                        "Vendor": "Microsoft",
                        "Version": "2008+"
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
                        "Type": "User",
                        "SubType": "Deny",
                        "Context": "Identity"
                    },
                    "Event": {
                        "Category": "LOGON/LOGOFF",
                        "Info": "An account failed to log on",
                        "SubCategory": "LOGON",
                        "SystemID": 10014625,
                        "Type": "Audit Failure",
                        "VendorID": "4625"
                    },
                    "Source": {
                        "IP": "ipv4",
                        "Domain": "domain_name",
                        "LogonTypeID": 3,
                        "Port": "port",
                        "UserName": "username"
                    },
                    "Severity": {
                        "ID": 2,
                        "Name": "critical"
                    },
                    "Category": {
                        "ID": 12544
                    },
                    "Failure": {
                        "Reason": "Unknown user name or bad password"
                    },
                    "EventSource": {
                        "Category": "Operating System",
                        "Collector": "wmicollector",
                        "Description": "Windows Server",
                        "IP": "192.168.1.154",
                        "PrefixID": 1001,
                        "Product": "Windows",
                        "Type": "Operating System",
                        "Vendor": "Microsoft",
                        "Version": "2008+"
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
                        "Type": "User",
                        "SubType": "Deny",
                        "Context": "Identity"
                    },
                    "Event": {
                        "Category": "LOGON/LOGOFF",
                        "Info": "An account failed to log on",
                        "SubCategory": "LOGON",
                        "SystemID": 10014625,
                        "Type": "Audit Failure",
                        "VendorID": "4625"
                    },
                    "Source": {
                        "IP": "ipv4",
                        "Domain": "domain_name",
                        "LogonTypeID": 3,
                        "Port": "port",
                        "UserName": "username"
                    },
                    "Severity": {
                        "ID": 2,
                        "Name": "critical"
                    },
                    "Category": {
                        "ID": 12544
                    },
                    "Failure": {
                        "Reason": "An Error occured during Logon."
                    },
                    "EventSource": {
                        "Category": "Operating System",
                        "Collector": "wmicollector",
                        "Description": "Windows Server",
                        "IP": "192.168.1.154",
                        "PrefixID": 1001,
                        "Product": "Windows",
                        "Type": "Operating System",
                        "Vendor": "Microsoft",
                        "Version": "2008+"
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
                        "Type": "User",
                        "SubType": "Logout",
                        "Context": "Identity"
                    },
                    "Event": {
                        "Category": "LOGON/LOGOFF",
                        "Info": "Account was logged off",
                        "SubCategory": "LOGOFF",
                        "SystemID": 10014634,
                        "Type": "Audit Success",
                        "VendorID": 4634
                    },
                    "Source": {
                        "Domain": "domain_name",
                        "LogonID": "0x250308a5",
                        "LogonTypeID": 3,
                        "Port": "48820",
                        "SecurityID": "S-1-5-21",
                        "UserName": "username"
                    },
                    "Severity": {
                        "ID": 6,
                        "Name": "information"
                    },
                    "Category": {
                        "ID": 12545
                    },
                    "EventSource": {
                        "Category": "Operating System",
                        "Collector": "wmicollector",
                        "Description": "Windows Server",
                        "IP": "192.168.1.154",
                        "PrefixID": 1001,
                        "Product": "Windows",
                        "Tag": "Windows-DC",
                        "Type": "Operating System",
                        "Vendor": "Microsoft",
                        "Version": "2008+"
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
                        "Type": "User",
                        "SubType": "Login",
                        "Context": "Identity"
                    },
                    "Event": {
                        "Category": "LOGON/LOGOFF",
                        "Info": "Account was logged on",
                        "SubCategory": "LOGOFF",
                        "SystemID": 10014624,
                        "Type": "Audit Success",
                        "VendorID": 4624
                    },
                    "Source": {
                        "Domain": "domain_name",
                        "IP": "ipv4",
                        "Hostname": "dst_computer_name",
                        "LogonID": "0x250308a5",
                        "LogonTypeID": 10,
                        "Port": "48820",
                        "SecurityID": "S-1-5-21",
                        "UserName": "username"
                    },
                    "Severity": {
                        "ID": 6,
                        "Name": "information"
                    },
                    "Category": {
                        "ID": 12545
                    },
                    "EventSource": {
                        "Category": "Operating System",
                        "Collector": "wmicollector",
                        "Description": "Windows Server",
                        "IP": "192.168.1.154",
                        "PrefixID": 1001,
                        "Product": "Windows",
                        "Tag": "Windows-DC",
                        "Type": "Operating System",
                        "Vendor": "Microsoft",
                        "Version": "2008+"
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
                        "Type": "User",
                        "SubType": "Add",
                        "Context": "Identity"
                    },
                    "Event": {
                        "Category": "Account Management",
                        "Info": "A user account was created",
                        "SubCategory": "User Account Management",
                        "SystemID": 10014720,
                        "Type": "Audit Success",
                        "VendorID": 4720
                    },
                    "Source": {
                        "Domain": "domain_name",
                        "LogonID": "0x250328a5",
                        "Port": "48820",
                        "SecurityID": "S-1-5-21",
                        "UserName": "username"
                    },
                    "Destination": {
                        "UserName": "dst_username",
                        "Domain": "domain_name"
                    },
                    "Severity": {
                        "ID": 6,
                        "Name": "information"
                    },
                    "Category": {
                        "ID": 12545
                    },
                    "Attributes": {
                        "AccountExpires": "<never>",
                        "DisplayName": "username",
                        "PasswordLastSet": "<never>",
                        "SAMAccountName": "username"
                    },
                    "EventSource": {
                        "Category": "Operating System",
                        "Collector": "wmicollector",
                        "Description": "Windows Server",
                        "IP": "192.168.1.154",
                        "PrefixID": 1001,
                        "Product": "Windows",
                        "Tag": "Windows-DC",
                        "Type": "Operating System",
                        "Vendor": "Microsoft",
                        "Version": "2008+"
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
                        "Type": "Password",
                        "SubType": "Change",
                        "Context": "Identity"
                    },
                    "Event": {
                        "Category": "Account Management",
                        "Info": "An attempt was made to reset an accounts password",
                        "SubCategory": "User Account Management",
                        "SystemID": 10014724,
                        "Type": "Audit Success",
                        "VendorID": 4724
                    },
                    "Source": {
                        "Domain": "domain_name",
                        "LogonID": "0x250328a5",
                        "Port": "48820",
                        "SecurityID": "S-1-5-21",
                        "UserName": "src_username"
                    },
                    "Destination": {
                        "UserName": "dst_username",
                        "Domain": "domain_name"
                    },
                    "Severity": {
                        "ID": 6,
                        "Name": "information"
                    },
                    "Category": {
                        "ID": 13824
                    },
                    "EventSource": {
                        "Category": "Operating System",
                        "Collector": "wmicollector",
                        "Description": "Windows Server",
                        "IP": "192.168.1.154",
                        "PrefixID": 1001,
                        "Product": "Windows",
                        "Tag": "Windows-DC",
                        "Type": "Operating System",
                        "Vendor": "Microsoft",
                        "Version": "2008+"
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
                        "Type": "Password",
                        "SubType": "Change",
                        "Context": "Identity"
                    },
                    "Event": {
                        "Category": "Account Management",
                        "Info": "An attempt was made to change an account's password",
                        "SubCategory": "User Account Management",
                        "SystemID": 10014723,
                        "Type": "Audit Success",
                        "VendorID": 4723
                    },
                    "Source": {
                        "Domain": "domain_name",
                        "LogonID": "0x250328a5",
                        "Port": "48820",
                        "SecurityID": "S-1-5-21...",
                        "UserName": "src_username"
                    },
                    "Destination": {
                        "UserName": "dst_username",
                        "Domain": "domain_name"
                    },
                    "Severity": {
                        "ID": 6,
                        "Name": "information"
                    },
                    "Category": {
                        "ID": 13824
                    },
                    "EventSource": {
                        "Category": "Operating System",
                        "Collector": "wmicollector",
                        "Description": "Windows Server",
                        "IP": "192.168.1.154",
                        "PrefixID": 1001,
                        "Product": "Windows",
                        "Tag": "Windows-DC",
                        "Type": "Operating System",
                        "Vendor": "Microsoft",
                        "Version": "2008+"
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
                        "Type": "Group",
                        "SubType": "Delete",
                        "Context": "Identity"
                    },
                    "Event": {
                        "Category": "Account Management",
                        "Info": "A security-enabled global group was deleted",
                        "SubCategory": "Security Group Management",
                        "SystemID": 10014730,
                        "Type": "Audit Success",
                        "VendorID": 4730
                    },
                    "Source": {
                        "Domain": "domain_name",
                        "LogonID": "0x250328a5",
                        "SecurityID": "S-1-5-21",
                        "UserName": "username"
                    },
                    "Group": {
                        "Name": "group_name",
                        "Domain": "domain_name"
                    },
                    "Severity": {
                        "ID": 6,
                        "Name": "information"
                    },
                    "Category": {
                        "ID": 13826
                    },
                    "EventSource": {
                        "Category": "Operating System",
                        "Collector": "wmicollector",
                        "Description": "Windows Server",
                        "IP": "192.168.1.154",
                        "PrefixID": 1001,
                        "Product": "Windows",
                        "Tag": "Windows-DC",
                        "Type": "Operating System",
                        "Vendor": "Microsoft",
                        "Version": "2008+"
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
                        "Type": "Group",
                        "SubType": "Add",
                        "Context": "Identity"
                    },
                    "Event": {
                        "Category": "Account Management",
                        "Info": "A member was added to a security-enabled local group",
                        "SubCategory": "Security Group Management",
                        "SystemID": 10014732,
                        "Type": "Audit Success",
                        "VendorID": 4732
                    },
                    "Source": {
                        "Domain": "domain_name",
                        "LogonID": "0x4C1A7",
                        "SecurityID": "S-1-5-21-3692184502-2293977038-605302642-500",
                        "UserName": "username"
                    },
                    "Group": {
                        "Domain": "domain_name",
                        "Name": "group_name"
                    },
                    "Destination": {
                        "Attribute": "cn=logsign_hotspot,CN=Users,DC=technical,DC=local"
                    },
                    "Severity": {
                        "ID": 6,
                        "Name": "information"
                    },
                    "Category": {
                        "ID": 13826
                    },
                    "EventSource": {
                        "Category": "Operating System",
                        "Collector": "wmicollector",
                        "Description": "Windows Server",
                        "IP": "192.168.1.154",
                        "PrefixID": 1001,
                        "Product": "Windows",
                        "Tag": "Windows-DC",
                        "Type": "Operating System",
                        "Vendor": "Microsoft",
                        "Version": "2008+"
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
                        "Type": "Group",
                        "SubType": "Add",
                        "Context": "Identity"
                    },
                    "Event": {
                        "Category": "Account Management",
                        "Info": "A security-enabled global group was created",
                        "SubCategory": "Security Group Management",
                        "SystemID": 10014727,
                        "Type": "Audit Success",
                        "VendorID": 4727
                    },
                    "Source": {
                        "Domain": "domain_name",
                        "LogonID": "0x4C1A7",
                        "SecurityID": "S-1-5-21",
                        "UserName": "username"
                    },
                    "Group": {
                        "Domain": "domain_name",
                        "Name": "group_name",
                        "SecurityID": "S-1-5-21-3692184502-2293977038-605302642-1145"
                    },
                    "Category": {
                        "ID": 13826
                    },
                    "Severity": {
                        "ID": 6,
                        "Name": "information"
                    },
                    "EventSource": {
                        "Category": "Operating System",
                        "Collector": "wmicollector",
                        "Description": "Windows Server",
                        "IP": "192.168.1.154",
                        "PrefixID": 1001,
                        "Product": "Windows",
                        "Tag": "Windows-DC",
                        "Type": "Operating System",
                        "Vendor": "Microsoft",
                        "Version": "2008+"
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
                        "Type": "Computer",
                        "SubType": "Add",
                        "Context": "Identity"
                    },
                    "Event": {
                        "Category": "Account Management",
                        "Info": "A Computer account was created",
                        "SubCategory": "Computer Account Management",
                        "SystemID": 10014741,
                        "Type": "Audit Success",
                        "VendorID": 4741
                    },
                    "Source": {
                        "Domain": "domain_name",
                        "LogonID": "0x4C1A7",
                        "SecurityID": "S-1-5-21-3692184502-2293977038-605302642-500",
                        "UserName": "src_username"
                    },
                    "Destination": {
                        "Domain": "domain_name",
                        "UserName": "dst_username"
                    },
                    "Severity": {
                        "ID": 6,
                        "Name": "information"
                    },
                    "Attributes": {
                        "AccountExpires": "<never>",
                        "PasswordLastSet": "<never>"
                    },
                    "Category": {
                        "ID": 13825
                    },
                    "EventSource": {
                        "Category": "Operating System",
                        "Collector": "wmicollector",
                        "Description": "Windows Server",
                        "IP": "192.168.1.154",
                        "PrefixID": 1001,
                        "Product": "Windows",
                        "Tag": "Windows-DC",
                        "Type": "Operating System",
                        "Vendor": "Microsoft",
                        "Version": "2008+"
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
                        "Type": "Computer",
                        "SubType": "Deleted",
                        "Context": "Identity"
                    },
                    "Event": {
                        "Category": "Account Management",
                        "Info": "A Computer account was deleted",
                        "SubCategory": "Computer Account Management",
                        "SystemID": 10014743,
                        "Type": "Audit Success",
                        "VendorID": 4743
                    },
                    "Source": {
                        "Domain": "domain_name",
                        "LogonID": "0x4C1A7",
                        "SecurityID": "S-1-5-21-3692184502-2293977038-605302642-500",
                        "UserName": "src_username"
                    },
                    "Destination": {
                        "Domain": "domain_name",
                        "UserName": "dst_username"
                    },
                    "Severity": {
                        "ID": 6,
                        "Name": "information"
                    },
                    "Category": {
                        "ID": 13825
                    },
                    "EventSource": {
                        "Category": "Operating System",
                        "Collector": "wmicollector",
                        "Description": "Windows Server",
                        "IP": "192.168.1.154",
                        "PrefixID": 1001,
                        "Product": "Windows",
                        "Tag": "Windows-DC",
                        "Type": "Operating System",
                        "Vendor": "Microsoft",
                        "Version": "2008+"
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
                        "Type": "User",
                        "SubType": "Delete",
                        "Context": "Identity"
                    },
                    "Event": {
                        "Category": "Account Management",
                        "Info": "A user account was deleted",
                        "SubCategory": "User Account Management",
                        "SystemID": 10014726,
                        "Type": "Audit Success",
                        "VendorID": 4726
                    },
                    "Source": {
                        "Domain": "domain_name",
                        "LogonID": "0x250328a5",
                        "SecurityID": "S-1-5-21",
                        "UserName": "src_username"
                    },
                    "Destination": {
                        "Domain": "domain_name",
                        "UserName": "dst_username"
                    },
                    "Severity": {
                        "ID": 6,
                        "Name": "information"
                    },
                    "Category": {
                        "ID": 12545
                    },
                    "EventSource": {
                        "Category": "Operating System",
                        "Collector": "wmicollector",
                        "Description": "Windows Server",
                        "IP": "192.168.1.154",
                        "PrefixID": 1001,
                        "Product": "Windows",
                        "Tag": "Windows-DC",
                        "Type": "Operating System",
                        "Vendor": "Microsoft",
                        "Version": "2008+"
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
                        "Type": "User",
                        "SubType": "Enable",
                        "Context": "Identity"
                    },
                    "Event": {
                        "Category": "Account Management",
                        "Info": "A user account was enabled",
                        "SubCategory": "User Account Management",
                        "SystemID": 10014722,
                        "Type": "Audit Success",
                        "VendorID": 4722
                    },
                    "Source": {
                        "Domain": "domain_name",
                        "LogonID": "0x250328a5",
                        "Port": "23220",
                        "SecurityID": "S-1-5-21...",
                        "UserName": "src_username"
                    },
                    "Destination": {
                        "Domain": "domain_name",
                        "UserName": "dst_username"
                    },
                    "Severity": {
                        "ID": 6,
                        "Name": "information"
                    },
                    "Category": {
                        "ID": 12545
                    },
                    "EventSource": {
                        "Category": "Operating System",
                        "Collector": "wmicollector",
                        "Description": "Windows Server",
                        "IP": "192.168.1.154",
                        "PrefixID": 1001,
                        "Product": "Windows",
                        "Tag": "Windows-DC",
                        "Type": "Operating System",
                        "Vendor": "Microsoft",
                        "Version": "2008+"
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
                        "Type": "User",
                        "SubType": "Disable",
                        "Context": "Identity"
                    },
                    "Event": {
                        "Category": "Account Management",
                        "Info": "A user account was disabled",
                        "SubCategory": "User Account Management",
                        "SystemID": 10014725,
                        "Type": "Audit Success",
                        "VendorID": 4725
                    },
                    "Source": {
                        "Domain": "domain_name",
                        "LogonID": "0x250228a5",
                        "Port": "13220",
                        "SecurityID": "S-1-5-21",
                        "UserName": "src_username"
                    },
                    "Destination": {
                        "Domain": "domain_name",
                        "UserName": "dst_username"
                    },
                    "Severity": {
                        "ID": 6,
                        "Name": "information"
                    },
                    "Category": {
                        "ID": 13824
                    },
                    "EventSource": {
                        "Category": "Operating System",
                        "Collector": "wmicollector",
                        "Description": "Windows Server",
                        "IP": "192.168.1.154",
                        "PrefixID": 1001,
                        "Product": "Windows",
                        "Tag": "Windows-DC",
                        "Type": "Operating System",
                        "Vendor": "Microsoft",
                        "Version": "2008+"
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
                        "Type": "User",
                        "SubType": "Lock",
                        "Context": "Identity"
                    },
                    "Event": {
                        "Category": "Account Management",
                        "Info": "A user account was locked out",
                        "SubCategory": "User Account Management",
                        "SystemID": 10014740,
                        "Type": "Audit Success",
                        "VendorID": 4740
                    },
                    "Source": {
                        "Domain": "domain_name",
                        "LogonID": "0x3e7",
                        "SecurityID": "S-1-5-18-3692184502-2293977038-605302642-500",
                        "UserName": "src_username"
                    },
                    "Destination": {
                        "UserName": "dst_username",
                        "HostName": "dst_computer_name",
                        "SecurityID": "S-1-5-18-3692184502-2293977038-605302642-1132"
                    },
                    "Severity": {
                        "ID": 6,
                        "Name": "information"
                    },
                    "Category": {
                        "ID": 13824
                    },
                    "EventSource": {
                        "Category": "Operating System",
                        "Collector": "wmicollector",
                        "Description": "Windows Server",
                        "IP": "192.168.1.154",
                        "PrefixID": 1001,
                        "Product": "Windows",
                        "Tag": "Windows-DC",
                        "Type": "Operating System",
                        "Vendor": "Microsoft",
                        "Version": "2008+"
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
                        "Type": "User",
                        "SubType": "Unlock",
                        "Context": "Identity"
                    },
                    "Event": {
                        "Category": "Account Management",
                        "Info": "A user account was unlocked",
                        "SubCategory": "User Account Management",
                        "SystemID": 10014767,
                        "Type": "Audit Success",
                        "VendorID": 4767
                    },
                    "Source": {
                        "Domain": "domain_name",
                        "LogonID": "0x29ef1f23",
                        "SecurityID": "S-1-5-18",
                        "UserName": "src_username"
                    },
                    "Destination": {
                        "Domain": "domain_mame",
                        "UserName": "dst_username"
                    },
                    "Severity": {
                        "ID": 6,
                        "Name": "information"
                    },
                    "Category": {
                        "ID": 13824
                    },
                    "EventSource": {
                        "Category": "Operating System",
                        "Collector": "wmicollector",
                        "Description": "Windows Server",
                        "IP": "192.168.1.154",
                        "PrefixID": 1001,
                        "Product": "Windows",
                        "Tag": "Windows-DC",
                        "Type": "Operating System",
                        "Vendor": "Microsoft",
                        "Version": "2008+"
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
                        "Type": "User",
                        "SubType": "Change",
                        "Context": "Identity"
                    },
                    "Event": {
                        "Category": "Account Management",
                        "Info": "The name of an account was changed",
                        "SubCategory": "User Account Management",
                        "SystemID": 10014781,
                        "Type": "Audit Success",
                        "VendorID": 4781
                    },
                    "Source": {
                        "Domain": "domain_name",
                        "LogonID": "0x29ef1f23",
                        "SecurityID": "S-1-5-18",
                        "UserName": "src_username"
                    },
                    "Destination": {
                        "Domain": "domain_mame",
                        "UserName": "dst_username"
                    },
                    "Severity": {
                        "ID": 6,
                        "Name": "information"
                    },
                    "Category": {
                        "ID": 13824
                    },
                    "EventSource": {
                        "Category": "Operating System",
                        "Collector": "wmicollector",
                        "Description": "Windows Server",
                        "IP": "192.168.1.154",
                        "PrefixID": 1001,
                        "Product": "Windows",
                        "Tag": "Windows-DC",
                        "Type": "Operating System",
                        "Vendor": "Microsoft",
                        "Version": "2008+"
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
                        "Type": "Group",
                        "SubType": "Change",
                        "Context": "Identity"
                    },
                    "Event": {
                        "Category": "Account Management",
                        "Info": "A security-enabled global group was changed",
                        "SubCategory": "Security Group Management",
                        "SystemID": 10014737,
                        "Type": "Audit Success",
                        "VendorID": 4737
                    },
                    "Source": {
                        "Domain": "domain_name",
                        "LogonID": "0x29ef1f23",
                        "SecurityID": "S-1-5-18",
                        "UserName": "src_username"
                    },
                    "Group": {
                        "Domain": "domain_mame",
                        "Name": "group_name"
                    },
                    "Severity": {
                        "ID": 6,
                        "Name": "information"
                    },
                    "Category": {
                        "ID": 13824
                    },
                    "EventSource": {
                        "Category": "Operating System",
                        "Collector": "wmicollector",
                        "Description": "Windows Server",
                        "IP": "192.168.1.154",
                        "PrefixID": 1001,
                        "Product": "Windows",
                        "Tag": "Windows-DC",
                        "Type": "Operating System",
                        "Vendor": "Microsoft",
                        "Version": "2008+"
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
                        "Type": "Fileshare",
                        "SubType": "Grant",
                        "Context": "Object"
                    },
                    "Event": {
                        "Action": "Delete",
                        "Category": "OBJECT Access",
                        "Info": "A network share object was checked for access",
                        "SubCategory": "Detailed File Share",
                        "SystemID": 10015145,
                        "Type": "Audit Success",
                        "VendorID": 5145
                    },
                    "Source": {
                        "Domain": "domain_name",
                        "IP": "ipv4",
                        "LogonID": "0x4e15a65",
                        "Port": "61266",
                        "LogonId": 61266,
                        "SecurityID": "S-3-5-18",
                        "UserName": "username"
                    },
                    "Severity": {
                        "ID": 6,
                        "Name": "information"
                    },
                    "AccessCheckResults": {
                        "DELETE": "Granted by D:(A;;FA;;;WD)",
                        "ReadAttributes": "Granted by D:(A;;FA;;;WD)"
                    },
                    "Category": {
                        "ID": 12811
                    },
                    "EventSource": {
                        "Category": "Operating System",
                        "Collector": "wmicollector",
                        "Description": "Windows Server",
                        "IP": "192.168.1.154",
                        "PrefixID": 1001,
                        "Product": "Windows",
                        "Tag": "File Server",
                        "Type": "Operating System",
                        "Vendor": "Microsoft",
                        "Version": "2008+"
                    },
                    "Object": {
                        "Access": "ReadAttributes,DELETE",
                        "AccessMask": "0x1008a0",
                        "Name": "object_name",
                        "Type": "File"
                    },
                    "Share": {
                        "Name": "share_name",
                        "Path": "share_path"
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
                        "Type": "Fileshare",
                        "SubType": "Grant",
                        "Context": "Object"
                    },
                    "Event": {
                        "Action": "Execute",
                        "Category": "OBJECT Access",
                        "Info": "A network share object was checked for access",
                        "SubCategory": "Detailed File Share",
                        "SystemID": 10015145,
                        "Type": "Audit Success",
                        "VendorID": 5145
                    },
                    "Source": {
                        "Domain": "domain_name",
                        "IP": "ipv4",
                        "LogonID": "0x4e15a65",
                        "Port": "61266",
                        "LogonID": 61216,
                        "SecurityID": "S-1-5-18",
                        "UserName": "username"
                    },
                    "Severity": {
                        "ID": 6,
                        "Name": "information"
                    },
                    "AccessCheckResults": {
                        "Execute/Traverse": "Granted by D:(A;;FA;;;WD)",
                        "ReadAttributes": "Granted by D:(A;;FA;;;WD)"
                    },
                    "Category": {
                        "ID": 12811
                    },
                    "EventSource": {
                        "Category": "Operating System",
                        "Collector": "wmicollector",
                        "Description": "Windows Server",
                        "IP": "192.168.1.154",
                        "PrefixID": 1001,
                        "Product": "Windows",
                        "Tag": "File Server",
                        "Type": "Operating System",
                        "Vendor": "Microsoft",
                        "Version": "2008+"
                    },
                    "Object": {
                        "Access": "ReadAttributes,Execute/Traverse,SYNCHRONIZE",
                        "AccessMask": "0x1000a0",
                        "Name": "object_name",
                        "Type": "File"
                    },
                    "Share": {
                        "Name": "share_name",
                        "Path": "share_path"
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
                        "Type": "Fileshare",
                        "SubType": "Grant",
                        "Context": "Object"
                    },
                    "Event": {
                        "Action": "Write",
                        "Category": "OBJECT Access",
                        "Info": "A network share object was checked for access",
                        "SubCategory": "Detailed File Share",
                        "SystemID": 10015145,
                        "Type": "Audit Success",
                        "VendorID": 5145
                    },
                    "Source": {
                        "Domain": "domain_name",
                        "IP": "ipv4",
                        "LogonID": "0x4e15a65",
                        "Port": "61261",
                        "LogonId": 61216,
                        "SecurityID": "S-2-5-18",
                        "UserName": "username"
                    },
                    "Severity": {
                        "ID": 6,
                        "Name": "information"
                    },
                    "AccessCheckResults": {
                        "WriteAttributes": "Granted by D:(A;;FA;;;WD)",
                        "WriteData(orAddFile)": "Granted by D:(A;;FA;;;WD)",
                        "WriteEA": "Granted by D:(A;;FA;;;WD)"
                    },
                    "Category": {
                        "ID": 12811
                    },
                    "EventSource": {
                        "Category": "Operating System",
                        "Collector": "wmicollector",
                        "Description": "Windows Server",
                        "IP": "192.168.1.154",
                        "PrefixID": 1001,
                        "Product": "Windows",
                        "Tag": "File Server",
                        "Type": "Operating System",
                        "Vendor": "Microsoft",
                        "Version": "2008+"
                    },
                    "Object": {
                        "Access": " WriteAttributes,ReadAttributes,WriteEA,AppendData,WriteData,SYNCHRONIZE",
                        "AccessMask": "0x1000a0",
                        "Name": "object_name",
                        "Type": "File"
                    },
                    "Share": {
                        "Name": "share_name",
                        "Path": "share_path"
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
                        "Type": "Fileshare",
                        "SubType": "Grant",
                        "Context": "Object"
                    },
                    "Event": {
                        "Action": "Read",
                        "Category": "OBJECT Access",
                        "Info": "A network share object was checked for access",
                        "SubCategory": "Detailed File Share",
                        "SystemID": 10015145,
                        "Type": "Audit Success",
                        "VendorID": 5145
                    },
                    "Source": {
                        "Domain": "domain_name",
                        "IP": "ipv4",
                        "LogonID": "0x4e15a65",
                        "Port": "31161",
                        "LogonID": 61216,
                        "SecurityID": "S-2-5-18",
                        "UserName": "username"
                    },
                    "Severity": {
                        "ID": 6,
                        "Name": "information"
                    },
                    "AccessCheckResults": {
                        "WriteAttributes": "Granted by D:(A;;FA;;;WD)",
                        "WriteData(orAddFile)": "Granted by D:(A;;FA;;;WD)",
                        "WriteEA": "Granted by D:(A;;FA;;;WD)"
                    },
                    "Category": {
                        "ID": 12811
                    },
                    "EventSource": {
                        "Category": "Operating System",
                        "Collector": "wmicollector",
                        "Description": "Windows Server",
                        "IP": "192.168.1.154",
                        "PrefixID": 1001,
                        "Product": "Windows",
                        "Tag": "File Server",
                        "Type": "Operating System",
                        "Vendor": "Microsoft",
                        "Version": "2008+"
                    },
                    "Object": {
                        "Access": " WriteAttributes,ReadAttributes,WriteEA,AppendData,SYNCHRONIZE,READ_CONTROL",
                        "AccessMask": "0x1000a0",
                        "Name": "object_name",
                        "Type": "File"
                    },
                    "Share": {
                        "Name": "share_name",
                        "Path": "share_path"
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
                        "Type": "File",
                        "SubType": "Access",
                        "Context": "Object"
                    },
                    "Event": {
                        "Action": "Delete",
                        "Category": "OBJECT Access",
                        "Info": "An attempt was made to access an object",
                        "SubCategory": "File System",
                        "SystemID": 10014663,
                        "Type": "Audit Success",
                        "VendorID": 4663
                    },
                    "Source": {
                        "Domain": "domain_name",
                        "LogonID": "0x23ab79c",
                        "SecurityID": "S-2-5-18",
                        "UserName": "username"
                    },
                    "Severity": {
                        "ID": 6,
                        "Name": "information"
                    },
                    "Category": {
                        "ID": 12801
                    },
                    "EventSource": {
                        "Category": "Operating System",
                        "Collector": "wmicollector",
                        "Description": "Windows Server",
                        "IP": "192.168.1.154",
                        "PrefixID": 1001,
                        "Product": "Windows",
                        "Tag": "File Server",
                        "Type": "Operating System",
                        "Vendor": "Microsoft",
                        "Version": "2008+"
                    },
                    "Object": {
                        "Access": "DELETE",
                        "AccessMask": "0x10000",
                        "Name": "object_name",
                        "Server": "Security",
                        "Type": "File"
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
                        "Type": "File",
                        "SubType": "Access",
                        "Context": "Object"
                    },
                    "Event": {
                        "Action": "Read",
                        "Category": "OBJECT Access",
                        "Info": "An attempt was made to access an object",
                        "SubCategory": "File System",
                        "SystemID": 10014663,
                        "Type": "Audit Success",
                        "VendorID": 4663
                    },
                    "Source": {
                        "Domain": "domain_name",
                        "LogonID": "0x2315d6c",
                        "SecurityID": "S-1-5-3",
                        "UserName": "username"
                    },
                    "Severity": {
                        "ID": 6,
                        "Name": "information"
                    },
                    "AccessCheckResults": {
                        "WriteAttributes": "Granted by D:(A;;FA;;;WD)",
                        "WriteData(orAddFile)": "Granted by D:(A;;FA;;;WD)",
                        "WriteEA": "Granted by D:(A;;FA;;;WD)"
                    },
                    "Category": {
                        "ID": 12800
                    },
                    "EventSource": {
                        "Category": "Operating System",
                        "Collector": "wmicollector",
                        "Description": "Windows Server",
                        "IP": "192.168.1.154",
                        "PrefixID": 1001,
                        "Product": "Windows",
                        "Tag": "File Server",
                        "Type": "Operating System",
                        "Vendor": "Microsoft",
                        "Version": "2008+"
                    },
                    "Object": {
                        "Access": "ReadData (or ListDirectory)",
                        "AccessMask": "0x1",
                        "Name": "object_name",
                        "Server": "Security",
                        "Type": "File"
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
                        "Type": "File",
                        "SubType": "Access",
                        "Context": "Object"
                    },
                    "Event": {
                        "Action": "Write",
                        "Category": "OBJECT Access",
                        "Info": "An attempt was made to access an object",
                        "SubCategory": "File System",
                        "SystemID": 10014663,
                        "Type": "Audit Success",
                        "VendorID": 4663
                    },
                    "Source": {
                        "Domain": "domain_name",
                        "LogonID": "0x2315d6c",
                        "SecurityID": "S-1-5-21",
                        "UserName": "username"
                    },
                    "Severity": {
                        "ID": 6,
                        "Name": "information"
                    },
                    "AccessCheckResults": {
                        "WriteAttributes": "Granted by D:(A;;FA;;;WD)",
                        "WriteData(orAddFile)": "Granted by D:(A;;FA;;;WD)",
                        "WriteEA": "Granted by D:(A;;FA;;;WD)"
                    },
                    "Category": {
                        "ID": 12800
                    },
                    "EventSource": {
                        "Category": "Operating System",
                        "Collector": "wmicollector",
                        "Description": "Windows Server",
                        "IP": "192.168.1.154",
                        "PrefixID": 1001,
                        "Product": "Windows",
                        "Tag": "File Server",
                        "Type": "Operating System",
                        "Vendor": "Microsoft",
                        "Version": "2008+"
                    },
                    "Object": {
                        "Access": "ReadData (or ListDirectory)",
                        "AccessMask": "0x1",
                        "Name": "object_name",
                        "HandleID": "0x1160",
                        "Server": "Security",
                        "Type": "File"
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
                        "Type": "File",
                        "SubType": "Access",
                        "Context": "Object"
                    },
                    "Event": {
                        "Action": "Execute",
                        "Category": "OBJECT Access",
                        "Info": "An attempt was made to access an object",
                        "SubCategory": "File System",
                        "SystemID": 10014663,
                        "Type": "Audit Success",
                        "VendorID": 4663
                    },
                    "Source": {
                        "Domain": "domain_name",
                        "LogonID": "0x2315d6c",
                        "SecurityID": "S-1-5-21",
                        "UserName": "username"
                    },
                    "Severity": {
                        "ID": 6,
                        "Name": "information"
                    },
                    "AccessCheckResults": {
                        "WriteAttributes": "Granted by D:(A;;FA;;;WD)",
                        "WriteData(orAddFile)": "Granted by D:(A;;FA;;;WD)",
                        "WriteEA": "Granted by D:(A;;FA;;;WD)"
                    },
                    "Category": {
                        "ID": 12800
                    },
                    "EventSource": {
                        "Category": "Operating System",
                        "Collector": "wmicollector",
                        "Description": "Windows Server",
                        "IP": "192.168.1.154",
                        "PrefixID": 1001,
                        "Product": "Windows",
                        "Tag": "File Server",
                        "Type": "Operating System",
                        "Vendor": "Microsoft",
                        "Version": "2008+"
                    },
                    "Object": {
                        "Access": "Execute/Traverse",
                        "AccessMask": "0x1",
                        "Name": "object_name",
                        "HandleID": "0x1160",
                        "Server": "Security",
                        "Type": "File"
                    },
                    "Time": {
                        "Generated": "es_date",
                        "Received": "es_date"
                    }
                }
    ]
}
