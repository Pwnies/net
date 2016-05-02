# net

Super lightweight network manager.

## Usage

RTFM:

```
$ net help
usage: net [<command>] [<args>] [--config=<config>] [--iface=<interface>]
           [--no-vpn] [--verbose] [-h] [--help]

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
  vpn <name> [stop]:
    Connect to, or disconnect from, VPN.
  show [<connection>]:
    Show configuration options.  If no connection is specified, all are show.
  help:
    You're reading it.

Options:
  --config=<config>:
    Select configurations file.  If <config> is "-" no configuration file is
    used.  Defaults to "~/.net.conf".
  --iface=<interface>:
    Select networking interface.  Overridden by configuration file if specified.
    Defaults to first WiFi capable interface found.
  --no-vpn:
    Don't connect to a VPN.  Acts as if the connection configuration did not
    have a `vpn` field.
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
  # Always connect to VPN
  vpn: myvpn

ignored:
  interfaces:
  - br[0-9]+
  - tap[0-9]+
  - tun[0-9]+
  # Docker
  - docker[0-9]+
  # Virtualbox
  - vboxnet[0-9]+
  # VMWare
  - vmnet[0-9]+

vpn:
  myvpn: |
    client
    dev tun

    proto udp
    remote my-server-1 1194

    resolv-retry infinite
    nobind
    persist-key
    persist-tun

    ca ca.crt
    cert client.crt
    key client.key

    comp-lzo
    verb 3

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
      identity="YOUR-ID-HERE@ku.dk"
      password="YOUR-PASSPHRASE-HERE"
      key_mgmt=WPA-EAP
      pairwise=TKIP
      eap=TTLS
      phase2="auth=MSCHAPv2"
    }

my-home-network:
  ssid: SSID-HERE
  psk: PASSPHRASE-HERE
  vpn: # Empty: don't connect to VPN when at home
```

Using this config file you can connect to `my-home-network` using the command:

```
$ net my-home-network
```

Notice that the section `common` does not define a network but rather settings
common to *all* network configurations (in this case using Google's DNS servers,
randomizing the MAC address and hostname [`<name>` will be replaced by an actual
name] and connecting to a VPN).

The `ignored` and `vpn` sections do not define networks either.  The `ignored`
section contains a list of interfaces to be ignored by e.g. `net stop` and the
`vpn` section contains the OpenVPN configurations for each VPN.

## Installing

Put `net` in your `PATH`.

## `Bash` completion

Put `_net_bash_completion` in your path and add the line

```
_net_bash_completion
```

to `~/.bash_completion`.

## Dependencies

| Dependency             | Debian package                |
|------------------------|-------------------------------|
| `/bin/ip`              | `iproute2`                    |
| `/sbin/ethtool`        | `ethtool`                     |
| `/sbin/ifconfig`       | `net-tools`                   |
| `/sbin/iw`             | `iw`                          |
| `/sbin/iwconfig`       | `wireless-tools`              |
| `/sbin/udhcpc`         | `udhcpc`                      |
| `/sbin/wpa_cli`        | `wpasupplicant`               |
| `/sbin/wpa_supplicant` | `wpasupplicant`               |
| `/usr/bin/awk`         | `mawk` / `gawk`               |
| `/usr/bin/chattr`      | `e2fsprogs`                   |
| `/usr/bin/expand`      | `coreutils`                   |
| `/usr/bin/pkill`       | `procps`                      |
| `/usr/sbin/openvpn`    | `openvpn`                     |
| Python package `yaml`  | `python-yaml` / PyPI `pyyaml` |

## Contributers

This script was developed by [myself](https://github.com/br0ns) and
[Idolf](https://github.com/idolf).
