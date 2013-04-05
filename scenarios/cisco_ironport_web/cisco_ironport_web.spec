{
    "fields" : [
        { "templateCount" : {"count":1} },
        { "date": {"type": "random", "generate_type":"datetime", "format": "%b %d %H:%M:%S" } },
        { "number" : {"type": "random", "generate_type":"integer", "min":0, "max":100 } },
        { "ip" : {"type": "random", "generate_type":"IPv4" } },
        { "url" : {"type": "from_list_file", "file" : "url.list", "method":"sequential" } },
        { "ip2" : {"type": "from_list_file", "file" : "ip.list", "method":"random" } },
        { "port" : {"type": "random", "generate_type":"integer", "min":1, "max":10000 } },
        { "port2" : {"type": "random", "generate_type":"integer", "min":1, "max":5000 } }
    ],
    "template" : [
          "${date} Logsign-accesslogs: Info: 1355748378.759 7 ${ip} TCP_MISS/304 ${number} GET ${url} - DIRECT/$url - DEFAULT_CASE_11-AscPol-AscLocalNetwork-NONE-NONE-NONE-DefaultGroup <IW_news,5.9,0,\"-\",0,0,0,-,\"-\",-,-,-,\"-\",-,-,\"-\",\"-\",-,-,IW_news,-,\"-\",\"-\",\"Unknown\",\"Unknown\",\"-\",\"-\",208.00,0,-,\"-\",\"-\"> -"
    ]
}
