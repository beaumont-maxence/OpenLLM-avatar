import pytest

from src.open_llm_vtuber.chat_history_manager import (
    _get_safe_history_path,
    _is_safe_filename,
    _sanitize_path_component,
)


def test_safe_filename_accepts_normal_names():
    assert _is_safe_filename("conf_001")
    assert _is_safe_filename("history-2025-01-01_12-00-00")
    assert _is_safe_filename("角色配置")


def test_safe_filename_rejects_bad_names():
    assert not _is_safe_filename("")
    assert not _is_safe_filename("a" * 256)
    assert not _is_safe_filename("foo/bar")
    assert not _is_safe_filename("foo\x00bar")


def test_sanitize_path_component_strips_directories():
    assert _sanitize_path_component("../../etc/passwd") == "passwd"
    assert _sanitize_path_component("dir/name") == "name"


def test_sanitize_path_component_rejects_invalid():
    with pytest.raises(ValueError):
        _sanitize_path_component("../")


def test_safe_history_path_stays_in_base_dir():
    path = _get_safe_history_path("conf", "../../../etc/passwd")
    assert path.startswith("chat_history")
    assert ".." not in path
