{
    "fields" : [
        { "templateCount" : {"count":4} },
        { "datetime": {"type": "random", "generate_type":"datetime", "format": "%b %d %H:%M:%S" } },
        { "pri" : {"type": "random", "generate_type":"integer", "min":0, "max":8 } },
        { "ip" : {"type": "random", "generate_type":"IPv4" } },
        { "ip2" : {"type": "from_list_file", "file" : "ip.list", "method":"random" } },
        { "port" : {"type": "random", "generate_type":"integer", "min":1, "max":10000 } },
        { "port2" : {"type": "random", "generate_type":"integer", "min":1, "max":5000 } },
        { "sent" : {"type": "random", "generate_type":"integer", "min":1, "max":10000 } },
        { "rcvd" : {"type": "random", "generate_type":"integer", "min":1, "max":10000 } },
        { "duration" : {"type": "random", "generate_type":"integer", "min":0, "max":20 } },
        { "duration2" : {"type": "random", "generate_type":"integer", "min":0, "max":59 } },
        { "number" : {"type": "random", "generate_type":"integer", "min":0, "max":500 } },
        { "url" : {"type": "from_list_file", "file" : "url.list", "method":"random" } },
        { "arg" : {"type": "from_list_file", "file" : "arg.list", "method":"random" } },
        { "mailto" : {"type": "from_list_file", "file" : "mail.list", "method":"random" } },
        { "mailfrom" : {"type": "from_list_file", "file" : "mail.list", "method":"random" } }
    ],
    "template" : [
        "${datetime} CompanyXYZ http-proxy[2129]: Allow 2-Managament 5-Wifi tcp ${ip} ${ip2} ${port} ${port2} msg=\"HTTP Request\" proxy_act=\"HTTP_Genel\" op=\"GET\" dstname=\"${url}\" arg=\"${arg}\" sent_bytes=\"${sent}\" rcvd_bytes=\"${rcvd}\" elapsed_time=\"${duration}.${duration2} sec(s)\" reputation=\"${number}\"  (HTTP_Genel-00)",
        "${datetime} CompanyXYZ firewall: Allow 2-Managament 5-Wifi 44 tcp 20 64 ${ip} ${ip2} ${port} ${port2} offset 6 AF 1860955081 win 32950 app_name=\"unknown\" app_cat_name=\"unknown\" app_id=\"65535\" app_cat_id=\"255\" app_beh_id=\"255\" app_beh_name=\"unknown\" msg=\"Application identified\" (HTTP_Genel-00)",
        "${datetime} CompanyXYZ smtp-proxy[2125]: Allow 5-Wifi 2-Managament tcp ${ip} ${ip2} ${port} ${port2} msg=\"ProxyAllow: SMTP spamBlocker exception was matched\" proxy_act=\"SMTP-in\" from=\"${mailfrom}\" to=\"${mailto}\"  (Smtp_in-00)",
        "${datetime} CompanyXYZ cfm[2128]: msg_id=\"0F03-0006\" callback failed for DATA event in https handler using HTTPS_Genel proxy action"
    ]
}
