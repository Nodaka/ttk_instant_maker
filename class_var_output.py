import types
import tkinter as tk
    
    root=tk.Tk()
    
    instant_globals_dict = dict(globals())
    
    class class_output:
        def __init__(self):
            self.func_list = []
            self.tkvar_list = []
            self.class_name = None
    
    class_output_list = []
    for key, value in instant_globals_dict.items():
        if type(value) == type:
            instant_class = class_output()
            instant_class.class_name = key
    
            for c_key, c_value in eval(instant_class.class_name).__dict__.items():
                if type(eval(instant_class.class_name + "." + c_key)) == types.FunctionType:
                    instant_class.func_list.append(c_key)
            
            try:
                instant_class.func_list.remove("__init__")
            except:
                print("class: " + instant_class.class_name + " doesn't have __init__ !")
            
            for c_key, c_value in eval(instant_class.class_name+"()").__dict__.items():
                if type(c_value) in [tk.StringVar, tk. IntVar, tk.DoubleVar, tk.BooleanVar]:
                    instant_class.tkvar_list.append(c_key)        
    
    print(instant_class.class_name)
    print(instant_class.func_list)
    print(instant_class.tkvar_list)
    
    nbtof.nbtof_generate(
        output_py_file="class_output.py",
        notebook_file=__vsc_ipynb_file__,
    )
