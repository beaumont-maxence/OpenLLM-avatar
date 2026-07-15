# upgrade/constants.py
# CURRENT_SCRIPT_VERSION = "0.2.0"
from ruamel.yaml import YAML
from src.open_llm_vtuber.config_manager.utils import load_text_file_with_guess_encoding
import os

USER_CONF = "conf.yaml"
BACKUP_CONF = "conf.yaml.backup"

JA_DEFAULT_CONF = "config_templates/conf.JP.default.yaml"
EN_DEFAULT_CONF = "config_templates/conf.default.yaml"

yaml = YAML()
# user_config = yaml.load(load_text_file_with_guess_encoding(USER_CONF))
# CURRENT_SCRIPT_VERSION = user_config.get("system_config", {}).get("conf_version")


def load_user_config():
    if not os.path.exists(USER_CONF):
        return None
    text = load_text_file_with_guess_encoding(USER_CONF)
    if text is None:
        return None
    return yaml.load(text)


def get_current_script_version():
    config = load_user_config()
    if config:
        return config.get("system_config", {}).get("conf_version", "UNKNOWN")
    return "UNKNOWN"


CURRENT_SCRIPT_VERSION = get_current_script_version()

TEXTS = {
    "ja": {
        # "welcome_message": f"Auto-Upgrade Script {CURRENT_SCRIPT_VERSION}\nOpen-LLM-VTuber アップグレードスクリプト - このスクリプトは実験的な段階であり、期待通りに動作しない場合があります。",
        "welcome_message": f"{CURRENT_SCRIPT_VERSION} から自動アップグレードを開始しています...",
        # "lang_select": "言語を選択してください/Please select language (ja/en):",
        # "invalid_lang": "言語の選択が無効なため、デフォルトの英語を使用します",
        "not_git_repo": "エラー: 現在のディレクトリは git リポジトリではありません。Open-LLM-VTuber ディレクトリ内でこのスクリプトを実行してください。\nまた、ダウンロードした Open-LLM-VTuber に .git フォルダが含まれていない可能性もあります（git clone ではなく zip アーカイブをダウンロードした場合に発生します）。その場合、このスクリプトではアップグレードできません。",
        "backup_user_config": "{user_conf} を {backup_conf} にバックアップしています",
        "configs_up_to_date": "[DEBUG] ユーザー設定は最新です。",
        "no_config": "警告: conf.yaml が見つかりません",
        "copy_default_config": "テンプレートからデフォルト設定をコピーしています",
        "uncommitted": "コミットされていない変更が見つかりました。stash しています...",
        "stash_error": "エラー: 変更を stash できませんでした",
        "changes_stashed": "変更を stash しました",
        "pulling": "リモートリポジトリから更新を pull しています...",
        "pull_error": "エラー: 更新を pull できませんでした",
        "restoring": "stash した変更を復元しています...",
        "conflict_warning": "警告: stash した変更の復元中に競合が発生しました",
        "manual_resolve": "競合を手動で解決してください",
        "stash_list": "'git stash list' で stash した変更を確認できます",
        "stash_pop": "'git stash pop' で変更を復元してください",
        "upgrade_complete": "アップグレードが完了しました！",
        "check_config": "1. conf.yaml の更新が必要かどうか確認してください",
        "resolve_conflicts": "2. 設定ファイルに競合がある場合は手動で解決してください",
        "check_backup": "3. 重要な設定が失われていないか、バックアップ設定を確認してください",
        "git_not_found": "エラー: Git が見つかりません。先に Git をインストールしてください:\nWindows: https://git-scm.com/download/win\nmacOS: brew install git\nLinux: sudo apt install git",
        "operation_preview": """
このスクリプトは以下の操作を実行します：
1. 現在の conf.yaml 設定ファイルをバックアップ
2. コミットされていない変更をすべて stash (git stash)
3. リモートリポジトリから最新のコードを pull (git pull)
4. 以前 stash した変更の復元を試行 (git stash pop)

続行しますか？(y/N): """,
        "merged_config_success": "新しい設定項目をマージしました:",
        "merged_config_none": "新しい設定項目は見つかりませんでした。",
        "merge_failed": "設定のマージに失敗しました: {error}",
        "updating_submodules": "サブモジュールを更新しています...",
        "submodules_updated": "サブモジュールの更新が完了しました",
        "submodule_error": "サブモジュールの更新中にエラーが発生しました",
        "no_submodules": "サブモジュールが検出されなかったため、更新をスキップします",
        "env_info": "システム環境: {os_name} {os_version}, Python {python_version}",
        "git_version": "Git バージョン: {git_version}",
        "current_branch": "現在のブランチ: {branch}",
        "operation_time": "操作 '{operation}' が完了しました。所要時間: {time:.2f} 秒",
        "checking_stash": "コミットされていない変更を確認しています...",
        "detected_changes": "{count} 個のファイルに変更を検出しました",
        "submodule_updating": "サブモジュールを更新しています: {submodule}",
        "submodule_updated": "サブモジュールを更新しました: {submodule}",
        "submodule_update_error": "❌ サブモジュールの更新に失敗しました。",
        "checking_remote": "リモートリポジトリの状態を確認しています...",
        "remote_ahead": "ローカルバージョンは最新です",
        "remote_behind": "pull 可能な新しいコミットが {count} 件見つかりました",
        "config_backup_path": "設定バックアップのパス: {path}",
        "start_upgrade": "アップグレード処理を開始しています...",
        "version_upgrade_success": "設定バージョンをアップグレードしました: {old} → {new}",
        "version_upgrade_none": "アップグレードは不要です。現在のバージョンは {version} です",
        "version_upgrade_failed": "設定バージョンのアップグレードに失敗しました: {error}",
        "finish_upgrade": "アップグレード処理が完了しました。合計所要時間: {time:.2f} 秒",
        "backup_used_version": "✅ バックアップから設定バージョンを読み込みました: {backup_version}",
        "backup_read_error": "⚠️ バックアップファイルの読み込みに失敗しました。デフォルトバージョン {version} を使用します。エラー: {error}",
        "version_too_old": "🔁 サポートされる最小バージョンより低い旧バージョン {found} を検出したため、強制的に {adjusted} を使用します",
        "checking_ahead_status": "🔍 未 push のローカルコミットを確認しています...",
        "local_ahead": "🚨 'main' ブランチにリモートへ push されていないローカルコミットが {count} 件あります。",
        "push_blocked": (
            "⛔ 'main' ブランチへの push 権限がありません。\n"
            "これらのコミットはローカルにのみ存在し、GitHub には同期されません。\n"
            "このままアップグレードを続行すると、これらのコミットが失われたり、リモートの変更と競合したりする可能性があります。"
        ),
        "backup_suggestion": (
            "🛟 作業内容を安全に保つために、以下のいずれかの方法を選択できます：\n"
            "🔄 1. 直近のコミットを取り消す：\n"
            "   • GitHub Desktop: 右下の「Undo」ボタンをクリック\n"
            "   • ターミナル: git reset --soft HEAD~1 を実行\n"
            "📦 2. コミットを patch ファイルとしてエクスポート：\n"
            "   → ターミナルで実行: git format-patch origin/main --stdout > backup.patch\n"
            "🌿 3. バックアップ用のブランチを作成：\n"
            "   → ターミナルで実行: git checkout -b my-backup-before-upgrade\n"
            "💡 ヒント: コミットを取り消した後、新しいブランチに切り替えたり、必要に応じて変更をエクスポートしたりできます。"
        ),
        "abort_upgrade": "🛑 ローカルコミットを保護するため、アップグレードを中止しました。",
        "no_config_fatal": (
            "❌ 設定ファイル conf.yaml が見つかりません。\n"
            "以下のいずれかを行ってください：\n"
            "👉 古い設定ファイルを現在のディレクトリにコピーする\n"
            "👉 または run_server.py を実行してデフォルトのテンプレートを生成する"
        ),
    },
    "en": {
        # "welcome_message": f"Auto-Upgrade Script {CURRENT_SCRIPT_VERSION}\nOpen-LLM-VTuber upgrade script - This script is highly experimental and may not work as expected.",
        "welcome_message": f"Starting auto upgrade from {CURRENT_SCRIPT_VERSION}...",
        # "lang_select": "Please select language (ja/en):",
        # "invalid_lang": "Invalid language selection, using English as default",
        "not_git_repo": "Error: Current directory is not a git repository. Please run this script inside the Open-LLM-VTuber directory.\nAlternatively, it is likely that the Open-LLM-VTuber you downloaded does not contain the .git folder (this can happen if you downloaded a zip archive instead of using git clone), in which case you cannot upgrade using this script.",
        "backup_user_config": "Backing up {user_conf} to {backup_conf}",
        "configs_up_to_date": "[DEBUG] User configuration is up-to-date.",
        "no_config": "Warning: conf.yaml not found",
        "copy_default_config": "Copying default configuration from template",
        "uncommitted": "Found uncommitted changes, stashing...",
        "stash_error": "Error: Unable to stash changes",
        "changes_stashed": "Changes stashed",
        "pulling": "Pulling updates from remote repository...",
        "pull_error": "Error: Unable to pull updates",
        "restoring": "Restoring stashed changes...",
        "conflict_warning": "Warning: Conflicts occurred while restoring stashed changes",
        "manual_resolve": "Please resolve conflicts manually",
        "stash_list": "Use 'git stash list' to view stashed changes",
        "stash_pop": "Use 'git stash pop' to restore changes",
        "upgrade_complete": "Upgrade complete!",
        "check_config": "1. Please check if conf.yaml needs updating",
        "resolve_conflicts": "2. Resolve any config file conflicts manually",
        "check_backup": "3. Check backup config to ensure no important settings are lost",
        "git_not_found": "Error: Git not found. Please install Git first:\nWindows: https://git-scm.com/download/win\nmacOS: brew install git\nLinux: sudo apt install git",
        "operation_preview": """
This script will perform the following operations:
1. Backup current conf.yaml configuration file
2. Stash all uncommitted changes (git stash)
3. Pull latest code from remote repository (git pull)
4. Attempt to restore previously stashed changes (git stash pop)

Continue? (y/N): """,
        "merged_config_success": "Merged new configuration items:",
        "merged_config_none": "No new configuration items found.",
        "merge_failed": "Configuration merge failed: {error}",
        "updating_submodules": "Updating submodules...",
        "submodules_updated": "Submodules updated successfully",
        "submodule_error": "Error updating submodules",
        "no_submodules": "No submodules detected, skipping update",
        "env_info": "Environment: {os_name} {os_version}, Python {python_version}",
        "git_version": "Git version: {git_version}",
        "current_branch": "Current branch: {branch}",
        "operation_time": "Operation '{operation}' completed in {time:.2f} seconds",
        "checking_stash": "Checking for uncommitted changes...",
        "detected_changes": "Detected changes in {count} files",
        "submodule_updating": "Updating submodule: {submodule}",
        "submodule_updated": "Submodule updated: {submodule}",
        "submodule_update_error": "❌ Submodule update failed.",
        "checking_remote": "Checking remote repository status...",
        "remote_ahead": "Local version is up to date",
        "remote_behind": "Found {count} new commits to pull",
        "config_backup_path": "Config backup path: {path}",
        "start_upgrade": "Starting upgrade process...",
        "version_upgrade_success": "Config version upgraded: {old} → {new}",
        "version_upgrade_none": "No upgrade needed. Current version is {version}",
        "version_upgrade_failed": "Failed to upgrade config version: {error}",
        "finish_upgrade": "Upgrade process completed, total time: {time:.2f} seconds",
        "backup_used_version": "✅ Loaded config version from backup: {backup_version}",
        "backup_read_error": "⚠️ Failed to read backup file. Falling back to default version {version}. Error: {error}",
        "version_too_old": "🔁 Detected old version {found} which is lower than the minimum supported version, forced to use {adjusted}",
        "checking_ahead_status": "🔍 Checking for unpushed local commits...",
        "local_ahead": "🚨 You have {count} local commit(s) on 'main' that are NOT pushed to remote.",
        "push_blocked": (
            "⛔ You do NOT have permission to push to the 'main' branch.\n"
            "Your commits are local only and will NOT be synced to GitHub.\n"
            "Continuing the upgrade may cause those commits to be lost or conflict with remote changes."
        ),
        "backup_suggestion": (
            "🛟 To keep your work safe, you can choose one of the following options:\n"
            "🔄 1. Undo the last commit:\n"
            "   • GitHub Desktop: Click the 'Undo' button at the bottom right.\n"
            "   • Terminal: Run: git reset --soft HEAD~1\n"
            "📦 2. Export your commit(s) as a patch file:\n"
            "   → Run: git format-patch origin/main --stdout > backup.patch\n"
            "🌿 3. Create a backup branch:\n"
            "   → Run: git checkout -b my-backup-before-upgrade\n"
            "💡 Recommendation: After undoing the commit, you can switch to a new branch or export changes as needed."
        ),
        "abort_upgrade": "🛑 Upgrade aborted to protect your local commits.",
        "no_config_fatal": (
            "❌ Config file conf.yaml not found.\n"
            "Please either:\n"
            "👉 Copy your old config file to the current directory\n"
            "👉 Or run run_server.py to generate a default template"
        ),
    },
}

