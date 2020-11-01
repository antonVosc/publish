'''
with open('C:\Windows\System32\drivers\etc\hosts','r') as hosts:
    host = hosts.readlines() #list
    for i in host:
        print(i)

with open('C:\Windows\System32\drivers\etc\hosts','a') as hosts:
    hosts.write('	127.0.0.1       www.youtube.com')
    print('written')
'''

def blocked_websites():
    with open('C:\Windows\System32\drivers\etc\hosts','r') as hosts:
        host = hosts.readlines() #list
        websites = []

        for i in host:
            write = False
            site_name = ''
            if 'www' not in i:
                pass
            else:
                for g in i:
                    if g == 'w':
                        write = True
                    if g == "\n":
                        write = False
                    if write == True:
                        site_name += g
                websites.append(site_name)
                
    return websites

sites = blocked_websites()
print(sites)
