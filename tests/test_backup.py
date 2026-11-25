"""Reproduction test suite for storage backup."""
import pytest
from storage_service.backup import run_backup

def test_safe_backup():
    assert run_backup("data/file.txt", "backups") is True

def test_unsafe_backup_rejection():
    with pytest.raises(PermissionError):
        run_backup(".env", "backups")
