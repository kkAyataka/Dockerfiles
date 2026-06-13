from pathlib import Path
import sys
import tiktoken

def list_paths(dir):
    """指定のディレクトリを再起的に調べてファイルパスを列挙する"""

    paths = []
    for path in Path(dir).iterdir():
        if path.is_dir():
            paths.extend(list_paths(path))
        elif path.is_file():
            paths.append(path)
    return paths

def token_pretty_str(token_count):
    """値の大きさに合わせて読みやすい文字列にして返す。

    1,000単位の区切り文字を入れ、K（x1,000）、M（1,000,000）をつける。
    """

    if token_count < 1_000:
        return f"{token_count}"
    elif token_count < 1_000_000:
        return f"{token_count/1_000:.1f}K"
    else:
        return f"{token_count/1_000_000:.1f}M"

if __name__ == "__main__":
    """tiktokenを使ってトークン数を表示する"""

    enc = tiktoken.get_encoding("o200k_base")

    root_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    if root_path.is_dir():
        sum_token = 0
        paths = list_paths(root_path)
        for p in paths:
            try:
                tokens = enc.encode(p.read_text())
                token_count = len(tokens)
                sum_token += token_count
                print(f"{p}: {token_count:,} ({token_pretty_str(token_count)})")
            except Exception:
                print(f"{p}: error")
        print("----------")
        print(f"Sum: {sum_token:,} ({token_pretty_str(sum_token)})")
    elif root_path.is_file():
        try:
            tokens = enc.encode(root_path.read_text())
            token_count = len(tokens)
            print(f"{p}: {token_count:,} ({token_pretty_str(token_count)})")
        except Exception:
            print(f"{root_path}: error")
    else:
        tokens = enc.encode(sys.argv[1])
        print(len(tokens))
