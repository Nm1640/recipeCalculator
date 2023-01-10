def save(inventory):
    # Save the contents of the inventory list to a file named inventory.txt
    with open('inventory.txt', 'w') as file:
        for item in inventory:
            print(item)
            file.write('%s\n' % item)            
    print('File Saved')

def load(inventory):
    # Load the contents of the inventory.txt file to the inventory list.
    # if the file doesn't exist, create a file instead.
    try:
        with open('inventory.txt', 'r') as file:
            for item in file:
                parsed = item[:-1] # remove the \n
                inventory.append(parsed)
        print('File Opened')
        
    except:
        print('File Not Found')
        with open('inventory.txt', 'w') as file:
            file.write('')
        print('File Created')