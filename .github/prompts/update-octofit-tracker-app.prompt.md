mode: 'agent'
model: GPT-4.1

# Django アプリの更新

- すべての Django プロジェクトファイルは `octofit-tracker/backend/octofit_tracker` ディレクトリにあります。

1. MongoDB 接続と CORS のために `settings.py` を更新します。
2. `models.py`、`serializers.py`、`urls.py`、`views.py`、`tests.py`、`admin.py`を更新し、ユーザー、チーム、アクティビティ、リーダーボード、ワークアウトのコレクションをサポートします。
3. `/`がAPIを指し、`urls.py`に`api_root`が存在することを確認します。
