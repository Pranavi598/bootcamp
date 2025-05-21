import os
import shutil
import pytest
from app.monitor import recover_underprocess

@pytest.fixture
def setup_folders(tmp_path, monkeypatch):
    # Create temp dirs to mock underprocess/ and unprocessed/
    under = tmp_path / "underprocess"
    unproc = tmp_path / "unprocessed"
    under.mkdir()
    unproc.mkdir()

    # Create dummy file in underprocess/
    test_file = under / "logfile1.txt"
    test_file.write_text("dummy data")

    # Monkeypatch the monitor module's folder paths
    monkeypatch.setattr("app.monitor.UNDERPROCESS", str(under))
    monkeypatch.setattr("app.monitor.UNPROCESSED", str(unproc))

    return str(test_file), str(unproc)

def test_recover_underprocess_moves_files(setup_folders):
    test_file, unprocessed_dir = setup_folders

    # Run the recovery logic
    recover_underprocess()

    recovered_path = os.path.join(unprocessed_dir, "logfile1.txt")
    assert os.path.exists(recovered_path), "File should be moved to unprocessed"
    assert not os.path.exists(test_file), "Original file should no longer exist in underprocess"
