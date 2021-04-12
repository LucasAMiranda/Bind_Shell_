# python shell server

import sys
import socket
import os

host = "127.0.0.1"
size = 512

try:
    port = sys.argv[1]
except:
    port = 4444

try:
    sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

except(socket.error, e):
    print("Error in creating socket: ", e)
    sys.exit(1)

sockfd.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:
    sockfd.bind((host, port))

except(socket.error, e):
    print("Erro in Binding: ", e)
    sys.exit(1)

print("\n\n======================================================")
print("-------- Server Listening on Port %d --------------" % port)
print("======================================================\n\n")



try:
    while 1:
        try:
            cmd = clientsock.recv(SIZE)
        except:
            break
            pipe = os.popen(cmd)
            rawOutput = pipe.readlines()

            print(cmd)

            if cmd == 'g2g': # close the connection and move on for others
                print("\n-----------Connection Closed----------------");
                clientesock.shutdown()
                break
            try:
                output = ""

                # Parse the output from list to string
                for data in rawOutput:
                    output += data

                clientesock.send("Comando output :- \n ", output, "\r\n")

            except(socket.error, e):
                print("\n-----------Connection Closed--------")
                clientesock.close()
                break
except keyboardInterrupt:

    print("\n\n>>>> See You. File provided by LSHACKER <<<<<\n")


