from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class ChatBot:
    def __init__(self,root):
        self.root=root
        self.root.title("ChatBot")
        self.root.geometry("730x650+0+0")
        self.root.bind('<Return>',self.enter_func)

        main_frame=Frame(self.root,bd=4,bg="powder blue",width=610)
        main_frame.pack()

        img_chat=Image.open('college_images\chatbot_main.png')
        img_chat=img_chat.resize((200,70),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img_chat)

        Title_label=Label(main_frame,bd=3,relief=RAISED,anchor='nw',width=730,compound=LEFT,image=self.photoimg,text='CHAT ME',font=("arial",30,"bold"),fg='green',bg='white')
        Title_label.pack(side=TOP)


        self.scroll_y=ttk.Scrollbar(main_frame,orient=VERTICAL)
        self.text=Text(main_frame,width=65,height=20,bd=20,relief=RAISED,font=('arial',14),yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.text.pack()


        btn_frame=Frame(self.root,bd=4,bg='white',width=730)
        btn_frame.pack()

        label_1=Label(btn_frame,text="Type Something",font=("arial",14,"bold"),fg='green',bg='white')
        label_1.grid(row=0,column=0,padx=5,sticky=W)


        self.entry=StringVar()
        self.entry1=ttk.Entry(btn_frame,textvariable=self.entry,width=40,font=("arial",15,"bold"))
        self.entry1.grid(row=0,column=1,padx=5,sticky=W)

        self.send=Button(btn_frame,text="Send>>",command=self.send,font=('arial',15,'bold'),bg='green')
        self.send.grid(row=0,column=2,padx=5,sticky=W)

        self.clear=Button(btn_frame,text="Clear Data",command=self.clear,font=('arial',15,'bold'),bg='red',fg='white')
        self.clear.grid(row=1,column=0,padx=5,sticky=W)


        self.msg=''
        self.lable_11=Button(btn_frame,text=self.msg,font=('arial',14,'bold'),bg='white')
        self.lable_11.grid(row=1,column=1,padx=5,sticky=W)


    # ===========fuction declairation=============
    def enter_func(self,event):
        self.send.invoke()
        self.entry.set('')

    def clear(self):
        self.text.delete('1.0',END)
        self.entry.set('')



    def send(self):
        send='\t\t\t'+'You: '+self.entry.get()
        self.text.insert(END,'\n'+send)
        self.text.yview(END)

        if (self.entry.get()==''):
            self.msg='Please enter some input'
            self.lable_11.config(text=self.msg,fg='red')

        else:
            self.msg=''
            self.lable_11.config(text=self.msg,fg='red')

        if (self.entry.get()=="hello"):
            self.text.insert(END,'\n\n'+'Bot: Hi')

        elif (self.entry.get()=="hi"):
            self.text.insert(END,'\n\n'+'Bot: Hello')
        
        elif (self.entry.get()=="How are you?"):
            self.text.insert(END,'\n\n'+'Bot: fine and you')
        
        elif (self.entry.get()=="how are you?"):
            self.text.insert(END,'\n\n'+'Bot: fine and you')
        
        elif (self.entry.get()=="Fantastic"):
            self.text.insert(END,'\n\n'+'Bot: Nice to Hear')

        elif (self.entry.get()=="Who created you?"):
            self.text.insert(END,'\n\n'+'Bot: Paras Mahajan did using Python')

        elif (self.entry.get()=="What is your name?"):
            self.text.insert(END,'\n\n'+'Bot: My name is Mr.Helper')

        
        elif (self.entry.get()=="Can you speak Marathi"):
            self.text.insert(END,'\n\n'+"Bot: I'm still learning it..")

        elif (self.entry.get()=="What is machine learning?"):
            self.text.insert(END,'\n\n'+'Bot: Machine learning is a branch\nof artificial intelligence {AI} focused\non building applications that learn\nfrom data and improve their accuracy\nover time without being programmed\nto so')

        elif (self.entry.get()=="How does face recognition work?"):
            self.text.insert(END,'\n\n'+'Bot: Face recognition works by identifying and verifying a person based on unique facial features. Here’s a brief rundown of the process:\n1. Detection: The system first detects a face in an image or video frame using methods like Haar Cascades or deep learning models.\n2. Alignment: Once detected, the face is aligned to ensure consistent positioning, making it easier to analyze facial features accurately.\n3. Feature Extraction: The system extracts distinctive facial features, such as the distance between the eyes or shape of the jawline. This is often done using neural networks.\n4. Comparison: These features are converted into a mathematical representation and compared with stored facial data to identify or verify the person.\n5. Decision: If the extracted features match a stored profile, the person is recognized; otherwise, they remain unidentified.\nThis process relies heavily on machine learning and image processing techniques to ensure accuracy.')


        elif (self.entry.get()=="How many countries use facial recognition?"):
            self.text.insert(END,'\n\n'+"Bot: As of 2024, facial recognition technology (FRT) is actively\nused by 98 countries, with widespread applications across\npublic and private sectors. An additional 12 countries\nhave approved FRT but have yet to implement it, and 13\nmore are exploring its potential. However, three countries,\nincluding Belgium and Luxembourg, have officially\nbanned the technology due to concerns about privacy\nand surveillance issues​​")

        elif (self.entry.get()=="What is python programming?"):
            self.text.insert(END,'\n\n'+"Bot: Python programming involves writing code in Python, a\nbeginner-friendly, high-level language known for its\nsimplicity and readability. It's versatile, used widely for\ntasks like web development, data analysis, and\nautomation. Python's extensive libraries and supportive\ncommunity make it popular across diverse fields, from AI\nto scientific computing.")

        elif (self.entry.get()=="What is chatbot?"):
            self.text.insert(END,'\n\n'+"Bot: A chatbot is a software application designed to simulate\nhuman conversation, allowing users to interact with it\nthrough text or voice. Chatbots use natural language\nprocessing (NLP) and, in more advanced cases, artificial\nintelligence (AI) to understand and respond to queries in\nreal time. They are commonly used for customer support,\ninformation retrieval, and personal assistance on\nplatforms like websites, messaging apps, and smart\ndevices.")

        elif (self.entry.get()=="bye"):
            self.text.insert(END,'\n\n'+'Bot: Thank You For Chatting')

        else:
            self.text.insert(END,'\n\n'+"Bot: Sorry I didn't get it")





if __name__=='__main__':
    root=Tk()
    obj=ChatBot(root)
    root.mainloop()