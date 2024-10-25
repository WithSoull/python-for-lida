def main(*args, **kwargs):
    print(args)
    print(kwargs)
    print("-------------------")

main(1, 2, 3)
main(1, 2)
main(1, 2, 3, 4)

main(a=1, b=2, c="hi")
main(1, 2, 3, a="hello", b="world")
