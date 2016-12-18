try:
    a=10;
    b="&"
    c=int(a)/int(b)

    print(c)
except ValueError as e:
    print(e)
except ZeroDivisionError as zero:
    print(zero)
