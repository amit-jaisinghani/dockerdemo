import time

f = open("testFile.txt","w")

f.write("Super important stuff that I will want to read later.")

f.close()


time.sleep(3600)
