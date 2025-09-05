from multiprocessing import Pool
import os
import asyncio as asy
import keyboard as kb
from ctypes import *
import time
system_tasks ={}
working = True
tasks = []
clear = lambda: os.system('cls')
async def stop_all_task():
    print("start_process_clear\n")
    global working
    working = False
async def out_task():
    print(f"{len(asy.all_tasks())} кол-во процссов :\n")
    for i in asy.all_tasks():
        print(f"|\t{i}\n")
async def next_stream(inf,tim):
    data = 0
    global working
    while working:
        await asy.sleep(tim)
        data += 1
        print(f"\tTask: {inf} , data:{data}")
    print(f"Task: {inf} closed")
    return 0
async def main():
    nameT = 1
    proces_counter =1
    system_tasks[f"{nameT}"] = asy.create_task(next_stream(0, 1))
    while nameT<=2:
        proces_counter+=1
        print(f"all_task:{system_tasks}")
        system_tasks[f"{nameT}"] = asy.create_task(next_stream(proces_counter,2+(proces_counter)/5))
        await asy.sleep(1)
        tasks.clear()
        nameT += 1
        clear()
    out_T = asy.create_task(out_task())
    clear_mem = asy.create_task(stop_all_task())
    await asy.sleep(3)
    clear_mem.cancel()
print(windll.kernel32)
print(os.environ.get("HOME"))
asy.run(main())
#pyinstaller --onefile test.py
