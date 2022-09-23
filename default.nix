# https://github.com/davhau/mach-nix
#
with (import <nixpkgs> {});
let

  algoliasearch = pkgs.python38Packages.buildPythonPackage rec {
    pname = "algoliasearch";
    version = "2.6.2";

    src = pkgs.python38Packages.fetchPypi {
      inherit pname version;
      sha256 = "0jar4r4vm40spbpmbs18yf1i57gj2cvbp7vyg1l1s8infskpz8j6";
    };

    propagatedBuildInputs = with pkgs.python38Packages; [
      setuptools
      tox
      mypy
      requests
      types-requests
    ];

    doCheck = false;
  };

  pip-pkgs = python-packages: with python-packages; [
    requests
    algoliasearch
  ];

  python-env = python38.withPackages pip-pkgs;

in
mkShell {
  buildInputs = [
    python-env
  ];

  # shellHook = ''  '';
}
