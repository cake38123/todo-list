import sys

from main import main

def test_add_then_list(monkeypatch, tmp_path, capsys):
    monkeypatch.chdir(tmp_path)

    monkeypatch.setattr(sys, "argv", ["main.py", "add", "Buy milk"])
    main()

    assert (tmp_path / "data.json").is_file()
    capsys.readouterr()

    monkeypatch.setattr(sys, "argv", ["main.py", "list"])
    main()

    output = capsys.readouterr().out

    assert "Buy milk" in output
    assert "To do" in output