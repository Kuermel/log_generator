{
    "fields" : [
        { "templateCount" : {"count":1} },
        { "datetime": {"type": "random", "generate_type":"datetime", "format": "%b %d %H:%M:%S" } },
        { "pri" : {"type": "random", "generate_type":"integer", "min":0, "max":8 } },
        { "ip" : {"type": "random", "generate_type":"IPv4" } },
        { "ip2" : {"type": "from_list_file", "file" : "ip.list", "method":"random" } },
        { "port" : {"type": "random", "generate_type":"integer", "min":1, "max":10000 } },
        { "port2" : {"type": "random", "generate_type":"integer", "min":1, "max":5000 } },
        { "sent" : {"type": "random", "generate_type":"integer", "min":1, "max":10000 } },
        { "rcvd" : {"type": "random", "generate_type":"integer", "min":1, "max":10000 } },
        { "number" : {"type": "random", "generate_type":"integer", "min":0, "max":500 } },
        { "url" : {"type": "from_list_file", "file" : "url.list", "method":"random" } },
        { "arg" : {"type": "from_list_file", "file" : "arg.list", "method":"random" } }
    ],
    "template" : [
        "Original Address=${ip} SIEMLOG|${datetime}|${ip}|7.7.0|${pri}|Transaction permitted|reason=-|act=permitted|1|app=http|dvc=${ip}|dst=${ip2}|dhost=company.name.com|dpt=${port2}|src=${ip}|spt=${port}|suser=LDAP://127.0.0.1 OU\\=BDN,OU\\=XX,OU\\=YY,DC\\=ZZ,DC\\=XX/User|destinationTranslatedPort=${port2}|rt=1362658920000|in=${rcvd}|out=${sent}|requestMethod=GET|requestClientApplication=Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; WOW64; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.2; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)|Policy=role-8**IMKB Policy|DynCat=0|ContentType=image/jpeg|DispositionCode=1048|ScanDuration=2|request=${url}${arg}"
    ]
}
