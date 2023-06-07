# How to upload program code to the Jetnano development board

This guide requires the following:

1. Doing all the steps of the [Setup Drawbot guide](connect_jetbot_computer.md)
2. A monitor with an HDMI or Display Port output
3. An HDMI or Display Port cable
4. A USB keyboard

## 1. Getting the Drawbot ip-address

You need the ip-address of the Drawbot to connect with it.

1. Enter the username

```bash
login: [JETBOT-LOGIN-GOES-HERE]
```

2. Enter the password

```bash
password: [JETBOT-PASSWORD-GOES-HERE]
```

2. Getting the ip-address

```bash
hostname -I
```

The result will be unique for everyone. You should see a result like

```bash
192.0.82.1
```

## 2. Connecting to the device wirelessly

Now that we have the ip-address, we can access the Jupiter Notebook environment of the Drawbot

1. Open your browser and go to the ip-address that you've obtained in the previous step like this:

```
[ip-address]:8888
```

You should see a screen popping up with the Jupiter Notebook logo. If the page doesn't load, something is wrong with the
internet connection.

2. Login with

```
jetbot
```

You are now connected with the Drawbot and able to add the program code.

## 3. Connecting to the device using micro-usb

This guide is a work in progress

In short:

1. Use a jumper wire to enable power using the DC-connector.
2. Plug in the DC-connector into a wall outlet. Plug the other end into the DC input on the Drawbot
3. Plug in a micro usb cable into the Drawbot. Plug the other end into your computer.

Next steps cannot be tested since we don't require a DC-connector.

### [Work in Progress]

