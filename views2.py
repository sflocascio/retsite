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