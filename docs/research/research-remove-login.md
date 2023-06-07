#How to remove login
The root account is often the most targeted account by crackers via SSH under Linux. An enabled SSH root account on a Linux server exposed to a network or, worse, exposed in Internet can pose a high degree of security concern by system administrators.
The SSH root account should be disabled in all cases in Linux in order to harden your server security. You should login via SSH on a remote server only with a normal user account and, then, change privileges to root account via sudo or su command.
In order to disable SSH root account, first log in to your server console with a normal account with root privileges by issuing the below commands.
```bash
$ su tecmint
$ sudo su -   # Drop privileges to root account
```

After you’ve logged in to console, open the main SSH configuration file for editing with your favorite text editor by issuing the below command. The SSH main configuration file is usually located in /etc/ssh/ directory in most of Linux distributions.

```bash
# nano /etc/ssh/sshd_config
```

In this file, search for the line “PermitRootLogin” and update the line to look like in the below file excerpt. On some Linux distributions, the “PermitRootLogin” line is preceded by the hashtag sign (#) meaning that the line is commented. In this case uncomment the line by removing the hashtag sign and set the line to no.
```bash
PermitRootLogin no
```

