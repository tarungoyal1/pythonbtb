import sys

def sqrt(x):
    if x < 0:
        raise ValueError("Cannot find square root of negative number {} ".format(x))
    return x



def main():
    try:
        sqrt(-1)
    except ValueError as e:
        print(str(e))


if __name__ == '__main__':
    main()
