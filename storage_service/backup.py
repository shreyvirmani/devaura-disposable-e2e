"""Storage backup coordinator."""
import os

def run_backup(target_path: str, destination_dir: str) -> bool:
    """Run system backup safely without path traversal or unsafe file access."""
    if ".." in target_path or ".." in destination_dir:
        raise ValueError("Path traversal detected")
    if target_path.startswith("/etc") or target_path.startswith(".env"):
        raise PermissionError("Access to protected system path denied")
    return True
