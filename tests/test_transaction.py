import json
import pytest
from unittest.mock import Mock

from hdacpy.transaction import Transaction


def test_sign():
    private_key = "2afc5a66b30e7521d553ec8e6f7244f906df97477248c30c103d7b3f2c671fef"
    unordered_sign_message = {
        "chain_id": "friday-devtest",
        "account_number": "1",
        "fee": {"gas": "21906", "amount": [{"amount": "0", "denom": ""}]},
        "memo": "",
        "sequence": "0",
        "msgs": [
            {
                "type": "cosmos-sdk/Send",
                "value": {
                    "inputs": [
                        {
                            "address": "friday1qperwt9wrnkg5k9e5gzfgjppzpqhyav5j24d66",
                            "coins": [{"amount": "1", "denom": "STAKE"}],
                        }
                    ],
                    "outputs": [
                        {
                            "address": "friday1yeckxz7tapz34kjwnjxvmxzurerquhtrmxmuxt",
                            "coins": [{"amount": "1", "denom": "STAKE"}],
                        }
                    ],
                },
            }
        ],
    }
    dummy_num = 1337
    tx = Transaction(
        host="http://localhost:1317",
        privkey=private_key,
        chain_id="friday-devnet",
    )
    tx._get_sign_message = Mock(return_value=unordered_sign_message)  # type: ignore

    expected_signature = (
        "5YvLtcxp3BzxCTGM6TlKZ//nNBakmWyUrvydJgOCeQAc5DnFEnm5/Q48zEtEHy0dS3iNB7KH/ykqcYnWGHWbNQ=="
    )

    actual_signature = tx._sign()
    assert actual_signature == expected_signature

@pytest.mark.skip(reason="only works if RESTful server runs in local")
def test_transfer():
    _tx_total_cost = 388000
    fee = 1000
    amount = _tx_total_cost - fee

    tx = Transaction(
        host="http://localhost:1317",
        privkey="26d167d549a4b2b66f766b0d3f2bdbe1cd92708818c338ff453abde316a2bd59",
        chain_id="friday-devnet",
    )
    tx.transfer(
        sender_address="friday1lgharzgds89lpshr7q8kcmd2esnxkfpwmfgk32",
        recipient_address="friday1z47ev5u5ujmc7kwv49tut7raesg55tjyk2wvhd",
        amount=str(amount)+"dummy", gas_price=18000000, fee=10000
    )

    res = tx.send_tx()
    resp = res.json()
    resp['tx']['msg'][1]['value'].pop('session_code')
    resp['tx']['msg'][1]['value'].pop('payment_code')

    assert res.status_code == 200

@pytest.mark.skip(reason="only works if RESTful server runs in local")
def test_bond():
    _tx_total_cost = 388000
    fee = 1000
    amount = _tx_total_cost - fee

    tx = Transaction(
        host="http://localhost:1317",
        privkey="26d167d549a4b2b66f766b0d3f2bdbe1cd92708818c338ff453abde316a2bd59",
        chain_id="friday-devnet",
    )
    tx.bond(
        address="friday1lgharzgds89lpshr7q8kcmd2esnxkfpwmfgk32",
        amount=amount, gas_price=2000000, fee=10000
    )

    res_without_bin = tx._get_pushable_tx()
    res_without_bin['tx']['msg'][0]['value'].pop('session_code')
    res_without_bin['tx']['msg'][0]['value'].pop('payment_code')

    res = tx.send_tx()
    print(res.json())
    assert res.status_code == 200

@pytest.mark.skip(reason="only works if RESTful server runs in local")
def test_unbond():
    _tx_total_cost = 388000
    fee = 1000
    amount = _tx_total_cost - fee

    tx = Transaction(
        host="http://localhost:1317",
        privkey="26d167d549a4b2b66f766b0d3f2bdbe1cd92708818c338ff453abde316a2bd59",
        chain_id="friday-devtest",
    )
    tx.unbond(
        address="friday1lgharzgds89lpshr7q8kcmd2esnxkfpwmfgk32",
        amount=amount, gas_price=2000000, fee=10000
    )

    res_without_bin = tx._get_pushable_tx()
    res_without_bin['tx']['msg'][0]['value'].pop('session_code')
    res_without_bin['tx']['msg'][0]['value'].pop('payment_code')

    res = tx.send_tx()
    print(res.json())
    assert res.status_code == 200
