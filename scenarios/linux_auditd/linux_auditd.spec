{
    "fields" : [
        { "templateCount" : {"count":2 } },
        { "datetime": {"type": "random", "generate_type":"datetime", "format": "%b %d %H:%M:%S" } },
        { "timestamp": {"type": "random", "generate_type":"timestamp" } },
        { "url" : {"type": "from_list_file", "file" : "url.list", "method":"sequential" } },
        { "id" : {"type": "random", "generate_type":"integer", "min":1, "max":100000 } }
    ],
    "template" : [
        "${datetime} debian audispd: node=debian type=PATH msg=audit(${timestamp}:${id}): item=0 name=\"${url}\" inode=175 dev=fe:00 mode=041777 ouid=0 ogid=0 rdev=00:00",
        "type=PATH msg=audit(${timestamp}:${id}): item=0 name=\"${url}\" inode=175 dev=fe:00 mode=${id} ouid=0 ogid=0 rdev=00:00"
     ]
}
