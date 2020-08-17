{
  inputs = {
    nixpkgs-unstable.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs = { nixpkgs-unstable, self, ... }@inputs:
    {
      defaultPackage.x86_64-linux =
        with import nixpkgs-unstable { system = "x86_64-linux"; };
        callPackage ./derivation.nix { };

      checks.x86_64-linux.build = self.defaultPackage.x86_64-linux;

      overlay = final: prev: {
        net = self.defaultPackage.x86_64-linux;
      };
    };
}
