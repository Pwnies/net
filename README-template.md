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
  genkey:
    Generate a WireGuard key pair.
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
Connecting to MyWirelessNetwork
Sending DHCP request
Address acquired: 192.168.1.42
```

### Configuration

The file `~/.net.conf` holds a list of configured networks (in YAML).  An
example is included in `.net.conf.example`:

```
#include ".net.conf.example"
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

| Dependency             | Debian package                       |
|------------------------|--------------------------------------|
| `/bin/ip`              | `iproute2`                           |
| `/sbin/ethtool`        | `ethtool`                            |
| `/sbin/iw`             | `iw`                                 |
| `/sbin/udhcpc`         | `udhcpc`                             |
| `/sbin/wpa_cli`        | `wpasupplicant`                      |
| `/sbin/wpa_supplicant` | `wpasupplicant`                      |
| `/usr/bin/chattr`      | `e2fsprogs`                          |
| `/usr/bin/expand`      | `coreutils`                          |
| `/usr/bin/cut`         | `coreutils`                          |
| `/usr/bin/pkill`       | `procps`                             |
| `/usr/sbin/openvpn`    | `openvpn`                            |
| `/usr/bin/wg`          | `https://www.wireguard.com/install/` |
| Python package `yaml`  | `python-yaml` / PyPI `pyyaml`        |

It is also a good idea to uninstall resolvconf, as it overwrites the DNS settings.

**udhcpc** is part of the busybox suite, and can be installed, and used,
on non-Debian systems, which doesn't have a separate package, by:
* Install busybox with udhcpc compiled in
* Hard-link busybox as udhcpc
```
# ln /bin/busybox /usr/local/bin/udhcpc
```
* Install a client script somewhere and make it executable - [udhcpc README](https://udhcp.busybox.net/README.udhcpc)
* Set _udhcpc-config:_ under _common:_
```
common:
  udhcpc-config: /etc/udhcpc/default.script
```

## Contributors

If you want to contribute, feel free to make a pull request on [Github](https://github.com/Pwnies/net), please read [CONTRIBUTING](CONTRIBUTING) and [the license](UNLICENSE) first.

This project was originally developed by [br0ns](https://github.com/br0ns) and based on [IdolfHatler/vcsh-wifi](https://git.pwnies.dk/IdolfHatler/vcsh-wifi) by [Idolf](https://github.com/idolf).
For a complete list; check the log.
