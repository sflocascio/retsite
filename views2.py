#Old Views not currently in use 

def create_object(request, *args, **kwargs):
    #file_upload = '/Users/samsmacbookair/projects/john_proj/core/retStaged.txtrpt'
    if request.method == "POST":
        #for input in 
        #file_upload = request.FILES['alpha_pos_1'] # get the uploaded file
        print(" \n === Entered Upload Block === Method is POST ... ")
        #file = DocumentForm(request.POST, request.FILES)
        cleaned_file_list = []
        #print("This is the first uploaded form:", form)
        
        file = request.FILES.getlist('document')
        print("File List Contains:", file)
        for formfile in file:
            print(" \n Form File in FOR loop:", formfile)
            search_string = request.GET.get('alpha1')
            print("Search string :", search_string)
            #newfile = DocumentForm(request.POST, request.FILES)
            newfile = Document(document = formfile)
            #if formfile.is_valid():
            print("  New Document File Object declared from text file:", newfile.document)
            
            # this `initial_obj` if you need to update before it uploaded.
            # such as `initial_obj.user = request.user` if you has fk to `User`, 
            # if not you can only using `obj = form.save()`
            #initial_obj = newfile.save(commit=False)
            newfile.save()
            print("Document Object saved, from file that was renamed:", newfile.document)
            
            cleaned_file = newfile.document
            cleaned_file_list.append(cleaned_file)
            print("Current Cleaned FILE LIST", cleaned_file_list)
            print(" repeating FOR loop ")
            # print("Inital OBject.document.url:", initial_obj.document.url)


    else:
        file = DocumentForm()
        print("Entered Else Block of FORM validation")

    print("\n === EXITED upload block ====")
    for input_file in cleaned_file_list:
        uploaded_file_name = Document.objects.get(document = input_file)
        print("Current FILER document name", uploaded_file_name.document)
        #Splits the Input File in individual RET.Txt files 
        with open(uploaded_file_name.document.path) as fo:
            print("entered Parsing Block ")
            op = ''
            start = 0
            cntr = 1
            files_created = []
            for x in fo.read().split("\n"):
                if not x.strip():
                    if(start == 1):
                        with open(str(cntr) + '.txt', 'w') as opf:
                            opf.write(op)
                            name_of_file = opf
                            if (opf.name != '1.txt'):
                                files_created.append(opf.name)
                            print(opf.name)
                            opf.close()
                            op = ''
                            cntr += 1
                    else:
                        start = 1
                else:
                    if (op == ''):
                        op = x
                    else:
                        op = op + '\n' + x
            total_files_created = cntr - 1
            print( "total # of files created" , total_files_created)
            print("Files Created LIST ", files_created)
            fo.close()
        
        # Turn one TXT file into JSON RET object 
        #filename = '4.txt'
        jsoncntr = 1
        json_files_created = []
        for filename in files_created:
            commands = {}
            print("JSON cntertop", jsoncntr)
            with open(filename) as fh:
                print(filename)
                for line in fh:
                    command, description = line.strip().split(':', 1)
                    commands[command] = description.strip()

            # dump into JSON File 
            with open(str(jsoncntr) + '.json', 'w') as fp:
                json_files_created.append(fp.name)
                fp.write("{" + "\n" + '"' + "Data"+ '":['  )
                json.dump(commands, fp, indent=2, sort_keys=True)
                fp.write("\n" + "]" + "\n" + "}" )
                jsoncntr += 1
                print("JSON COunter bottom:", jsoncntr)

        for file in json_files_created:
            print("Entering Creating Objects BLOCK ")
            print("file in process block:", file)
            # Read file 
            f = open(file)
            json_string = f.read()
            f.close()
            data = json.loads(json_string)

            for values in data['Data']:
                object = Ret.objects.create(
                address=values['Address'],
                name=file , 
                aisg_version=values['AISG Version'], 
                bearing=values['Bearing'], 
                hw_version=values['HW Version'])
                print("object ADdress: ", object.address)
                object.save()

            print("JSON file list created:", json_files_created)

    return render(request, 'about.html')