# Multilingual texts for merge_configs log messages
TEXTS_MERGE = {
    "ja": {
        "new_config_item": "[INFO] 新しい設定項目: {key}",
    },
    "en": {
        "new_config_item": "[INFO] New config item: {key}",
    },
}

# Multilingual texts for compare_configs log messages
TEXTS_COMPARE = {
    "ja": {
        "missing_keys": "ユーザー設定に以下のキーがありません。設定が古い可能性があります: {keys}",
        "extra_keys": "ユーザー設定にデフォルト設定に存在しない以下のキーが含まれています: {keys}",
        "up_to_date": "ユーザー設定はデフォルト設定と一致しています。",
        "compare_passed": "{name} の比較に合格しました。",
        "compare_failed": "{name} の比較に失敗しました: 設定が一致しません。",
        "compare_diff_item": "- {item}",
        "compare_error": "{name} の比較中にエラーが発生しました: {error}",
        "comments_up_to_date": "コメントは最新のため、コメントの同期をスキップします。",
        "extra_keys_deleted_count": "{count} 個の余分なキーを削除しました:",
        "extra_keys_deleted_item": "  - {key}",
        "comment_sync_success": "すべてのコメントの同期が完了しました。",
        "comment_sync_error": "コメントの同期に失敗しました: {error}",
    },
    "en": {
        "missing_keys": "User config is missing the following keys, which may be out-of-date: {keys}",
        "extra_keys": "User config contains the following keys not present in default config: {keys}",
        "up_to_date": "User config is up-to-date with default config.",
        "compare_passed": "{name} comparison passed.",
        "compare_failed": "{name} comparison failed: configs differ.",
        "compare_diff_item": "- {item}",
        "compare_error": "{name} comparison error: {error}",
        "comments_up_to_date": "Comments are up to date, skipping comment sync.",
        "extra_keys_deleted_count": "Deleted {count} extra keys:",
        "extra_keys_deleted_item": "  - {key}",
        "comment_sync_success": "All comments synchronized successfully.",
        "comment_sync_error": "Failed to synchronize comments: {error}",
    },
}

