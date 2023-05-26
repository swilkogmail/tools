#!/usr/bin/env python3

ready = 'HIGHQ,CE,ASC,ACT,ASK,TPS,STAGEMART'
required = 'HIGHQ,CE,ASC,ACT,ASK,STAGEMART,TPS'
ready_lst = sorted(ready.split(','))
required_lst = sorted(required.split(','))

# we just need to check the all the batched that are required are ready

try:
    for realm in required_lst:
        if realm in ready_lst:
            continue
        else:
            raise Exception
except Exception:
    print(f"War: {err}")
else:
    print("run the load")
# finally:
#     print("finally is running")