def create_object_new(request, *args, **kwargs):
    #Using ModelForm to create OBJECTS
    #file_upload = '/Users/samsmacbookair/projects/john_proj/core/retStaged.txtrpt'
    if request.method == "POST":
        #input_list = [] 
        #alpha1 = request.FILES['alpha_pos_1'] # get the uploaded file
        #input_list.append(alpha1)
        #alpha2 = request.FILES['alpha_pos_2'] 
        #input_list.append(alpha2)
        print(" \n === Entered New Upload Block === Method is POST ... ")
        #print("Input List", input_list)
        #file = DocumentForm(request.POST, request.FILES)
        cleaned_file_list = []
        #print("This is the first uploaded form:", form)
        
        #file = request.FILES.getlist('document')
        #print("File List Contains:", file)
        #for formfile in input_list:
        for formfile in request.FILES.getlist('document'):
            request.FILES['document'] = formfile #THis allows differentiation between files
            #print("POST REQUEST:" , request.POST)
            #position = request.value
            #print("position:", position)
            # request.FILES['name'] = name
            print(" \n Form File in FOR loop:", formfile)
            newfile = DocumentForm(request.POST, request.FILES) #using Form 
            #print("This is the Newfile that is created in loop", newfile.document)
            #newfile = Document(document = formfile) #Using model. not Form
            if newfile.is_valid():
                #print("  New Document File Object declared from text file:", newfile.document)
                #print(newfile.fields[document])
                # this `initial_obj` if you need to update before it uploaded.
                # such as `initial_obj.user = request.user` if you has fk to `User`, 
                # if not you can only using `obj = form.save()`
                initial_obj = newfile.save(commit=False)
                newfile.save()
                
                print("Document Object saved, from file that was renamed:", newfile)
                
                #cleaned_file = newfile.document
                #cleaned_file = newfile.document
                #print("cleanedFILE:", cleaned_file.document)
                #cleaned_file_list.append(cleaned_file)
                #print("Current Cleaned FILE LIST", cleaned_file_list)
                print(" repeating FOR loop ")
                # print("Inital OBject.document.url:", initial_obj.document.url)
            else:
                print("Form NOT valid")


    else:
        file = DocumentForm()
        print("Entered Else Block of FORM validation")

    print("\n === EXITED upload block ====")
    for input_file in cleaned_file_list:
        uploaded_file_name = Document.objects.get(document = input_file)
        print("Current FILER document name", uploaded_file_name.document)
        #Splits the Input File in individual RET.Txt files 
        with open(uploaded_file_name.document.path) as fo:
            print("entered Parsing Block ")
            op = ''
            start = 0
            cntr = 1
            files_created = []
            for x in fo.read().split("\n"):
                if not x.strip():
                    if(start == 1):
                        with open(str(cntr) + '.txt', 'w') as opf:
                            opf.write(op)
                            name_of_file = opf
                            if (opf.name != '1.txt'):
                                files_created.append(opf.name)
                            print(opf.name)
                            opf.close()
                            op = ''
                            cntr += 1
                    else:
                        start = 1
                else:
                    if (op == ''):
                        op = x
                    else:
                        op = op + '\n' + x
            total_files_created = cntr - 1
            print( "total # of files created" , total_files_created)
            print("Files Created LIST ", files_created)
            fo.close()
        
        # Turn one TXT file into JSON RET object 
        #filename = '4.txt'
        jsoncntr = 1
        json_files_created = []
        for filename in files_created:
            commands = {}
            print("JSON cntertop", jsoncntr)
            with open(filename) as fh:
                print(filename)
                for line in fh:
                    command, description = line.strip().split(':', 1)
                    commands[command] = description.strip()

            # dump into JSON File 
            with open(str(jsoncntr) + '.json', 'w') as fp:
                json_files_created.append(fp.name)
                fp.write("{" + "\n" + '"' + "Data"+ '":['  )
                json.dump(commands, fp, indent=2, sort_keys=True)
                fp.write("\n" + "]" + "\n" + "}" )
                jsoncntr += 1
                print("JSON COunter bottom:", jsoncntr)

        for file in json_files_created:
            print("Entering Creating Objects BLOCK ")
            print("file in process block:", file)
            # Read file 
            f = open(file)
            json_string = f.read()
            f.close()
            data = json.loads(json_string)

            for values in data['Data']:
                object = Ret.objects.create(
                address=values['Address'],
                name=file , 
                aisg_version=values['AISG Version'], 
                bearing=values['Bearing'], 
                hw_version=values['HW Version'])
                print("object ADdress: ", object.address)
                object.save()

            print("JSON file list created:", json_files_created)

    return render(request, 'about.html')

