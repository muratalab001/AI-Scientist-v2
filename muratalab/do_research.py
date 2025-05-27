import subprocess
import os

# 実行するスクリプトのパス
script_path = "./do_research.sh"

# スクリプトが存在するか確認
if not os.path.exists(script_path):
    print(f"Error: {script_path} が見つかりません。")
else:
    try:
        # スクリプトを実行
        result = subprocess.run(
            ['sh', script_path],  # 'sh' を使わず直接実行する場合は [script_path] と記述
            capture_output=True,  # 標準出力と標準エラーを取得
            text=True             # 出力をテキスト形式で取得
        )

        # 実行結果を表示
        print("標準出力:", result.stdout)
        print("標準エラー:", result.stderr)
        print("終了コード:", result.returncode)

        # 終了コードが非ゼロの場合、エラーとみなす
        if result.returncode != 0:
            print(f"Error: スクリプトが非ゼロ終了コード {result.returncode} を返しました。")

    except FileNotFoundError:
        print("Error: 'sh' コマンドが見つかりません。シェルが正しくインストールされているか確認してください。")
    except Exception as e:
        print(f"予期しないエラーが発生しました: {e}")
