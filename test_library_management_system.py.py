import pytest
from datetime import datetime, timedelta
from main import LibraryManagementSystem, Book

@pytest.fixture
def library_system():
    system = LibraryManagementSystem()
    system.initialize_catalog()
    return system

def test_display_catalog(capsys, library_system):
    library_system.display_catalog()
    captured = capsys.readouterr()
    assert "Available Books Catalog" in captured.out

def test_checkout_books(capsys, monkeypatch, library_system):
    monkeypatch.setattr('builtins.input', lambda _: '001,002\n3\nY\n')
    library_system.checkout_books()
    captured = capsys.readouterr()
    assert "Checkout Summary" in captured.out

def test_return_books(capsys, monkeypatch, library_system):
    # Assuming some books are checked out before returning
    library_system.checked_out_books = {'001': 2, '002': 1}
    
    monkeypatch.setattr('builtins.input', lambda _: '001,002\n')
    library_system.return_books()
    captured = capsys.readouterr()
    assert "Return Summary" in captured.out

def test_display_checked_out_books(capsys, library_system):
    library_system.checked_out_books = {'001': 2, '002': 1}
    library_system.display_checked_out_books()
    captured = capsys.readouterr()
    assert "Books Checked Out" in captured.out

def test_calculate_late_fee(library_system):
    due_date = datetime.now() + timedelta(days=7)
    late_fee = library_system.calculate_late_fee(due_date)
    assert late_fee == 0.0

    due_date = datetime.now() - timedelta(days=7)
    late_fee = library_system.calculate_late_fee(due_date)
    assert late_fee == 7.0 * library_system.LATE_FEE_PER_DAY

def test_read_positive_integer(monkeypatch, library_system):
    monkeypatch.setattr('builtins.input', lambda _: '5\n')
    result = library_system.read_positive_integer()
    assert result == 5

    monkeypatch.setattr('builtins.input', lambda _: 'abc\n1\n')
    result = library_system.read_positive_integer()
    assert result == 1
