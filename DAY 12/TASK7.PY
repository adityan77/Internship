lock=False
try:
    lock=True
    print("Lock Acquired")

    result=1/0
finally:
    lock =False
    print("Lock Released")
