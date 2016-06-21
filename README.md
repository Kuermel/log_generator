Simple Log Generator from scenarios.       

Load up scenario from scenario files
Can generate date,ipv4,integer field values
Can sends generated logs to remote syslog server

Usage:
 $ ./start.sh                            # output to stdout
 $ ./start.sh -o stdout                  # output to stdout
 $ ./start.sh -o syslog -s 192.168.1.100 # output to syslog server

 -w no to disable eps_wave

- How to write new scenarios?
  Check out scenarios/ directory. You simple need to write a json file.

- web_browse scenario generates

--- CUT ---
date="2012/03/03 22:13:34" url="http://www.yahoo.com/" src="146.240.218.193" dst="157.241.168.141" recv="654906" sent="234" user_agent="Mozilla" respond_code="404"
date="2012/03/03 22:13:34" url="http://www.logsign.net/" src="104.106.112.143" dst="62.47.195.125" recv="996068" sent="598" user_agent="Mozilla" respond_code="500"
date="2012/03/03 22:13:34" url="http://www.google.com/" src="84.240.129.251" dst="86.17.20.69" recv="367147" sent="845" user_agent="Mozilla" respond_code="500"
--- CUT ---

- apache2_accesslog scenario generates

--- CUT ---
187.181.217.240 - - [2012/03/03 22:58:55 -0200] "GET /index.html HTTP/1.0" 301 1631
134.171.13.58 - - [2012/03/03 22:58:55 -0200] "GET /blog/1 HTTP/1.0" 301 4382
252.210.15.127 - - [2012/03/03 22:58:55 -0200] "GET /help HTTP/1.0" 301 4380
40.162.52.217 - - [2012/03/03 22:58:55 -0200] "OPTIONS /index.html HTTP/1.0" 301 4664
168.70.227.79 - - [2012/03/03 22:58:55 -0200] "OPTIONS /blog/1 HTTP/1.1" 301 4293
53.119.191.182 - - [2012/03/03 22:58:55 -0200] "POST /help HTTP/1.0" 301 6707
--- CUT ---

This file was modified by IntelliJ IDEA 11.0.2 for binding GitHub repository

demo servera 10.0.0.1,10.0.0.2 seklinde eklenen senderlar icin log generator calistirdiginda sistem uzerine bu network icin router eklenmesi gerekiyor.
yoksa calismaz.

route add -net 10.0.0.0 netmask 255.255.255.0 lo