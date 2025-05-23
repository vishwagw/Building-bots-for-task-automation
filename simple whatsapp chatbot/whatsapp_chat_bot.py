from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import os
import time
import math

class Message():
    def __init__(self, user, message):
        self.user = user
        self.message = message

    def __eq__(self, other) :
        return self.message == other.message
    
if os.name == "nt":
    driverPath = "E:\programing\my projects\whatsapp chatbot\cortana\chromedriver_win32\chromedriver.exe"
    dataPath = "Data/chatbot"

else:
    driverPath = "E:\programing\my projects\whatsapp chatbot\cortana\chromedriver_win32\chromedriver.exe"
    dataPath = "Data/Chatbot"

options = webdriver.ChromeOptions()
options.add_argument("--user--data--dir=" + dataPath)
driver = webdriver.Chrome(options)
driver.get('https://web.whatsapp.com/')
driver.execute_script("window.open('','_blank');")
driver.switch_to.window(driver.window_handles[1])
#driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)

input("Choose a chat on WHATSAPP and press ENTER : ")
chatHistory = []
replyQueue = []
firstRun = True

print("Starting the program...")

while True:
    try:
        driver.switch_to.window(driver.window_handles[0])
        usersDiv = driver.find_element_by_id("side")
        messageDiv = driver.find_element_by_id("main")
        messageList = messageDiv.find_elements_by_class_name("msg")

        newMessages = []
        for message in reversed(messageList):
            bubbleText = None
            try:
                bubbleText = message.find_element_by_class_name("bubble")
            except:
                pass

            if bubbleText is not None:
                author = "Unknown"
                msgObj = None
                if "has-author" in bubbleText.get_attribute("class"):
                    try:
                        author = bubbleText.find_element_by_class_name(
                            "message-author").find_element_by_class_name("emojitext").text
                    except Exception as e:
                        pass
                elif "msg-group" in message.get_attribute("class"):
                    author = "VishwaGW"
                try:
                    text_message = bubbleText.find_element_by_class_name(
                        "message-text").find_element_by_class_name("emojitext").text
                    if len(text_message) > 0:
                        msgObj = Message(author, text_message)

                except Exception as e:
                    pass

                if len(chatHistory) > 0 and (msgObj is not None) and msgObj == chatHistory[-1]:
                    break
                elif msgObj is not None:
                    newMessages.append(msgObj)
        for message in reversed(newMessages):
            chatHistory.append(message)
        
        for i in range(len(chatHistory)):
            if i > 0 and chatHistory[i].user == "unkown":
                chatHistory[i].user = chatHistory[i - 1].user

        for message in reversed(newMessages):
            if message.message[0] == "$" and firstRun == False:
                replyQueue.append(message)

        firstRun = False
        if len(replyQueue) == 0:
            continue

        driver.switch_to.window(driver.window_handles[0])
        driver.switch_to.default_content()
        driver.switch_to.frame('input')
        textField = driver.find_element_by_tag_name("input")[1]

        responses = []

        for message in replyQueue:

            textField.send_keys(message.message[1:] + Keys.ENTER)
            responseBody = None
            fontTags = driver.find_elements_by_tag_name("font")

            for tag in fontTags:
                if tag.get_attribute("face") == "Trebuchet MS,Arial" and tag.get_attribute("color") == "#000000":
                   responseBody = tag
                   break

            start = responseBody.text.find("Cortana")
            end = responseBody.text.find("you", 4)
            firstName = message.user.split(' ')[0]
            resp = responseBody.text[start + 10:end - 2]
            print(start, end, repr(resp))
            responses.append("@" + firstName + " : " + resp)
        
        replyQueue = []

        driver.switch_to.window(driver.window_handles[0])
        inputMessage = messageDiv.find_element_by_class_name('pluggable-input-body')
        
        for response in responses:
            lines = response.split('\n')
            for line in lines:
                inputMessage.send_keys(line)
                inputMessage.send_keys(Keys.SHIFT, Keys.ENTER)
            inputMessage.send_keys(Keys.ENTER)
    
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)






    



                   



                        

