arr = {'global': []}
arrayOut = []

count = int(input())

while count > 0:
    command, namespace, name = input().split()
    if command == 'add':
        if namespace == 'global' and 'global' not in arr:
            arr.update({'global': [namespace, name]})
        else:
            if namespace in arr:
                b = []
                a = b.__add__(arr[namespace]).__add__([name])
                arr[namespace] = arr[namespace].append(name)
                arr.update({namespace: a})

    if command == 'create':
        if name in arr:
            arr.update({namespace: [name]})

    if command == 'get':
        if namespace in arr:
            isGo = True
            while isGo:
                if namespace == 'global' and name not in arr[namespace]:
                    arrayOut.append('None')
                    isGo = False
                else:
                    if name in arr[namespace]:
                        arrayOut.append(namespace)
                        isGo = False
                    else:
                        if len(arr[namespace]) > 0:
                            namespace = arr[namespace][0]
                            if namespace == 'global':
                                if name not in arr[namespace]:
                                    arrayOut.append('None')
                                    isGo = False
                        else:
                            arrayOut.append('None')
                            isGo = False
        else:
            arrayOut.append('None')
    count -= 1

print('\n'.join(arrayOut))