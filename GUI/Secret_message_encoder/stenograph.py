from stegano import lsb
secret = lsb.hide("car.png", "Zdarova Anton")
secret.save("test-secret.png")

'''
clear_message = lsb.reveal("test-secret.png")
print(clear_message)
'''
