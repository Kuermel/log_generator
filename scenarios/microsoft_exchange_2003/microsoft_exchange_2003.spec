{
    "fields" : [
        { "templateCount" : {"count":1} },
        { "datetime": {"type": "random", "generate_type":"datetime", "format": "%b %d %H:%M:%S" } },
        { "datetime2": {"type": "random", "generate_type":"datetime", "format": "%Y-%m-%d %H:%M:%S" } },
        { "ip" : {"type": "random", "generate_type":"IPv4" } },
        { "ip2" : {"type": "from_list_file", "file" : "ip.list", "method":"random" } },
        { "mailto" : {"type": "from_list_file", "file" : "mail.list", "method":"random" } },
        { "mailfrom" : {"type": "from_list_file", "file" : "mail.list", "method":"random" } }
    ],
    "template" : [
          "${datetime} ServerXYZ [info] ${datetime2} GMT ${ip} XYZ-PC server.company.com ServerXYZ ${ip2} ${mailto} 1031 ServerXYZ9KuERIqVDokS00004d8e@company.com 0 0 114311 6 ${datetime2} GMT 0 Version: 6.0.3790.4675 - =?iso-8859-9?Q?RE:mail_subject_data=FD?= ${mailfrom} -#am=FD?= ${mailfrom} -#_program=FD?= ${mailfrom} -#am=FD?= ${mailfrom} -#rogram=FD?="
    ]
}
