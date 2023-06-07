# How to make the Drawbot work upon power

There are several ways a script can run on startup on Linux Ubuntu.
A way of doing it, is by executing a service with systemd.

## Make and execute systemd service

1. Downloading the file below. Name it: 'startup_service.py'
```python
import argparse
import getpass
import os

STARTUP_SERVICE_TEMPLATE = """
[Unit]
Description=JetBot stats display service
[Service]
Type=simple
User=%s
ExecStart=/bin/sh -c "python3 -m jetbot.apps.startup"
WorkingDirectory=%s
Restart=always
[Install]
WantedBy=multi-user.target
"""

STATS_SERVICE_NAME = 'jetbot_startup'

def get_startup_service():
    return STARTUP_SERVICE_TEMPLATE % (getpass.getuser(), os.environ['HOME'])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', default='jetbot_startup.service')
    args = parser.parse_args()

    with open(args.output, 'w') as f:
        f.write(get_startup_service())
```

2. Run the downloaded file with
```python
python3 startup_service.py
```

3. A file: jetbot_startup.service has been created. We now need to move it to the system directory. This can be done with
```bash
mv jetbot_startup.service etc/systemd/system/jetbot_startup.service
```
systemd is a software suite that provides an array of system components for Linux operating systems. Its main aim is to unify service configuration and behavior across Linux distributions

4. Next step is to enable the created service:
```bash
sudo systemctl daemon-reload
sudo systemctl enable jetbot_startup.service
```
We have now told the systemd package that we want to execute the following command upon startup"
```bash
/bin/sh -c "python3 -m jetbot.apps.startup"
```

5. Lastly, we put the python file we want to execute in
```bash
# File path
```
