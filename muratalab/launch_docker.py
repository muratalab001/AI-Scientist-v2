#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
run_test.py

以下のコマンドと同等の操作を Docker SDK for Python で実行します：
  docker run --rm -it -p 8888:8888 --gpus all \
    -v /home/test/Documents/MasakiMurata/AI-Scientist-v2:/tf \
    ai-scientist-v2 \
    python test.py
"""
import docker
from docker.types import DeviceRequest

def main():
    # Docker デーモンに接続
    client = docker.from_env()

    # 使用するイメージ名
    image_name = "ai-scientist-v2"

    # ポートマッピング: ホスト8888 → コンテナ8888
    ports = {"8888/tcp": 8888}

    # ボリュームマウント: ホストディレクトリ → /tf
    volumes = {
        "/home/test/Documents/GitHub/AI-Scientist-v2": {
            "bind": "/tf",
            "mode": "rw"
        }
    }

    # --gpus all 相当
    device_requests = [
        DeviceRequest(count=-1, capabilities=[["gpu"]])
    ]

    try:
        # コンテナを起動して test.py を実行、終了したら自動破棄 (--rm)
        # detach=False にするとコマンド完了まで待機し標準出力を返却
        output = client.containers.run(
            image=image_name,
            command=["python3", "./muratalab/test.py"],
            #command = ["python3", "--version"],
            remove=True,               # --rm
            ports=ports,
            volumes=volumes,
            device_requests=device_requests,
            working_dir="/tf",         # カレントディレクトリを /tf に
            stdin_open=True,           # -i
            tty=True,                  # -t
            stdout=True,
            stderr=True,
            detach=False
        )

        # バイト列で返ってくるのでデコード
        print(output.decode("utf-8").rstrip())
    except docker.errors.ImageNotFound:
        print(f"イメージ '{image_name}' が見つかりません。")
    except docker.errors.APIError as e:
        print(f"Docker API エラー: {e.explanation}")
    except Exception as e:
        print(f"予期しないエラーが発生しました: {e}")

if __name__ == "__main__":
    main()
