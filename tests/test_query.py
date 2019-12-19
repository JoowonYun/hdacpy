import json
from unittest.mock import Mock

from hdacpy.transaction import Transaction

def test_balance():
    tx = Transaction(
        host="http://localhost:1317",
        privkey="26d167d549a4b2b66f766b0d3f2bdbe1cd92708818c338ff453abde316a2bd59",
        account_num=11335,
        sequence=0,
        gas=37000,
        chain_id="friday-devtest",
    )
    resp = tx.balance(address="friday15evpva2u57vv6l5czehyk69s0wnq9hrkqulwfz")
    
    assert resp.status_code == 200
    assert resp.json()['value'] == "500000000"