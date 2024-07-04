from io import TextIOWrapper
from pathlib import Path
from random import randint
from subprocess import run
from tempfile import TemporaryFile
from typing import IO, List
import os


# 다음 횟수만큼 임의의 테스트케이스를 생성하고, 출력결과를 비교한다.
N_TRIES = 1000


def files_to_compare(repository_dir: Path) -> List[Path]:
    # 다음 파일들의 출력을 비교한다.
    return [
        repository_dir / '2주차 Knapsack' / '김동주' / 'boj_1535.py',
        repository_dir / '2주차 Knapsack' / '서동혁' / 'boj_1535.py',
    ]


def generate_random_testcase(stdin: TextIOWrapper):
    # 임의의 테스트케이스를 stdin에 작성한다.
    N = randint(1, 20)
    L = [randint(0, 100) for i in range(N)]
    J = [randint(0, 100) for i in range(N)]

    stdin.write(f"{N}\n")
    stdin.write(f"{' '.join(map(str, L))}\n")
    stdin.write(f"{' '.join(map(str, J))}")


###############################################################
# 아래는 수정하지 마시오
###############################################################


def is_windows():
    return os.name == 'nt'


PYTHON = 'python3.exe' if is_windows() else 'python3'

REPOSITORY_DIR = Path(__file__).parent


def main():
    files = files_to_compare(REPOSITORY_DIR)
    stdin = TextIOWrapper(TemporaryFile()) # 가상 stdin

    for i in range(N_TRIES):
        stdin.truncate(0)
        stdin.seek(0)

        generate_random_testcase(stdin)

        if compare_outputs(stdin, *files) == False:
            break


def compare_outputs(stdin: IO[str], *python_file: Path) -> bool:
    n_files = len(python_file)

    stdouts = [TemporaryFile() for i in range(n_files)]
    outputs = [''] * n_files

    stdin.seek(0)
    input = stdin.read().strip()

    for i in range(n_files):
        stdin.seek(0)

        run(args=[PYTHON, python_file[i]], stdin=stdin, stdout=stdouts[i])

        stdouts[i].seek(0)
        outputs[i] = stdouts[i].read()

    for j in range(1, n_files):
        i = j-1
        if outputs[i].strip() != outputs[j].strip():
            print('\n'.join([
                f"================================================================",
                f"아래의 입력에 대한 출력결과가 다릅니다.",
                f"================================================================",
                f"입력:",
                f"----------------------------------------------------------------",
                f"{input}",
                f"================================================================",
                f"{python_file[i].relative_to(REPOSITORY_DIR)}의 출력:",
                f"----------------------------------------------------------------",
                f"{str(outputs[i], encoding='utf8')}",
                f"================================================================",
                f"{python_file[j].relative_to(REPOSITORY_DIR)}의 출력:",
                f"----------------------------------------------------------------",
                f"{str(outputs[j], encoding='utf8')}",
                f"================================================================",
            ]))
            return False
    return True


if __name__ == "__main__":
    main()
