{
    "fields" : [
        { "templateCount" : {"count":3} },
        { "date": {"type": "random", "generate_type":"datetime", "format": "%b %d %H:%M:%S.%f" } }
    ],
    "template" : [
          "1|17673: ${date}: %LINK-3-UPDOWN: Interface GigabitEthernet1/16, changed state to up",
          "3802505: *${date}: %AUTHMGR-7-RESULT: Authentication result 'no-response' from 'dot1x' for client (Unknown MAC) on Interface Gi1/0/10 AuditSessionID 0A64C82100000E505294D249",
          "1|17673: ${date}: %LINK-3-UPDOWN: Interface GigabitEthernet1/16, changed state to up"
    ]
}
