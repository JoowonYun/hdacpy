import json
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
        account_num=dummy_num,
        sequence=dummy_num,
        gas_price=dummy_num,
    )
    tx._get_sign_message = Mock(return_value=unordered_sign_message)  # type: ignore

    expected_signature = (
        "5YvLtcxp3BzxCTGM6TlKZ//nNBakmWyUrvydJgOCeQAc5DnFEnm5/Q48zEtEHy0dS3iNB7KH/ykqcYnWGHWbNQ=="
    )

    actual_signature = tx._sign()
    assert actual_signature == expected_signature


def test_transfer():
    expected_pushable_tx = '{"mode":"sync","tx":{"fee":{"amount":[],"gas":"37000"},"memo":"","msg":[{"type":"executionengine/Execute","value":{"block_hash":"AA==","contract_owner_account":"friday1lgharzgds89lpshr7q8kcmd2esnxkfpwmfgk32","exec_account":"friday1lgharzgds89lpshr7q8kcmd2esnxkfpwmfgk32","gas_price":"2000000","payment_args":"AQAAAAQAAAADgIQe","session_args":"AgAAABgAAAAUAAAAFX2WU5Tkt49ZzKlXxfh9zBFKLkQIAAAAAAAAAAAAAAA="}}],"signatures":[{"account_number":"11335","pub_key":{"type":"tendermint/PubKeySecp256k1","value":"A49sjCd3Eul+ZXyof7qO460UaO73otrmySHyTNSLW+Xn"},"sequence":"0","signature":"spk/FpIIwMvPv1aKKPCxGWgJ0jdfATpAd2Z0Go+onOhPgMXJtNdiyl+MDaqPLevVlGaZPw42BbhHxrt/EtXFLg=="}]}}'  # noqa: E501

    _tx_total_cost = 388000
    fee = 1000
    amount = _tx_total_cost - fee

    tx = Transaction(
        host="http://localhost:1317",
        privkey="26d167d549a4b2b66f766b0d3f2bdbe1cd92708818c338ff453abde316a2bd59",
        account_num=11335,
        sequence=0,
        gas_price=37000,
        chain_id="friday-devtest",
    )
    tx.transfer(
        sender_address="friday1lgharzgds89lpshr7q8kcmd2esnxkfpwmfgk32",
        recipient_address="friday1z47ev5u5ujmc7kwv49tut7raesg55tjyk2wvhd",
        amount=amount, gas_price=2000000
    )

    res_without_bin = tx._get_pushable_tx()
    res_without_bin['tx']['msg'][0]['value'].pop('session_code')
    res_without_bin['tx']['msg'][0]['value'].pop('payment_code')

    assert expected_pushable_tx == json.dumps(res_without_bin, separators=(",", ":"), sort_keys=True)

    res = tx.send_tx()
    print(res.json())
    assert res.status_code == 200

def test_bond():
    expected_pushable_tx = '{"mode":"sync","tx":{"fee":{"amount":[],"gas":"37000"},"memo":"","msg":[{"type":"executionengine/Execute","value":{"block_hash":"AA==","contract_owner_account":"friday1lgharzgds89lpshr7q8kcmd2esnxkfpwmfgk32","exec_account":"friday1lgharzgds89lpshr7q8kcmd2esnxkfpwmfgk32","gas_price":"2000000","payment_args":"AQAAAAQAAAADgIQe","session_args":"AgAAABgAAAAUAAAA+i/RiQ2By/DC4/APbG2qzCZrJC4IAAAAAAAAAAAAAAA="}}],"signatures":[{"account_number":"11335","pub_key":{"type":"tendermint/PubKeySecp256k1","value":"A49sjCd3Eul+ZXyof7qO460UaO73otrmySHyTNSLW+Xn"},"sequence":"0","signature":"Ouv7wssXWeqTlgFD2Eu9Baq0Mx0ugFvR0qRlQseK/XA82obFV8TdiqkYhwZGBL4wL3CIE0DzqkYEwaHdSnecMA=="}]}}'  # noqa: E501

    _tx_total_cost = 388000
    fee = 1000
    amount = _tx_total_cost - fee

    tx = Transaction(
        host="http://localhost:1317",
        privkey="26d167d549a4b2b66f766b0d3f2bdbe1cd92708818c338ff453abde316a2bd59",
        account_num=11335,
        sequence=0,
        gas_price=37000,
        chain_id="friday-devtest",
    )
    tx.bond(
        address="friday1lgharzgds89lpshr7q8kcmd2esnxkfpwmfgk32",
        amount=amount, gas_price=2000000
    )

    res_without_bin = tx._get_pushable_tx()
    res_without_bin['tx']['msg'][0]['value'].pop('session_code')
    res_without_bin['tx']['msg'][0]['value'].pop('payment_code')

    assert expected_pushable_tx == json.dumps(res_without_bin, separators=(",", ":"), sort_keys=True)

    res = tx.send_tx()
    print(res.json())
    assert res.status_code == 200

def test_unbond():
    expected_pushable_tx = '{"mode":"sync","tx":{"fee":{"amount":[],"gas":"37000"},"memo":"","msg":[{"type":"executionengine/Execute","value":{"block_hash":"AA==","contract_owner_account":"friday1lgharzgds89lpshr7q8kcmd2esnxkfpwmfgk32","exec_account":"friday1lgharzgds89lpshr7q8kcmd2esnxkfpwmfgk32","gas_price":"2000000","payment_args":"AQAAAAQAAAADgIQe","session_args":"AgAAABgAAAAUAAAA+i/RiQ2By/DC4/APbG2qzCZrJC4IAAAAAAAAAAAAAAA="}}],"signatures":[{"account_number":"11335","pub_key":{"type":"tendermint/PubKeySecp256k1","value":"A49sjCd3Eul+ZXyof7qO460UaO73otrmySHyTNSLW+Xn"},"sequence":"0","signature":"X1sW95QiiXWBftf2xOlldpGPI9KU8AKJCBs/Hfoeg9obVveqigbSLFdL+1vWnJXsgaKLqWQSfhUetPisiH2eaQ=="}]}}'  # noqa: E501

    _tx_total_cost = 388000
    fee = 1000
    amount = _tx_total_cost - fee

    tx = Transaction(
        host="http://localhost:1317",
        privkey="26d167d549a4b2b66f766b0d3f2bdbe1cd92708818c338ff453abde316a2bd59",
        account_num=11335,
        sequence=0,
        gas_price=37000,
        chain_id="friday-devtest",
    )
    tx.unbond(
        address="friday1lgharzgds89lpshr7q8kcmd2esnxkfpwmfgk32",
        amount=amount, gas_price=2000000
    )

    res_without_bin = tx._get_pushable_tx()
    res_without_bin['tx']['msg'][0]['value'].pop('session_code')
    res_without_bin['tx']['msg'][0]['value'].pop('payment_code')

    assert expected_pushable_tx == json.dumps(res_without_bin, separators=(",", ":"), sort_keys=True)

    res = tx.send_tx()
    print(res.json())
    assert res.status_code == 200
