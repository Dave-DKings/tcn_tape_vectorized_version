"""Utilities to persist training/evaluation artifacts to long-term storage."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
import json
from pathlib import Path
import shutil
from typing import Iterable, List, Optional


DEFAULT_ARTIFACT_REL_PATHS: List[str] = [
    "tcn_fusion_results",
    "output_log",
    "data_exports",
    "data/master_features_NORMALIZED.csv",
]


@dataclass
class ArtifactCopyItem:
    rel_path: str
    source: str
    destination: str
    kind: str


def _copy_path(src: Path, dst: Path) -> str:
    if src.is_dir():
        shutil.copytree(src, dst, dirs_exist_ok=True)
        return "dir"
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
    return "file"


def save_artifacts_to_drive(
    *,
    project_root: str | Path,
    drive_root: str | Path,
    run_name: Optional[str] = None,
    artifact_rel_paths: Optional[Iterable[str]] = None,
    include_git_head: bool = True,
) -> dict:
    """
    Copy common project artifacts into a timestamped directory under drive_root.

    Returns a manifest dict with copied items and skipped paths.
    """
    project_root_path = Path(project_root).resolve()
    drive_root_path = Path(drive_root).resolve()
    drive_root_path.mkdir(parents=True, exist_ok=True)

    if not run_name:
        run_name = datetime.utcnow().strftime("run_%Y%m%d_%H%M%S_utc")
    run_dir = drive_root_path / run_name
    run_dir.mkdir(parents=True, exist_ok=True)

    rel_paths = list(artifact_rel_paths or DEFAULT_ARTIFACT_REL_PATHS)
    copied: List[ArtifactCopyItem] = []
    skipped: List[str] = []

    for rel in rel_paths:
        src = (project_root_path / rel).resolve()
        if not src.exists():
            skipped.append(rel)
            continue
        dst = run_dir / rel
        kind = _copy_path(src, dst)
        copied.append(
            ArtifactCopyItem(
                rel_path=rel,
                source=str(src),
                destination=str(dst),
                kind=kind,
            )
        )

    git_head = None
    if include_git_head:
        head_file = project_root_path / ".git" / "HEAD"
        if head_file.exists():
            git_head = head_file.read_text(encoding="utf-8", errors="ignore").strip()

    manifest = {
        "created_utc": datetime.utcnow().isoformat() + "Z",
        "project_root": str(project_root_path),
        "drive_root": str(drive_root_path),
        "run_dir": str(run_dir),
        "run_name": run_name,
        "copied": [item.__dict__ for item in copied],
        "skipped_missing": skipped,
        "git_head": git_head,
    }
    manifest_path = run_dir / "artifact_manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    manifest["manifest_path"] = str(manifest_path)
    return manifest

