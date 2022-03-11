{ lib, iw, wpa_supplicant, python2, busybox, ethtool, wireguard-tools, openvpn, runCommand }:

let
  pythonEnv = python2.withPackages (ps: with ps; [ pyyaml ]);
  path = lib.makeBinPath [ pythonEnv iw wpa_supplicant busybox ethtool wireguard-tools openvpn ];
in runCommand "net" {
  meta = with lib; {
    homepage = "https://github.com/Pwnies/net/";
    description = "Super lightweight network manager";
    license = licenses.unlicense;
    maintainers = with maintainers; [ kristoff3r TethysSvensson ];
  };
} ''
  mkdir -p $out/bin $out/share/bash-completion/completions
  cp ${./net} $out/bin/net
  cp ${./_net_bash_completion} $out/share/bash-completion/completions/net
  # Fix the path now to make patchShebangs do the right thing
  PATH=$PATH:${path} patchShebangs $out/bin/net
  sed -i "1 a import os; os.environ['PATH'] = '${path}:' + os.environ['PATH']" $out/bin/net
''
