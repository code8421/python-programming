import os


def main():
    n = 0
    path = "C:/Users/znu31/OneDrive/사진/Backgrounds/"
    for filename in os.listdir(path):
        n += 1
        try:
            rename = f'{path}image_{n}.jpg'
            source = path + filename
            os.rename(source, rename)
        except:
            continue


if __name__ == '__main__':
    main()
