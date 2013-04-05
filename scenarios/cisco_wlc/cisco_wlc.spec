{
    "fields" : [
        { "templateCount" : {"count":1} },
        { "date": {"type": "random", "generate_type":"datetime", "format": "%b %d %H:%M:%S.%f" } },
        { "number" : {"type": "random", "generate_type":"integer", "min":0, "max":5000 } }
    ],
    "template" : [
         "WLC1: *SISF BT Process: ${date}: %LOG-4-Q_IND: debug.c:${number} Unhandled debug module ${number}."
    ]
}
