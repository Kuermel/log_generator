{
    "fields" : [
        { "date": {"type": "random", "generate_type":"datetime", "format": "%Y/%m/%d %H:%S:%M" } },
        { "src" : {"type": "random", "generate_type":"IPv4" } },
        { "dst" : {"type": "random", "generate_type":"IPv4" } },
        { "url" : {"type": "from_list_file", "file" : "url.list", "method":"sequential" } },
        { "user_agent" : {"type": "from_list_file", "file" : "user_agent.list", "method":"random" } },
        { "respond_code" : {"type": "from_list_file", "file": "respond_codes.list", "method":"ratio", "ratio":"50,50" } },
        { "sent" : {"type": "random", "generate_type":"integer", "min":1, "max":1000 } },
        { "recv" : {"type": "random", "generate_type":"integer", "min":1, "max":1000000 } }
    ],
    "template" : "date=\"${date}\" url=\"${url}\" src=\"${src}\" dst=\"${dst}\" recv=\"${recv}\" sent=\"${sent}\" user_agent=\"${user_agent}\" respond_code=\"${respond_code}\""
}