def upload_file(request):
    if request.method == "POST":
        #my_uploaded_file = request.FILES['alpha_pos_1'].read() # get the uploaded file
        data = json.loads(my_uploaded_file) 
        for values in data['Data']:
            object = Ret.objects.create(
            address=values['Address'],
            name="Nomm" , 
            aisg_version=values['AISG Version'], 
            bearing=values['Bearing'], 
            hw_version=values['HW Version'])
            object.save()

        return render(request, 'index.html')

        # do something with the file
        # and return the result            
    else:
        return render(request, 'index.html')

def create_object_form(request, *args, **kwargs):
    
    #Using ModelForm to create OBJECTS
    #Successfully process multiple Rets using Prefix from forms
    #Implemented the lazy way 

    if request.method == "POST":

        print(" \n === Entered New Upload Block === Method is POST ... ")
        modified_file_list = []

        newfile = DocumentForm(request.POST, request.FILES, prefix="a2")
        newfile2 = DocumentForm(request.POST, request.FILES, prefix="a1")

        print("newfile:::: ", newfile)

        if newfile.is_valid() or newfile2.is_valid():
            original_file_name = newfile.cleaned_data['document']
            modified_file_name = newfile.save()
            modified_file_name2 = newfile2.save()
            
            print("Modified File Name ", modified_file_name.document)
            print("Original File Name", original_file_name)
            modified_file_list.append(modified_file_name.document)
            modified_file_list.append(modified_file_name2.document)
            print(" Modified LIST ", modified_file_list)
            print(" repeating FOR loop ")

        else:
            print("Form NOT valid")
    else:
        file = DocumentForm()
        print("Entered Else Block of FORM validation")

    print("\n === EXITED upload block ====")
    for input_file in modified_file_list:
        uploaded_file_name = Document.objects.get(document = input_file)
        print("Current FILER document name", uploaded_file_name.document)
        #Splits the Input File in individual RET.Txt files 
        with open(uploaded_file_name.document.path) as fo:
            print("entered Parsing Block ")
            op = ''
            start = 0
            cntr = 1
            files_created = []
            for x in fo.read().split("\n"):
                if not x.strip():
                    if(start == 1):
                        with open(str(cntr) + '.txt', 'w') as opf:
                            opf.write(op)
                            name_of_file = opf
                            if (opf.name != '1.txt'):
                                files_created.append(opf.name)
                            print(opf.name)
                            opf.close()
                            op = ''
                            cntr += 1
                    else:
                        start = 1
                else:
                    if (op == ''):
                        op = x
                    else:
                        op = op + '\n' + x
            total_files_created = cntr - 1
            print( "total # of files created" , total_files_created)
            print("Files Created LIST ", files_created)
            fo.close()
        
        # Turn one TXT file into JSON RET object 
        #filename = '4.txt'
        jsoncntr = 1
        json_files_created = []
        for filename in files_created:
            commands = {}
            print("JSON cntertop", jsoncntr)
            with open(filename) as fh:
                print(filename)
                for line in fh:
                    command, description = line.strip().split(':', 1)
                    commands[command] = description.strip()

            # dump into JSON File 
            with open(str(jsoncntr) + '.json', 'w') as fp:
                json_files_created.append(fp.name)
                fp.write("{" + "\n" + '"' + "Data"+ '":['  )
                json.dump(commands, fp, indent=2, sort_keys=True)
                fp.write("\n" + "]" + "\n" + "}" )
                jsoncntr += 1
                print("JSON COunter bottom:", jsoncntr)

        for file in json_files_created:
            print("Entering Creating Objects BLOCK ")
            print("file in process block:", file)
            # Read file 
            f = open(file)
            json_string = f.read()
            f.close()
            data = json.loads(json_string)

            for values in data['Data']:
                object = Ret.objects.create(
                address=values['Address'],
                name=file , 
                aisg_version=values['AISG Version'], 
                bearing=values['Bearing'], 
                hw_version=values['HW Version'])
                print("object ADdress: ", object.address)
                object.save()

            print("JSON file list created:", json_files_created)

    return render(request, 'about.html')