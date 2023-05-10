from core.generator import CommitMessageGenerator

if __name__ == "__main__":
    diff = open("models/example.diff").read()
    generator = CommitMessageGenerator()
    print(generator(diff))