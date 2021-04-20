# 122 lines! #this is a joke and there is really nothing getting downloaded
import datetime
import time

timestamp_now = datetime.datetime.now().strftime('%Y-%m-%d')

print("""\n
##############################################
##############################################
##############################################
##############################################
##############################################
###########
###########
###########
###########                                                              #####              #####
###########                                                              #####              #####
###########                                                              #####              #####
###########                                                        #################    ###############
###########                                                        #################    ###############               
###########                                                              #####              #####
###########                                                              #####              #####
###########                                                              #####              #####
###########                                                             
################################################
################################################
################################################
################################################
################################################
""")
# Flags



def confirmation(question, default="no"):    
    valid = {"yes": True, "y": True, "ye": True,
                "no": False, "n": False} 
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    validInputEntered = False
    while not validInputEntered:
        data = input("{}{}".format(question, prompt)).lower()
        if data in valid:
            validInputEntered = True
            return valid[data]
        if data == "":
            validInputEntered = True
            return default




    print("[*]  Argument was omitted - going with 3s samples by default")
    samples = 3


# Global variables
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'
} 

print("""\nYou'll get latest samples from:
\t# Flytech Videos
\t# Endermanch
\t#Intendedlifecoding
""")

confirmed = confirmation("Confirm and start downloading 3 samples?")
if not confirmed:
    sys.exit(0)

print("\nSearching...")
# Flytech videos
def FlyTech(samples):
    global final_list

    url_list = []

    if samples <= 3:
        pages = 1
    else:
        pages = (samples // 5) + 1
time.sleep(.55)
print("[*]  FlyTech Videos samples - Done ")

#endermanch
def Endermanch(samples):
    global final_list

    url_list = []

    if samples <= 50:
        pages = 1
    else:
        pages = (samples // 50) + 1
time.sleep(.55)
print("[*]  Endermanch samples - Done ")

#Intendedlifecoding
def Intendedlifecoding(samples):
    global final_list

    url_list = []

    if samples <= 50:
        pages = 1
    else:
        pages = (samples // 50) + 1
time.sleep(.55)
print("Files have been downloaded! please wait 5 seconds...")


