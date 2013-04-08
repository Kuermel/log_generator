{
    "fields" : [
        { "templateCount" : {"count":1} },
        { "remote_ip" : {"type": "random", "generate_type":"IPv4" } },
        { "error_date": {"type": "random", "generate_type":"datetime", "format": "%a %b %d %H:%M:%S %Y" } }
    ],
    "template" : [
          "[${error_date}] [error] [client ${remote_ip}] PHP Warning:  Smarty error: unable to read resource: \"settings/admin.tpl\" in /opt/project/admin.class.php on line 1144, referer: http://127.0.0.1/admin.php"
    ]
}