UPGRADE_TEXTS = {
    "ja": {
        "model_dict_not_found": "⚠️ model_dict.json が見つかりません。アップグレードをスキップします。",
        "model_dict_read_error": "❌ model_dict.json の読み込みに失敗しました: {error}",
        "upgrade_success": "✅ model_dict.json を v1.2.1 形式にアップグレードしました（{language} 言語）",
        "already_latest": "model_dict.json はすでに最新の形式です。",
        "upgrade_error": "❌ model_dict.json のアップグレードに失敗しました: {error}",
        "no_upgrade_routine": "バージョン {version} 用のアップグレード処理はありません",
        "upgrading_path": "⬆️ 設定をアップグレードしています: {from_version} → {to_version}",
    },
    "en": {
        "model_dict_not_found": "⚠️ model_dict.json not found. Skipping upgrade.",
        "model_dict_read_error": "❌ Failed to read model_dict.json: {error}",
        "upgrade_success": "✅ model_dict.json upgraded to v1.2.1 format ({language} language)",
        "already_latest": "model_dict.json already in latest format.",
        "upgrade_error": "❌ Failed to upgrade model_dict.json: {error}",
        "no_upgrade_routine": "No upgrade routine for version {version}",
        "upgrading_path": "⬆️ Upgrading config: {from_version} → {to_version}",
    },
}
