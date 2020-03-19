import hashlib      #for calculating hashes
import math         #for mathematical functions such as power
import socket       #for communication at application layer
import _thread      #for handling multiple parallel tasks
import sys          #for handling cl arguments
import time         #for delays
import json         #for handling json files transferred over system
import subprocess   #for using cl commands with ease

#creating a node for the DC++ system

fnTabUpdate = False
leaving = False
m = 16
class node:
    """Class for completing the expected duties of a node"""
    myHash = ""
    m = 16
    fingerTable = {}
    IP = ""
    succ = []
    pred = []
    port = 0
    files = []
    def __init__(self, IP, port):
        self.updated = False
        self.IP = IP
        self.port = port
        strPort = str(self.port)
        self.myHash = int(hashlib.sha1((self.IP+strPort).encode()).hexdigest(), 16)%self.m
        for i in range(4):
            self.fingerTable[(self.myHash + (2**i))%self.m] = [self.IP, self.port,self.myHash] #int(string, base) converts the string to integer value
                                                                                #considering that the string is encoded as "base" value
        process = subprocess.Popen(['mkdir', str(self.myHash)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = process.communicate()

        process = subprocess.Popen('ls', stdout=subprocess.PIPE, stderr=subprocess.PIPE,cwd='./'+str(self.myHash))
        out,err = process.communicate()

        lsFiles = out.split()

        print(self.files)

        
    def leftFromTable(self, succesor, leaving):
        for i in self.fingerTable.keys():
            if i==leaving[0]:
                self.fingerTable[i] = succesor[0]
    

    def hash(self,ID):
        return int(hashlib.sha1((ID).encode()).hexdigest(), 16)%self.m
    
    
    def successor(self, hash):
        if (self.succ.__len__() == 0 and self.pred.__len__() == 0) or (self.myHash == (hash+1)%self.m) or (self.myHash == hash) :
            return [self.myHash, self.port, self.IP]
        if hash>self.myHash and hash<=self.succ[0]:
            return self.succ
        if hash>self.pred[0] and hash<=self.myHash:
            return [self.myHash, self.port, self.IP]


        sock = socket.socket()
        arr=[]
        for i in self.fingerTable.keys():
            arr.append(i)
        key = arr[arr.__len__()-1]
        marker = False
        

        for i in range(1, arr.__len__()):
            if(arr[i]<arr[i-1] and hash==(self.m-1)):
                key=arr[i]
                return [self.fingerTable[key][2],self.fingerTable[key][1],self.fingerTable[key][0]]
            if ((hash+1)%self.m == arr[i]):
                key=arr[i]
                return [self.fingerTable[key][2],self.fingerTable[key][1],self.fingerTable[key][0]]
            if arr[i] == hash:
                key = arr[i]
                return [self.fingerTable[key][2],self.fingerTable[key][1],self.fingerTable[key][0]]
            
            if(arr[i]>hash and hash>arr[i-1]):
                if(self.fingerTable[arr[i]][2]==self.fingerTable[arr[i-1]][2]):
                    key = arr[i]
                    return [self.fingerTable[key][2],self.fingerTable[key][1],self.fingerTable[key][0]]
                key = arr[i-1]
                marker = True
                break
            

        if not marker: 
            if hash<arr[arr.__len__()-1]:
                key = arr[arr.__len__()-1] 
            if arr[arr.__len__()-1] < hash and self.myHash == self.fingerTable[arr[arr.__len__()-1]][2]:
                key = arr[i]
                return [self.fingerTable[key][2],self.fingerTable[key][1],self.fingerTable[key][0]]       

        if(hash < arr[0]):
            key = arr[0]
        
        sock.connect((self.fingerTable[key][0],self.fingerTable[key][1]))
        req = {
            'type' : 'reqForSucc',
            'id' : hash
        }
        sock.send(json.dumps(req).encode())
        _response = sock.recv(1024)
        response = json.loads(_response)
        sock.close()
        return response['succ']
    
    def updateTable(self, hash, Ip, Port):
        for i in self.fingerTable.keys():
            if hash>=i and hash<self.fingerTable[i][2] and self.fingerTable[i][2]>i:
                self.fingerTable[i] = [Ip, Port, hash]
            if hash>=i and self.fingerTable[i][2]<i:
                self.fingerTable[i] = [Ip, Port, hash]
            if hash<self.fingerTable[i][2] and self.fingerTable[i][2]<i:
                self.fingerTable[i] = [Ip, Port, hash]
        
        print(self.fingerTable)

    def updateTableLeft(self, prev, new):
        for i in self.fingerTable.keys():
            if self.fingerTable[i][2] == prev[0]:
                self.fingerTable[i] = [new[2],new[1],new[0]]
        print(self.fingerTable)

    def fingerTableInit(self, hash):
        print(self.fingerTable)


def connectionHandle(conn,current):
    global leaving
    _req = conn.recv(1024)
    try:
        request = json.loads(_req)
    except: 
        print(_req)
        return
    if request['type']!='ping':
        pass
    if request['type'] == 'ping':
        response = {
            'type' : 'pingResponse',
            'pred' : current.pred,
            'listOfFiles' : current.files
        }
        conn.send(json.dumps(response).encode())
        conn.close()
        return
    if request['type'] == 'reqForSucc':
        ID = request['id']
        response = {
            'type' : 'succ',
            'succ' : current.successor(ID)
        }
        conn.send(json.dumps(response).encode())
        conn.close()
        return

    if request['type'] == 'reqForFiles':
        arr = []
        for i in current.files:
            if i[0] <= request['me'][0]:
                arr.append((i[0],i[1]))
                current.files.remove(i)
        response = {
            'type' : 'resReqFiles',
            'arr' : arr
        }
        conn.send(json.dumps(response).encode())
        conn.close()    
        return


    if request['type'] == 'giveFile':
        print(current.files)
        print(' ==== giving File ===== ')
        if request['action'] == 'put':
            file = open('./'+request['fileName'], 'rb')
        else:
            file = open('./'+str(current.myHash)+'/'+request['fileName'], 'rb')
        
        section = file.read(1024)
        while(section):
            conn.send(section)
            section = file.read(1024)
        
        file.close()
        conn.close()
        if leaving:
            for i in current.files:
                if i[1] == request['fileName']:
                    current.files.remove(i)
        print(' ==== file Given ==== ')
        return
        
    
    if request['type'] == 'reqForPred':
        if(current.pred.__len__()==0):
            current.pred = request['me']
            predecessor = [current.myHash, current.port, current.IP]
        else:
            predecessor = current.pred
        current.pred=request['me']
        conn.send(json.dumps(predecessor).encode())
        conn.close()
        return
    
    if request['type'] == 'changeSucc':
        temp = current.succ
        current.succ = request['me']
        for i in current.files:
            clientCon = socket.socket()
            clientCon.connect((current.succ[2],current.succ[1]))
            request = {
                'type'  : 'HaveToTakeFile',
                'me'    :  [current.myHash, current.port, current.IP],
                'fileName'  :  i[1],
                'action' : 'notPut'
            }
            clientCon.send(json.dumps(request).encode())
            res = clientCon.recv(1024)
            clientCon.close()  
        response = {
            'status' : 'done'
        }
        conn.send(json.dumps(response).encode())
        conn.close()
        return

    if request['type'] == 'updateTable':
        if (request['newNode'][0] == current.myHash):
            conn.close()
            print('--------------- fingerTables Updated ---------')
            divideFiles(current)
            return
        nodeSock = socket.socket()
        nodeSock.connect((request['newNode'][2], request['newNode'][1]))
        current.updateTable(request['newNode'][0],request['newNode'][2], request['newNode'][1])
        _request = {
            'type' : 'updateTable',
            'newNode' : request['newNode']
        }
        _req = {
            'type' : 'iMinSys',
            'me' : [current.myHash, current.port, current.IP]
        }
        nodeSock.send(json.dumps(_req).encode())
        nodeSock.close()
        sock = socket.socket()
        sock.connect((current.pred[2],current.pred[1]))
        sock.send(json.dumps(_request).encode())
        sock.close()
        conn.close()
        return
    if request['type'] == 'updateTableLeft':
        if (request['new'][0] == current.myHash):
            conn.close()
            print('--------------- fingerTables Updated ---------')
            return
        current.updateTableLeft(request['prev'],request['new'])
        conn.close()
        sock = socket.socket()
        sock.connect((current.pred[2],current.pred[1]))
        _request = {
            'type' : 'updateTableLeft',
            'prev' : request['prev'],
            'new' :  request['new']
        }
        sock.send(json.dumps(_request).encode())
        sock.close()
        return
    

    if request['type'] == 'iMinSys':
        current.updateTable(request['me'][0],request['me'][2],request['me'][1])
        conn.close()
        return

    if request['type'] == 'HaveToTakeFile':
        print(' ===== Taking File ===== ')
        haveToTake = True
        if request['me'][0] == current.myHash:
            haveToTake = False
            current.files.append((current.hash(request['fileName']),request['fileName']))
        for i in current.files:
            if i[1] == request['fileName']:
                haveToTake = False
        if not haveToTake:
            response = {
            'completed' : 'done'
            }
            conn.send(json.dumps(response).encode())
            conn.close()
            print(' ===== File Taken ===== ')
            return
                

        sock = socket.socket()
        sock.connect((request['me'][2],request['me'][1]))
        _request = {
            'type' : 'giveFile',
            'fileName' : request['fileName'],
            'me' : [current.myHash, current.port, current.IP]
        }
        if request['action'] == 'put':
            _request['action'] = 'put'
        else:
            _request['action'] = 'notPut'

        file = open('./'+str(current.myHash)+'/'+request['fileName'], 'wb')
        sock.send(json.dumps(_request).encode())
        section = sock.recv(1024)
        while (section):
            file.write(section)
            section  = sock.recv(1024)
        file.close()
        sock.close()
        current.files.append((current.hash(request['fileName']),request['fileName']))
        response = {
            'completed' : 'done'
        }
        conn.send(json.dumps(response).encode())
        print(current.files)
        conn.close()
        print(' ===== File Taken ===== ')
        return
    
    if request['type'] == 'changePred':
        current.pred = request['pred']  

        conn.close()
        return
    
    if request['type'] == 'giveUrSucc':
        response = {
            'succ' : current.succ
        }
        conn.send(json.dumps(response).encode())
        conn.close()
        return

    if request['type'] == 'leftTable':
        current.leftFromTable(request['succ'], request['leaving'])
        if request['succ'][0] == current.myHash:
            conn.close()
            return
        sock = socket.socket()
        sock.connect((current.pred[2], current.pred[1]))
        sock.send(json.dumps(request).encode())
        sock.close()
        conn.close()
        return

    if request['type'] == 'canDownload':
        fileName = request['fileName']
        haveFile = False
        for i in current.files:
            if i[1] == fileName:
                haveFile = True
                break
        
        response={
            'succ' : current.succ
        }
        if haveFile:
            response['can'] = 'yes'
        else:
            response['can'] = 'no'
        conn.send(json.dumps(response).encode())
        conn.close()
        return
    
    if request['type'] == 'Download':
        fileName = request['fileName']
        start = request['start']
        file = open('./'+str(current.myHash)+'/'+fileName, 'rb')
        section = file.read(1024)
        i = 0 
        while(section):
            if start>i:
                section = file.read(1024)
                i = i+1
                continue
            conn.send(section)
            i = i+1
            section = file.read(1024)

        file.close()
        conn.close()

    if request['type'] == 'wantLeave':
        print(current.pred)
        print(current.succ)
        clientCon = socket.socket()
        clientCon.connect((request['succesor'][2],request['succesor'][1]))
        _request = {
            'type' : 'changePred',
            'pred' : [current.myHash, current.port, current.IP]
        }
        clientCon.send(json.dumps(_request).encode())
        current.leftFromTable(request['succesor'], request['me'])
        current.succ = request['succesor']
        clientCon.close()
        clientCon = socket.socket()
        _request = {
            'type' : 'leftTable',
            'leaving' : request['me'],
            'succ' : current.succ
        }
        clientCon.connect((current.pred[2],current.pred[1]))
        clientCon.send(json.dumps(_request).encode())
        clientCon.close()
        _response = {
            'type' : 'leaveResponse',
            'order' : 'leave'
        }
        conn.send(json.dumps(_response).encode())
        conn.close()
        return
        



def serverHandle(s,curr):
    global leaving
    while True:
        conn, addr = s.accept()
        _thread.start_new_thread(connectionHandle, (conn, curr))      #thread for dealing with a new connection 



def divideFiles(current):
    for i in current.files:
        succOfI = current.successor(i[0])
        request ={
            'type' : 'giveUrSucc'
        }
        sock = socket.socket()
        sock.connect((succOfI[2],succOfI[1]))
        sock.send(json.dumps(request).encode())
        res = sock.recv(1024)
        response = json.loads(res)
        succOfSucc = response['succ']
        sock.close()
        if succOfSucc[0] != current.myHash:
            clientCon = socket.socket()
            clientCon.connect((succOfSucc[2],succOfSucc[1]))
            request = {
                'type'  : 'HaveToTakeFile',
                'me'    :  [current.myHash, current.port, current.IP],
                'fileName'  :  i[1],
                'action' : 'notPut'
            }
            clientCon.send(json.dumps(request).encode())
            clientCon.recv(1024)
            clientCon.close()
        print (succOfI, ' ===> ', i[1])
        if succOfI[0] != current.myHash:
            clientCon = socket.socket()
            clientCon.connect((succOfI[2],succOfI[1]))
            request = {
                'type'  : 'HaveToTakeFile',
                'me'    :  [current.myHash, current.port, current.IP],
                'fileName'  :  i[1],
                'action' : 'notPut'
            }
            clientCon.send(json.dumps(request).encode())
            clientCon.recv(1024)
            clientCon.close()


def leave(current):
    print(' #####Leaving######  ')
    global leaving

    if current.succ.__len__() == current.pred.__len__():
        leaving = True
        for i in current.files:
            current.files.remove(i)
        return True

    leaving = True
    for i in current.files:
        clientCon = socket.socket()
        clientCon.connect((current.succ[2],current.succ[1]))
        request = {
            'type'  : 'HaveToTakeFile',
            'me'    :  [current.myHash, current.port, current.IP],
            'fileName'  :  i[1],
            'action' : 'notPut'
        }
        clientCon.send(json.dumps(request).encode())
        res = clientCon.recv(1024)
        clientCon.close()
    clientCon = socket.socket()
    clientCon.connect((current.pred[2],current.pred[1]))
    request = {
        'type': 'wantLeave',
        'me' : [current.myHash, current.port, current.IP],
        'succesor' : current.succ 
    }
    clientCon.send(json.dumps(request).encode())
    _response = clientCon.recv(1024)
    response = json.loads(_response)
    clientCon.close()
    
    if response['order'] == 'leave':
        return True
    return False

def put(fileName , current):
    process = subprocess.Popen('ls', stdout=subprocess.PIPE, stderr=subprocess.PIPE,cwd='./'+str(current.myHash))
    out,err = process.communicate()

    lsFiles = out.split()
    print(lsFiles)
    
    found = False
    for i in range(lsFiles.__len__()):
        if fileName == lsFiles[i].decode('utf-8'):
            found = True 
    if not found:
        print("Problem Detected ::: File Not Available")
        return

    succOfFile = current.successor(current.hash(fileName))
    request = {
        'type' : 'giveUrSucc'
    } #finds the successor of the successor of file
    sock = socket.socket()
    sock.connect((succOfFile[2],succOfFile[1]))
    sock.send(json.dumps(request).encode())
    _res = sock.recv(1024)
    res = json.loads(_res)
    successorOfSuccessor = res['succ']

    #sending file to the succesor of the file
    sock = socket.socket()
    sock.connect((succOfFile[2],succOfFile[1]))
    request = {
        'type' : 'HaveToTakeFile',
        'me' : [current.myHash, current.port, current.IP],
        'fileName' : fileName,
        'action' : 'notPut'
    }
    sock.send(json.dumps(request).encode())
    sock.recv(1024)
    sock.close()

    #sending file to the successor of the file successor
    if successorOfSuccessor[0] != succOfFile[0]:
        sock = socket.socket()
        sock.connect((successorOfSuccessor[2] ,successorOfSuccessor[1]))
        request = {
            'type' : 'HaveToTakeFile',
            'me' : [current.myHash, current.port, current.IP],
            'fileName' : fileName,
            'action' : 'notPut'
        }
        sock.send(json.dumps(request).encode())
        sock.recv(1024)
        sock.close()

def ping(current):
    predOfPredecessor = []
    predFiles = []
    while True:
        try:
            if current.pred.__len__() != 0: 
                sock = socket.socket()
                sock.connect((current.pred[2], current.pred[1]))
                request = {
                    'type' : 'ping',
                    'me' : [current.myHash, current.port, current.IP]
                }
                sock.send(json.dumps(request).encode())
                _response = sock.recv(1024)
                response = json.loads(_response)
                predOfPredecessor = response['pred']
                predFiles = response['listOfFiles']
                sock.recv(1024)
                sock.close()
        except:
            print(sys.exc_info())
            temp = current.pred
            
            current.pred = predOfPredecessor
            
            if temp[0] == current.succ[0]:
                current.succ = [current.myHash, current.port, current.IP]
                current.pred = [current.myHash, current.port, current.IP]
                continue

            clientCon = socket.socket()
            clientCon.connect((current.pred[2], current.pred[1]))
            request = {
                'type' : 'changeSucc',
                'me'   : [current.myHash, current.port, current.IP]
            }
            clientCon.send(json.dumps(request).encode())
            clientCon.recv(1024)
            clientCon.close()

            for i in current.files:
                clientCon = socket.socket()
                clientCon.connect((current.succ[2],current.succ[1]))
                request = {
                    'type' : 'HaveToTakeFile',
                    'me' : [current.myHash, current.port, current.IP],
                    'fileName' : i[1],
                    'action' : 'notPut'
                }
                clientCon.send(json.dumps(request).encode())
                clientCon.recv(1024)
                clientCon.close()


            clientCon = socket.socket()
            clientCon.connect((current.pred[2],current.pred[1]))
            request = {
                'type' : 'updateTableLeft',
                'prev' : temp,
                'new' :  [current.myHash, current.port, current.IP]
            }
            clientCon.send(json.dumps(request).encode())
            clientCon.close()



def download(fileName, current):
    process = subprocess.Popen('ls', stdout=subprocess.PIPE, stderr=subprocess.PIPE,cwd='./'+str(current.myHash))
    out,err = process.communicate()

    lsFiles = out.split()
    
    found = False
    for i in range(lsFiles.__len__()):
        if fileName == lsFiles[i].decode('utf-8'):
            found = True 
    if found:
        print("=== Download Complete === ")
        return
    start = 0
    sock = socket.socket()
    request = {
        'type' : 'canDownload',
        'fileName' : fileName
    }
    fileSucc =  current.successor(current.hash(fileName))
    sock.connect((fileSucc[2],fileSucc[1]))
    sock.send(json.dumps(request).encode())
    _response = sock.recv(1024)
    response = json.loads(_response)
    if response['can'] != 'yes':
        print('Problem ::> There is no such file in system')
        return

    succOfSucc = response['succ']
    file = open('./'+str(current.myHash)+'/'+fileName,'wb')
    sock = socket.socket()
    request = {
        'type' : 'Download',
        'fileName' : fileName,
        'start' : start
    }
    fileSucc =  current.successor(current.hash(fileName))
    sock.connect((fileSucc[2],fileSucc[1]))
    sock.send(json.dumps(request).encode())
    file = open('./'+str(current.myHash)+'/'+fileName,'wb')
    section = sock.recv(1024)
    disconnected = True
    while (section):
        try:
                file.write(section)
                start = start+1
                section  = sock.recv(1024)
        except:
            disconnected = True
            break
    if disconnected:
        sock.close()
        file.close()
        start = 0
        file = open('./'+str(current.myHash)+'/'+fileName,'wb')
        sock = socket.socket()
        sock.connect((succOfSucc[2],succOfSucc[1]))
        request = {
            'type' : 'Download',
            'fileName' : fileName,
            'start' : start
        }
        sock.send(json.dumps(request).encode())
        section = sock.recv(1024)
        while (section):
            file.write(section)
            start = start+1
            section  = sock.recv(1024)
   
    file.close()
    print('============ Download Completed =============')
    sock.close() 


def main():
    """
        for initializing the node and dealing with the user
    """
    global m
    global fnTabUpdate
    newSys = False



    if sys.argv[1] == '0' and sys.argv[2] == '0':
        print("new sys ------ starting.....")
        newSys = True
    sysIP = sys.argv[1]
    sysPort = int(sys.argv[2])
    IP = '127.0.0.1'
    while True:
        port = int(input("Please input a port no: "))
        if newSys:
            break
        clientCon = socket.socket()
        clientCon.connect((sysIP, sysPort))
        requestForSuccesor = {
            "type" : 'reqForSucc',
            'id' : int(hashlib.sha1((sysIP+str(port)).encode()).hexdigest(), 16)%m  
        }
        clientCon.send(json.dumps(requestForSuccesor).encode())
        _response = clientCon.recv(1024)
        clientCon.close()
        response = json.loads(_response)
        successor = response['succ']
        if successor[0] != int(hashlib.sha1((sysIP+str(port)).encode()).hexdigest(), 16)%m:
            break
    current = node(IP, port)
    current.fingerTableInit("")
    s = socket.socket()
    s.bind(('127.0.0.1', port))
    s.listen()

    clientCon = socket.socket()

    if not newSys:
        clientCon.connect((sysIP, sysPort))
        requestForSuccesor = {
            "type" : 'reqForSucc',
            'id' :  current.myHash
        }
        clientCon.send(json.dumps(requestForSuccesor).encode())
        _response = clientCon.recv(1024)
        clientCon.close()
        response = json.loads(_response)
        successor = response['succ']
        print(successor)
        current.succ = successor

        clientCon=socket.socket()
        clientCon.connect((current.succ[2],current.succ[1]))
        request  = {
            'type' : 'reqForFiles',
            'me'   : [current.myHash, current.port, current.IP]
        }
        clientCon.send(json.dumps(request).encode())
        _response = clientCon.recv(1024)
        clientCon.close()

               
        _res = json.loads(_response)
        arr = _res['arr']
        for i in arr:
            current.files.append((i[0],i[1]))
            request = {
                'type' : 'giveFile',
                'me' : [current.myHash, current.port, current.IP],
                'fileName' : i[1],
                'action' : 'notPut'
            }
            clientCon = socket.socket()
            clientCon.connect((current.succ[2],current.succ[1])) 
            clientCon.send(json.dumps(request).encode())
            file = open('./'+str(current.myHash)+'/'+i[1],'wb')
            section = clientCon.recv(1024)
            while (section):
                file.write(section)
                section  = clientCon.recv(1024)
            file.close()
            clientCon.close()

             
        print(current.files)

        clientCon = socket.socket()
        clientCon.connect((current.succ[2],current.succ[1]))
        request = {
            'type' : 'reqForPred',
            'me' : [current.myHash, current.port, current.IP]
        }
        clientCon.send(json.dumps(request).encode())
        _res = clientCon.recv(1024)
        current.pred = json.loads(_res)
        clientCon.close()

        clientCon = socket.socket()
        clientCon.connect((current.pred[2], current.pred[1]))
        request = {
            'type' : 'changeSucc',
            'me'   : [current.myHash, current.port, current.IP]
        }
        clientCon.send(json.dumps(request).encode())
        clientCon.recv(1024)
        clientCon.close()



        clientCon = socket.socket()
        clientCon.connect((current.pred[2], current.pred[1]))
        request = {
            'type' : 'updateTable',
            'newNode' : [current.myHash, current.port, current.IP]
        }
        clientCon.send(json.dumps(request).encode())
        clientCon.close()

        print(current.updated)
        print(current.files)
        """ while not current.updated:
            time.sleep(2)
        if current.updated: 
             """


    _thread.start_new_thread(serverHandle, (s,current))
    _thread.start_new_thread(ping, (current,))

    if current.succ.__len__() != 0:
            print('here', current.succ)
            print(current.files)
            for i in range(current.files.__len__()):
                request = {
                    'type' : 'HaveToTakeFile',
                    'me' : [current.myHash, current.port, current.IP],
                    'fileName' : current.files[i][1],
                    'action' : 'notPut'
                }
                sock = socket.socket()
                sock.connect((current.succ[2], current.succ[1]))
                sock.send(json.dumps(request).encode())
                print(current.files[i])
                sock.recv(1024)
                sock.close()

    
    while(True):
        print('1: Leaving\n2: Upload\n3: succPred\n 4: Download\n 5: Files\n6: Finger Table\n')
        inp = (input("Enter :::> "))
        if inp == '1':
            """ _thread.start_new_thread(leave,(current,)) """
            leave(current)

            while (not leaving and current.files.__len__()!=0):
                time.sleep(1)
            "time.sleep(10)"
            print('     ######-----LEFT-----####### ')

            break
        elif inp == '2':
            fileName = input("Enter the filename  :--->  ")
            put(fileName,current);
        elif inp == '3': 
            print(current.files)
        elif inp == '4':
            fileName = input('Enter the filename  :--->  ')
            download(fileName,current)
        elif inp == '5':
            print(current.succ)
            print(current.pred)

        elif inp == '6':
            print(' =========== Finger Table ============== ')
            print(current.fingerTable)
        
        else:
            print('==== Unknown Command :: Check the exact Command Number ====')

if __name__ == "__main__":
    main()
