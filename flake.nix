{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/20.03";
  };

  outputs = { nixpkgs, self, ... }@inputs:
    {
      defaultPackage.x86_64-linux =
        with import nixpkgs { system = "x86_64-linux"; };
        callPackage ./derivation.nix { };

      checks.x86_64-linux.build = self.defaultPackage.x86_64-linux;

      overlay = final: prev: {
        net = self.defaultPackage.x86_64-linux;
      };
    };
}
