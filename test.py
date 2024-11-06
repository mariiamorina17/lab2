import pytest
from pop3main import read_pop3_emails

def test_read_pop3_emails():
    assert read_pop3_emails('pop.mail.ru', 'mariiamorina@yandex.ru', 'usoxwngsgsxurgsc') == None

def test_read_pop3_emails_mailru():
    with pytest.raises(TypeError):
        assert read_pop3_emails(1, 2, 3) == None