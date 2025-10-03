from main import main   


def test_main(capsys):
    assert main() is None