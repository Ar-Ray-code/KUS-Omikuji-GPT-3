import openai
import random
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

class openai_mikuji:

   def __init__(self):
      openai.api_key = "*******"
      random_num = random.randint(0, 7)

      if random_num == 0:
         text = "運勢：大吉です。ラッキーアイテムは"
      elif random_num == 1:
         text = "運勢：小吉です。ラッキーアイテムは"
      elif random_num == 2:
         text = "運勢：中吉です。ラッキーアイテムは"
      elif random_num == 3:
         text = "運勢：吉末です。ラッキーアイテムは"
      elif random_num == 4:
         text = "運勢：吉です。ラッキーアイテムは"
      elif random_num == 5:
         text = "運勢：凶です。ラッキーアイテムは"
      elif random_num == 6:
         text = "運勢：大凶です。ラッキーアイテムは"

      response = openai.Completion.create(
         engine="davinci",
         prompt=text,
         temperature=0.9,
         max_tokens=200,
         top_p=1,
         presence_penalty=0,
      )

      text_result =  response['choices'][0]['text']

      self.text_result = text + text_result.split('\n').pop(0)
      
   def generated_text(self):
      return self.text_result

class tk_widget:
   # using button and show result in Frame
   def __init__(self, master):
      self.master = master
      self.master.title("openai_mikuji")
      self.master.geometry("873x731")
      self.master.resizable(False, False)

      # load shrine.png and set background
      self.background_image = tk.PhotoImage(file="shrine.png")
      self.background_label = tk.Label(self.master, image=self.background_image)
      self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

      self.text_result = tk.Text(self.master, height=10, width=30)
      self.text_result.place(x=300, y=300)

      self.button = tk.Button(self.master, text="openai_mikuji", command=self.button_click)
      self.button.place(x=360, y=650)
   
   def button_click(self):
      print("button clicked")
      mikuji = openai_mikuji()
      text = mikuji.generated_text()
      self.text_result.delete(1.0, tk.END)
      self.text_result.insert(tk.END, text)


   
if __name__ == "__main__":
   root = tk.Tk()
   root.title("openai_mikuji")
   root.geometry("400x400")
   app = tk_widget(root)
   root.mainloop()
