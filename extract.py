
def location(block):
    # Your code here
    data = block.split(",")     #{0, 1}
    f_data = data[1] #{34.0S NWOT EPAC END} or {34.0S NABRUD END}
    space = f_data.find(" ")
    end = f_data.find("END")

    ff_data = f_data[space:end] #NABRUD or NWOT EPAC
    return ff_data[::-1]
    
def temperature(block):
    # Your code here
    data = block.split("_")[0]  #["BEGIN 12.2"]
    data1 = data.split(" ")     #["BEGIN", "12.2"]
    data2 = data1[1]     #   "12.2"

    temp = float(data2)

    return temp


def x_coordinate(block):
    # Your code here                                    #   0,      1
    data = block.split(":")[1].split(" ")[0].split(",")[0] #[18.6E, 34.0S]

    return data


def y_coordinate(block):
    # Your code here
    data = block.split(":")[1].split(" ")[0].split(",")[1] #[18.6E, 34.0S]
    return data


def pressure(block):
    # Your code here
    data = block.split(":")[0].split("_")[1]
    data1 = float(data)
    return data1


def get_block(data):
    # Your code here
    start = data.find("BEGIN")
    end = data.find("END")

    block_data = data[start: end+3]
    return block_data



def main():
    data = input('Enter the raw data:\n')
    block = get_block(data)
    print('Site information:')
    print(block)
    print('Location:', location(block))
    print('Coordinates:', y_coordinate(block), x_coordinate(block))
    print('Temperature: {:.2f} C'.format(temperature(block)))
    #print( temperature(block))
    print('Pressure: {:.2f} hPa'.format(pressure(block)))

if __name__=='__main__':
    main()
