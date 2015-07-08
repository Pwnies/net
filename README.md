# net

Super lightweight network manager.

## Usage

RTFM:

```
$ net help
usage: net [<command>] [<args>] [--config=<config>] [--iface=<interface>]
           [--verbose] [-h] [--help]

Shorthands:
  If no positional arguments are given the command is "list".
  If one positional argument is given the command is "connect".

Commands:
  list:
    List available connections.
  scan:
    Scan for access points.
  connect <connection> [<password>]:
    If <connection> is present in the configuration file then use that,
    otherwise connect to an access point with SSID <connection>, using the
    password <password> if specified.
  stop [<interface> [<interface> ...]]:
    Bring down the connection.  Brings down all interfaces if called with no
    arguments.
  dns [<dns> [<dns> ...]]:
    Change DNS server.  No argument or "dhcp" requests DNS servers via DHCP.
  mac [<mac>]:
    Change the MAC address of the interface specified by --iface.  If no address
    is given, one is chosen at random.
  help:
    You're reading it.

Options:
  --config=<config>:
    Select configurations file.  If <config> is "-" no configuration file is
    used.  Defaults to "~/.net.conf".
  --iface=<interface>:
    Select networking interface.  Overridden by configuration file if specified.
    Defaults to first WiFi capable interface found.
  --verbose:
    Print every executed command (and the result) to stdout.
```

The simplest usage is probably connecting to a wireless network:

```
$ net connect MyWirelessNetwork MySecretPassphrase
Connecting
Sending DHCP request
DONE (addr: 192.168.1.42)
```

### Configuration file

The file `~/.net.conf` holds a list of configured networks (in YAML).  An
example is included in `.net.conf.example`:

```
common:
  mac: 00:??:??:??:??:??
  dns: 8.8.8.8, 8.8.4.4
  hostname: <name>s-MacBook-Pro

wired:
  dns: dhcp
  mac: default
  hostname:

static:
  interface: eth0
  addr: 192.168.0.42/24
  gateway: 192.168.0.1

eduroam:
  ssid: eduroam
  wpa: |
    network={
      identity="YOUR-ID-HERE@alumni.ku.dk"
      password="YOUR-PASSPHRASE-HERE"
      anonymous_identity="anonymous@di.ku.dk"
      key_mgmt=WPA-EAP
      pairwise=TKIP
      eap=TTLS
      phase2="auth=PAP"
    }

my-home-network:
  ssid: SSID-HERE
  psk: PASSPHRASE-HERE
```

Using this config file you can connect to `my-home-network` using the command:

```
$ net my-home-network
```

Notice that the section `common` does not define a network but rather settings
common to *all* network configurations (in this case using Google's DNS servers
and randomizing the MAC address and hostname [`<name>` will be replaced by an
actual name]).

## Installing

Put `net` in your `PATH`.

## `Bash` comletion

Put `_net_bash_completion` in your path and add the line

```
_net_bash_completion
```

to `~/.bash_completion`.

## Dependencies

`net` depends on `udhcpc` (part of [BusyBox](http://www.busybox.net/)),
[`wpa_supplicant`](http://w1.fi/wpa_supplicant/) and probably other things as
well (YMMV).

## Contributers

This script was developed by [myself](https://github.com/br0ns) and
[Idolf](https://github.com/idolf).
