import customtkinter

def button_callback():
    print("button pressed")

app = customtkinter.CTk()
app.title("my app")
app.geometry("500x350")
app.grid_columnconfigure((0,1), weight=1)

# add button
button = customtkinter.CTkButton(app, text = "my button", command = button_callback)
# button.grid(row=0, column = 0, padx=20, pady=20)
# button spans the whole window
button.grid(row=0, column = 0, padx=20, pady=20, sticky="ew", columnspan =2) 

# add checkboxes basic 
# check1 = customtkinter.CTkCheckBox(app, text="check1")
# check1.grid(row=1, column = 0, padx=20, pady=(0, 20), sticky= "w")
# check2 = customtkinter.CTkCheckBox(app, text="check2")
# check2.grid(row=1, column = 1, padx=20, pady=(0, 20), sticky= "w")


# using frames
checkbox_frame=customtkinter.CTkFrame(app)
checkbox_frame.grid(row=0, column=0, padx=10 ,pady=(10, 0), sticky="nsw")

checkbox_1 = customtkinter.CTkCheckBox(app.checkbox_frame, text="checkbox 1")
checkbox_1.grid(row=0, column=0, padx=20, pady=(20, 0), sticky="w")
checkbox_2 = customtkinter.CTkCheckBox(app.checkbox_frame, text="checkbox 2")
checkbox_2.grid(row=1, column=0, padx=20, pady=(20, 0), sticky="w")


button = customtkinter.CTkButton(app, text="my button", command=button_callback)
button.grid(row=3, column=0, padx=20, pady=20, sticky="ew", columnspan=2)


app.mainloop()