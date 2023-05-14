# this is the same as main.py only that it is nested in a class App

import customtkinter

class MyCheckboxFrame(customtkinter.CTkFrame):
    def __init__(self, master,title, values):
        super().__init__(master)
        self.values = values
        self.checkboxes = []
        self.title = title


        self.title = customtkinter.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady= (10,0), sticky="ew")
        # self.checkbox_1 = customtkinter.CTkCheckBox(self, text="checkbox 1")
        # self.checkbox_1.grid(row=0, column=0, padx=20, pady=(20, 0), sticky="w")

        # self.checkbox_2 = customtkinter.CTkCheckBox(self, text="checkbox 2")
        # self.checkbox_2.grid(row=1, column=0, padx=20, pady=(20, 0), sticky="w")

        for i, value in enumerate(self.values):
            checkbox = customtkinter.CTkCheckBox(self, text = value)
            checkbox.grid(row=i+1, column=0, padx = 10, pady= (10,0), sticky = "w")
            self.checkboxes.append(checkbox)

    def get(self):
        checked_checkboxes = []
        # not pythonic
        # if self.checkbox_1.get() == 1:
        #     checked_checkboxes.append(self.checkbox_1.cget("text"))

        # if self.checkbox_2.get() == 1:
        #     checked_checkboxes.append(self.checkbox_2.cget("text"))

        # if self.checkbox_3.get() == 1:
        #     checked_checkboxes.append(self.checkbox_2.cget("text"))
        
        # return checked_checkboxes

        # dynamic
        for checkbox in self.checkboxes:
            if checkbox.get() == 1:
                checked_checkboxes.append(checkbox.cget("text"))
        return checked_checkboxes


class MyRadiobuttonFrame(customtkinter.CTkFrame):
    def __init__(self, master, title, values):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.title = title
        self.radiobuttons = []
        self.variable = customtkinter.StringVar(value="")

        self.title = customtkinter.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

        for i, value in enumerate(self.values):
            radiobutton = customtkinter.CTkRadioButton(self, text=value, value=value, variable=self.variable)
            radiobutton.grid(row=i + 1, column=0, padx=10, pady=(10, 0), sticky="w")
            self.radiobuttons.append(radiobutton)

    def get(self):
        return self.variable.get()

    def set(self, value):
        self.variable.set(value)



class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("my app")
        self.geometry("500x260")
        self.grid_columnconfigure((0,1), weight=1)
        self.grid_rowconfigure(0,weight=1)

        self.checkbox_frame = MyCheckboxFrame(self,"Values", values=['value 1', 'value 2', 'value 3'])
        self.checkbox_frame.grid(row=0, column=0, padx=10 ,pady=(10, 0), sticky="nsw")
        self.checkbox_frame.configure(fg_color="transparent")

        self.checkbox_frame_1 = MyCheckboxFrame(self,"Options",  values=['value 100', 'value 200', 'value 300'])
        self.checkbox_frame_1.grid(row=0, column=1, padx=10 ,pady=(10, 0), sticky="nsw")
        self.checkbox_frame_1.configure(fg_color="transparent")

        self.radiobutton_frame = MyRadiobuttonFrame(self, "Options", values=["option 1", "option 2"])
        self.radiobutton_frame.grid(row=0, column=2, padx=(0, 10), pady=(10, 0), sticky="nsew")
        self.radiobutton_frame.configure(fg_color="transparent")

        self.button = customtkinter.CTkButton(self, text="my button", command=self.button_callback)
        self.button.grid(row=3, column=0, padx=20, pady=20, columnspan=2)
        
    def button_callback(self):
        print("checked : ", self.checkbox_frame.get())
        print("checked : ", self.checkbox_frame_1.get())
        print("radiobutton : ", self.radiobutton_frame.get())

app = App()
app.mainloop()