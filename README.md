[![Build Status](https://travis-ci.org/psy2848048/hdacpy.svg?branch=master)](https://travis-ci.org/psy2848048/hdacpy)
[![codecov](https://codecov.io/gh/psy2848048/hdacpy/branch/master/graph/badge.svg)](https://codecov.io/gh/psy2848048/hdacpy)
# hdacpy

Tools for Hdac wallet management and offline transaction signing  
Forked from hukkinj1/cosmospy

<!--- Don't edit the version line below manually. Let bump2version do it for you. -->
> Version 0.1.3

> Tools for Hdac wallet management and offline transaction signing

## Installing
Installing from PyPI repository (https://pypi.org/project/hdacpy):
```bash
pip install hdacpy
```

## Usage

### Prerequisite

Run node & rest-server in following step: (https://docs.hdac.io/installation/build)  
This library runs on RESTful API

### Generating a wallet
```python
from hdacpy.wallet import generate_wallet
wallet = generate_wallet()
```
The value assigned to `wallet` will be a dictionary just like:
```python
{
    'private_key': '6dcd05d7ac71e09d3cf7da666709ebd59362486ff9e99db0e8bc663570515afa',
    'public_key': '03e8005aad74da5a053602f86e3151d4f3214937863a11299c960c28d3609c4775',
    'address': 'friday1r5v5srda7xfth3hn2s26txvrcrntldjuv7dedk'
}
 ```

### Signing transactions
```python
from hdacpy.transaction import Transaction
tx = Transaction(
        host="http://localhost:1317",
        privkey="26d167d549a4b2b66f766b0d3f2bdbe1cd92708818c338ff453abde316a2bd59",
        chain_id="friday-devtest",
    )
tx.transfer(
        sender_address="friday1lgharzgds89lpshr7q8kcmd2esnxkfpwmfgk32",
        recipient_address="friday1z47ev5u5ujmc7kwv49tut7raesg55tjyk2wvhd",
        amount=amount, gas_price=2000000, fee=10000
    )
res = tx.send_tx()
```
`transfer()` executes `POST` to organize tx, and `send_tx()` signs & broadcast the tx.

## Contributing
1. Fork/clone the repository.

1. Install dependencies (you'll probably want to create a virtual environment, using your preferred method, first).
    ```bash
    pip install -r requirements.txt
    ```

1. Install pre-commit hooks
    ```bash
    pre-commit install
    ```

1. After making changes and having written tests, make sure tests pass:
    ```bash
    pytest
    ```

1. Commit, push, and make a PR.
