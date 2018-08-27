# -*- coding: utf-8 -*-
import subprocess


def python_call_powershell():
    try:
        args = [r"powershell", r"D:\mywork\airtest_prj\mytest1.air\test.ps1"]  # args参数里的ip是对应调用powershell里的动态参数args[0],类似python中的sys.argv[1]
        # 如果报错，说禁止执行脚本，是因为没有权限，所以，把上面的一行代码换成
        # args = [r"C:\WINDOWS\system32\WindowsPowerShell\v1.0\powershell.exe",
        #           "-ExecutionPolicy", "Unrestricted", r"D:\jzhou\test_ping.ps1", ip]
        p = subprocess.Popen(args, stdout=subprocess.PIPE)
        dt = p.stdout.read()
        return dt
    except Exception as e:
        print(e)
    return False


if __name__ == "__main__":
    print(python_call_powershell())


