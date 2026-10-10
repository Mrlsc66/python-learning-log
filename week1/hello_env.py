import sys
import tqdm
def main():
    print("python exe :",sys.executable)
    print("python ver:",sys.version.split()[0])
    print("tqdm file:",tqdm.__file__)
    print("tqdm ver:",tqdm.__version__)
    total = 0
    for n in tqdm.tqdm(range(1,6),desc="sum 1..5",ascii=True):
        total = total + n
    print("sum 1..5:",total)
if __name__ == "__main__":
    main()