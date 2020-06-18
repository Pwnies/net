{ stdenv, fetchFromGitHub, isPy3k, iw, wpa_supplicant, python2, busybox, makeWrapper, ethtool, wireguard }:

let
  pythonEnv = python2.withPackages(ps: with ps; [ pyyaml ]);
in stdenv.mkDerivation rec {
  name = "net";

  src = ./.;

  buildInputs = [ makeWrapper ];

  disabled = isPy3k;

  installPhase = ''
    mkdir -p $out/bin
    cp $src/net $out/bin;
  '';

  postFixup = ''
      wrapProgram $out/bin/net \
        --prefix PATH : ${stdenv.lib.makeBinPath [ pythonEnv iw wpa_supplicant busybox ethtool wireguard ]}
  '';

  meta = with stdenv.lib; {
    homepage = "https://github.com/Pwnies/net/";
    description = "Super lightweight network manager";
    license = licenses.unlicense;
    maintainers = with maintainers; [ kristoff3r ];
  };
}
