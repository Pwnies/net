{ stdenv, iw, wpa_supplicant, python2, busybox, ethtool, wireguard, openvpn, runCommand }:

let
  pythonEnv = python2.withPackages(ps: with ps; [ pyyaml ]);
  path = stdenv.lib.makeBinPath [ pythonEnv iw wpa_supplicant busybox ethtool wireguard openvpn ];
in runCommand "net" {
  meta = with stdenv.lib; {
    homepage = "https://github.com/Pwnies/net/";
    description = "Super lightweight network manager";
    license = licenses.unlicense;
    maintainers = with maintainers; [ kristoff3r ];
  };
} ''
  mkdir -p $out/bin
  cp ${./net} $out/bin/net
  # Fix the path now to make patchShebangs do the right thing
  PATH=${path} patchShebangs $out/bin/net
  sed -i "1 a import os; os.environ['PATH'] = '${path}:' + os.environ['PATH']" $out/bin/net
''
