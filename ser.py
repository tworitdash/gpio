import serial
import asyncio

ser = serial.Serial("/dev/ttyAMA0", 9600, timeout=1)

async def writen():
    while True:
        w = input("Enter Your Input")
        data = await read()
        print(data)
        ser.write(str.encode('<'))
        ser.write(str.encode(w))

async def read():
    data = ser.readline().decode()
    print(data)
    return data

asyncio.get_event_loop().run_until_complete(writen())
asyncio.get_event_loop().run_forever()
