#Please install the IPy module
#python3
import os
import IPy
cmd_find="c:\windows\system32\iscsicli.exe ListTargetPortals |findstr 3260"
cmd_remove="c:\windows\system32\iscsicli.exe RemoveTargetPortal "
cmd_con="c:\windows\system32\iscsicli.exe QloginTarget "
num = 0
judge = input("Please enter a number:\r\n1.Add an ISCSI host\r\n2.Remove ISCSI connection\r\n")
def main():
    global num
    if judge == str(1):
        iplist = open("ip.txt","r")
        for ip in iplist:
            new_ip = ip
            def is_ip(new_ip):
                try:
                    IPy.IP(new_ip)
                    a = os.system("iscsicli QAddTargetPortal  {}".format(new_ip))
                except Exception as e:
                    print("Please put the IP address in ip.txt in this directory.")
            is_ip()
        iscsicli_listtarget = os.popen("c:\windows\system32\iscsicli.exe ListTargets")
        iscsicli_listtargets = iscsicli_listtarget.split()
        cmd_con_s=cmd_con+str(iscsicli_listtargets[7])
        establish_connection_cmd=os.popen(cnd_con_s) #Establish connection
        print("Established a successful connection")
    elif judge == str(2):
        iscsicli_list = os.popen(cmd_find)
        iscsicli_remove_list = iscsicli_list.read()
        iscsicli_remove_list = iscsicli_remove_list.replace("    地址和套接字   : ", "")
        f = open('scsi.txt', 'w')
        f.write(iscsicli_remove_list)
        f.close()
        for i in open("scsi.txt"):
            # print(i.strip())
            cmd_remove_cmd = cmd_remove + i.strip()
            print(cmd_remove_cmd)
            iscsicli_remove_succ = os.popen(cmd_remove_cmd)
            num = num + 1
            print("%d Target Remove Successful" % num)
    else:
        print('Please enter a correct number:')
    file_del = os.popen("del scsi.txt")


if __name__ == '__main__':
     main()