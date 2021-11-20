# net

Super lightweight network manager.

## Usage

RTFM:

```
#shell "./net help"
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
#include "config.example"
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
* Install a client script somewhere and make it executable - [udhcpc script](default.script) - [udhcpc README](https://udhcp.busybox.net/README.udhcpc)
* Set _udhcpc-config:_ under _common:_
```
common:
  udhcpc-config: /etc/udhcpc/default.script
```

## Contributors

If you want to contribute, feel free to make a pull request on [Github](https://github.com/Pwnies/net), please read [CONTRIBUTING](CONTRIBUTING) and [the license](UNLICENSE) first.

This project was originally developed by [br0ns](https://github.com/br0ns) and [TethysSvensson](https://github.com/TethysSvensson).

For a complete list; check the log.
