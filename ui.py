from tkinter import *
from random import randint
from radio import *
import custom_checkbox
import pattern
languages = ['English','Português']
choosen_language = 0
languages_indexes = {'English':0,'Português':1}

texts = {
    0:['Languages: ','Linguagem: '],
    1:['Package: ','Package: '],
    2:['Key id: ','Id da tecla: '],
    3:['Key settings: ','Configurações da tecla: '],
    4:['Infinite','Infinito'],
    5:['Amount of Frames','Quantidade de frames'],
    6:['Random','Aleatório'],
    7:['On Press',"Ao Apertar"],
    8:['On Release',"Ao Soltar"],
    9:['Pattern: ','Modelo: ']
}

allLabels = []
def UI():
    global window
    window = Tk()

    lang_package = Frame(window,name="lang_and_Package")
    lang_package.pack()


    ## Linguagem
    langLabel = Label(lang_package,text=texts[0][choosen_language])
    allLabels.append(langLabel)

    global lang_option
    lang_option = StringVar(lang_package)
    lang_option.set(languages[choosen_language])
    lang_option.trace('w',update_labels)
    lang = OptionMenu(lang_package,lang_option,*languages)

    langLabel.grid(row=0,column=0)
    lang.grid(row=0,column=1)

    ## Package
    packageLabel = Label(lang_package,text=texts[1][choosen_language])
    allLabels.append(packageLabel)
    package_option = StringVar(lang_package)
    package_option.set('')
    packages_folders = ['Meio complicado','Deixar para depois'] ## Preciso dar um [ls] em [./packages]
    package = OptionMenu(lang_package,package_option,*packages_folders)
    packageLabel.grid(row=1,column=0)
    package.grid(row=1,column=1)



    ## After choosing a valid package:
    key_config_patter_key_list = Frame(window,name="key_config-patter_key-list")
    key_config_patter_key_list.pack()

    ## Key id
    #frame
    package_everything = Frame(key_config_patter_key_list,name="key_config",highlightbackground="black", highlightthickness=1)
    package_everything.pack(padx=(10, 10))

    #[key id] label
    key_id_label = Label(package_everything,text=texts[2][choosen_language])
    allLabels.append(key_id_label)

    #[key id] dropdown
    global key_id
    key_id = StringVar(package_everything)
    key_id.set('')
    key_ids = ['']
    for x in range(randint(0,5)):
        key_ids.append(str(randint(0,5)))
    package = OptionMenu(package_everything,key_id,*key_ids)
    key_id_label.grid(row=0,column=0)
    package.grid(row=0,column=1)

    ## Key config
    key_config_label = Label(package_everything,text=texts[3][choosen_language])
    allLabels.append(key_config_label)
    key_config_label.grid(row=1,column=0)

    texts_radio = []
    chk_texts = []
    for x in range(3):
       texts_radio.append(texts[4+x][choosen_language])
    for x in range(2):
       chk_texts.append(texts[7+x][choosen_language])
    key_config_radio = Radio(package_everything,texts_radio,texts_radio,1,1)
    key_config_chk = custom_checkbox.Checkbox(package_everything,chk_texts,1,4)
    var = key_config_radio.selected_option
    var.trace('w',lambda a,b,c,x=var,chk=key_config_chk : gray_it_out(x,chk))
    for opt in key_config_radio.options:
        allLabels.append(opt)
    for opt in key_config_chk.options:
        allLabels.append(opt)


    ## Pattern
    pattern_frame = Frame(key_config_patter_key_list,name="pattern-frame")
    pattern_frame.pack()

    pattern_label = Label(pattern_frame,text=texts[9][choosen_language])
    pattern_label.grid(row=0,column=0)
    allLabels.append(pattern_label)

    pattern_area = pattern.Pattern(pattern_frame)

    window.mainloop()

def update_labels(lang,*args):
    global lang_option  
    for x in range(len(allLabels)):
        allLabels[x].configure(text=texts[x][languages_indexes[lang_option.get()]])
        allLabels[x].update()

def gray_it_out(change,checkbox):
    return
    # if change.get() == 'Amount of Frames' or change.get() == 'Infinite':
    #     checkbox.gray_setup([0,1,1])
    # else:
    #     checkbox.gray_setup([1,1,1])

UI()