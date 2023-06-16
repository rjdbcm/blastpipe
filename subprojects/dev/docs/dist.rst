
========
OZI dist
========

Distribution, provenance, and verification.

Default Toolchain
^^^^^^^^^^^^^^^^^
* pyc_wheel_:
  Strips binary of uncompiled sources.
* semantic-release_ (via python-semantic-release_):
  Automates determining the next version number, generating the release notes,
  and publishing the package.
* sigstore_ (via sigstore-python_):
  A tool for generating and verifying Sigstore signatures.

.. _pyc_wheel: https://pypi.org/project/pyc_wheel/
.. _semantic-release: https://semantic-release.gitbook.io/semantic-release/
.. _sigstore: https://www.sigstore.dev/
.. _sigstore-python: https://pypi.org/project/sigstore
.. _python-semantic-release: https://pypi.org/project/python-semantic-release
