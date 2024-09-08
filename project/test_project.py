import pytest
from unittest.mock import patch
from cryptography.fernet import Fernet
from project.project import encrypt_key, decrypt_key, ask_for_mk, mkf_exister
from unittest.mock import mock_open, patch


def test_encrypt_decrypt_key():
    encryption_key = Fernet.generate_key()
    original_key = "my_secret_key"
    encrypted_key = encrypt_key(original_key, encryption_key)
    decrypted_key = decrypt_key(encrypted_key, encryption_key)
    assert original_key == decrypted_key


def test_ask_for_mk_prompt():
    with patch('getpass.getpass') as mock_getpass:
        ask_for_mk()
        mock_getpass.assert_called_once_with("\nEnter master key: \n")


def test_mkf_exister():
    with patch('os.path.exists', return_value=True):
        assert mkf_exister() == True
    with patch('os.path.exists', return_value=False):
        assert mkf_exister() == False
