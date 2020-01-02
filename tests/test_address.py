import hdacpy.wallet as address

test_vector = {
    'private_key': '367360433d797cabd35361abdb3f6d0b94d27d7222d3af22a49028b7f4beb85d',
    'public_key': '0320a9b30c5fbbba3ffc34a1732c69365bc2a7de143f970318f8f1a2a38018dc6a',
    'address': 'friday1jg8n39n2m93aavjnxl7snnvt4q6n50g9alxgkl',
    'mnemonic': 'often day image remove film awful art satisfy stable honey provide cactus example flock vacuum adult cool install erase able pencil cancel retreat win'
    }


def test_mnemonic_to_privkey():
    assert address.mnemonic_to_privkey(test_vector["mnemonic"]) == test_vector['private_key']


def test_mnemonic_to_pubkey():
    assert address.mnemonic_to_pubkey(test_vector["mnemonic"]) == test_vector['public_key']


def test_mnemonic_to_address():
    assert address.mnemonic_to_address(test_vector["mnemonic"]) == test_vector['address']


def test_privkey_to_pubkey():
    assert address.privkey_to_pubkey(test_vector["private_key"]) == test_vector["public_key"]


def test_privkey_to_address():
    assert address.privkey_to_address(test_vector["private_key"]) == test_vector["address"]


def test_generate_wallet(mocker):
    mock_urandom = mocker.patch("os.urandom")
    mock_urandom.return_value = b"\x1e\xd2\x7f9\xa7\x0em\xfd\xa0\xb4\xaa\xc4\x0b\x83\x0e%\xbf\xe6DG\x7f:a\xe6#qa\x1ch5D\xa9"  # noqa: E501
    expected_wallet = {
        'private_key': 'bb8ac5bf9c342852fa5943d1366375c6f985d4601e596f23c5a49d095bfb2878',
        'public_key': '03a7cc51198fc666901ec7b627926dad0c85d128ebe3251a132f009dcde1d64e03',
        'address': 'friday1dep39rnnwztpt63jx0htxrkt3lgku2cd5p2l50',
        'mnemonic': 'burst negative solar evoke traffic yard lizard next series foster seminar enter wrist captain bulb trap giggle country sword season shoot boy bargain deal'
    }
    assert address.generate_wallet() == expected_wallet
