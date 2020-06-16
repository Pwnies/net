{ pkgs ? import <nixpkgs> {} }:

pkgs.callPackage ./derivation.nix { isPy3k = pkgs.pythonPackages.isPy3k; }
