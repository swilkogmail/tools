#!/usr/bin/env python3

ready = 'HIGHQ,CE,ASC,ACT,ASK,STAGEMART,TPS'
required = 'HIGHQ,CE,ASC,ACT,ASK,STAGEMART,TPS'

print(ready)
print(required)

ready_lst = sorted(ready.split(','))
required_lst = sorted(required.split(','))

print(ready_lst)
print(required_lst)

if required in ready:
    print('trigger load')
else:
    print('hang fire')