def script_function(Username,EventName,Source_IP,Destination_IP,Destination_Port,Action,Event_id,File_Hash):
    d={}
    d["Username"]=Username
    d["EventName"]=EventName
    d["Source_IP"]=Source_IP
    d["Destination_IP"]=Destination_IP
    d["Destination_Port"]=Destination_Port
    d["Action"]=Action
    d["Event_id"]=Event_id
    d["File_Hash"]=File_Hash
    import json
    a=[]
    def f1(d):
        for row in zip(*([key] + (value) for key, value in (d.items()))):
            yield row
        
    g=f1(d) 
    h=list(g)
    dt={}
    for i in h:
        if i not in dt:
            dt[i]=1
        else:
            dt[i]+=1
        
    names=[]
    Username=[]
    EventName=[]
    Source_IP=[]
    Destination_IP=[]
    Destination_Port=[]
    Action=[]
    Event_id=[]
    File_Hash=[]
    count=[]
    #aggregation
    for k,v in dt.items():
        if k==('Username', 'EventName', 'Source_IP', 'Destination_IP', 'Destination_Port','Action','Event_id','File_Hash'):
            pass
        
        else:
            count.append(v)
            for i in range(len(k)):
                if i==0:
                    Username.append(k[0])
                elif i==1:
                    EventName.append(None)
                elif i==2:
                    Source_IP.append(k[2])
                elif i==3:
                    Destination_IP.append(k[3])
                elif i==4:
                    Destination_Port.append(k[4])
                elif i==5:
                    Action.append(k[5])
                elif i==6:
                    Event_id.append(k[6])
                elif i==7:
                    File_Hash.append(k[7])
                else:
                    pass

    dct={}


    dct["Username"]=Username
    dct["EventName"]=EventName
    dct["Source_IP"]=Source_IP
    dct["Destination_IP"]=Destination_IP
    dct["Destination_Port"]=Destination_Port
    dct["Action"]=Action
    dct["Event_id"]=Event_id
    dct["File_Hash"]=File_Hash
    dct["count"]=count

    jdata=json.dumps(dct)
    import json
    import time
    
    Uname=[]
    Ename=[]
    SIP=[]
    DIP=[]
    Dport=[]
    An=[]
    Eid=[]
    Fhash=[]
    Ct=[]
    countn=[]
    #sorting
    s=sorted(dct["count"],reverse=True)
    for i in range(len(s)):
        for j in range(len(dct["count"])):
            if dct["count"][j]==s[i]:
                if j not in countn:
                    countn.append(j)
                    Uname.append(dct["Username"][j])
                    SIP.append(dct["Source_IP"][j])
                    DIP.append(dct["Destination_IP"][j])
                    Dport.append(dct["Destination_Port"][j])
                    Ename.append(dct["EventName"][j])
                    An.append(dct["Action"][j])
                    Eid.append(dct["Event_id"][j])
                    Fhash.append(dct["File_Hash"][j])
                    Ct.append(dct["count"][j])
                    
    
    newdict={
    "Username":Uname,
    "EventName":Ename,
    "Source_IP":SIP,
    "Destination_IP":DIP,
    "Destination_Port":Dport,
    "Action":An,
    "Event_id":Eid,
    "File_Hash":Fhash,
    "count":Ct
    }
    Uname=[]
    Ename=[]
    Eid=[]
    SIP=[]
    DIP=[]
    Dport=[]
    Fhash=[]
    Atn=[]
    ct=[]
    #slicing
    for i in range(len(newdict["EventName"])):
    
        if i>=5:
            pass
        else:
            Ename.append(newdict["EventName"][i])
            Uname.append(newdict["Username"][i])
            Eid.append(newdict["Event_id"][i])
            SIP.append(newdict["Source_IP"][i])
            DIP.append(newdict["Destination_IP"][i])
            Dport.append(newdict["Destination_Port"][i])
            Atn.append(newdict["Action"][i])
            Fhash.append(newdict["File_Hash"][i])
            ct.append(newdict["count"][i])
        
    data={
        "EventName":Ename,
        "Username":Uname,
        "Event_id":Eid,
        "Source_IP":SIP,
        "Destination_IP":DIP,
        "Destination_Port":Dport,
        "Action":Atn,
        "File_Hash":Fhash,
        "count":ct
    }
    jdata=json.dumps(data)
    c=""
    for i in jdata:
        if i=="'":
            pass
        else:
            c+=i
    b=json.loads(c)
    return b